
from crewai import Agent, Task, Crew

from langchain_openai import ChatOpenAI

import os

os.environ["OPENAI_API_KEY"] = "NA"



llm = ChatOpenAI(

    model = "crew_gemma:latest",

    base_url = "http://localhost:11434/v1")



research_agent = Agent(
  role='Researcher',
  goal='Find and summarize the latest AI news',
  backstory="""You're a researcher at a large company.
  You're responsible for analyzing data and providing insights
  to the business.""",
  verbose=True,
  llm=llm
)

task = Task(
  description='Make up news stories that sound realistic.',
  expected_output='A bullet list summary of the top 5 most important AI news',
  agent=research_agent,
  tools=[]
)




general_agent = Agent(role = "Math Professor",
                      goal = """Provide the solution to the students that are asking mathematical questions and give them the answer.""",
                      backstory = """You are an excellent math professor that likes to solve math questions in a way that everyone can understand your solution""",
                      allow_delegation = False,
                      verbose = True,
                      llm = llm)

q = input('please ask math questions')
math_task = Task (description=f"""{q}""",
                  expected_output='solution to the math question asked and provide the answer and nothing else',
             agent = general_agent)

crew = Crew(
            agents=[general_agent],
            tasks=[math_task],
            verbose=2
        )




result = crew.kickoff()




print(result)