"""
 in stuff method is suitable for token less than LLM caapcity what if 
 token limit exceeded in querying, then in that case we use document loader
 which internally used map -reduce and bring down size by doing aggregating.

"""
import pickle
import os
import langchain
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQAWithSourceChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

openapi_key = """"""

os.environ['OPENAI_API_KEY'] = openapi_key

llm = OpenAI(temperature=0.6, max_tokens=500)

loader = UnstructuredURLLoader(
    urls = [

        "https://www.moneycontrol.com/india/stockpricequote/lifehealth-insurance/sbilifeinsurancecompany/SLI03",
        "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01"
    ]
)

data = loader.load()
print(data[0])
print(data[0].metadata) 

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

docs = text_splitter.split_documents(data)
len(docs)



embeddings = OpenAIEmbeddings()

vectorindex_openai = FAISS.from_documents(docs, embeddings)

# here we can save vector index  create in local

file_path = "vector_index.pkl"
with open(file_path, "wb") as f:
    pickle.dump(vectorindex_openai, f)


# read vector index from file 

if os.path.exists(file_path):
    with open(file_path, "rb") as f:
        vectorIndex = pickle.load(f)

chain = RetrievalQAWithSourceChain.from__llm(llm=llm, retrievar=vectorIndex.as_retriever())
print(chain)


query  = "what is price of tiago ICNG?"

langchain.debug=True

chain({"question": query}, return_only_outputs=True)


