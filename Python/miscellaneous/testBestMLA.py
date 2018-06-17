import pandas
from sklearn import model_selection

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#names = ['ICA1', 'ICA1bis', 'ICA1bis1', 'ICA2', 'ICA2bis','ICA2bis2', 'ICA3', 'ICA3bis', 'ICA3bis3','ICA4', 'ICA4bis', 'ICA4bis4', 'class']
#names = ['ICA1', 'ICA1bis', 'ICA2', 'ICA2bis', 'ICA3', 'ICA3bis','ICA4', 'ICA4bis', 'class']
names = ['ICA1', 'ICA1bis', 'ICA2', 'ICA2bis', 'ICA3', 'ICA3bis', 'class']

#dataset = pandas.read_csv('.\\csv\\csvMLData.csv', names=names)
dataset = pandas.read_csv('.\\csv\\pcaData.csv', names=names)

# Split-out validation dataset
array = dataset.values
X = array[:,0:6]
Y = array[:,6]
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
	kfold = model_selection.KFold(n_splits=3, shuffle=True, random_state=seed)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	results.append(cv_results)
	names.append(name)
	msg = "{}: {:.2f} % {:.2f}".format(name, cv_results.mean()*100, cv_results.std())
	print(msg)