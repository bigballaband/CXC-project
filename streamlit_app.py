import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

# Define the Markov chain predictions as a DataFrame
markov_predictions = pd.read_csv("predictions.csv")

# Streamlit app title
st.title("Workflow Dashboard")

# Display the Markov chain predictions
st.header("Markov Chain Predictions")
st.dataframe(markov_predictions)

# Load and display the workflow diagrams
st.header("Workflow Diagrams")

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

# Run the Streamlit app
if __name__ == "__main__":
    st.write("Interactive Dashboard is running...")
