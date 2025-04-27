"""

    install python libraries:

    pip3 install unstructured libmagic  python-magic  python-magic-bin

"""

from langchain.document_loaders import TextLoader

loader = TextLoader("data.txt")
data = loader.load()
print(data)
print(data[0].page_content)
print(data[0].metadata)



from langchain.document_loaders.csv_loader import CSVLoader

loader = CSVLoader("data.csv")
data = loader.load()
print(data)
print(data[0].page_content)
print(data[0].metadata)  # print {'source': 'data.csv' , 'row': 0}

loader = CSVLoader("data.csv", source_column="title")  # title is one of column in csv
data = loader.load()
print(data[0].metadata)  # print {'source': 'Vamsi krishna' , 'row': 0}


from langchain.document_loaders import UnstructuredURLLoader

loader = UnstructuredURLLoader(
    urls = [

        "https://www.moneycontrol.com/india/stockpricequote/lifehealth-insurance/sbilifeinsurancecompany/SLI03",
        "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01"
    ]
)

data = loader.load()
print(data[0])
print(data[0].metadata) 



text = """



"""

chunk = []

s = ""
for word in words:
    s+= word + " "
    if len(s) > 200:
        chunk.append(s)
        s = ""
chunk.append(s)

#  when you use this this will split data at any point  reference 


from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=200,
    chunk_overlap=0
)

chunks = splitter.split_text(text)
len(chunk)

for chunk in chunks:
    print(len(chunk))

# here if \n ends with some huge data then len of chunk for few chunks will be above 200 
# how could we optimise this to split data below 200 size then we use RecusriveCharacterTextSplitter

from  langchain.text_splitter import RecursiveCharacterTextSplitter

r_splitter = RecursiveCharacterTextSplitter(
    separator=["\n\n", "\n", " "],
    chunk_size=200,
    chunk_overlap=0
)

chunks = r_splitter.split_text(text)
print(len(chunks))

for chunk in chunks:
    print(len(chunk))  # here all chunk size on majority will be below 200

# one think here RecursiveCharacterTextSplitter will also perform merge of chunks incase if any 
# chunk size is very less  then it will merge few of chunks to merge and make sure less than user specified 200 size. 

