import numpy as np
import pandas
import os

from sklearn import decomposition
#from sklearn import datasets

names = ['ICA1', 'ICA1bis', 'ICA1bis2', 'ICA2', 'ICA2bis','ICA2bis2', 'ICA3', 'ICA3bis', 'ICA3bis2','ICA4', 'ICA4bis', 'ICA4bis2', 'class']
#names = ['ICA1', 'ICA1bis', 'ICA2', 'ICA2bis', 'ICA3', 'ICA3bis','ICA4', 'ICA4bis', 'class']
dataset = pandas.read_csv('.\\csv\\csvMLData.csv', names=names)

array = dataset.values
X = array[:,0:12]
Y = array[:,12]

n_components=4

pca = decomposition.PCA(n_components=n_components)
pca.fit(X)
X = pca.transform(X)

if os.path.exists('.\\csv\\pcaData.csv'):
    os.remove('.\\csv\\pcaData.csv')

with open('.\\csv\\pcaData.csv', 'a+') as csvfile:
    for i in range(0, len(X)):
        info = ''
        for ii in range(0, n_components):
            value = X[i][ii]
            info += "{0:.7}".format(str(value)) + ','
        info+= Y[i] + '\n'
        csvfile.write(info)
