import streamlit as st
import json

@st.cache_data
def load_data():
    with open("data.json", "r") as f:
        return json.load(f)

st.title("Role Descriptions")
data = load_data()

for role, details in data["roles"].items():
    st.subheader(role)
    st.write(details.get("summary", "No description available."))
    st.divider()