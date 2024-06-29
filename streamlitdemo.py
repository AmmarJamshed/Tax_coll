#!/usr/bin/env python
# coding: utf-8

# In[25]:


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


# In[26]:


tax_collection(0,0.2,120)


# In[27]:


import streamlit as st


# In[28]:


# Streamlit app
st.title("Tax Collection Application")


# In[29]:


# Button to calculate tax collection status
if st.button("Check Tax Payment Status"):
    if income > 0 and tax_rate > 0 and tax_amount >= 0:
        result = tax_collection(tax_amount, tax_rate, income)
        st.write(result)
    else:
        st.write("Please enter all values to check tax payment status.")


# In[30]:


# Input fields
income = st.number_input("Enter your income:", min_value=0.0, step=0.01, format="%.2f")
tax_rate = st.number_input("Enter the tax rate (as a decimal):", min_value=0.0, max_value=1.0, step=0.01, format="%.2f")
tax_amount = st.number_input("Enter the tax amount paid:", min_value=0.0, step=0.01, format="%.2f")

