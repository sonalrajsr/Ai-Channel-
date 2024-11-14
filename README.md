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
- **Search API**: [Serpapi](https://serpapi.com/) (free)
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