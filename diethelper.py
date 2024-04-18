import os
import re
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI  # Updated import statement
from langchain.chains import LLMChain

os.environ["OPENAI_API_KEY"] = "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"

# Instantiate the OpenAI class
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

# Define input data
input_data = {
    'age': 21,
    'gender': 'female',
    'weight': 50,
    'height': 5,
    'veg_or_nonveg': 'veg',
    'disease': 'sugar',
    'allergies': 'Latex Allergy',
    'foodtype': 'Fruits'
}

# Invoke the LLMChain
results_dict = chain_resto.invoke(input_data)

# Extract the text content from the dictionary
results_text = results_dict["text"]

# Print the results
print(results_text)

# Extract recommendations
breakfast_nameslist = re.findall(r'Breakfast Names:(.*?)Dinner Names:', results_text, re.DOTALL)
Dinner_nameslist = re.findall(r'Dinner Names:(.*?)Workout Names:', results_text, re.DOTALL)
workout_nameslist = re.findall(r'Workout Names:(.*?)$', results_text, re.DOTALL)

# Process and print recommendations
if breakfast_nameslist:
    breakfast_names = [name.strip() for name in breakfast_nameslist[0].strip().split('\n') if name.strip()]
if Dinner_nameslist:
    dinner_names = [name.strip() for name in Dinner_nameslist[0].strip().split('\n') if name.strip()]
if workout_nameslist:
    workout_names = [name.strip() for name in workout_nameslist[0].strip().split('\n') if name.strip()]

print("Recommendation breakfast:",breakfast_names)
print("Recommendation dinner:", dinner_names)
print("Recommendation workout:", workout_names)
