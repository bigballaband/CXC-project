import streamlit as st
import pandas as pd
from streamlit.components.v1 import html

# Define the Markov chain predictions as a DataFrame
markov_predictions = pd.DataFrame({
    'current_event': [
        'account-lines::widget:render', 'account-lines::configurable-table:render',
        'account-property-rating:pricing-detail:configurable-table:render', 'submissions:all-exposures::view',
        'submissions:all-exposures:configurable-table:render', 'dashboard:my-book:configurable-table:render',
        'account-lines::layout:render', 'account:::view', 'dashboard:my-book:widget:render',
        'dashboard:my-book::view', ':all-accounts:layout:render', 'application-window-opened',
        'session_end', 'dashboard:my-book:layout:render', 'triaged-submission:triaged_submissions-definition:layout:render',
        '::configurable-table:render', 'account-lines:::view', 'submissions:exposures-create::submit-click',
        'submissions:policy-create:configurable-table:render', 'dashboard:portfolio-insights:widget:render',
        ':all-accounts:configurable-table:render', ':all-accounts:widget:render', 'session_start',
        'action-center:::view', 'account-property-rating:perils:configurable-table:render'
    ],
    'next_event': [
        'account-lines::widget:render', 'account-lines::widget:render',
        'account-property-rating:pricing-detail:configurable-table:render', 'submissions:exposures-create::view',
        'submissions:all-exposures::view', 'dashboard:my-book:widget:render',
        'account-lines:::view', 'account-lines::widget:render', 'dashboard:my-book:configurable-table:render',
        'dashboard:my-book:widget:render', ':all-accounts::view', 'account-property-rating:perils:configurable-table:render',
        'application-window-opened', 'dashboard:my-book::view', 'triaged-submission:triaged_submissions-definition::view',
        '::configurable-table:render', 'account:::view', 'submissions:all-exposures:configurable-table:render',
        'submissions:policy-create::submit-click', 'dashboard:portfolio-insights:layout:render',
        ':all-accounts:widget:render', ':all-accounts:layout:render', 'dashboard:my-book:configurable-table:render',
        'action-center:action-details::view', 'account-property-rating:perils::view'
    ]
})

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
