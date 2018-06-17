import pandas
from sklearn.tree import DecisionTreeClassifier

# training of the supervised learning algorithm
def trainingDecisionTree():
    names = ['ICA1', 'ICA1bis', 'ICA2', 'ICA2bis', 'ICA3', 'ICA3bis','ICA4', 'ICA4bis', 'class']
    dataset = pandas.read_csv('.\\csv\\csvMLData.csv', names=names)

    array = dataset.values
    X = array[:,0:8]
    Y = array[:,8]

    model = DecisionTreeClassifier()
    model.fit(X, Y)

    return model