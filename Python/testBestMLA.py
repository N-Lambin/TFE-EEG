import pandas
from sklearn import model_selection

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

names = ['AF3-2Hz', 'AF3-4Hz', 'F3-2Hz', 'F3-4Hz', 'F4-2Hz', 'F4-4Hz', 'F8-2Hz', 'F8-4Hz', 'AF4-2Hz', 'AF4-4Hz', 'class']
dataset = pandas.read_csv('.\\csv\\csvMLData.csv', names=names)

# Split-out validation dataset
array = dataset.values
X = array[:,0:10]
Y = array[:,10]
validation_size = 0.10
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Spot Check Algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('TC', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

# evaluate each model in turn
results = []
names = []
scoring = 'accuracy'
for name, model in models:
	kfold = model_selection.KFold(n_splits=5, shuffle=True, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "{}: {:.2f} %".format(name, cv_results.mean()*100)
	print(msg)