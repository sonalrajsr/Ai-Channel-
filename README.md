# AI Agent Dashboard

Welcome to the AI Agent Dashboard project! This tool allows you to upload a dataset, perform automated web searches on each entity within the data, and retrieve structured information based on customizable prompts. Designed for ease of use and functionality, this dashboard provides a user-friendly interface that enables quick extraction of information from the web using open-source tools.

---

## Project Overview

The AI Agent Dashboard leverages free resources to build a functional AI agent with no costs involved. It reads through datasets (CSV files or Google Sheets), performs web searches for specified entities, and uses language models to parse search results and extract relevant information. This project showcases skills in web scraping, language model processing, and API integration, providing a real-world application for data enrichment tasks.

### Features
1. **CSV/Google Sheet Data Upload**: Upload a CSV file or connect a Google Sheet directly for data input.
2. **Customizable Prompt Input**: Define queries using placeholders to dynamically replace entities from the dataset.
3. **Automated Web Search**: Perform searches for each entity in the dataset using DuckDuckGo's free API.
4. **Information Extraction**: Use a language model from Hugging Face to process and extract specific information from search results.
5. **Results Display and Download**: View the extracted information in a table format within the dashboard and download the results as a CSV file.

---

## Technologies Used

- **Frontend/UI**: [Streamlit](https://streamlit.io/)
- **Data Handling**: [Pandas](https://pandas.pydata.org/)
- **Search API**: [Serpapi(google)](https://serpapi.com/) (free)
- **Language Model**: [Gorq(Model :- gemma2-9b-it)](https://groq.com/)
- **Backend Language**: Python

---

## Project Structure

The project is organized into modular files and folders, with the following structure:

```plaintext
AI AGENT/
├── myenv/                      # Virtual environment (not included in the repo)
├── src/                        # Source code directory
│   ├── data_loader.py          # Handles data loading from CSV/Google Sheets
│   ├── llm_parser.py           # Processes data using language models
│   ├── search_api.py           # Contains API handling for DuckDuckGo
│   ├── utils/                  # Utility functions
│   │   └── helper_functions.py # Helper functions used across the project
├── .env                        # Environment variable configuration file
├── .gitignore                  # Git ignore file
├── app.py                      # Main application file (Streamlit)
├── README.md                   # Project documentation
└── requirements.txt            # List of dependencies

# Project Setup Instructions

## Prerequisites
* Python 3.7 or above
* Pip (Python package installer)

## Installation Steps

### Step 1: Clone the Repository
```bash
git clone https://github.com/sonalrajsr/Ai-Channel-.git
cd your-repo-name
```

### Step 2: Install Dependencies
Install the dependencies using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Step 3: Install PyTorch
Since the language model API may require PyTorch as a backend, install PyTorch with:
```bash
pip install torch
```

### Step 4: Configure Environment Variables
Set up a `.env` file in the project root directory with any required API keys or other environment variables.

### Step 5: Run the Application
Start the Streamlit application:
```bash
streamlit run app.py
```
Open the provided URL in your web browser to access the dashboard.

# Usage Guide

## Step 1: Upload CSV File
Upload a CSV file containing entities (e.g., company names). The dashboard previews the uploaded data.

## Step 2: Connect Google Sheets (Optional)
If preferred, you can connect a Google Sheet by entering the Sheet ID and Range.

## Step 3: Define Search Query
Enter a search query template using `{entity}` as a placeholder. The agent will perform searches based on this template for each entity in the selected column.

## Step 4: Choose Column for Entities
Select the column containing entities in your dataset, which the agent will use for search and information extraction.

## Step 5: Define Extraction Prompt
Specify a custom prompt for extracting information from the search results. Use `{entity}` as a placeholder within the prompt.

## Step 6: Run AI Agent
Click **"Fetch and Extract Information"** to:
1. Perform searches for each entity.
2. Pass search results and JSON data to the language model for extraction.

## Step 7: View and Download Results
The extracted information will be displayed in a table. Download the results as a CSV file with the **"Download CSV"** button.

# Code Explanation

### `app.py` - Main Application File
This file defines the user interface using Streamlit, allowing users to upload files, enter prompts, and interact with the AI agent.

### `src/data_loader.py` - Data Loader Module
Handles CSV file uploads and Google Sheets integration, loading data into a Pandas DataFrame.

### `src/llm_parser.py` - Language Model Parser
Processes search results using the language model to extract specific information, taking JSON context as input.

### `src/search_api.py` - Web Search API Integration
Interacts with the DuckDuckGo API to retrieve search snippets for each entity.

# API Setup

This project uses the Serpapi API and the Groq API as follows:

1. **Serpapi API**
   - Used for free web searches to retrieve text snippets

2. **Groq API**
   - Utilized for language model processing, extracting specific information based on user-defined prompts and JSON context

## API Authentication
1. Add your `groq_api_key` to the `.env` file for authentication with the Groq API
2. Add your `Serpapi_api_key` to the `.env` file for authentication with the Serp API