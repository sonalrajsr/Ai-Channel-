from transformers import pipeline
import re

# Initialize the summarizer model (DistilBART is lightweight and good for summarization)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_specific_info(entity, search_results, user_prompt):
    # Combine search snippets into one text block for the LLM
    combined_text = " ".join(result['snippet'] for result in search_results)
    
    # Regex to extract placeholder text from the user_prompt
    pattern = r'\{(.*?)\}'  # This looks for text between curly braces
    place_holders = re.findall(pattern, user_prompt)  # List of all placeholders
    
    if not place_holders:
        return "No placeholder found in the user prompt."
    
    place_holder = place_holders[0]  # Assuming there's only one placeholder to replace
    
    # Ensure the placeholder is correctly replaced in the user prompt
    prompt = user_prompt.format(**{place_holder: entity})  # Replace the placeholder with the entity name

    # Generate the final prompt to send to the LLM
    full_prompt = f"{prompt} Here is the information: {combined_text}"
    
    try:
        # Use the LLM to summarize and extract the required information
        summary = summarizer(full_prompt, max_length=50, min_length=25, do_sample=False)
        return summary[0]['summary_text']
    
    except Exception as e:
        print(f"Error processing entity '{entity}': {e}")
        return "Information extraction failed."

def parse_info(results, user_prompt):
    extracted_data = {}
    
    for entity, search_results in results.items():
        if search_results:
            extracted_data[entity] = extract_specific_info(entity, search_results, user_prompt)
        else:
            extracted_data[entity] = "No relevant information found."
    
    return extracted_data
