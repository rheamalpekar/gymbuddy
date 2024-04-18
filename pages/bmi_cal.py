import streamlit as st 
import pandas as pd


st.title("BMI Calculator")

height=st.slider("Enter your height (in cms):",100,250,175)
weight=st.slider("Enter your Weight (in Kg):",30,300,50)
bmi=weight / ((height/100) ** 2)

st.header(f"Your BMI is {bmi:.2f}")

st.markdown(" # BMI Categories")
st.markdown("- Under weight : BMI less than 18.5")
st.markdown("- Normal weight : BMI between 18.5 to 24.9")
st.markdown("- Over weight : BMI between 25 to 29.9")
st.markdown("- Obesity : BMI 30 or greater than 30")
