from langchain_openai import ChatOpenAI
from langchain.llms import OpenAI

import os

from langchain.chat_models import ChatOpenAI as oai
from langchain_groq import ChatGroq


os.environ["OPENAI_API_KEY"] = "NA"
os.environ["GROQ_API_KEY"] = "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"




class LLMClient:
    def __init__(self):

        self.model_dict = {'phi':"crew_phi3:latest",
                      'gemma':'crew_gemma:latest',
                      }
        self.base_url = "http://localhost:11434/v1"
        
    def get_llm(self,model_name):

        if model_name == 'phi':
            model = self.model_dict[model_name]

            llm = ChatOpenAI(
                model=model,
                base_url=self.base_url)
            return llm
        
        if model_name == 'gemma':
            model = self.model_dict[model_name]

            llm = ChatOpenAI(
                model=model,
                base_url=self.base_url)
            return llm
        
        if model_name == 'openai':
            return ChatOpenAI(model='gpt-3.5-turbo')
        
        if model_name == 'groq':
            return ChatGroq(api_key='',
                            model='llama3-70b-8192')


            

        
 