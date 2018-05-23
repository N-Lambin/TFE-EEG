import pandas
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

names = ['AF3-2Hz', 'AF3-4Hz', 'AF3-6Hz', 'F3-2Hz', 'F3-4Hz', 'F3-6Hz', 'F4-2Hz', 'F4-4Hz', 'F4-6Hz', 'F8-2Hz', 'F8-4Hz', 'F8-6Hz', 'AF4-2Hz', 'AF4-4Hz', 'AF4-6Hz', 'class']

dataset = pandas.read_csv('.\\csv\\csvMLData.csv', names=names)

dataset.hist()
plt.show()
