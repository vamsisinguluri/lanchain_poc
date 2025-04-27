import os
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import openai
from langchain_community.llms import OpenAI



openapi_key = """"""

os.environ['OPENAI_API_KEY'] = openapi_key


llm = OpenAI(temperature=0.6)


tools = load_tools(["wikipedia", "llm-math"], llm=llm)

agent = initialize_agent(
    tools, 
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)


agent.run("when was elon musk born ? what is his age right now in 2025")
