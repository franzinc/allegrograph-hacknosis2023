import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config (page_title="Readmission Dashboard", page_icon=":bar_chart:", layout="wide")

#-- Read readmission encounters list
@st.cache_data
def get_readmissions():
    df = pd.read_csv('readmit_df.csv')
    return df

df_readmit = get_readmissions()

@st.cache_data
def get_predictions():
    df = pd.read_csv('predict_readmit.csv')
    return df

df_predict = get_predictions()
df_predict.sort_values(by=['score'], ascending=False, inplace=True)

#--- SIDE-BAR ---
st.sidebar.markdown("## 30 Day Readmission Metric: ")
st.sidebar.markdown("The 30-day re-admissions metric is a healthcare performance indicator that measures the rate at which patients are readmitted to a hospital within 30 days of their initial discharge for the same or a related medical condition. This metric is used to assess the quality of care provided by healthcare facilities and to identify potential issues in patient care transitions, post-discharge follow-up, and overall patient management.")

st.sidebar.markdown("## Risk Prediction Method: ")
st.sidebar.markdown("We use a Recurrent Neural Network (RNN) trained on patient encounter events such as diagnosis, medications and procedure events to predict 30 day readmission risk.")

#--- DASHBOARD

st.markdown("# 30-Day Readmissions Dashboard.")

col1, col2 = st.columns(2)

with col1:
    st.header("Top 10 Reasons for Readmission")
    st.bar_chart(df_readmit.groupby (['reason', 'gender']).size ().unstack(level=1).sort_values (by=['F','M'], ascending=False).head (10))

with col2:
    st.header("Readmission Rate")
    st.metric(label="", value="35%")

st.header("High risk patient(s) for 30 day readmissions (Predicted):")
st.dataframe(df_predict[['first', 'last','gender','score']].head(10), 
             column_config={"first": "First Name",
                            "last": "Last Name",
                            "gender": "Gender",
                            "score": "Risk Score"},
             hide_index=True,
             use_container_width=True)

