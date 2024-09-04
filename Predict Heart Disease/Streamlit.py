import streamlit as st
import joblib
import numpy as np 



st.sidebar.title("Machine Learning Models")
st.sidebar.markdown("## Predict Heart Disease")
st.sidebar.markdown("### Ml Models :- Random Forest")

st.header("Predict Heart Disease")

male = st.selectbox("Male",["Yes" , "No"])
male_dict={"Yes":1, "No": 0}
male = male_dict[male]

age = st.number_input("Age",10,90)

currentSmoker = st.selectbox("currentSmoker",["Yes","No"])
currentSmoker_dict={"Yes":1, "No": 0}
currentSmoker=currentSmoker_dict[currentSmoker]

cigsPerDay = st.number_input("cigsPerDay",0,100)

BPMeds = st.selectbox("BPMeds",["Yes" , "No"])
BPMeds_dict={"Yes":1, "No": 0}
BPMeds=BPMeds_dict[BPMeds]

prevalentStroke = st.selectbox("prevalentStroke",["Yes" , "No"])
prevalentStroke_dict={"Yes":1, "No": 0}
prevalentStroke=prevalentStroke_dict[prevalentStroke]

prevalentHyp = st.selectbox("prevalentHyp",["Yes" , "No"])
prevalentHyp_dict={"Yes":1, "No": 0}
prevalentHyp=prevalentHyp_dict[prevalentHyp]

diabetes = st.selectbox("diabetes",["Yes" , "No"])
diabetes_dict={"Yes":1, "No": 0}
diabetes=diabetes_dict[diabetes]

totChol = st.number_input("totChol",0,700)
sysBP = st.number_input("sysBP",0,200)
diaBP = st.number_input("diaBP",0,100)
BMI = st.number_input("BMI",0,100)
heartRate = st.number_input("heartRate",0,100)
glucose = st.number_input("glucose",0,200)


button = st.button("SUBMIT")
bank_model_pkl = r'C:\\Users\\Anish Avasthi\\Desktop\\Sunstone\\random_for_heart.pkl'
loaded_model = joblib.load(bank_model_pkl)

x = np.array([[male ,age , currentSmoker,cigsPerDay ,	BPMeds	,prevalentStroke, prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI ,heartRate , glucose ]])

predicted_value =  loaded_model.predict(x)

decode_dict = {0:"No", 1:"Yes"}

predicted_name = decode_dict[predicted_value[0]]

if button:
    st.info(predicted_value)
    st.info(predicted_name)

