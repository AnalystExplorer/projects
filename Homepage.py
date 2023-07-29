from collections import Counter
from itertools import count
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import seaborn as sns
import warnings
import numpy as np
warnings.filterwarnings('ignore')
st.set_page_config(page_title= "Your report",page_icon=":bar_chart:",layout="wide")
st.title(":bar_chart: Your Report")
st. markdown('<style> div.block-container {padding-top:1rem;}</style>',unsafe_allow_html=True)

#remove watermark
hide_st_style = """<style>
footer {visibility: hidden;}
</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)

#upload your database
fl=st.file_uploader(":file_folder: Upload a file", type=(["csv","txt","xlsx","xls"]))
if fl is not None:
    filename = fl.name
    st.write(filename)
    df=pd.read_csv(filename, encoding = "ISO-8859-1")
else:
    default_file_path = r"C:\Users\ksswa\OneDrive\Desktop\projects\dataset.csv"
    df =pd.read_csv("dataset.csv", encoding = "ISO-8859-1")
col1, col2 = st.columns((2))
df["date1"] = pd.to_datetime(df["date1"])

#getting the min and max date
startDate= pd.to_datetime(df["date1"]).min()
endDate= pd.to_datetime(df["date1"]).max()
with col1:
    date =pd.to_datetime(st.date_input("startDate",startDate))

with col2:
    date2 =pd.to_datetime(st.date_input("startDate",endDate))

df= df[(df["date1"] >= date) & (df["date1"] <= date2)].copy()

#Plotting the chart
##Time series analysis
###for temp_max
df["month_year"] = df["date1"].dt.to_period("M")
st.subheader('Time Series Analysis for maximum temperature according to months')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))
                         ["temp_max1"].max()).reset_index()
fig2=px.line(linechart, 
             x="month_year",
             y="temp_max1", 
             height=500, 
             width = 1000, 
             template="gridon")

st.plotly_chart(fig2,use_container_width=True)
#download the data based on the chart
with st.expander("view Data of TimeSeries: "):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data = csv, file_name = "TimeSeries.csv") 
###for temp_min
df["month_year"] = df["date1"].dt.to_period("M")
st.subheader('Time Series Analysis for minimum temperature according to months')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))
                         ["temp_min1"].min()).reset_index()
fig2=px.line(linechart, 
             x="month_year" ,
             y="temp_min1", 
             height=500, 
             width = 1000, 
             template="gridon")

st.plotly_chart(fig2,use_container_width=True)
#download the data based on the chart
with st.expander("view Data of TimeSeries: "):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data = csv, file_name = "TimeSeries.csv") 

###for percipitation
df["month_year"] = df["date1"].dt.to_period("M")
st.subheader('Time Series Analysis for getting maximum percipitation according to month')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))
                         ["prediction1"].max()).reset_index()
fig2=px.line(linechart, 
             x="month_year" ,
             y="prediction1", 
             height=500, 
             width = 1000, 
             template="gridon")

st.plotly_chart(fig2,use_container_width=True)
#download the data based on the chart
with st.expander("view Data of TimeSeries: "):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data = csv, file_name = "TimeSeries.csv") 

###for temp_min
df["month_year"] = df["date1"].dt.to_period("Y")
st.subheader('Time Series Analysis for minimum temperature for the year')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))
                         ["temp_min1"].min()).reset_index()
fig2=px.line(linechart, 
             x="month_year" ,
             y="temp_min1", 
             height=500, 
             width = 1000, 
             template="gridon")

st.plotly_chart(fig2,use_container_width=True)
#download the data based on the chart
with st.expander("view Data of TimeSeries: "):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data = csv, file_name = "TimeSeries0.csv")
     
###for temp_max
df["month_year"] = df["date1"].dt.to_period("Y")
st.subheader('Time Series Analysis for maximum temperature for Year')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))
                         ["temp_max1"].max()).reset_index()
fig2=px.line(linechart, 
             x="month_year" ,
             y="temp_max1", 
             height=500, 
             width = 1000, 
             template="gridon")

st.plotly_chart(fig2,use_container_width=True)
#download the data based on the chart
with st.expander("view Data of TimeSeries: "):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data = csv, file_name = "TimeSeries1.csv") 


#Total Count the weather categories according to month
df["month_year"] = df["date1"].dt.to_period("M")
st.subheader('Weathe count ')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))
                         ["weather1"].value_counts()).reset_index()
fig2=px.histogram(linechart, 
             x="weather1",
             height=500, 
             width = 1000, 
             template="gridon")
st.plotly_chart(fig2,use_container_width=True)















   








    










   








    



