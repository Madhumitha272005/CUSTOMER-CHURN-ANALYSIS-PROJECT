import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("customer_churn.csv")

print("Columns in dataset:", df.columns.tolist())

# -------------------------------
# DATA CLEANING
# -------------------------------
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)

# Normalize churn column
df['Churn'] = df['Churn'].astype(str).str.lower().str.strip()

# -------------------------------
# METRICS
# -------------------------------
total_customers = df['CustomerID'].nunique()
churned_customers = df[df['Churn'].isin(['yes', '1', 'true'])].shape[0]
churn_rate = (churned_customers / total_customers) * 100
avg_monthly_charge = df['MonthlyCharges'].mean()
avg_tenure = df['Tenure'].mean()

# -------------------------------
# REPORT
# -------------------------------
print("\nCUSTOMER CHURN ANALYSIS REPORT")
print("-" * 45)
print(f"Total Customers        : {total_customers}")
print(f"Churned Customers      : {churned_customers}")
print(f"Churn Rate             : {churn_rate:.2f}%")
print(f"Average Monthly Charge : ₹{avg_monthly_charge:.2f}")
print(f"Average Tenure         : {avg_tenure:.1f} months")

# -------------------------------
# VISUALIZATIONS
# -------------------------------
churn_counts = df['Churn'].value_counts()

plt.figure()
churn_counts.plot(kind='bar')
plt.title("Customer Churn Distribution")
plt.xlabel("Churn")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.show()

plt.figure()
churn_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Churn Percentage")
plt.ylabel("")
plt.tight_layout()
plt.show()
