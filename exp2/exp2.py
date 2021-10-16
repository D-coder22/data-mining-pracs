import pandas as pd

df = pd.read_csv('exp2/exp2.csv')


def bins(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def binner(binn, header_name):
    binn1 = []
    binn2 = []
    binn3 = []

    binn = list(bins(binn, 3))

    for item in binn:
        low_bound = item[0]
        up_bound = item[-1]
        mean = round(sum(item)/len(item), 3)
        median = 0
        if len(item) % 2 == 0:
            median = round((item[len(item)//2] + item[len(item)//2])/2, 3)
        else:
            median = item[len(item)//2]

        item1 = []
        item2 = []
        item3 = []
        for ind, val in enumerate(item):
            item1.append(mean)
            item2.append(median)
            val = low_bound if (
                val - low_bound) <= (up_bound - val) else up_bound
            item3.append(val)

        binn1.append(item1)
        binn2.append(item2)
        binn3.append(item3)

    print(header_name+" - Mean Bin\n"+str(binn1))
    print(header_name+" - Median Bin\n"+str(binn2))
    print(header_name+" - Boundary Bin\n"+str(binn3)+"\n")


# Segregation
age = df['age'].tolist()
workhours = df['workhours'].tolist()
yoe = df['years of exp'].tolist()
position = df['position'].tolist()


# Binning
binner(age, "Age")
binner(workhours, "Workhours")
binner(yoe, "Years of Experience")
binner(position, "Position")
