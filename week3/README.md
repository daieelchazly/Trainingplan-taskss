# Telco customer churn prediction

## Project overview

This project aims to predict if a customer will leave a telecom company or continue using its services

The goal is to understand customer behavior, find the main reasons for churn, and build machine learning models that can help companies keep their customers

## Dataset

The project uses the Telco customer churn dataset

- 7,043 rows (customers)
- 21 columns (features)
- Target column: `Churn` (Yes / No)

The dataset contains customer details, contract types, internet services, payment methods, monthly charges, and total charges.

## Tools and libraries

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Imbalanced-learn
- XGBoost
- SciPy
- SQL (pandasql)

## Project workflow

### 1. Data inspection and cleaning

- Checked data types, missing values, and duplicates
- Checked for empty and whitespace values
- Converted `TotalCharges` from object to numeric
- Found 11 missing values, all from customers with zero tenure
- Replaced these missing values with zero

### 2. Outlier detection

- Used the modified z-score method with a threshold of 3.5
- Found 136 possible outliers in `TotalCharges`
- Checked their tenure and monthly charges
- Kept them because they were valid customer records, not clear data errors

### 3. Exploratory data analysis (EDA)

Explored customer behavior and the relationship between different features and churn

Main findings:

- 73.46% of customers stayed, while 26.54% left
- Customers with month-to-month contracts had the highest churn rate (42.71%)
- Customers with two-year contracts had the lowest churn rate (2.83%)
- Customers who left generally had higher monthly charges
- 31.04% of customers had a tenure of 12 months or less

### 4. SQL analysis

Used SQL queries with pandasql to explore the data

- Counted customers by contract type
- Checked churn by internet service
- Used `LEFT JOIN` to combine customer and service information

### 5. Feature engineering

Created three new features:

- `Total_Services`: Counts the additional services used by each customer
- `Avg_Monthly_Spent`: Calculates average spending using total charges and tenure
- `Tenure_Group`: Groups customers into New, Medium, and Loyal based on their tenure

### 6. Data preprocessing

- Removed `customerID` because it is only an identifier
- Split the data into 80% training and 20% testing
- Used stratification to keep the same class ratio
- Applied One-Hot Encoding to categorical features
- Applied StandardScaler to numerical features
- Combined the encoded and scaled features using sparse matrices

### 7. Machine learning models

Trained and tested different models:

- Dummy Classifier as a baseline
- Logistic Regression
- Logistic Regression with class weighting
- Logistic Regression with SMOTE
- XGBoost with class weighting
- XGBoost with SMOTE

### 8. Handling class imbalance

The dataset had more customers who stayed than customers who left

To handle this problem, two techniques were tested:

**Class weighting:** Gives more importance to the minority class during training

**SMOTE:** Creates new synthetic samples for the minority class

Both techniques improved the model's ability to detect customers who were likely to leave

---

### Main results

- Logistic Regression achieved the highest accuracy (80.6%)
- XGBoost with class weighting achieved the highest recall (79.4%)
- XGBoost with class weighting also achieved the highest F1-score (0.630)
- SMOTE improved churn detection compared with the original Logistic Regression model

## Final conclusion

XGBoost with class weighting was selected as the best model for this project

Its results were:

- Accuracy: 75.2%.
- Precision: 52.2%.
- Recall: 79.4%.
- F1-score: 0.630.

It was selected because it could identify more customers who were likely to leave 

In this project, finding customers who may leave is more important than getting high accuracy alone, because companies need to identify these customers early and try to keep them

## Project structure

```text
Telco-Customer-Churn-Prediction/
│
├── data_inspection+ML.ipynb
├── Telco-Customer-Churn.csv
└── README.md
```

## How to run

1. Clone the repository
2. Install the required libraries:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn scipy pandasql imbalanced-learn xgboost
```

3. Open the notebook using Google Colab or Jupyter Notebook
4. Upload the dataset
5. Run the notebook cells in order

## In the notebook :

- Data cleaning and preparation
- Exploratory data analysis
- SQL queries and joins
- Feature engineering
- One-Hot Encoding and StandardScaler
- Logistic Regression and XGBoost
- Class imbalance handling
- SMOTE and class weighting
- Model evaluation and comparison
