import streamlit as st

st.title("BMI Calculator")

height = st.slider("Enter your height slider (in cm's):", 100, 250, 175)
weight = st.slider("Enter your weight slider(in KG's):", 40, 200, 70)

bmi = weight/((height/100) **2)

st.write(f"Your BMI is: {bmi:.2f}")

st.write("### BMI Categories ###")
if bmi <18.5:
    st.write("Underweight: BMI less than 18.5")
elif 18.51 < bmi <24.9:
    st.write("Normal weight: BMI between 18.51 and 24.9")
elif 24.91 < bmi < 30.0:
    st.write("Over weight: BMI between 24.91 and 30.0")
else:
    st.write("Obesity: BMI 30 or greater")