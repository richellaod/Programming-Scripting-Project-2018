# Richella O'Driscoll 14.04.2018
# Programming & Scripting Project 2018


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
from sklearn.svm import SVC #Import all of the modules, functions and objects which are needed to complete the project.

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names) #Used to Load the Iris Dataset


print(dataset.shape) #Display how many instances and how many attributes the data contains.

print(dataset.head(20))#Display the first 20 rows of data.

print(dataset.describe())#Display a summary of each attribute.This includes the  mean, the min and max values which is a project requirement.

print(dataset.groupby('class').size()) #Display  the number of instances that belong to each class.


