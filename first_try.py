#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 23:06:49 2025

@author: pranavrevankar
"""

import pandas as pd
import streamlit as st
import numpy as np
#import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime,time,timedelta


#define function

#load data
@st.cache_data
def load_data():
    df = pd.read_csv("sleep_cycle_productivity.csv")
    df['Date']= pd.to_datetime(df['Date'])
   
    df_no = df[df['Sleep Start Time']>23.00]
    df_eb = df[df['Sleep Start Time']<23.00]
  
    return df, df_eb, df_no

df_agg, df_eb, df_no = load_data()
#engineer data
## What metrics are important?
## Can any new metric or ratios be created?

#build dashboard

add_sidebar = st.sidebar.selectbox("Let's analyse Sleep", 
                                   ("Aggregate metrics","Early Birds","Night owls","How's my sleep?"))


## Aggregate dashboard
if add_sidebar == 'Aggregate metrics':
    df_agg_metrics = df_agg[['Age','Total Sleep Hours','Sleep Quality','Exercise (mins/day)','Screen Time Before Bed (mins)','Productivity Score','Mood Score','Stress Level']]
    df_agg_avg = df_agg_metrics.mean()
    col1, col2, col3, col4 = st.columns(4)
    columns = [col1,col2,col3, col4]

    count =0
    for i in df_agg_avg.index:
        with columns[count]:
            st.metric(i,round(df_agg_avg[i],1))
            count +=1
        if count >=4:
            count =0
    #st.write(df_agg)
    
    appointment = st.slider(
    "Schedule your appointment:", value=(time(11, 30), time(12, 45))
    )
    st.write("You're scheduled for:", appointment)
            


if add_sidebar == 'Early Birds':
    df_eb_metrics = df_eb[['Age','Total Sleep Hours','Sleep Quality','Exercise (mins/day)','Screen Time Before Bed (mins)','Productivity Score','Mood Score','Stress Level']]
    df_eb_avg = df_eb_metrics.mean()
    col1, col2, col3, col4 = st.columns(4)
    columns = [col1,col2,col3, col4]

    count =0
    for i in df_eb_avg.index:
        with columns[count]:
            st.metric(i,round(df_eb_avg[i],1))
            count +=1
        if count >=4:
            count =0
    st.dataframe(data=df_eb)
            
    
if add_sidebar == 'Night owls':
    df_no_metrics = df_no[['Age','Total Sleep Hours','Sleep Quality','Exercise (mins/day)','Screen Time Before Bed (mins)','Productivity Score','Mood Score','Stress Level']]
    df_no_avg = df_no_metrics.mean()
    col1, col2, col3, col4 = st.columns(4)
    columns = [col1,col2,col3, col4]

    count =0
    for i in df_no_avg.index:
        with columns[count]:
            st.metric(i,round(df_no_avg[i],1))
            count +=1
        if count >=4:
            count =0
    st.dataframe(data=df_no)

if add_sidebar == "How's my sleep?":


    today_10pm = datetime.combine(datetime.today(), datetime.min.time()) + timedelta(
    hours=22
    )
    tomorrow_6am = datetime.combine(datetime.today(), datetime.min.time()) + timedelta(
    days=1, hours=6
    )

    sleep_time = st.slider(
    "Choose your sleep time:",
    min_value=(today_10pm),
    max_value=(tomorrow_6am),
    format="hh:mm",
    value=(today_10pm, tomorrow_6am)
    )
    st.write("So you sleep around ", (sleep_time[1]-sleep_time[0]).seconds/3600, " hours")
    
    
    

            
