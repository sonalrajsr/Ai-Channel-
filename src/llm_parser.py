from langchain_groq import ChatGroq
import re
import json  # Add import for handling JSON if needed

llm_model = ChatGroq(
    temperature=0,
    groq_api_key='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',
    model="gemma2-9b-it"
)

def extract_specific_info(entity, search_results, user_prompt, json_data):
    # Combine search snippets into one text block for the LLM
    combined_text = " ".join(result['snippet'] for result in search_results)
    
    # Regex to extract placeholder text from the user_prompt
    pattern = r'\{(.*?)\}'  # This looks for text between curly braces
    place_holders = re.findall(pattern, user_prompt)
    
    if not place_holders:
        return "No placeholder found in the user prompt."
    
    place_holder = place_holders[0]  # assuming only one placeholder
    
    # Replace placeholder with the entity name in the user prompt
    prompt = user_prompt.format(**{place_holder: entity})

    # Incorporate JSON data in the final prompt
    full_prompt = f"{prompt}\n\nHere is the JSON data for additional context:\n{json_data}\n\nHere is the search information:\n{combined_text}"
    
    try:
        # Use the LLM to summarize and extract the required information
        summary = llm_model.invoke(full_prompt)
        return summary.content
    
    except Exception as e:
        print(f"Error processing entity '{entity}': {e}")
        return "Information extraction failed."

def parse_info(results, user_prompt, json_data):
    extracted_data = {}
    
    for entity, search_results in results.items():
        if search_results:
            # Pass the JSON data as an additional parameter to extract_specific_info
            extracted_data[entity] = extract_specific_info(entity, search_results, user_prompt, json_data)
        else:
            extracted_data[entity] = "No relevant information found."
    
    return extracted_data
