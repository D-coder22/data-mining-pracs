import pandas as pd
import random

df = pd.read_csv('exp4/iris.csv')


def distancer(rows):
    euc = [[], [], [], [], []]
    mink = [[], [], [], [], []]
    for i in range(0, len(rows)):
        for j in range(i, len(rows)):
            euc_dist = 0
            mink_dist = 0
            row1 = rows[i]
            row2 = rows[j]
            for item1, item2 in zip(row1, row2):
                val = item1 - item2
                euc_dist += val**2
                mink_dist += abs(val)
            euc_dist = round(euc_dist**0.5, 2)
            mink_dist = round(mink_dist, 2)
            euc[j].append(euc_dist)
            mink[j].append(mink_dist)
    euc_df = pd.DataFrame(euc)
    mink_df = pd.DataFrame(mink)
    print("\nEuclidean Distance Matrix")
    print(euc_df)
    print("\nMinkowski Distance Matrix")
    print(mink_df)


rows = df.sample(n=5)
print(rows)
rows = rows.drop('class', axis=1).values.tolist()


distancer(rows)
