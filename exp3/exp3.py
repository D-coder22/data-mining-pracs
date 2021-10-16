import pandas as pd

df = pd.read_csv('exp3/exp3.csv')


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
        val = item/(10**count)
        norm1.append(val)
        val = round((item - mini)/(maxi - mini), 3)
        norm2.append(val)
        val = round((item - mean)/devi, 3)
        norm3.append(val)

    print(header_name+" - Decimal Scaling\n"+str(norm1))
    print(header_name+" - MinMax Normalization\n"+str(norm2))
    print(header_name+" - Z Score Normalization\n"+str(norm3)+"\n")


# Segregation
age = df['age'].tolist()
workhours = df['workhours'].tolist()
yoe = df['years of exp'].tolist()
position = df['position'].tolist()

# Normalization
normalizer(age, "Age")
normalizer(workhours, "Workhours")
normalizer(yoe, "Years of Experience")
normalizer(position, "Position")
