import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Job Requirements Dashboard", layout="wide")

try:
    df_jobs = pd.read_csv("data/jobs.csv")
    df_skills = pd.read_csv("data/top_skills.csv")
except FileNotFoundError as e:
    st.error(f"File not found: {e.filename}")
    st.stop()

st.title("Job Requirements Dashboard")
st.markdown("Visualization of key requirements in Data Science, ML, and Python job postings.")

st.subheader("Top 10 Most In-Demand Skills")
top_10 = df_skills.head(10)
fig1, ax1 = plt.subplots()
ax1.barh(top_10["skill"][::-1], top_10["count"][::-1], color="skyblue")
ax1.set_xlabel("Mentions")
ax1.set_title("Most Frequent Skills")
st.pyplot(fig1)

st.subheader("Experience Level Distribution")
exp_counts = df_jobs["experience"].fillna("Not specified").value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(exp_counts, labels=exp_counts.index, autopct="%1.1f%%", startangle=90)
ax2.set_title("Experience Requirements")
st.pyplot(fig2)

st.subheader("Job Postings by Region")
area_counts = df_jobs["area"].value_counts().head(10)
fig3, ax3 = plt.subplots()
sns.barplot(y=area_counts.index, x=area_counts.values, ax=ax3, palette="viridis")
ax3.set_xlabel("Number of Job Postings")
ax3.set_title("Top 10 Regions")
st.pyplot(fig3)
