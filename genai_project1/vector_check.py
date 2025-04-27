"""

install pip install faiss-cpu  sentence-transformers

"""

import pandas as pd

pd.set_option('display.max_colwidth', 100)

df = pd.read_csv("sample_text.csv")
df.shape

print(df) #  -> columns   text , categtory


from sentence_transformers import SentenceTransformer

encoder= SentenceTransformer("all-mpnet-base-v2")
vectors = encoder.encode(df.text)
vectors.shape

print(vectors)  # two dimensional array ( 8, 768 ) 

print(vectors.shape[1])   # size of one vector  768 so we have 8 such vectors

dim = vectors.shape[1]


import faiss

index = faiss.IndexFlatL2(dim)
print(index)

index.add(vectors)


search_query = "I want to buy a polo t-shirt"
vec = encoder.encode(search_query)
vec.shape  # ( 768, )  this is one dimensional

import numpy as np
svec = np.array(vec).reshape(1, -1) # convert one dimensional  to two dimensional
svec.shape  # ( 1, 768)

distances, I = index.search(svec, k=2)  # k stands for how many similar vectors we want

print(I)  

df.loc[[3,2]]  or df.loc[I[0]]










