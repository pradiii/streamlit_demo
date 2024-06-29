import joblib
import streamlit as st
import numpy as np


model_name = "RF_Loan_model.joblib"  #RF_Loan_model.joblib
model = joblib.load(model_name)

def prediction(Gender,Married,Dependents,Education,Self_Employed,
                            Applicant_Income,CoApplicant_Income,Loan_Amount,Loan_Amount_Term,
                            Credit_History,Property_Area):
    if Gender=="Male":
        Gender=1
    else:
        Gender=0

    if Married=="Yes":
        Married=1
    else:
        Married=0

    if Education=="Graduate":
        Education=0
    else:
        Education=1

    if Self_Employed=="Yes":
        Self_Employed=1
    else:
        Self_Employed=0

    if Credit_History=="Outstanding Loan":
        Credit_History=1
    else:
        Credit_History=0
    
    if Property_Area=="Rural":
        Property_Area=0
    elif Property_Area=="Urban":
        Property_Area=1
    else:
        Property_Area=2

    Total_Income = Applicant_Income+CoApplicant_Income

    prediction = model.predict([[Gender,Married,Dependents,Education,Self_Employed,Loan_Amount,Loan_Amount_Term,
                            Credit_History,Property_Area,Total_Income]])
    
    print(prediction)

    if prediction==0:
        pred = "Rejected" 
    else:
        pred = "Approved"

    print("Streamlit model")
    return pred


def main():
    #Front end 
    
    st.title("Welcome to loan application")
    st.header("please enter details to procede with your prediction")

    Gender  = st.selectbox("Gender",("Male","Female"))
    Married = st.selectbox("Married",("Yes","No"))
    Dependents = st.number_input("Number of dependents")
    Education = st.checkbox("Education",("Graducate","Not Graducate"))
    Self_Employed = st.selectbox("Self_Employed",("Yes","No"))
    Applicant_Income = st.number_input("Applicant Income")
    CoApplicant_Income = st.number_input("CoApplicant Income")
    Loan_Amount = st.number_input("Loan Amount")
    Loan_Amount_Term = st.number_input("Loan Amount Term")
    Credit_History = st.selectbox("Credit_History",("Outstanding Loan","Not Outstanding loan"))
    Property_Area = st.selectbox("Property Area",("Rural","Urban","Semi Urbanm"))


    if st.button('Predict'):
        result = prediction(Gender,Married,Dependents,Education,Self_Employed,
                            Applicant_Income,CoApplicant_Income,Loan_Amount,Loan_Amount_Term,
                            Credit_History,Property_Area)
        
        if result == "Approved":
            st.success("Your loan application is Approved")

        else:
            st.error("Your loan application is Rejected")




if __name__=="__main__":
    main()