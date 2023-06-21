import streamlit as st
from dotenv import load_dotenv
import os.path
from utils import handle_resume, generate_cover_letter

def main():

    # Load environment variables
    load_dotenv()

    # Building the Streamlit page
    st.set_page_config(page_title="Cover Letter Generator")

    #TODO Insert css or session variables here if needed

    st.header("Cover Letter Generator")

    # If resume not uploaded, ask user to upload resume
    # if not os.path.isfile("./resume"):
    resume = st.file_uploader("Upload your resume", type=["pdf"], accept_multiple_files=False)
        
        # if st.button("Upload"):
        #     with st.spinner("Uploading resume..."):
        #         if resume is not None:
        #             handle_resume(resume)

    # Ask for description of job and job title
    name = st.text_input("Your Name")
    job_title = st.text_input("Job Title")
    company_name = st.text_input("Company Name")
    job_description = st.text_area("Job Description")

    # Button to generate cover letter
    output = None
    if st.button("Generate Cover Letter"):
        with st.spinner("Generating Cover Letter..."):
            output = generate_cover_letter(name, job_title, company_name, job_description, resume)
    
    if output is not None:
        st.write(output)

if __name__ == "__main__":
    main()