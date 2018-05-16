from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt

# Loading IRIS dataset from scikit-learn object into iris variable.
iris = datasets.load_iris()

# Prints the type/type object of iris
print(type(iris))
# <class 'sklearn.datasets.base.Bunch'>

# prints the dictionary keys of iris data
print(iris.keys())

# prints the type/type object of given attributes
print(type(iris['data']), type(iris['target']))

# prints the no of rows and columns in the dataset
print(iris['data'].shape)

# prints the target set of the data
print(iris['target_names'])

# Load iris training dataset
X = iris['data']

# Load iris target set
Y = iris['target']

# Convert datasets' type into dataframe
df = pd.DataFrame(X, columns=iris['feature_names'])

# Print the first five tuples of dataframe.
print(df.head())

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

# Load iris dataset from sklearn
iris = datasets.load_iris()

# Declare an of the KNN classifier class with the value with neighbors.
knn = KNeighborsClassifier(n_neighbors=6)

# Fit the model with training data and target values
knn.fit(iris['data'], iris['target'])

# Provide data whose class labels are to be predicted
X = [
    [5.9, 1.0, 5.1, 1.8],
    [3.4, 2.0, 1.1, 4.8],
]

# Prints the data provided
print(X)

# Store predicted class labels of X
prediction = knn.predict(X)

# Prints the predicted class labels of X
print(prediction)