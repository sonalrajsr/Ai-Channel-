import time
from serpapi import GoogleSearch
import re 
import streamlit as st

def search_entity(query_template, entity):
    # Extract the placeholder from the query_template using regex
    pattern = r'\{(.*?)\}'
    place_holders = re.findall(pattern, query_template)

    if not place_holders:
        st.warning("No placeholder found in the query template.")
        return {}

    place_holder = place_holders[0]

    # Format the query by replacing the placeholder with the entity
    query = query_template.format(**{place_holder: entity})
    message_placeholder = st.empty()
    message_placeholder.write(f"Searching for Prompt: {query}")
    time.sleep(10)
    message_placeholder.empty()

    params = {
        "engine": "google",
        "q": query,
        "api_key": '30064ac4d6420f4efbda97e5dd97d09933f72964ba991c111c6aa146c5de6f05'
    }
    
    search = GoogleSearch(params)
    try:
        results = search.get_dict()
        
        # Check for errors in the response
        if "error" in results:
            print(f"Error: {results['error']}")
            return {}

        # Store relevant data from organic results
        search_results = []
        for item in results.get("organic_results", []):
            result_data = {
                "title": item.get("title"),
                "url": item.get("link"),
                "snippet": item.get("snippet"),
                "source": item.get("source")
            }
            search_results.append(result_data)

        return search_results
    
    except Exception as e:
        print(f"An error occurred for {entity}: {e}")
        return {}

def perform_search_for_all_entities(query_template, entities):
    all_results = {}
    
    for entity in entities:
        all_results[entity] = search_entity(query_template, entity)
        
        time.sleep(1)

    return all_results