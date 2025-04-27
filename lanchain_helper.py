
import os
from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain_community.chains import LLMChain
from langchain_community.chains import SimpleSequentialChain
from langchain.chains import SequentialChain


openapi_key = """"""

os.environ['OPENAI_API_KEY'] = openapi_key


llm = OpenAI(temperature=0.6)


def generate_restaurant_name_and_items(country):

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
    response  = chain({'country': country})
    print(response)
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Indian"))

# def generate_restaurant_name_and_items(country):
#     return {
#         'restaurant_name' : "Curry Delight",
#         'menu_items' : 'samosa, paneer tikka'
#     }

