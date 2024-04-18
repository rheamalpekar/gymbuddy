import streamlit as st 
import pandas as pd
from streamlit.components.v1 import html

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)


def main():
 with open ('style.css') as f:
  st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

st.markdown(" # Welcome to Gymbuddy")
st.image('Gym background.jpg')
col1,col2,col3=st.columns(3,gap='large')
with col1:
   st.image("calculator.png")
   st.markdown(' ##### <a href="bmi_cal" target="_self">  BMI Calculator</a>', unsafe_allow_html=True)
  
with col2:
   st.image("upcoming.png") 
   st.markdown(' ##### <a href="/bmi_calculator" target="_self"> Exercise Scheduler</a>', unsafe_allow_html=True)
 

with col3:
  st.image("guide.png")
  st.markdown(' ##### <a href="/bmi_calculator" target="_self">Guide Book</a>', unsafe_allow_html=True)
 

with col1:
   st.image("muscle.png")
   st.markdown(' ##### <a href="/bmi_cal" target="_self">Muscle/Fat Calculator</a>', unsafe_allow_html=True)
 

with col2:
   st.image("heartbeat.png")
   st.markdown(' ##### <a href="/bmi_calculator" target="_self">Cardiac Health</a>', unsafe_allow_html=True)
   
with col3:
  st.image("nutrition-plan.png")
  st.markdown(' ##### <a href="/diet" target="_self">Diet Predictor</a>', unsafe_allow_html=True)
 

with col2:
 st.image("exercise-routine.png")
 st.markdown(' ##### <a href="/exercise" target="_self"> Gym-Buddy</a>', unsafe_allow_html=True)


with st.sidebar:
 st.title("Hi USERS!!!")
 st.button("Todays Activities")
 st.button("Generate daily Report")
 st.page_link("/login.py", label="Login", icon="🌎")
 st.page_link("/caloriecounter.py", label="Calorie Counter")

