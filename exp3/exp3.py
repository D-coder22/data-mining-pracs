import pandas as pd

df = pd.read_csv('exp3/iris.csv')


def normalizer(norm, header_name):
    norm1 = []
    norm2 = []
    norm3 = []

    mini = min(norm)
    maxi = max(norm)
    maxi2 = maxi

    mean = sum(norm)/len(norm)
    devi = (sum((x-mean)**2 for x in norm)/(len(norm) - 1))**(0.5)

    count = 0
    while maxi2 != 0:
        maxi2 //= 10
        count += 1

    for item in norm:
        val = round(item/(10**count), 2)
        norm1.append(val)
        val = round((item - mini)/(maxi - mini), 3)
        norm2.append(val)
        val = round((item - mean)/devi, 3)
        norm3.append(val)

    print(header_name+" - Decimal Scaling\n"+str(norm1[0:10]))
    print(header_name+" - MinMax Normalization\n"+str(norm2[0:10]))
    print(header_name+" - Z Score Normalization\n"+str(norm3[0:10])+"\n")


# Segregation
sepal_length = df['sepal length'].tolist()
sepal_width = df['sepal width'].tolist()
petal_length = df['petal length'].tolist()
petal_width = df['petal width'].tolist()

# Normalization
normalizer(sepal_length, "Sepal Length")
normalizer(sepal_width, "Sepal Width")
normalizer(petal_length, "Petal Length")
normalizer(petal_width, "Petal Width")
