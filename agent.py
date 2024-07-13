import os
from decouple import config
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.llms import OpenAI
#from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI( temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

print(agent.run("What are the current trending topics related to chatbots?"))