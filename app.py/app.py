import streamlit as st
from snowflake.snowpark.context import get_active_session

st.set_page_config(layout="wide")
st.title("Enterprise Analytics Dashboard")

session = get_active_session()

df = session.sql(
    "SELECT * FROM ENTERPRISE_DB.GOLD.VW_EXEC_SUMMARY"
).to_pandas()

st.dataframe(df)

