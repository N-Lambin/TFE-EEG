import pandas
from sklearn.tree import DecisionTreeClassifier

# training of the supervised learning algorithm
def trainingDecisionTree():
    names = ['PCA1', 'PCA2', 'PCA3', 'PCA4', 'class']
    dataset = pandas.read_csv('.\\csv\\pcaData.csv', names=names)

    array = dataset.values
    X = array[:,0:4]
    Y = array[:,4]

    model = DecisionTreeClassifier()
    model.fit(X, Y)

    return model