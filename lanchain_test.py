import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.chains import LLMChain
from langchain_community.chains import SimpleSequentialChain
from langchain.chains import SequentialChain


openapi_key = """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"""

os.environ['OPENAI_API_KEY'] = openapi_key


llm = OpenAI(temperature=0.6)
name = llm("I want to open a restuarant for indian food. suggest me a fancy name for this")
print(name)


# picking run time inputs from user :
prompt_template_name= PromptTemplate(
    input_variables = ['country']
    template = "I want to open a restuarant for {country} food. suggest me a fancy name for this"
)
prompt_template_name.format(country="Indian")


chain = LLMChain(llm=llm, prompt=prompt_template_name)
chain.run("Mexio")





prompt_template_name= PromptTemplate(
    input_variables = ['country']
    template = "I want to open a restuarant for {country} food. suggest me a fancy name for this"
)
name_chain = LLMChain(llm=llm, prompt=prompt_template_name)

prompt_template_items= PromptTemplate(
    input_variables = ['restaurant_name']
    template = "suggest some menu items for {restaurant_name}. return it as comma separated."
)
food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items)

chain = SimpleSequentialChain(chains = [name_chain, food_items_chain])
response  = chain.run("Indian")
print(response)





prompt_template_name= PromptTemplate(
    input_variables = ['country']
    template = "I want to open a restuarant for {country} food. suggest me a fancy name for this"
)
name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

prompt_template_items= PromptTemplate(
    input_variables = ['restaurant_name']
    template = "suggest some menu items for {restaurant_name}. return it as comma separated."
)
food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

chain = SequentialChain(
    chains = [name_chain, food_items_chain],
    input_variables = ['indian'],
    ouput_variables = ['restaurant_name', 'menu_items']
    )
response  = chain({'country': "indian"})
print(response)









