# Telco customer churn analysis & documentation

## Installation & setup

### Clone the repository:

```bash
git clone https://github.com/your-username/telco-churn-analysis.git
cd telco-churn-analysis
```

### Set up a virtual environment & install dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install pandas numpy matplotlib seaborn pandasql
```

### Run the notebook:

```bash
jupyter notebook notebooks/telco_churn_analysis.ipynb
```

## Analysis and documentation:

This project performs Analysis  using Python (Pandas, Matplotlib, Seaborn) and SQL (pandasql) on the Telco Customer Churn dataset.

## Dataset overview & data cleaning workflow:

The dataset consists of 7,043 rows (individual customers) and 21 features

### Telco customer churn

### Dataset structure & schema:

- Customers who left : the column is called Churn
- Services that each customer has signed up for : phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
- Account Info:enure, Contract, PaperlessBilling, PaymentMethod
- Services: PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection ,TechSupport, StreamingTV, StreamingMovies
- Financials :MonthlyCharges, TotalCharges
- Target Variable: churn (yes/no)

## Data cleaning & transformation steps

### A. Handling whitespaces and data types

As whitespaces are not considered empty values i checked for them first and found 11 whitespaces in the TotalCharges column

During the first inspection (df.info()), the TotalCharges column was found to have an object data type instead of a numeric type

**Action Taken:**

- Removed extra spaces from the values
- Converted the column to numeric using pd.to_numeric()

### B. Imputation of missing values:

The 11 NaN values in TotalCharges belonged exclusively to new customers with a tenure of 0 months.

**Logic:** Customers with 0 months of tenure have not yet accumulated billings

**Action Taken:** Filled all 11 NaN values with 0.0.

### C. Outlier investigation (Modified Z-Score)

Applying the Modified Z-Score method  shows 136 potential outliers in TotalCharges.

From the business logic it make sense that these are customers that have high tenure may have high totalcharges because of the long time of subscribtions

In the notebook visulization the red dots (outliers) are all clustered way up at the very top of the TotalCharges, and it clearly shows that they aren't random mistakes;

These are the people with the highest Value for the company

If outlier handling is necessary, regardless outliers are valid according to business logic, I would apply log transformation this will help me compress the scale of TotalCharges, reducing the relative differences between large and small values while preserving all customer records , making extreme values have less impact for ML algorithms that will be used later

I would use capping or upper and lower bound it would change the numbers totally which i not support

### D. Churn imbalance analysis:

- (No): 5,174 customers (73.46%)
- (Yes): 1,869 customers (26.54%)

**Result interpreting:** The target variable demonstrates a class imbalance

For further , If training a model later the data would better be balanced (will be applied in the machine learning notebook )

## Examples of some columns impact :

### Impact of internet service on churn :

- DSL Churn Volume: 459 customers
- Fiber Optic Churn Volume: 1,297 customers
- No Internet Service Churn Volume: 113 customers

**Insight:** Fiber optic users are churning at a rate much higher compared to DSL users

### The count /number of customers in each contract :

- 31.04% of customers have been with the company for 12 months or less
- 21.06% have maintained their subscriptions for at least 60 months.

The result knowing the count of customer in each type of contract

### Monthly billing impact (boxplot) :

Customers who churned had higher monthly charges than those who stayed

- The average monthly charge was 74.4 for churned customers and 61.2 for non-churned
- customers who canceled their subscription have a higher average monthly bill (median around 80)

This means that higher monthly costs are one of the main drivers of churn

## SQL data analysis & relational joins (pandasql)

To simulate enterprise database environments, relational SQL queries were run directly on the DataFrames using pandasql.

### Query 1: Customer distribution by contract type

**Goal:** subscribers grouped by their contract model

### Query 2: Churn across internet service types

**Goal:** Determine churn counts across different internet services types

### Query 3: Multi-table relational LEFT JOIN

**Goal:** To practice I splitted the data to 2 tables

goal to see combination between the contract and internet service that a certain customers have and are these who churn

For further sight when training ML algorithm i may need to apply one-hot encoding (week3)  

src: 
https://github.com/fawwazmts/outlier-detection-zscore-modifiedzscore/
https://www.w3schools.com/python/pandas/pandas_analyzing.asp
