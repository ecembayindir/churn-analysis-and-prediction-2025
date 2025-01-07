<h1 align="center">Churn Analysis and Prediction</h1>

<br/>

<h2>🚀 <strong>Project Overview</strong></h2>
<p>
This project delves into customer churn analysis for a business using a data-driven approach. Leveraging structured customer data, I analysed key features such as demographics, services, contract types, and financial metrics to identify churn drivers and predict churn probability. By combining <strong>SQL Server</strong>, <strong>Tableau</strong>, and <strong>Python</strong>, I developed an end-to-end solution that offers actionable insights to reduce customer attrition.
</p>

<h2>📈 <strong>Project Workflow</strong></h2>
<ul>
  <li><strong>ETL Process in SQL Server</strong>: Extracted and transformed customer data for analysis. Key columns such as <code>Churn_Category</code> and <code>Churn_Reason</code> were analysed to determine the primary churn drivers.</li>
  <li><strong>Data Cleaning in SQL Server</strong>: Ensured data quality by addressing missing values and inconsistencies in fields like <code>Monthly_Charge</code> and <code>Total_Charges</code>.</li>
  <li><strong>Transformations in Tableau</strong>: Prepared and optimized data for advanced visualizations to understand churn trends across demographics, contract types, and usage metrics.</li>
  <li><strong>Visualization and Insights in Tableau</strong>: Created dashboards to visualise churn patterns, allowing stakeholders to prioritise retention efforts.</li>
  <li><strong>Machine Learning Model in Python</strong>: Built and trained a <strong>Random Forest model</strong> to predict churn probability using features like <code>Tenure_in_Months</code>, <code>Payment_Method</code>, and <code>Internet_Type</code>.</li>
  <li><strong>Predicted Data Visualization in Tableau</strong>: Integrated model predictions into Tableau for enhanced decision-making and insights.</li>
</ul>

<div align="center">
    <img src="https://i.imgur.com/ivI6L73.png" alt="Summary Page" style="display: block; margin: 0 auto; max-width: 80%; height: auto;">
    <p><strong>Figure 1</strong>: Summary Page</p>
</div>

<div align="center">
    <img src="https://i.imgur.com/qtyMDnK.png" alt="Churn Prediction Page" style="display: block; margin: 0 auto; max-width: 80%; height: auto;">
    <p><strong>Figure 2</strong>: Churn Prediction Page</p>
</div>

<h2>📊 <strong>Key Insights</strong></h2>
<ul>
  <li><strong>Primary Churn Drivers:</strong> Competitor offerings and dissatisfaction with product reliability were the top reasons for churn.</li>
  <li><strong>Customer Segmentation:</strong> Customers with month-to-month contracts showed significantly higher churn rates, indicating a need for loyalty-focused strategies.</li>
  <li><strong>Retention Strategies:</strong> Highlighted opportunities to improve network reliability and provide incentives for long-term contracts.</li>
  <li><strong>Predictive Insights:</strong> Random Forest predictions helped identify at-risk customers, enabling targeted retention campaigns.</li>
</ul>

<h2>🛠️ <strong>Tools & Technologies Used</strong></h2>
<div align="center">
    <img src="https://img.shields.io/badge/sql-F29111?style=for-the-badge&logo=microsoft-sql-server&logoColor=white" alt="SQL Server"/>
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" alt="Python"/>
    <img src="https://img.shields.io/badge/tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white" alt="Tableau"/>
    <img src="https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white" alt="Excel"/>
    <img src="https://img.shields.io/badge/Random_Forest-FFD700?style=for-the-badge" alt="Random Forest"/>
    <img src="https://img.shields.io/badge/Matplotlib-ff5733?style=for-the-badge" alt="Matplotlib"/>
    <img src="https://img.shields.io/badge/Seaborn-007ACC?style=for-the-badge" alt="Seaborn"/>
</div>

<h2>📂 <strong>Repository Structure</strong></h2>
<pre>
├── data/
│   ├── raw_data/              # Raw data files
│   ├── processed_data/        # Processed data files
├── scripts/
│   ├── data_etl.sql           # SQL script for ETL process
│   ├── data_cleaning.sql      # SQL script for data cleaning
│   ├── random_forest.py       # Python script for ML model
├── dashboards/
│   ├── tableau_summary.twbx   # Tableau dashboard - Summary
│   ├── tableau_prediction.twbx # Tableau dashboard - Churn Prediction
├── README.md                  # Project overview and instructions
</pre>

<h2>📊 <strong>Key Visuals & Insights</strong></h2>
<p>Explore the full Tableau dashboard via the button below:</p>
<div align="center">
    <a href="https://public.tableau.com/views/ChurnAnalysisandPrediction2025_17362583805820/Summary?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link" style="text-decoration: none;">
        <button style="background-color: #E97627; color: white; padding: 15px 30px; font-size: 20px; border: none; border-radius: 10px; cursor: pointer;">
            🌟 View Interactive Tableau Dashboard 🌟
        </button>
    </a>
</div>

<h2>💻 <strong>How to Use This Repository</strong></h2>
<ol>
  <li><strong>Clone the Repository</strong>: <code>git clone https://github.com/ecembayindir/churn-analysis-prediction</code></li>
  <li><strong>Database Setup</strong>: Load the raw data into SQL Server and execute the provided ETL and cleaning scripts.</li>
  <li><strong>Run Scripts</strong>: Use Python for model training and predictions.</li>
  <li><strong>Explore Dashboards</strong>: Open the Tableau files to interact with the visualizations and insights.</li>
</ol>

<h2>📫 <strong>Connect with Me</strong></h2>
<ul>
    <li><a href="https://www.linkedin.com/in/ecembayindir/"><img src="https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white" alt="LinkedIn"/></a></li>
    <li><a href="mailto:ecmbyndr@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?logo=gmail&logoColor=white" alt="Email"/></a></li>
</ul>

<h2>📜 <strong>Conclusion</strong></h2>
<p>
This project highlights my expertise in data engineering, visualization, and machine learning to solve critical business problems. By identifying churn drivers and predicting at-risk customers, the project demonstrates my ability to bridge data insights with actionable strategies for customer retention.
</p>

<p align="center">&copy; 2025 Ecem Bayındır. All rights reserved.</p>

<hr>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=ecembayindir&label=Repository%20views&color=0e75b6&style=flat" alt="Repository Views">
</p>
