import streamlit as st
from dotenv import load_dotenv
import os.path
from utils import handle_resume, generate_cover_letter
import webbrowser
from google_api_key import GOOGLE_API_KEY

def main():

    # Load environment variables
    load_dotenv()

    # Building the Streamlit page
    st.set_page_config(page_title="Cover Letter Prompt Generator")

    st.header("Cover Letter Prompt Generator")

    # If resume not uploaded, ask user to upload resume
    if not os.path.isdir("./resume"):
        resume = st.file_uploader("Upload your resume", type=["pdf"], accept_multiple_files=False)
        
        if st.button("Upload"):
            with st.spinner("Uploading resume..."):
                handle_resume(resume)

    # Ask for description of job and job title
    name = st.text_input("Your Name")
    job_title = st.text_input("Job Title")
    company_name = st.text_input("Company Name")
    job_description = st.text_area("Job Description")

    # Button to generate cover letter
    output = None

    if st.button("Generate Cover Letter"):
        with st.spinner("Generating Cover Letter..."):
            output = generate_cover_letter(name, job_title, company_name, job_description)

    if output is not None:
        if GOOGLE_API_KEY is not None:
            # Cover letter generated
            st.code(output[1])
        else:
            # Cover letter prompt generated
            st.code(output[0])

            # Add buttons to open CHAT GPT and Google Bard

            col1, col2 = st.columns(2)

            with col1:
                if st.button("Open Chat GPT"):
                    webbrowser.open_new_tab("https://chat.openai.com/")

            with col2:
                if st.button("Open Google Bard"):
                    webbrowser.open_new_tab("https://bard.google.com/")

        

    

if __name__ == "__main__":
    main()