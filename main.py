import streamlit as st
from PIL import Image
from functions.img_to_text import describe_image
from functions.description_to_foresight import detailed_foresight_analysis
from functions.foresight_to_future_vision import transform_future_vision

# Setup Streamlit configuration and API clients
st.set_page_config(page_title="Crystal Ball", page_icon="🔮")

# Sidebar for API keys input
st.sidebar.header('Settings')
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
replicate_api_key = st.sidebar.text_input('Replicate API Key', type='password')

# Ensure both API keys are entered
if not openai_api_key or not replicate_api_key:
    st.sidebar.error('Please enter both OpenAI and Replicate API keys!')
    st.stop()

# Title and introduction
st.title('Crystal Ball 🔮')
st.subheader('Explore future scenarios through AI-powered visions.')

# UI for image upload and processing
uploaded_image = st.file_uploader("Upload a 360-degree image", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Session state to retain image description and foresight analysis
    if 'image_description' not in st.session_state or 'foresight_analysis' not in st.session_state:
        st.session_state['image_description'] = describe_image(uploaded_image, openai_api_key)
        st.session_state['foresight_analysis'] = detailed_foresight_analysis(st.session_state['image_description'], openai_api_key)

    st.write("Image description:", st.session_state['image_description'])
    st.write("Foresight Analysis:", st.session_state['foresight_analysis'])

    scenario_options = ["Continued Growth", "Collapse", "Disciplined Society", "Transformation"]
    selected_scenario = st.selectbox("Choose a future scenario to visualize:", scenario_options)

    if selected_scenario and st.button("Visualize Selected Scenario"):
        transformed_image_url = transform_future_vision(uploaded_image, st.session_state['image_description'], selected_scenario, replicate_api_key)
        if transformed_image_url and transformed_image_url.startswith('http'):
            st.image(transformed_image_url, caption=f"Visualized Future Scenario: {selected_scenario}")
        else:
            st.error("Failed to visualize the future scenario.")
