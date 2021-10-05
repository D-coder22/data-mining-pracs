import pandas as pd

df = pd.read_csv('exp2/exp2.csv')


def binner(binn, header_name):
    binn1 = []
    binn2 = []
    binn3 = []
    low_bound = binn[0]
    up_bound = binn[-1]
    mean = round(sum(binn)/len(binn), 3)
    median = 0
    if len(binn) % 2 == 0:
        median = round((binn[len(binn)//2] + binn[len(binn)//2])/2, 3)
    else:
        median = binn[len(binn)//2]

    for item in binn:
        binn1.append(mean)
        binn2.append(median)
        val = low_bound if (
            item - low_bound) <= (up_bound - item) else up_bound
        binn3.append(val)

    print(header_name+" - Mean Bin\n"+str(binn1))
    print(header_name+" - Median Bin\n"+str(binn2))
    print(header_name+" - Boundary Bin\n"+str(binn3)+"\n")


def normalizer(norm, header_name):
    norm1 = []
    norm2 = []
    mini = min(norm)
    maxi = max(norm)

    mean = sum(norm)/len(norm)
    devi = (sum((x-mean)**2 for x in norm)/(len(norm) - 1))**(0.5)

    for item in norm:
        val = round((item - mini)/(maxi - mini), 3)
        norm1.append(val)
        val = round((item - mean)/devi, 3)
        norm2.append(val)

    print(header_name+" - MinMax Normalization\n"+str(norm1))
    print(header_name+" - Z Score Normalization\n"+str(norm2)+"\n")


# Segregation
age = df['age'].tolist()
workhours = df['workhours'].tolist()
yoe = df['years of exp'].tolist()
position = df['position'].tolist()


# Age Bin
binner(age, "Age")
binner(workhours, "Workhours")
binner(yoe, "Years of Experience")
binner(position, "Position")


# Normalization
print("\n\n")
normalizer(age, "Age")
normalizer(workhours, "Workhours")
normalizer(yoe, "Years of Experience")
normalizer(position, "Position")
