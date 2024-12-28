# Importing Required libraries
import streamlit as st
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

# Parsing the data from text files.

source_files = Path(r"diary/").glob("*.txt")
filenames = []
scores = []
for files in source_files:
    filenames.append(files.stem)
    with open(files,"r") as text_files:
        diary = text_files.read()
    analyser = SentimentIntensityAnalyzer()
    scores.append(analyser.polarity_scores(diary))

# Filtering the data required.

pos_scores = [scores[i]['pos'] for i in range(len(scores))]
neg_scores = [scores[i]['neg'] for i in range(len(scores))]
pos_fig = px.line(x=filenames,y=pos_scores,title="Postive Analysis Graph"
                  ,markers=True,labels={"x":"Date/File","y":"Positive Score"})
neg_fig = px.line(x=filenames,y=neg_scores,title="Negative Analysis Graph"
                  ,markers=True,labels={"x":"Date/File","y":"Positive Score"})
rel_fig = px.scatter(x=pos_scores,y=neg_scores,color=filenames,title="Relationship between Positive and Negative Scores"
                  ,labels={"x":"Negative Score","y":"Positive Score","color":"File Name"})

# Creating the streamlit UI

st.header("Showing Positive and Negative Sentiment Analysis")
st.divider()
if st.button("Positve Score Chart",help="Click me"):
    st.plotly_chart(pos_fig,theme="streamlit",use_container_width=True)
    st.write("The chart above shows the quantitative data of positivity in the text files marked as date")
if st.button("Negative Score Chart",help="Click me"):
    st.plotly_chart(neg_fig,theme="streamlit",use_container_width=True)
    st.write("The chart above shows the quantitative data of negativity in the text files marked as date")
if st.button("Positive and Negetive Relation"):
    st.plotly_chart(rel_fig,theme="streamlit",use_container_width=True)
    
