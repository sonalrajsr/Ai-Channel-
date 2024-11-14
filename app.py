import streamlit as st
import pandas as pd
from src.data_loader import load_csv_data, fetch_google_sheet_data
from src.search_api import perform_search_for_all_entities
from src.llm_parser import parse_info

# Streamlit app configuration
st.title("AI Agent Dashboard")
st.subheader("Upload a CSV file or connect a Google Sheet")

# File upload section
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
data = None
if uploaded_file:
    data = load_csv_data(uploaded_file)
    st.write("Data Preview", data.head(10))

# Google Sheets connection section
st.subheader("Connect Google Sheets")
sheet_id = st.text_input("Google Sheet ID")
range_name = st.text_input("Range (e.g., 'Sheet1!A1:D10')")
if sheet_id and range_name:
    data = fetch_google_sheet_data(sheet_id, range_name)
    st.write("Data Preview", data.head())

# Dynamic query input for web search
st.subheader("Define Search Query")
query_template = st.text_input("Enter your query template (e.g., 'Get the email address of {company}')")

# Column selection for entities
if data is not None:
    selected_column = st.selectbox("Select the column with entities", data.columns)

# Custom prompt for information extraction
st.subheader("Define Extraction Prompt")
extraction_prompt = st.text_input("Enter extraction prompt (e.g., 'Extract the email address of {company} from the following web results.')")

# Perform search and extract information
if st.button("Fetch and Extract Information"):
    if data is not None and query_template and extraction_prompt:
        # Get list of entities from the selected column
        entities = data[selected_column].tolist()
        
        # Perform search for all entities using the query template
        search_results = perform_search_for_all_entities(query_template, entities)
        st.write("Search Results:", search_results)
        
        # Extract information based on the custom extraction prompt
        extracted_data = parse_info(search_results, extraction_prompt)
        st.write("Extracted Information:", extracted_data)
        
        # Output section to download extracted data as CSV
        output_df = pd.DataFrame.from_dict(extracted_data, orient="index", columns=["Extracted Info"])
        st.download_button("Download CSV", output_df.to_csv(index=False), "extracted_info.csv")
    else:
        st.warning("Please upload a file, enter both search and extraction prompts, and select a column.")
