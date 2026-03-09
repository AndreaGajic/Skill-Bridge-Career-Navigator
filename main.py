import streamlit as st

# Define your navigation
pg = st.navigation([
    st.Page("pages/app.py", title="Career Navigator"),
    st.Page("pages/roles_list.py", title="Role Descriptions"),
])

pg.run()