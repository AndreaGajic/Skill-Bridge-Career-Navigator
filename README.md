Candidate Name: Andrea Gajic

Scenario Chosen: Scenario 2

Estimated Time Spent: 5 hours

Video Link: https://youtu.be/uhBbyPxYOfQ

Quick Start:

    Prerequisites: Python 3.10+, PyPDF2, streamlit
    
    Run Commands: 
    
        Install Dependencies:
        
            pip install streamlit openai python-dotenv PyPDF2

        Launch Application:
     
            streamlit run main.py
 
    Test Commands:
    
        Once the web application launches, a PDF resume can be uploaded to verify text extraction and check the AI Generated Roadmap. 

AI Disclosure:

    Did you use an AI assistant (Copilot, ChatGPT, etc.)?: Yes
    
    How did you verify the suggestions: With each suggestion made, I consulted either exact documentation pages or StackOverflow to see if the suggestion had been made there before, particularly if I wasn't sure what the suggestion was really doing. After I verified that the suggestion was potentially valid, I would slowly work it into my code and test it.   
    
    Give one example of a suggestion you rejected or changed: One suggestion I rejected was for how to best add multiple pages to my web application with their own names instead of the file name by default. The suggestion I received was to remove the files from the /pages folder I had them in and place them in the root directory. However, this resulted in repeat reads and made the application become sluggish.

Tradeoffs & Prioritization:
    
    What did you cut to stay within the 4-6 hour limit?: There was more functionality I could have added, such as searchable databases or other AI-driven features such as resume advice for improving resumes, mock-interview, questions, and more. 
   
    What would you build next if you had more time?
   
    The previously discussed functionalities are some I considered adding, but I would also look to add a Skill Match Percentage dashboard to show how the applicant compares to the required skills for the role. 
  
    Known limitations:
       
        PDF parsing is a limitation as the PyPDF2 parser will not work with image-based PDFs. 
        API Dependency is also a limitation as the AI is limited to OpenAI's API. If the rate limit is hit or connection issues occur, the user will be restricted to Manual Mode. # Skill-Bridge-Career-Navigator
