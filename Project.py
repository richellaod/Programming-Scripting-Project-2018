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

print(dataset.groupby('class').size()) #Display the number of instances that belong to each class.

dataset.hist('sepal-length') #plot my histogram showing the sepal length
plt.title('Histogram of the Sepal Length in the Iris Data Set') #title of my histogram
plt.xlabel('Sepal Length in Centimetres') #x axis label
plt.ylabel('Number of Samples') #y axis label
plt.savefig('project_hist_sepallength.png') #save the plot
plt.show() #show my histogram

dataset.hist('sepal-width')  #plot my histogram showing the sepal width
plt.title('Histogram of the Sepal Width in the Iris Data Set') #title of my histogram
plt.xlabel('Sepal Width in Centimetres')  #x axis label
plt.ylabel('Number of Samples')  #y axis label
plt.savefig('project_hist_sepalwidth.png') #save plot
plt.show()  #show my histogram

dataset.hist('petal-length') #plot my histogram showing the petal length
plt.title('Histogram of the Petal Length in the Iris Data Set') #title of my histogram
plt.xlabel('Petal Length in Centimetres')  #x axis label
plt.ylabel('Number of Samples')  #y axis label
plt.savefig('project_hist_petallength.png') #save plot
plt.show()  #show my histogram

dataset.hist('petal-width') #plot my histogram showing the petal width
plt.title('Histogram of the Petal Width in the Iris Data Set') #title of my histogram
plt.xlabel('Petal Width in Centimetres')  #x axis label
plt.ylabel('Number of Samples')  #y axis label
plt.savefig('project_hist_petalwidth.png') #save plot
plt.show()  #show my histogram

#Box & Whiskers
color = dict(boxes='Red', whiskers='Blue',medians='Yellow', caps='Green')#colours of my Box and Whisker Plot for univariate data
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False, color=color)#plot type box
plt.savefig('project_box_and_whisker_plot.png') #save my plot
plt.show() #show my plot

#Scatter Plot
scatter_matrix(dataset) #scatter plot matrix used to spot structured relationships between input variables.
plt.show()




