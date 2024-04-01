import requests
import json  # Import JSON library

def send_prompt(prompt, openai_api_key, max_tokens=4096):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }
    data = {
        "model": "gpt-4-0125-preview",  # Ensure correct model identifier
        "messages": [{
            "role": "user",
            "content": prompt
        }],
        "max_tokens": max_tokens
    }

    # Use the correct chat completions endpoint
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        return result['choices'][0]['message']['content']
    else:
        # Improved error handling
        error_details = json.loads(response.text).get('error', {})
        raise Exception(f"OpenAI API request failed. Status code: {response.status_code}, Error Type: {error_details.get('type')}, Message: {error_details.get('message')}")

# Example of using this function within your application
def detailed_foresight_analysis(pdf_path, openai_api_key):
    # Example of extracting text from a PDF or another source
    pdf_text = "Your extracted text from PDF goes here..."

    # Define your prompts based on the extracted text or any other context
    prompts = {
        "STEEPV": f"Based on the following context:\n{pdf_text}\nPerform a detailed STEEPV analysis.",
        "Signals": "Identify strong and weak signals based on the given context.",
        "Critical Uncertainties": "Define critical uncertainties that could impact the future scenarios.",
        "Scenarios": "Outline future scenarios based on the identified signals using the four future scenario archetypes Growth, Collapse, Discipline and Tranformation."
        
    }

    analysis_results = {}
    for key, prompt in prompts.items():
        try:
            analysis_results[key] = send_prompt(prompt, openai_api_key)
        except Exception as e:
            print(f"Error during {key} analysis: {e}")
            analysis_results[key] = "Error in analysis"

    # Compiling the segmented analyses into a comprehensive report
    foresight_report = "\n\n".join([f"**{key} Analysis**:\n{result}" for key, result in analysis_results.items()])

    return foresight_report

# Assuming 'openai_api_key' is defined with your actual OpenAI API key
if __name__ == "__main__":
    # Example usage
    pdf_path = 'path_to_your_pdf_file.pdf'
    openai_api_key = "your_openai_api_key_here"
    try:
        foresight_report = detailed_foresight_analysis(pdf_path, openai_api_key)
        print(foresight_report)
    except Exception as e:
        print(f"An error occurred: {e}")
