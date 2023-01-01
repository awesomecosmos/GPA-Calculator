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

# option to download template CSV
template_csv = pd.DataFrame([{
    'assignment_name':'Homework #1',
    'weight':20,
    'percent_obtained':96.4,
}]).reset_index(drop=True)

# title of app
st.title('GPA-Percentage Calculator')

col1, col2 = st.columns(2)

# with col1:
st.sidebar.write("This is an app to calculate your Grade Point Average for a course, in terms of a percentage.")
st.sidebar.write("Assuming that all assignments in the course have a percentage of the total grade assigned to them, and you earn a percentage on each of those assignments, this app returns how much of the final grade (100%) you have earned so far.")
st.sidebar.write("For example, in the table on the right, there are 4 assignments in this course, worth 20%, 20%, 30% and 30% respectively (called 'weight'), adding up to 100%. Let's say you earned 96.4%, 97.8%, 89.1% and 95.5% (called 'percent_obtained') on each of the assignments respectively.")
st.sidebar.write("The app will calculate your final percentage, in this case, 94.22%. You can compare this final percentage against your school's GPA scale, and estimate what final grade you will get.")
st.sidebar.write("At my school, a final course grade of 94.22% gives me an A grade, which translates to a 4.0 on my school's GPA scale. Not bad!")

with col1:
    st.markdown("## Upload your grades for a course here")

    # giving example of CSV
    st.write("Upload a CSV in this format (column names must be exactly these):")
    st.write(example_df)

    # giving template to user
    template = convert_df(template_csv)
    st.download_button(
        label='Download a template CSV like this to fill in!',
        data=template,
        file_name='template_grades.csv',
        mime='text/csv',
    )

    # option for user to upload their CSV
    uploaded_file = st.file_uploader("Upload a CSV:")

with col2:
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
        pass