import streamlit as st
import os
import re
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain

st.header("Diet and Workout Recommendation System")

col1, col2 = st.columns(2)

age = col1.number_input("Age")
gender = col2.selectbox("Gender", ["Female", "Male"])
weight = col1.number_input("Weight (kg)")
height = col2.number_input("Height(m)")
pref = col1.text_input("Veg or Non Veg")
dis = col2.text_input("Generic Disease")
food = col1.text_input("Food Type")
allergy = col2.text_input("Allergies")

# Button to trigger recommendation

    # Instantiate the OpenAI class
os.environ["OPENAI_API_KEY"] = "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"
llm_resto = OpenAI(temperature=0.6)

    # Define the prompt template
prompt_template_resto = PromptTemplate(
input_variables=["age", "gender", "weight", "height", "veg_or_nonveg", "disease", "allergies", "foodtype"],
template="Diet Recommendation System:\n"
                 "I want you to recommend 6 breakfast names, 6 dinner names, and 6 workout names, "
                 "based on the following criteria:\n"
                 "Person age: {age}\n"
                 "Person gender: {gender}\n"
                 "Person weight: {weight}\n"
                 "Person height: {height}\n"
                 "Person veg_or_nonveg: {veg_or_nonveg}\n"
                 "Person generic disease: {disease}\n"
                 "Person allergies: {allergies}\n"
                 "Person's foodtype: {foodtype}"
)

    # Create the LLMChain object with the OpenAI instance
chain_resto = LLMChain(llm=llm_resto, prompt=prompt_template_resto)

    # Define input data based on user input
input_data = {
        'age': age,
        'gender': gender.lower(),
        'weight': weight,
        'height': height,
        'veg_or_nonveg': pref.lower(),
        'disease': dis,
        'allergies': allergy,
        'foodtype': food
}

    # Invoke the LLMChain
results_dict = chain_resto.invoke(input_data)

    # Extract the text content from the dictionary
results_text = results_dict["text"]

    # Extract recommendations
breakfast_nameslist = re.findall(r'Breakfast Names:(.*?)Dinner Names:', results_text, re.DOTALL)
Dinner_nameslist = re.findall(r'Dinner Names:(.*?)Workout Names:', results_text, re.DOTALL)
workout_nameslist = re.findall(r'Workout Names:(.*?)$', results_text, re.DOTALL)

    # Process and display recommendations
if breakfast_nameslist:
    breakfast_names = [name.strip() for name in breakfast_nameslist[0].strip().split('\n') if name.strip()]
    
    dinner_names = [name.strip() for name in Dinner_nameslist[0].strip().split('\n') if name.strip()]
      
if workout_nameslist:
    workout_names = [name.strip() for name in workout_nameslist[0].strip().split('\n') if name.strip()]
        

if st.button("Recommend Diet", type="primary"):
     st.write("Recommendation workout:", workout_names)
     st.write("Recommendation dinner:", dinner_names)
     st.write("Recommendation breakfast:", breakfast_names)