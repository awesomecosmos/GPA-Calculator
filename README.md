# GPA-Calculator

This is an app to calculate your Grade Point Average for a course, in terms of a percentage. Play with it on [Streamlit](https://awesomecosmos-gpa-calculator-appmain-yvvhgc.streamlit.app/)!

## Authors

- [@awesomecosmos](https://www.github.com/awesomecosmos) (me!)

## Table of Contents

  - [Introduction](#introduction)
  - [How It Works](#how-it-works)
  - [About The App](#about-the-app)
  
## Introduction
I am currently pursuing my MS in Data Science, and it is really important to track my grades, to make sure I satisfy all registration requirements. Ordinarily, I have a neat color-coded Excel spreadsheet on my desktop to continously enter my grades and track them. However, sometimes I would love to be able to do this on-the-go, which is why I developed this [web app](https://awesomecosmos-gpa-calculator-appmain-yvvhgc.streamlit.app/). It is my hope that other students can also use this app to calculate their course percentages, and therefore estimate their GPA!

## How It Works
Assuming that all assignments in the course have a percentage of the total grade assigned to them, and you earn a percentage on each of those assignments, this app returns how much of the final grade (100%) you have earned so far. For example, let's say there are 4 assignments in your course, worth 20%, 20%, 30% and 30% respectively (called 'weight'), adding up to 100%. Let's say you earned 96.4%, 97.8%, 89.1% and 95.5% (called 'percent_obtained') on each of the assignments respectively. The app will calculate your final percentage, in this case, 94.22%. You can compare this final percentage against your school's GPA scale, and estimate what final grade you will get.

At my school, a final course grade of 94.22% gives me an A grade, which translates to a 4.0 on my school's GPA scale. Not bad!

## About The App
This app was built in Streamlit using Python. Check out the ```app/main.py``` for a look at the code!

<img src="https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif"
