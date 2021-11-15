import pandas as pd

doc1 = "organization accumulate vast amounts of data this data will be used for mining"
doc2 = "data mining techniques are used to support a number of business applications"
query = "data mining is integral to knowledge discovery"

print("Document 1:\n", doc1)
print("Document 2:\n", doc2)
print("Query:\n", query)


word1 = doc1.split(" ")
word2 = doc2.split(" ")
word3 = query.split(" ")

allwords = list(set(word1+word2+word3))

print(len(allwords))

word_dict = {"doc_name": ["Doc 1", "Doc 2", "Query Doc"], }

for word in allwords:
    word_dict[word] = []
    word_dict[word].append(word1.count(word))
    word_dict[word].append(word2.count(word))
    word_dict[word].append(word3.count(word))

word_df = pd.DataFrame(word_dict).set_index("doc_name")

print(word_df)

doc1_row = word_df.loc["Doc 1"].tolist()
doc2_row = word_df.loc["Doc 2"].tolist()
doc3_row = word_df.loc["Query Doc"].tolist()

x1 = 0
x2 = 0
x3 = 0
sim1 = 0
sim2 = 0

for (v1, v2, v3) in zip(doc1_row, doc2_row, doc3_row):
    x1 += v1*v1
    x2 += v2*v2
    x3 += v3*v3

    sim1 += v1*v3
    sim2 += v2*v3

x1 = x1**0.5
x2 = x2**0.5
x3 = x3**0.5

sim1 = round(sim1/(x1*x3), 3)
sim2 = round(sim2/(x2*x3), 3)


print("\nCosine similarity Between Document 1 and Query is ", str(sim1))
print("Cosine similarity Between Document 2 and Query is ", str(sim2))
