# CUSTOMER-CHURN-ANALYSIS-PROJECT
📌 Project Overview

The Customer Churn Analysis project is an advanced data analysis project developed as part of Week 5 – Advanced Data Manipulation with Pandas. The objective of this project is to analyze customer churn behavior using real-world structured data and extract meaningful business insights that can help organizations improve customer retention.

The project demonstrates a complete data analysis workflow including data loading, cleaning, transformation, aggregation, filtering, and visualization using Python, Pandas, and Matplotlib. It focuses on understanding customer tenure, monthly charges, churn rate, and overall customer behavior patterns.

🎯 Objectives

Analyze customer churn patterns from a real dataset

Calculate key churn metrics such as churn rate and average tenure

Perform advanced Pandas operations including aggregation and filtering

Clean and preprocess raw data for accurate analysis

Visualize churn distribution for better insight

🛠️ Technologies Used

Python 3.x

Pandas – data manipulation and analysis

Matplotlib – data visualization

CSV Dataset – customer churn data

📂 Dataset Description

The dataset (customer_churn.csv) contains customer-level information such as:

Customer ID

Tenure

Monthly Charges

Total Charges

Contract Type

Payment Method

Churn Status

The data is cleaned and normalized before analysis to handle missing values, duplicates, and inconsistent churn labels.

⚙️ Project Workflow

Load customer churn dataset using Pandas

Explore data structure and column types

Clean data by handling missing values and duplicates

Normalize churn labels for accurate filtering

Calculate churn metrics:

Total customers

Churned customers

Churn rate

Average monthly charges

Average tenure

Generate a formatted churn analysis report

Create visualizations to show churn distribution

📊 Sample Output
CUSTOMER CHURN ANALYSIS REPORT
---------------------------------------------
Total Customers        : 7043
Churned Customers      : 1869
Churn Rate             : 26.54%
Average Monthly Charge : ₹64.76
Average Tenure         : 32.4 months

📈 Visualizations

Bar chart showing churn vs non-churn customers

Pie chart representing churn percentage

These visualizations help in quickly understanding customer retention patterns.

🧪 Testing & Validation

Manual testing performed with complete and incomplete datasets

Verified accurate handling of missing values

Ensured consistent churn calculations across different churn formats

No runtime errors observed during execution

📁 Repository Structure
Customer_Churn_Analysis/
│── churn_analysis.py
│── customer_churn.csv
│── requirements.txt

✅ Key Learnings

Advanced Pandas data manipulation techniques

Aggregation and filtering using real business data

Handling inconsistent and missing data

Translating raw data into actionable insights

Creating professional, readable analysis reports
