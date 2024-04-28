
from crewai import Agent, Task, Crew

from langchain_openai import ChatOpenAI

from llm_src import LLMClient

import os
from agents import AgentCreator

import PyPDF2
from textwrap import dedent


def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text




# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_text = extract_text_from_pdf(r"pdf_data/Lecture 9_Times Series Forecasting (Stationary Data)(3).pdf")



LLM = LLMClient()
a = AgentCreator('agents.json')

llm = LLM.get_llm(model_name='openai')
research_agent = a.create_agent('agent_tester',llm)

pdf_cleaner_agent = a.create_agent('PDF_Cleaner',llm)



task = Task(
  description=dedent(f'''Given the following text 
                        -------------- text --------------------
                        {pdf_text}
                        ----------------------------------------
                        clean the text 
                        '''),
  expected_output='good clean text ',
  agent=pdf_cleaner_agent,
)


# task = Task(
#   description='Make up news stories that sound realistic.',
#   expected_output='A bullet list summary of the top 5 most important AI news',
#   agent=research_agent,
#   tools=[]
# )




# general_agent = Agent(role = "Math Professor",
#                       goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
#                       backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
#                       allow_delegation = False,
#                       verbose = True,
#                       llm = llm)

# q = input('please ask math questions')
# math_task = Task (description=f"""{q}""",
#                   expected_output='solution to the math question asked and provide the answer and nothing else',
#              agent = general_agent)

crew = Crew(
            agents=[pdf_cleaner_agent],
            tasks=[task],
            verbose=2
        )




result = crew.kickoff()




print(result)