from langchain.text_splitter import CharacterTextSplitter
from PyPDF2 import PdfReader
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceInstructEmbeddings
from sample_cover_letter import example
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import HuggingFaceHub

def handle_resume(resume_file):
    """
    Function to handle resume file uploaded and store the vector embeddings in local storage.

    Parameters 
    ----------
    resume_file : file
        Resume file uploaded by user

    Returns
    -------
    None
    """

    # Process and read resume 
    pdf_reader = PdfReader(resume_file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()
    
    return resume_text

    # # Create chunks from pdf text
    # text_splitter = CharacterTextSplitter(
    #     separator="\n",
    #     chunk_size=1000,
    #     chunk_overlap=200,
    #     length_function=len
    # )

    # chunks = text_splitter.split_text(text=resume_text)

    # # Create embeddings
    # embedding = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    # vector_store = FAISS.from_embeddings(chunks, embedding=embedding)

    # # Save vector store to local storage
    # vector_store.save_local("resume")

def generate_cover_letter(name, job_title, company_name, job_description, resume):
    """
    Function to generate cover letter based on job title and job description.

    Parameters
    ----------
    name : str
        Name of applier
    job_title : str
        Job title of job application
    company_name : str
        Company name of job application
    job_description : str
        Job description of job application

    Returns
    -------
    cover_letter : str
        Generated cover letter
    """

    # # Load resume vector store
    # resume_vector_store = FAISS.load_local("resume")

    # Make prompt template
    prompt_template = """Use the resume, example cover letter, name of applier, job title, job description, and company name below to write a cover letter.
                        The cover letter should include opening paragraph which clearly states the why you're writing name the
                        position or type of work you’re exploring. A summary statement
                        may work well here by including three reasons you think you would be
                        a good fit for the opportunity. The body of the letter should be one to 
                        Explain why you are interested in this employer
                        and your reasons for desiring this type of work. If you’ve had relevant 
                        school or work experience, be sure to point it out with one or two key 
                        examples. Emphasize skills or 
                        abilities that relate to the job. The closing paragraph should Reiterate your interest in the position, and 
                        your enthusiasm for using your skills to contribute to the work 
                        of the organization. Thank the reader for their consideration of 
                        your application, and end by stating that you look forward to the 
                        opportunity to further discuss the position. 
                        Resume: {resume}
                        Name: {name}
                        Job Title: {job_title}
                        Job Description: {job_description}
                        Company Name: {company_name}
                        Cover Letter:"""

    PROMPT = PromptTemplate(template=prompt_template, input_variables=["resume", "name", "job_title", "job_description", "company_name"])

    # Create chain
    llm = HuggingFaceHub(repo_id="mosaicml/mpt-7b-instruct")

    chain = LLMChain(llm=llm, prompt=PROMPT)

    # Generate cover letter
    return chain.apply(
        [{
            "resume": handle_resume(resume),
            "name": name,
            "job_title": job_title,
            "job_description": job_description,
            "company_name": company_name
        }]
    )
