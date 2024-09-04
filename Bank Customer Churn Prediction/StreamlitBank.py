import streamlit as st
import joblib
import numpy as np


st.sidebar.title("Machine Learning Models")
st.sidebar.markdown("## Bank Customer Churn Prediction")
st.sidebar.markdown("### Ml Models :- Random Forest")

st.header("Bank Customer Churn Prediction")


CreditScore = st.text_input("Credit Score",300 , 1000)

Geography = st.selectbox("Geography " , ['France', 'Spain', 'Germany'])
Geography_dist = {'France':0, 'Spain':1, 'Germany':2}
Geography = Geography_dist[Geography]

Gender = st.selectbox("Gender",['Female', 'Male'])
Gender_dist = {'Female':0, 'Male':1}
Gender = Gender_dist[Gender]

Age = st.number_input("customer's Age",10,90)

Tenure = st.number_input("The number of years the customer",0,10)

Balance = st.text_input("Customer's Balance",0,200000)

NumOfProducts = st.number_input("Num Of Products Use",1,4)

HasCrCard = st.selectbox("Customer has a credit card",["Yes" , "No"])
HasCrCard_dist = {"Yes":1, "No":0}
HasCrCard = HasCrCard_dist[HasCrCard]

IsActiveMember = st.selectbox("Customer is an Active",["Yes" , "No"])
IsActiveMember_dist = {"Yes":1, "No":0}
IsActiveMember = IsActiveMember_dist[IsActiveMember]

EstimatedSalary = st.text_input("Estimated Salary of the customer",0,200000)

button = st.button("SUBMIT")
bank_model_pkl = 'C:\\Users\\Anish Avasthi\\Desktop\\Sunstone\\random_for_BankCustomer.pkl'
loaded_model = joblib.load(bank_model_pkl)

x = np.array([[CreditScore,Geography,Gender,Age,Tenure,Balance,NumOfProducts,HasCrCard,IsActiveMember,EstimatedSalary]])

predicted_value =  loaded_model.predict(x)

decode_dict = {0:"No", 1:"Yes"}

predicted_name = decode_dict[predicted_value[0]]

if button:
    st.text("Bank Customer Prediction")
    st.info(predicted_value)
    st.info(predicted_name)

