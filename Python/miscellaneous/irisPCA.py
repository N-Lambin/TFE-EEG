import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


from sklearn import decomposition
from sklearn import datasets

np.random.seed(5)

iris = datasets.load_iris()
X = iris.data[0:30,0:2]
y = iris.target

pca = decomposition.PCA(n_components=1)
pca.fit(X)
X1 = pca.transform(X)

plt.subplot(211)
plt.scatter(X[:,0], X[:,1], color='#263248', marker='.')

plt.subplot(212)
plt.scatter(X1, np.zeros_like(X1), color='#263248', marker='.')

plt.show()