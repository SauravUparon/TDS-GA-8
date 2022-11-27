import streamlit as st

st.title('Find largest among 3 given numbers')

num1 = st.number_input("Input first number",  format = "%g")
num2 = st.number_input("Input second number", format = "%g")
num3 = st.number_input("Input third number" , format = "%g")

max_number = max(num1,num2,num3)

if st.button("MAX"):
  st.write("Maximum of the above three numbers {},{} and {} is equal to the {}".format(num1,num2,num3,max_number))

  


