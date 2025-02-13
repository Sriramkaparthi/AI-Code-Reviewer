import streamlit as st
import google.generativeai as genai

# Set your Gemini API key
genai.configure(api_key="your_api_key")

# Define system prompt for AI model
system_prompt = """
Assume you are a expert python code debugger.
Allow users to submit their Python code for review and receive feedback on potential bugs along with suggestions for fixes.
Analyze the submitted code and identify potential bugs, errors, or areas of improvement.
Provide the output with three clear sections:
1. **Code Review** (bold, bigger size) - This section should contain the overall review of the code without mentioning any errors.
2. **Bug Report** (bold, bigger size) - The bug report should contain only the details of issues found in the code, each bug in a new line.
3. **Fixed Code** (bold, bigger size) - The fixed code should contain only the corrected version of the given code, and strictly mention the changes you have made.
Ensure that the bug report appears strictly under the Bug Report heading and the fixed code appears strictly under the Fixed Code heading.
"""
gemini = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp", system_instruction=system_prompt)
# Streamlit UI
st.title("📝 An AI Code Reviewer")
# Text area for code input
user_prompt = st.text_area("Enter your Python code here:", height=200)
# Generate review button
if st.button("Generate Review", help="Click to analyze and fix your code"):
    if user_prompt.strip():  # Ensure the user has entered some code
        with st.spinner("Reviewing your code..."):
            try:
                # Interact with the Gemini model
                response = gemini.generate_content(user_prompt)
                st.write(response.text)  # Display the complete response text directly from the model

            except Exception as e:
                st.error(f"Error during analysis: {str(e)}")
    else:
        st.warning("⚠️ Please enter some Python code to review.")
