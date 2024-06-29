#!/usr/bin/env python
# coding: utf-8

# In[25]:


import streamlit as st

# Define the tax_collection function
def tax_collection(tax_amount, tax_rate, income):
    if tax_amount == income * tax_rate:
        return "Thank you for paying your tax honestly"
    elif tax_amount > income * tax_rate:
        return "You have overpaid your taxes due and shall be refunded the extra amount shortly"
    elif tax_amount < income * tax_rate:
        return "You have not fully paid your tax and pay before penalty gets imposed by FBR"
    else:
        return tax_amount

# Streamlit app
st.title("Tax Collection Application")

# Input fields
income = st.number_input("Enter your income:", min_value=0.0, step=0.01, format="%.2f")
tax_rate = st.number_input("Enter the tax rate (as a decimal):", min_value=0.0, max_value=1.0, step=0.01, format="%.2f")
tax_amount = st.number_input("Enter the tax amount paid:", min_value=0.0, step=0.01, format="%.2f")

# Button to calculate tax collection status
if st.button("Check Tax Payment Status"):
    # Check if inputs are valid
    if income is None or tax_rate is None or tax_amount is None:
        st.write("Please enter all values to check tax payment status.")
    else:
        result = tax_collection(tax_amount, tax_rate, income)
        st.write(result)

tax_amount = st.number_input("Enter the tax amount paid:", min_value=0.0, step=0.01, format="%.2f")

