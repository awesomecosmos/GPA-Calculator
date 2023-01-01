import streamlit as st
import pandas as pd
import numpy as np

#-------------------------------------------------------------------------------
# move these to utils.py
def bearing_on_final_grade(weight, percent_obtained):
    bearing_on_final_grade_percent = (weight * percent_obtained) / 100
    return (bearing_on_final_grade_percent)

def process_csv(df):
    df[['weight', 'percent_obtained']] = df[['weight', 'percent_obtained']].apply(pd.to_numeric)
    df['bearing_on_final_grade'] = bearing_on_final_grade(df['weight'], df['percent_obtained'])
    total_cumulative_grade = np.sum(df['bearing_on_final_grade'])
    return (df, total_cumulative_grade)

@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')
#-------------------------------------------------------------------------------

# example df to display
example_df = pd.DataFrame.from_dict({
    'assignment_name':['Homework #1','Homework #2','Midterm','Final Exam'],
    'weight':[20,20,30,30],
    'percent_obtained':[96.4,97.8,89.1,95.5],
}).reset_index(drop=True)

# title of app
st.title('GPA Calculator')

# option to download template CSV
template_csv = pd.DataFrame([{
    'assignment_name':'Homework #1',
    'weight':20,
    'percent_obtained':96.4,
}]).reset_index(drop=True)

st.markdown("## Upload your grades for a course here")

template = convert_df(template_csv)

st.download_button(
    label='Download a template CSV to fill in!',
    data=template,
    file_name='template_grades.csv',
    mime='text/csv',
)

# option for user to upload their CSV
uploaded_file = st.file_uploader("Upload a CSV:")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    df, total_cumulative_grade = process_csv(df)
    st.markdown("## Here are your grades!")
    st.write(df)
    st.write("You earned: {}% out of a total of 100% of your course grade.".format(total_cumulative_grade))
    calculated_grades = convert_df(df)

    st.download_button(
        label="Download as CSV",
        data=calculated_grades,
        file_name='calculated_grades.csv',
        mime='text/csv',
    )
    
else:
    st.write("Upload a CSV in this format (column names must be exactly these):")
    st.write(example_df)