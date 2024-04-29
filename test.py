
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
pdf_text = extract_text_from_pdf(r"pdf_data/2404.14619v1.pdf")



LLM = LLMClient()
a = AgentCreator('agents.json')

llm = LLM.get_llm(model_name='openai')
research_agent = a.create_agent('agent_tester',llm)

tutor_agent = a.create_agent('Personalized_Learning_Tutor',llm)
quiz_agent = a.create_agent('quiz_Tutor',llm)
summary_agent = a.create_agent('Paper_Summarizer',llm)



# task = Task(
#   description=dedent(f'''Given the following notes from pdf 
#                         -------------- text --------------------
#                         {pdf_text}
#                         ----------------------------------------
#                         Given a set of class notes Tutor is tasked 
#                         with going through it and help to understand all concepts provided
                         
#                         '''),
#   expected_output=dedent(f'''
# a structured notes of all the concepts in the notes as a md file.
#                          and key points to understand
# '''),
#   agent=tutor_agent,
#   output_file='e1.md'
# )


summary_task = Task(
  description=dedent(f'''
                     You are tasked with developing an AI-powered research paper summarizer. 
                     The system should take as input a research paper in digital format (e.g., PDF or plain text) and generate a concise summary that captures the key findings,
                      methodologies, and implications of the paper. The summarizer should leverage natural language processing (NLP) techniques to analyze the content of the paper and identify the most important information. 
                     The output summary should be well-structured, coherent, and informative, 
                     providing readers with a clear understanding of the paper's contribution to the field.
                     
                     following is the paper
                        -------------- text --------------------
                        {pdf_text}
                        ----------------------------------------
                        
                         
                        '''),
  expected_output=dedent(f'''A bullet list summary of the top 5 most important points'''),
  agent=tutor_agent,
  output_file='e1111.md'
)
# quiz_task = Task(
#   description=dedent(f'''
#                         Given a set of class notes Tutor is tasked 
#                         with going through and provide a quiz on the key topics
                         
#                         '''),
#   expected_output=dedent(f'''
# a structured quizzes of all the concepts in the notes as a md file along with the answers.
                         
# '''),
#   agent=quiz_agent,
#   output_file='q1.md'

# )

# quiz_task = Task(
#   description=dedent(f'''Given the following notes from pdf 
#                         -------------- text --------------------
#                         {pdf_text}
#                         ----------------------------------------
#                         Given a set of class notes Tutor is tasked 
#                         with going through and provide a quiz on the key topics
                         
#                         '''),
#   expected_output=dedent(f'''
# a structured quizzes of all the concepts in the notes as a md file along with the answers.
                         
# '''),
#   agent=quiz_agent,
#   output_file='q1.md'

# )


# quiz_task.context = [task]

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

# crew = Crew(
#             agents=[tutor_agent,quiz_agent],
#             tasks=[task,quiz_task],
#             verbose=2
#         )

crew = Crew(
            agents=[summary_agent],
            tasks=[summary_task],
            verbose=2
        )



result = crew.kickoff()

def write_to_md_file(text, file_name):
    with open(file_name, 'w') as md_file:
        md_file.write(text)


file_name = "example4.md"
write_to_md_file(result, file_name)