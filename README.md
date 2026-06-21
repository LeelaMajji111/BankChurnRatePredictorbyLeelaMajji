 Bank Customer Churn Prediction

##  Live Demo
https://bankchurnratepredictorbyleelamajji-8gyekrb53tdyappcvvhfwuf.streamlit.app/

## Project Overview
This project predicts whether a bank customer is likely to leave the bank (churn) using Machine Learning.

The model learns from customer details and predicts:
- ✅ Customer will stay
- ❌ Customer may churn

A Streamlit web application is created to make predictions easily through an interactive user interface.

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Random Forest Classifier
- SMOTE (Synthetic Minority Oversampling Technique)

## Dataset Features

The model uses customer information such as:

- Credit Score
- Age
- Tenure
- Balance
- Number of Products
- Credit Card Status
- Active Membership
- Estimated Salary
- Geography
- Gender

## Machine Learning Workflow

1. Data Cleaning
2. Exploratory Data Analysis
3. Feature Encoding using pd.get_dummies()
4. Handling class imbalance using SMOTE
5. Feature Scaling using StandardScaler
6. Model Training using Random Forest Classifier
7. Creating Pipeline (Scaler + Model)
8. Saving model using Pickle
9. Deploying with Streamlit

## Model

Algorithm used:

*Random Forest Classifier*

