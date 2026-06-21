import streamlit as st
import pickle
import gzip
import pandas as pd

with gzip.open("churn.pkl.gz","rb") as f:
    model=pickle.load(f)


st.title("Bank Churn Prediction")


CreditScore = st.number_input("Credit Score",min_value=300,max_value=900,step=1)
Geography = st.selectbox(
    "Geography",
    ["France","Germany","Spain"]
)
Gender = st.selectbox(
    "Gender",
    ["Male","Female"]
)
Age = st.number_input("Age",min_value=18,max_value=100,step=1)
Tenure=st.number_input("Tenure",min_value=0,max_value=10,step=1)
Balance = st.number_input("Balance",min_value=0.0,step=1000.0)
NumOfProducts = st.number_input("Number of Products",min_value=1,max_value=4,step=1)

HasCrCard = st.selectbox(
    "Has Credit Card",
    [0,1]
)

IsActiveMember = st.selectbox(
    "Is Active Member",
    [0,1]
)

EstimatedSalary = st.number_input("Estimated Salary",min_value=0.0,step=1000.0)









if st.button("Predict"):

    input_data = pd.DataFrame([{
        "CreditScore": CreditScore,
        "Age": Age,
        "Tenure":Tenure,
        "Balance": Balance,
        "NumOfProducts": NumOfProducts,
        "HasCrCard": HasCrCard,
        "IsActiveMember": IsActiveMember,
        "EstimatedSalary": EstimatedSalary,

        "Geography_Germany": 1 if Geography=="Germany" else 0,
        "Geography_Spain": 1 if Geography=="Spain" else 0,
        "Gender_Male": 1 if Gender=="Male" else 0,



    }])


    prediction = model.predict(input_data)


    if prediction[0] == 1:
        st.error("Customer will churn ❌")
    else:
        st.success("Customer will stay ✅")