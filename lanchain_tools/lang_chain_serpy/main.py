"""

    serpapi is google search api where it fetches results from google.

"""

import os
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.llms import openai
from langchain_community.llms import OpenAI



serpapi_key = """"""

os.environ['SERPAPI_API_KEY'] = serpapi_key


llm = OpenAI(temperature=0.6)


tools = load_tools(["serpapi", "llm-math"], llm=llm)

agent = initialize_agent(
    tools, 
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run("what was the GDP of india in 2025 plus ?")
