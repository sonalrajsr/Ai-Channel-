import streamlit as st
import pandas as pd
import json
from src.data_loader import load_csv_data, fetch_google_sheet_data
from src.search_api import perform_search_for_all_entities
from src.llm_parser import parse_info

# Header Streamlit Page
st.title("AI Agent Dashboard")
st.subheader("Upload a CSV file or connect a Google Sheet")

# File upload section
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
data = None
json_data = None  # Initialize JSON data

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
st.subheader("Define Search Query (Web Search)")
query_template = st.text_input("Enter your query template (Place holder can be passed like : {company})")

# Column selection for entities
if data is not None:
    selected_column = st.selectbox("Select the column with entities", data.columns)
    st.write("Entities are:", data[selected_column].tolist())

# Custom prompt for information extraction
st.subheader("Define Extraction Prompt (LLM)")
extraction_prompt = st.text_input("Enter extraction prompt (Place holder can be passed like : {company})")

# Convert CSV to JSON based on selected column
if data is not None and selected_column:
    # Group data by the selected column and convert to JSON format
    grouped_data = {}
    for item, group in data.groupby(selected_column):
        grouped_data[item] = group.drop(columns=[selected_column]).to_dict(orient="records")

    # Convert the grouped data dictionary to JSON string
    json_data = json.dumps(grouped_data, indent=4)


# Perform search, extract information, and pass JSON to LLM
if st.button("Fetch and Extract Information"):
    if data is not None and query_template and extraction_prompt and json_data:
        # List of all entities from the selected column
        entities = data[selected_column].tolist()
        
        # Perform search for each entity and get snippets
        search_results = perform_search_for_all_entities(query_template, entities)
        st.write(search_results)
 
        # Pass the combined input to the LLM for extraction
        extracted_data = parse_info(search_results, extraction_prompt, json_data)
        st.write("Extracted Information:", extracted_data)

        # Convert extracted data to a DataFrame for download
        output_df = pd.DataFrame.from_dict(extracted_data, orient="index", columns=["Extracted Info"])
        st.download_button("Download CSV", output_df.to_csv(index=False), "extracted_info.csv")
    else:
        st.warning("Please upload a file, enter both search and extraction prompts, and select a column.")