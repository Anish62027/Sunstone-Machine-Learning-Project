import streamlit as st
import numpy as np
import joblib

st.header("Household Income Analysis")
st.sidebar.title("Machine Learning Models")
st.sidebar.markdown("## Household Income Analysis")
st.sidebar.markdown("### Ml Models :- Random Forest")


Age = st.number_input("Age",10,100)

Education_Level = st.selectbox("Education_Level",["Bachelor's","Doctorate", "High School" ,"Master's"])
Education_Level_dist = {"Bachelor's":0,"Doctorate":1, "High School":2 ,"Master's":3}
Education_Level = Education_Level_dist[Education_Level]

Occupation = st.selectbox("Occupation",['Technology', 'Finance', 'Others', 'Education', 'Healthcare'])
Occupation_dist = {'Technology':0, 'Finance':1, 'Others':2, 'Education':3, 'Healthcare':4}
Occupation = Occupation_dist[Occupation]


Number_of_Dependents = st.number_input("Number of Dependents",0,5)


Location = st.selectbox("Location",['Urban', 'Rural', 'Suburban'])
Location_dist = {'Urban':0, 'Rural':1, 'Suburban':2}
Location = Location_dist[Location]

Work_Experience = st.number_input("Work Experience",0,55)

Marital_Status = st.selectbox("Marital_Status",['Married', 'Single', 'Divorced'])
Marital_Status_dist = {'Married':0, 'Single':1, 'Divorced':2}
Marital_Status = Marital_Status_dist[Marital_Status]

Employment_Status = st.selectbox("Employment Status",['Full-time', 'Self-employed', 'Part-time'])
Employment_Status_dist = {'Full-time':0, 'Self-employed':1, 'Part-time':2}
Employment_Status = Employment_Status_dist[Employment_Status]


Household_Size = st.number_input("Household Size",1,7)

Homeownership_Status = st.selectbox("Homeownership Status",['Own', 'Rent'])
Homeownership_Status_dist = {'Own':0, 'Rent':1}
Homeownership_Status = Homeownership_Status_dist[Homeownership_Status]


Type_of_Housing = st.selectbox("Type_of_Housing",['Apartment', 'Single-family home', 'Townhouse'])
Type_of_Housing_dist = {'Apartment':0, 'Single-family home ':1, 'Townhouse':2}
Type_of_Housing = Type_of_Housing_dist[Type_of_Housing]


Gender = st.selectbox("Gender",['Male', 'Female'])
Gender_dist = {'Male':0, 'Female':1}
Gender = Gender_dist[Gender]

Primary_Mode_of_Transportation = st.selectbox("Primary Mode of Transportation",['Public transit', 'Biking', 'Car', 'Walking'])
Primary_Mode_of_Transportation_dist = {'Public transit':0, 'Biking':1, 'Car':2, 'Walking':3}
Primary_Mode_of_Transportation = Primary_Mode_of_Transportation_dist[Primary_Mode_of_Transportation]

Income = st.number_input("Income ",0,1000000)

Income_model = 'C:\\Users\\Anish Avasthi\\Desktop\\Sunstone\\random_for_Income.pkl'

loaded_model = joblib.load(Income_model)

x = np.array([[Age,Education_Level,Occupation,Number_of_Dependents,Location,Work_Experience,Marital_Status,Employment_Status,Household_Size,Homeownership_Status,Type_of_Housing,Gender,Primary_Mode_of_Transportation,Income]])

predicted_value =  loaded_model.predict(x)


button = st.button("SUBMIT")

if button:
    st.text("Income Analysis")
    st.info(predicted_value)


