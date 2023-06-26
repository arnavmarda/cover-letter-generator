# Cover Letter Generator
An AI bot that uses your resume and a job description to generate a cover letter for the job.

# Installation
1. Clone the repository
```
git clone https://github.com/arnavmarda/cover-letter-generator.git
```

2. Install the requirements
```
pip install -r requirements.txt
```

# Setup
1. Create a file called `.env` in the root directory of the project.
2. Add the following lines to the file:
```
HUGGINGFACEHUB_API_TOKEN=<your-api-token>
```
Replace `<your-api-token>` with your HuggingFace API key. You can get your API key from [here](https://huggingface.co/settings/tokens).
***Note - The program will not work without a HuggingFace API key.***

**Optional Usage** - If you want to generate cover letters with the app, then change the value of the `GOOGLE_API_KEY` variable in a the file `google_api_key.py`. This is the PaLM API and MakerSuite API key. You can get your API key from [here](https://makersuite.google.com/u/1/app/apikey). If you do not set this variable, the app will generate a prompt for you to use in Chat GPT or Google Bard.

# Running
To run the app, run the following command in your root directory:
```
streamlit run app.py
```

# Usage Instructions
1. On first use, upload your resume using the file uploader. You will not need to upload your resume after the first time. If you need to change the resume you have uploaded, run the following command in your root directory:
```
rm -r ./resume
```

2. Enter the information about the job you are applying for. This includes the job title, company name, and job description. You also need to input your name. 

3. After the resume has been processed, and additional information added, you will be able to generate a cover letter. If you have added a PaLM API key, the app will generate a cover letter. Otherwise, it will generate a prompt which you can copy and use in Chat GPT or Google Bard. There are buttons at the bottom to navigate directly to Chat GPT and Google Bard (only works when the app is running locally).