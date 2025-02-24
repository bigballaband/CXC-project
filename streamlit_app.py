import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

# Define the Markov chain predictions as a DataFrame
markov_predictions = pd.read_csv("predictions.csv")
sampleData = pd.read_csv("sampleData.csv")


# Streamlit app title
st.title("CxC Project Dashboard, Federato")

# Display the Markov chain predictions
st.header("Markov Chain Model Predictions:")
st.text("Given the current event, the event most likely to happen is next event. This was implemented using a markov chain training model.")
st.dataframe(markov_predictions)

st.subheader("Our model prediction accuracy is 54%.")

# Load and display the workflow diagrams
st.header("Workflow Diagrams:")
st.text("These are the five most common event types within the 2025 dataset.")

# Function to load and display HTML files
def display_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    html(html_content, height=600)

# Display each workflow diagram
st.subheader("All Accounts Configurable Table Render Event Transitions")
display_html("_all-accounts_configurable-table_render_event_transitions.html")

st.subheader("Account Lines Layout Render Event Transitions")
display_html("account-lines__layout_render_event_transitions.html")

st.subheader("Application Window Opened Event Transitions")
display_html("application-window-opened_event_transitions.html")

st.subheader("Dashboard My Book Layout Render Event Transitions")
display_html("dashboard_my-book_layout_render_event_transitions.html")

st.subheader("Session End Event Transitions")
display_html("session_end_event_transitions.html")

