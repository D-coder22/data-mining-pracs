import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

iris = load_iris()
data = iris.data
target = iris.target
df = pd.DataFrame(data=data, columns=iris.feature_names)
df["class"] = target

treee = DecisionTreeClassifier(criterion="entropy").fit(data, target)

plt.figure(figsize=(10, 7))
plot_tree(treee, feature_names=iris.feature_names,
          class_names=iris.target_names)
plt.show()

# Calculating Information Gain


def calc_entropy(column):
    counts = np.bincount(column)
    probabilities = counts / len(column)
    entropy = 0
    for prob in probabilities:
        if prob > 0:
            entropy += prob * math.log(prob, 2)
    return -entropy


original_entropy = calc_entropy(target)


def calc_information_gain(split_name):
    values = df[split_name].unique()
    left_split = df[df[split_name] == values[0]]
    right_split = df[df[split_name] == values[1]]
    to_subtract = 0
    for subset in [left_split, right_split]:
        prob = (subset.shape[0] / df.shape[0])
        to_subtract += prob * calc_entropy(subset["class"])
    return original_entropy - to_subtract


rootn = [0, ""]
for feat in iris.feature_names:
    gain = round(calc_information_gain(feat), 3)
    if(rootn[0] <= gain):
        rootn = [gain, feat]
    print(feat, " Gain = ", str(gain))

print("\nThe root node with the Highest Gain is ",
      str(rootn[1]), "Gain = ", str(rootn[0]))
