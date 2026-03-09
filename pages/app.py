# Import Libraries
import streamlit as st  # for building web app
from openai import OpenAI  # for interacting with API
from dotenv import load_dotenv  # for loading environment variables from .env
import os  # for accessing environment variables
import json  # for parsing data from data.json
import PyPDF2  # for parsing PDF files

# Load the environment from the .env file
load_dotenv()

# Retrieve the API key from .env and initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Cache the data loading function to improve performance by avoiding repeated file reads
@st.cache_data
def load_data():
    # Open and load the JSON file containing role data
    with open("data.json", "r") as f:
        return json.load(f)

# Load the role data once for use in the app
data = load_data()

# Function to extract text from a PDF file (e.g., resume)
def extract_text_from_pdf(file):
    try:
        # Initialize PDF reader and extract text from all pages
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        # Handle any errors during PDF reading
        return f"Error reading PDF: {str(e)}"

# Function to generate a career roadmap using OpenAI API
def get_ai_roadmap(user_skills, target_role):
    # Retrieve role requirements from loaded data
    role_info = data["roles"].get(target_role, {})

    # Note: This line seems redundant as api_key is already fetched earlier; possibly a typo or leftover
    current_key = os.getenv("OPENAI_API_KEY")

    # Define the system prompt for the AI to generate a customized roadmap
    system_prompt = f"""
    You're an expert Career Coach. Your goal is to create a learning roadmap for the applicant.
    You must use these predefined requirements for the role ({target_role}): {role_info}.
    You must compare these requirements against the user's current skills: {user_skills}.
    Highlight the skills the applicant is missing for the role and provide a 3-step learning plan that includes: Foundations, Projects/Courses, and Certifications.
    For the projects heading, provide suggestion for free courses that can be taken as well to improve skills.
    """

    try:
        # Check if API key is available
        if not api_key:
            raise ValueError("API Key is missing.")

        # Call OpenAI API to generate the roadmap
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": "Generate the roadmap."}
            ]
        )
        # Return the generated content from the API response
        return response.choices[0].message.content
    except Exception as e:
        # Handle API errors and return error message
        return f"API Error: {str(e)}"
        return None  # Note: This return is unreachable due to the previous return

# Set up the Streamlit app interface
st.title("Skill-Bridge Career Navigator")

# Allow user to choose how to input skills
input_method = st.radio("Choose input method:", ["Manual Entry", "Upload Resume (PDF)"])

# Initialize user_skills variable
user_skills = ""

# Handle PDF upload input method
if input_method == "Upload Resume (PDF)":
    uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
    if uploaded_file:
        # Parse the uploaded PDF while showing a spinner
        with st.spinner("Parsing resume..."):
            user_skills = extract_text_from_pdf(uploaded_file)
            st.success("Resume parsed successfully!")
else:
    # Handle manual text entry for skills
    user_skills = st.text_area("Enter your skills manually:")

# Dropdown to select the target career role from available roles in data
target_role = st.selectbox("Select target role:", sorted(list(data["roles"].keys())))

# Button to trigger roadmap generation
if st.button("Generate Roadmap"):
    if not user_skills:
        # Warn if no skills are provided
        st.warning("Please provide your skills via upload or manual entry.")
    else:
        # Generate roadmap while showing a spinner
        with st.spinner("AI is thinking..."):
            ai_result = get_ai_roadmap(user_skills, target_role)
            
            # Display error or success based on API result
            if "API Error" in ai_result or ai_result is None:
                st.error(ai_result if ai_result else "An unknown error occurred.")
            else:
                st.success("AI Generated Roadmap:")
                st.markdown(ai_result)
