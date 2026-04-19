import streamlit as st
import pandas as pd
from utils import get_students, get_analytics

st.title("PragyanAI Student Analytics Dashboard")

st.subheader(" All Students ")
res = get_students()

if res.status_code == 200:
    df = pd.DataFrame(res.json())
    if not df.empty:
        st.dataframe(df)
    else:
        st.write("No Student")

st.subheader(" Students Analytics ")

res = get_analytics()

if res.status_code == 200:

    data = res.json()

    st.subheader(" Key Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Avg CGPA", round(data["avg_cgpa"], 2))

    with col2:
        st.metric("Placement Rate", round(data["placement_rate"], 2))

    st.subheader(" Top Students")
    top_df = pd.DataFrame(data["top_students"])
    st.dataframe(top_df)

    st.subheader(" At Risk Students")
    risk_df = pd.DataFrame(data["at_risk_students"])
    st.dataframe(risk_df)

else:
    st.error("Failed to fetch data")
    st.write(res.status_code)
