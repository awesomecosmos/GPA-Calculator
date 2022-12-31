import streamlit as st
import pandas as pd
import numpy as np

st.title('GPA Tracker')

def bearing_on_final_grade(weight, percent_obtained):
    bearing_on_final_grade_percent = (weight * percent_obtained) / 100
    return (bearing_on_final_grade_percent)

col1, col2, col3 = st.columns(3)

with col1:
    assignment_name = st.text_input(
    "Name of assignment:",
    "Homework #1",
    key="placeholder1",)

with col2:
    weight = st.text_input(
    "Enter the percentage this assignment is worth of your final grade, as a number:",
    20,
    key="placeholder2",)

with col3:
    percent_obtained = st.text_input(
    "Enter the percentage you earned on this assignment, as a number:",
    96.4,
    key="placeholder3",)

percent_earned = bearing_on_final_grade(float(weight), float(percent_obtained))
st.write("You earned: {}% out of a total of {}% on {}.".format(percent_earned, weight, assignment_name))

df = pd.DataFrame([{
    'Assignment Name':assignment_name,
    'Weight of Assignment (%)':float(weight),
    'Percentage Earned (%)':float(percent_obtained),
}])

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(df)

st.download_button(
    label="Download as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)