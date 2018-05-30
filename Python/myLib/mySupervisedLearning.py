import pandas
from sklearn.tree import DecisionTreeClassifier

# training of the supervised learning algorithm
def trainingDecisionTree():
    names = ['AF3-2Hz', 'AF3-4Hz', 'F3-2Hz', 'F3-4Hz', 'F4-2Hz', 'F4-4Hz', 'F8-2Hz', 'F8-4Hz', 'AF4-2Hz', 'AF4-4Hz', 'class']

    dataset = pandas.read_csv('.\\csv\\csvMLData.csv', names=names)
    array = dataset.values
    X = array[:,0:10]
    Y = array[:,10]

    model = DecisionTreeClassifier()
    model.fit(X, Y)

    return model