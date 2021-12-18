import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./iris.csv')


data = pd.DataFrame(columns=df.columns)
for species in df["class"].unique():
    temp = df[df["class"] == species].sample(n=7)
    data = data.append(temp, ignore_index=True)

# Dropping Columns Yielding Negligible Euclidean Distance

data.drop(['sepal width',	'petal width'], axis=1, inplace=True)

cent1 = data.iloc[:7].sample(n=1)
cent2 = data.iloc[7:14].sample(n=1)
cent3 = data.iloc[14:].sample(n=1)

for i in range(3):
    for idx, item in data.iterrows():
        dist1 = ((cent1["sepal length"]-item["sepal length"]) **
                 2 + (cent1["petal length"]-item["petal length"])**2)**0.5
        dist2 = ((cent2["sepal length"]-item["sepal length"]) **
                 2 + (cent2["petal length"]-item["petal length"])**2)**0.5
        dist3 = ((cent3["sepal length"]-item["sepal length"]) **
                 2 + (cent3["petal length"]-item["petal length"])**2)**0.5

        dist1 = dist1.values.tolist()
        dist2 = dist2.values.tolist()
        dist3 = dist3.values.tolist()

        if dist1[0] < dist2[0] and dist1[0] < dist3[0]:
            cent1["sepal length"] = (
                cent1["sepal length"] + item["sepal length"])/2
            cent1["petal length"] = (
                cent1["petal length"] + item["petal length"])/2
            data.at[idx, "Epoch "+str(i+1)] = "setosa"
        elif dist2[0] < dist1[0] and dist2[0] < dist3[0]:
            cent2["sepal length"] = (
                cent2["sepal length"] + item["sepal length"])/2
            cent2["petal length"] = (
                cent2["petal length"] + item["petal length"])/2
            data.at[idx, "Epoch "+str(i+1)] = "versicolor"
        else:
            cent3["sepal length"] = (
                cent3["sepal length"] + item["sepal length"])/2
            cent3["petal length"] = (
                cent3["petal length"] + item["petal length"])/2
            data.at[idx, "Epoch "+str(i+1)] = "virginica"

print(data)

# Scatter Plot
plt.figure(figsize=(10, 7))
plt.scatter(data[data["Epoch 2"] == 'setosa']["sepal length"], data[data["Epoch 2"]
                                                                    == 'setosa']["petal length"], c='red', label='Setosa Cluster')
plt.scatter(data[data["Epoch 2"] == 'versicolor']["sepal length"], data[data["Epoch 2"]
                                                                        == 'versicolor']["petal length"], c='blue', label='Versicolor Cluster')
plt.scatter(data[data["Epoch 2"] == 'virginica']["sepal length"], data[data["Epoch 2"]
                                                                       == 'virginica']["petal length"], c='green', label='Virginica Cluster')
plt.legend()
plt.show()
