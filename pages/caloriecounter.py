import streamlit as st 
import pandas as pd


st.title("Calorie Calculator")

height=st.slider("Enter your height (in inches):",40,100,70)
weight=st.slider("Enter your Weight (in pounds):",60,660,100)
age=st.slider("Enter your Age (in years):",2,100,35)
sex=st.text_input("Sex: male/female")
activity_level=st.text_input("sedentary/lightly active/moderately active")
def calculate_bmr(weight, height, age, sex):
    if sex == "male":
        bmr = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    else:
        bmr = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    return bmr

def calculate_daily_calories(bmr, activity_level):
    if activity_level == "sedentary":
        calories = bmr * 1.2
    elif activity_level == "lightly active":
        calories = bmr * 1.375
    elif activity_level == "moderately active":
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725
    return calories

bmr = calculate_bmr(weight, height, age, sex)
calories = calculate_daily_calories(bmr, activity_level)

st.header(f"Your daily intake should be is {calories:.2f} calories")

