from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# Assume you have your OpenAI key set
llm = ChatOpenAI(model="gpt-4", temperature=0)

def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."


# 1st Step: Get city from user
city_prompt = PromptTemplate(
    input_variables=["city"],
    template="Tell me about the weather in {city}."
)
weather_chain = LLMChain(
    llm=llm,
    prompt=city_prompt,
    output_key="weather_info"
)

# 2nd Step: Wrap your custom tool call inside another chain
def weather_tool_chain(inputs):
    city = inputs['city']
    return {"weather_info": get_weather(city)}

# 3rd Step: SequentialChain
chain = SequentialChain(
    chains=[weather_chain],
    input_variables=["city"],
    output_variables=["weather_info"],
    verbose=True
)




