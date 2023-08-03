from collections import Counter
from itertools import count
import streamlit as st
import plotly.express as px
import pandas as pd
import os
import seaborn as sns
import warnings
import numpy as np
import altair as alt
from altair_saver import save
import altair_viewer
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
df["Date"] = pd.to_datetime(df["Date"])

#getting the min and max date
startDate= pd.to_datetime(df["Date"]).min()
endDate= pd.to_datetime(df["Date"]).max()
with col1:
    date =pd.to_datetime(st.date_input("startDate",startDate))

with col2:
    date2 =pd.to_datetime(st.date_input("startDate",endDate))

df= df[(df["Date"] >= date) & (df["Date"] <= date2)].copy()

#Plotting the chart
#Maximum temperature and precipitation based on daily data and count of weathwe categories
st.subheader('Maximum temperature and precipitation based on daily data and count of weather categories')
scale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
)
color = alt.Color("Weather:N", scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=["x"])
click = alt.selection_multi(encodings=["color"])

# Top panel is scatter plot of temperature vs time
points = (
    alt.Chart()
    .mark_point()
    .encode(
        alt.X("monthdate(Date):T",
              title="Date"),
        alt.Y(
            "Temp_max:Q",
            title="Maximum Daily Temperature (C)",
            scale=alt.Scale(domain=[-5, 40]),
        ),
        color=alt.condition(brush, color, alt.value("lightgray")),
        size=alt.Size("Precipitation:Q", scale=alt.Scale(range=[5, 200])),
    )
    .properties(width=550, height=300)
    .add_selection(brush)
    .transform_filter(click)
)


# Bottom panel is a bar chart of weather type
bars = (
    alt.Chart()
    .mark_bar()
    .encode(
        x="count()",
        y="Weather:N",
        color=alt.condition(click, color, alt.value("lightgray")),
    )
    .transform_filter(brush)
    .properties(
        width=550,
    )
    .add_selection(click)
)

chart = alt.vconcat(points, bars, data=df, title="Seattle Weather: 2012-2015")

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)
    
    
    
    
#Maximum temperature and precipitation based on daily data and count of weathwe categories
st.subheader('Minimum temperature and precipitation based on daily data and count of weather categories')
scale = alt.Scale(
    domain=["sun", "fog", "drizzle", "rain", "snow"],
    range=["#e7ba52", "#a7a7a7", "#aec7e8", "#1f77b4", "#9467bd"],
)
color = alt.Color("Weather:N", scale=scale)

# We create two selections:
# - a brush that is active on the top panel
# - a multi-click that is active on the bottom panel
brush = alt.selection_interval(encodings=["x"])
click = alt.selection_multi(encodings=["color"])

# Top panel is scatter plot of temperature vs time
points = (
    alt.Chart()
    .mark_point()
    .encode(
        alt.X("monthdate(Date):T",
              title="Date"),
        alt.Y(
            "Temp_min:Q",
            title="Minimum Daily Temperature (C)",
            scale=alt.Scale(domain=[-5, 40]),
        ),
        color=alt.condition(brush, color, alt.value("lightgray")),
        size=alt.Size("Precipitation:Q", scale=alt.Scale(range=[5, 200])),
    )
    .properties(width=550, height=300)
    .add_selection(brush)
    .transform_filter(click)
)


# Bottom panel is a bar chart of weather type
bars = (
    alt.Chart()
    .mark_bar()
    .encode(
        x="count()",
        y="Weather:N",
        color=alt.condition(click, color, alt.value("lightgray")),
    )
    .transform_filter(brush)
    .properties(
        width=550,
    )
    .add_selection(click)
)

chart = alt.vconcat(points, bars, data=df, title="Seattle Weather: 2012-2015")

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Altair native theme"])

with tab1:
    st.altair_chart(chart, theme="streamlit", use_container_width=True)
with tab2:
    st.altair_chart(chart, theme=None, use_container_width=True)

##Time series analysis
###for temp_max
df["month_year"] = df["Date"].dt.to_period("M")
st.subheader('Time Series Analysis for maximum temperature according to months')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))
                         ["Temp_max"].max()).reset_index()
fig2=px.line(linechart, 
             x="month_year",
             y="Temp_max", 
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
df["month_year"] = df["Date"].dt.to_period("M")
st.subheader('Time Series Analysis for minimum temperature according to months')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))
                         ["Temp_min"].min()).reset_index()
fig2=px.line(linechart, 
             x="month_year" ,
             y="Temp_min", 
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
df["month_year"] = df["Date"].dt.to_period("M")
st.subheader('Time Series Analysis for getting maximum percipitation according to month')

linechart = pd.DataFrame(df.groupby(df["month_year"].dt.strftime("%Y : %b"))
                         ["Precipitation"].max()).reset_index()
fig2=px.line(linechart, 
             x="month_year" ,
             y="Precipitation", 
             height=500, 
             width = 1000, 
             template="gridon")

st.plotly_chart(fig2,use_container_width=True)
#download the data based on the chart
with st.expander("view Data of TimeSeries: "):
    st.write(linechart.T.style.background_gradient(cmap="Blues"))
    csv = linechart.to_csv(index=False).encode("utf-8")
    st.download_button('Download Data', data = csv, file_name = "TimeSeries.csv") 












   








    










   








    



