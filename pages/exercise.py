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

st.markdown(" # Exercises: Lets Do it!!!")
col1,col2,col3=st.columns(3,gap='large')
with col1:
   
   st.image("squat_5147228.png") 
   st.markdown(' ##### <a href="/bmi_calculator" target="_self">Squats</a>', unsafe_allow_html=True)
  
with col2:
   st.image("pushup.png") 
   st.markdown(' ##### <a href="/bmi_calculator" target="_self">Pushups</a>', unsafe_allow_html=True)
   
with col3:
  st.image("squats.png")
  st.markdown(' ##### <a href="/bmi_calculator" target="_self">Crunches</a>', unsafe_allow_html=True)
 

with col1:
   st.image("lungesgym.png")
   st.markdown(' ##### <a href="/bmi_calculator" target="_self">Lunges</a>', unsafe_allow_html=True)
   

with col2:
   st.image("side lateral raise.JPG")
   st.markdown(' ##### <a href="/bmi_calculator" target="_self">Side raise</a>', unsafe_allow_html=True)
   

with col3:
  st.image("gympullups.png")
  st.markdown(' ##### <a href="/bmi_calculator" target="_self">Pull-Ups</a>', unsafe_allow_html=True)
 

with col1:
 st.image("gymjumping.png")
 st.markdown(' ##### <a href="/bmi_calculator" target="_self">Jumping-Jack</a>', unsafe_allow_html=True)
 

with col2:
   st.image("gymbicepcurl.png")
   st.markdown(' ##### <a href="/bmi_calculator" target="_self">Bicep-Curl</a>', unsafe_allow_html=True)
  
with col3:
   st.image("overhead.png") 
   st.markdown(' ##### <a href="/bmi_calculator" target="_self">Overhead Dumbbell Press</a>', unsafe_allow_html=True)
   

with col1:
  st.image("glutebridge.JPG")
  st.markdown(' ##### <a href="/bmi_calculator" target="_self">Glute Bridge</a>', unsafe_allow_html=True)


with col2:
   st.image("singlelegdeadlift.jpg")
   st.markdown(' ##### <a href="/bmi_calculator" target="_self">Single Leg Deadlift</a>', unsafe_allow_html=True)
  
with col3:
   st.image("onesquat.png") 
   st.markdown(' ##### <a href="/bmi_calculator" target="_self">Single Leg Squats</a>', unsafe_allow_html=True)
   


with st.sidebar:
 st.title("Hi USERS!!!")
 st.button("Todays Activities")
 st.button("Generate daily Report")

