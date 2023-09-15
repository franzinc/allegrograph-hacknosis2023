import pandas as pd
import plotly.express as px
import streamlit as st
import altair as alt

## -- Setup Page title and other page properties
st.set_page_config (page_title="NQF0059:  Diabetes: Hemoglobin A1c (HbA1c) Poor Control (>9%)", page_icon=":bar_chart:", layout="wide")

#-- Read diabetes subtypes list ---
@st.cache_data
def get_diabetes_hier ():
    df = pd.read_csv ('diabetes_hier.csv')
    return df

df_hier = get_diabetes_hier ()

#-- Read diabetes population synthea ---
@st.cache_data
def get_diabetes_cohort():
    df = pd.read_csv ('df_nqf.csv')
    df ['cond_label'] = df['cond'].map(lambda x: next(iter(df_hier[df_hier['cond']==x]['cond_label'].to_list ()), None))
    return df

df_nqf = get_diabetes_cohort()
df_nqf ['age-bin'] = pd.cut(x=df_nqf['age'], bins=[1,10,20,30,40,50,60,70,80,90,100], labels=['0-9','10-19','20-29','30-39','40-49','50-59','60-69','70-79','80-89','90-99'])

defaults = df_nqf ["cond_label"].unique ()

#--- SIDE-BAR ----
st.sidebar.header ("Select Diabetes Sub-Types to Include:")
diseases = st.sidebar.multiselect(
    "Select Diabetes Sub-Types:",
    options=df_hier["cond_label"].unique(),
    default= defaults [defaults != None]  #['Diabetes Mellitus, Insulin-Dependent', 'Diabetes Mellitus, Non-Insulin-Dependent']
)

st.sidebar.header ("Select Age Range:")
age_range = st.sidebar.slider(
    "Select age range:",
    0.0,120.00, (18.0, 75.0)
)

#-- Filter diabetes cohort based on sidebar selection
df_selection = df_nqf[(df_nqf['age'] >= age_range[0]) & (df_nqf['age'] <= age_range[1])]
df_selection = df_selection[df_selection ['cond_label'].isin (diseases)]

#-- PAGE LAYOUT
st.markdown ("# Clinical Quality Metric [NQF0059] - Percentage of patients 18-75 years of age with high hemoglobin A1c reading.")

col1, col2 = st.columns (2)

with col1:
    st.markdown ("### Measure Description")
    st.markdown ("Percentage of patients 18-75 years of age with diabetes who had hemoglobin A1c > 9.0% during the measurement period")

with col2:
    # Metric for uncontrolled diabetes percentage
    st.header ("Uncontrolled Diabetes:")
    categories = df_selection.groupby (['category'], as_index=False).size ()
    st.metric (label="", value=" ".join ([str(next (iter (categories [categories ['category'] == 'UNCONTROLLED DIABETES'] ['size'].to_list ()), None)), "%"]))

st.header ("Cohort Distribution:")

tab1, tab2 = st.tabs (['Cohort distribution by age, gender','Cohort distribution by age, diabetes category'])

with tab1:
    st.bar_chart (df_selection.groupby (['age-bin', 'gender']).size ().unstack (level=1))

with tab2:
    st.bar_chart (df_selection.groupby (['age-bin', 'category']).size ().unstack (level=1))

col1, col2 = st.columns (2)

with col1:
    st.header ("Diabetes subtypes:")

    # pie chart for diabetes subtypes
    c = alt.Chart (df_selection.groupby (['cond_label'], as_index=False).size ()).mark_arc (innerRadius = 50).encode (
        theta = alt.Theta (field='size', type="quantitative"),
        color = alt.Color (field='cond_label', type="nominal")
    )
    st.altair_chart (c, theme='streamlit', use_container_width=True)

with col2:
    st.header ("Diabetes NQF0059 Categories")

    # pie chart for diabetes categories
    c1 = alt.Chart (df_selection.groupby (['category'], as_index=False).size ()).mark_arc (innerRadius = 50).encode (
        theta = alt.Theta (field='size', type="quantitative"),
        color = alt.Color (field='category', type="nominal")
    )
    st.altair_chart (c1, theme='streamlit', use_container_width=True)
