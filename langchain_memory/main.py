
import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.chains import LLMChain
from langchain_community.chains import SimpleSequentialChain
from langchain.chains import SequentialChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()


openapi_key = """"""

os.environ['OPENAI_API_KEY'] = openapi_key


llm = OpenAI(temperature=0.6)


prompt_template_name= PromptTemplate(
    input_variables = ['country']
    template = "I want to open a restuarant for {country} food. suggest me a fancy name for this"
)
name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name", memory=memory)
name = name_chain.run("Indian")


print(name_chain.memory)
print(name_chain.memory.buffer) --> this helps in saving history in database / persisted somewhere. 

# problem with ConversationBufferMemory when you ask new query it send all the previous history to LLM their
# upon it charges more based on token. ideal case is to send last few history chat. it can be implemented with 
# Converation Chain

from langchain.chains import ConversationChain

# ConversationChain by default it comes with inbuilt conversation buffer memory

convo = ConversationChain(lll=llm)

print(convo.prompt)
print(convo.prompt.template)
print(convo.memory)
print(convo.memory.buffer)


convo.run("who won first cricket world cup?")



from langchain.memory import ConversationBufferWindowMemory

memory = ConversationBufferWindowMemory(k=1)  # remember only last 1 trasaction

convo = ConversationChain(lll=llm, memory=memory)
convo.run("who won first cricker world cup?")
convo.run("what is 5 + 5?")
convo.run("who was captain of the winning team?") # "I am sorry I dont know" as it remembers only last transaction.








