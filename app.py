# Main Streamlit app file
# This sets up the multi-page structure and runs the dashboard

import streamlit as st

# Import the MultiPage class
from app_pages.multi_page import MultiPage

# Import dashboard page function
from app_pages.dashboard import dashboard_body


# Create app instance
app = MultiPage(app_name="Healthcare Insurance Dashboard")

# Add pages to the app
app.add_page("Insurance Dashboard", dashboard_body)

# Run the app
app.run()