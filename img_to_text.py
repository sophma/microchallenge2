import base64
import requests

def describe_image(image_file, openai_api_key):
    """
    Describe and categorize the content of an image using OpenAI's GPT-4 Vision model,
    focusing on urban elements and strategic foresight categories.
    Accepts a Streamlit UploadedFile object or similar file-like object.
    """
    # Function to encode the image from a file-like object
    def encode_image(file_like):
        file_like.seek(0)  # Reset file pointer to the beginning
        return base64.b64encode(file_like.read()).decode('utf-8')

    # Getting the base64 string and formatting it for JSON payload
    base64_image = encode_image(image_file)
    image_data_url = f"data:image/jpeg;base64,{base64_image}"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Given an image, describe and categorize the objects within the image based on urban design and strategic foresight categories: Infrastructure, Built Environment, Natural Elements, Social Dynamics, Emerging Technologies, and Signs of Change."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_data_url
                        }
                    }
                ]
            }
        ],
        "max_tokens": 4096
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        response_data = response.json()
        categorized_description = response_data['choices'][0]['message']['content']
        return categorized_description
    else:
        print(f"Failed to generate description. Status Code: {response.status_code}, Response: {response.text}")
        return "Error in generating image description."