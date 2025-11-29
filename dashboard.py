import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.title("My Name is Garvit")
st.text("Welcome to Dashboard")
st.header("I am a header")
st.write("you can write : ",10+5)
name = st.text_input("Enter your name :")
age = st.number_input("Enter your age : ")
st.write("your name is : ",name,"your age is : ",age)
st.selectbox("Enter your course :",["BCA","B.tech","MCA"])
if st.button("CLICK ME"):
    st.success("Clicked button")
file = st.file_uploader("Uplload your file")
if file:
    content = file.read()
    st.write("File uploaded successfully..")

data = {"Name" : ["tom","jack"],"marks" : [10,20]}
df =pd.DataFrame(data)
st.dataframe(df)

data = pd.DataFrame({
    "Marks" : [10,20,20,10]
})
st.line_chart(data)
st.bar_chart(data)
subject = [["Python"], ["c++"], ["Java"]]
marks = [20,10,5]

fig , ax= plt.subplots()
ax.pie(marks,labels = subject,autopct='%1.1f%%')
st.pyplot(fig)