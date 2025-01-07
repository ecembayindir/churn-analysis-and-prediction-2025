# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, RocCurveDisplay
from sklearn.preprocessing import LabelEncoder
import joblib

# Display all rows and columns in a DataFrame
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Part 1: Train the Model and Save It
# Define the path to the Excel file
file_path = r"/Users/ecembayindir/Desktop/DATA ANALYTICS/PROJECTS/customer_churn_prediction_bi/Data & Resources/Data/Prediction_Data.xlsx"
sheet_name = 'vw_ChurnData'

# Load data
data = pd.read_excel(file_path, sheet_name=sheet_name)

# Display the first few rows of the data
print("Original Data (First 5 Rows):")
print(data.head())

# Check for missing values
print("Missing Values:")
print(data.isnull().sum())

# Handle missing values
numeric_columns = data.select_dtypes(include=['number']).columns
categorical_columns = data.select_dtypes(include=['object']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())
for column in categorical_columns:
    data[column] = data[column].fillna(data[column].mode()[0])

# Drop unnecessary columns
data = data.drop(['Customer_ID', 'Churn_Category', 'Churn_Reason'], axis=1)

# Encode categorical variables
columns_to_encode = [
    'Gender', 'Married', 'State', 'Value_Deal', 'Phone_Service', 'Multiple_Lines',
    'Internet_Service', 'Internet_Type', 'Online_Security', 'Online_Backup',
    'Device_Protection_Plan', 'Premium_Support', 'Streaming_TV', 'Streaming_Movies',
    'Streaming_Music', 'Unlimited_Data', 'Contract', 'Paperless_Billing',
    'Payment_Method'
]

label_encoders = {}
for column in columns_to_encode:
    label_encoders[column] = LabelEncoder()
    data[column] = label_encoders[column].fit_transform(data[column])

# Encode target variable
data['Customer_Status'] = data['Customer_Status'].map({'Stayed': 0, 'Churned': 1}).astype(int)

# Split data into features and target
X = data.drop('Customer_Status', axis=1)
y = data['Customer_Status']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Hyperparameter tuning and model training
rf_model = RandomForestClassifier(random_state=42)
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [10, 20, None],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)
best_rf_model = grid_search.best_estimator_

# Save model and label encoders
joblib.dump(best_rf_model, r"/Users/ecembayindir/Desktop/DATA ANALYTICS/PROJECTS/customer_churn_prediction_bi/random_forest_model.pkl")
for column, encoder in label_encoders.items():
    joblib.dump(encoder, rf"/Users/ecembayindir/Desktop/DATA ANALYTICS/PROJECTS/customer_churn_prediction_bi/{column}_label_encoder.pkl")

# Evaluate the model
y_pred = best_rf_model.predict(X_test)
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nAUC-ROC Score:")
print(roc_auc_score(y_test, best_rf_model.predict_proba(X_test)[:, 1]))

# Plot Feature Importance
importances = best_rf_model.feature_importances_
indices = np.argsort(importances)[::-1]
plt.figure(figsize=(15, 6))
sns.barplot(x=importances[indices], y=X.columns[indices])
plt.title('Feature Importances')
plt.xlabel('Relative Importance')
plt.ylabel('Feature Names')
plt.show()

# Part 2: Use the Model for Predictions
# Define the path to the new data file
new_file_path = r"/Users/ecembayindir/Desktop/DATA ANALYTICS/PROJECTS/customer_churn_prediction_bi/Data & Resources/Data/Prediction_Data.xlsx"
sheet_name = 'vw_JoinData'

# Load new data
new_data = pd.read_excel(new_file_path, sheet_name=sheet_name)

# Display the first few rows of the new data
print("New Data (First 5 Rows):")
print(new_data.head())

# Retain the original DataFrame to preserve unencoded columns
original_data = new_data.copy()

# Retain the Customer_ID column
customer_ids = new_data['Customer_ID']

# Drop unnecessary columns
columns_to_drop = ['Customer_ID', 'Customer_Status', 'Churn_Category', 'Churn_Reason']
new_data = new_data.drop(columns=columns_to_drop, axis=1)

# Handle missing values and encode categorical variables
for column in new_data.select_dtypes(include=['object']).columns:
    if column in label_encoders:  # Check if a label encoder exists for the column
        # Fill missing values with the mode of the column
        mode_value = new_data[column].mode()[0]
        new_data[column] = new_data[column].fillna(mode_value)  # Assign updated column
        # Encode the column using the saved label encoder
        new_data[column] = label_encoders[column].transform(new_data[column])
    else:
        raise ValueError(f"No encoder found for column: {column}")


# Make predictions
new_predictions = best_rf_model.predict(new_data)
prediction_probabilities = best_rf_model.predict_proba(new_data)[:, 1]  # Get probabilities for "Churned"

# Add predictions and probabilities to the original DataFrame
original_data['Customer_Status_Predicted'] = new_predictions
original_data['Churn_Probability'] = prediction_probabilities

# Filter the DataFrame to include only records predicted as "Churned"
churned_customers = original_data[original_data['Customer_Status_Predicted'] == 1]

# Save the results to a CSV file
output_file_path = r"/Users/ecembayindir/Desktop/DATA ANALYTICS/PROJECTS/customer_churn_prediction_bi/Predictions.csv"
churned_customers.to_csv(output_file_path, index=False)

# Display success message
print(f"Predicted churned customers saved to {output_file_path}")
