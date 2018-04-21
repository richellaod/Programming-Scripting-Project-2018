# Programming- and-Scripting-Project-2018

Project for Programming and Scripting Module 2018 by Richella O'Driscoll


## Problem Statement

This project concerns the well known Fishers Iris Data Set. The project entails you to research the data set and then write documentation and code in the Python Programming Language based on your research.
An online search for information on the data set will convince you that many people have investigated and written about it previously, many of those are not experienced programmers. You are expected to break the project into several smaller tasks that are easier to solve and to plug these together after they have been completed. You might do that for this project as follows:

1. Research background information about the data set and write a summary about it.
2. Keep a list of references you used in completing the project.
3. Download the data set and write some Python code to investigate it.
4. Summarise the data set by calculating the maximum, minimum and mean of each column of the data set. 
5. Write a summary of your investigations.
6. Include supporting tables and graphics that you deem to be neccasary.

## The Iris Data Set

The Iris flower data set or Fisher's Iris data set is a multivariate data set which was introduced by the British statistician and biologist Ronald Fisher, in his 1936 paper “The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis”. It can also be referred to as Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.

![Image of Ronald Fisher](https://github.com/richellaod/Images-for-Project-2018/blob/master/Ronald-Fisher.jpg)

#This data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length of the sepals and the width of the sepals, and the length of the petals and the width of the petals in centimetres. Based on the combination of these four features, Fisher went on to develop a linear discriminant model which would distinguish the species from each other. The data is provided in CSV format and looks something like the below:

![Image of Iris Data Set](https://github.com/richellaod/Images-for-Project-2018/blob/master/Iris%20Data%20Set.JPG)


![Image of an Iris](https://github.com/richellaod/Images-for-Project-2018/blob/master/iris_petal_sepal.png)

The above image shows exactly what we are talking about when we refer to sepal length and width and petal length and width.


I must admit when I first came across this data set I thought I would never be able to understand it or be able to write Python code which would enable me to extract information out of the data set to complete the project. However after a lot of research I figured out I was not the only one in this situation! Bringing information from different sources together and revising over Python code which our lecturer had gone through with us over the last couple of months enabled me to put everthing together as such.


## My Analysis

In order for me to compete this project there were a number of resources I needed. These included:

1. Visual Studio Code version 1.21.1 
2. Github
3. Python version 3.6 downloaded through Anaconda3
4. Iris dataset which I downloaded from UCI website [1]

Thankfully I had all of these downloaded in the previous weeks in order to complete other tasks which had been set out by my lecturer.

After a lot of research I realised that I would also need to ensure that there was a number of other libraries installed on Python so that I would be able to complete this project. These included matplotlib, numpy and pandas. From that I then had to ensure that other modules and functions were installed which would help me to extract the results from the Iris Data set and also give me the ability to create different types of graphs to display the data[2] (lines 4-16 on https://github.com/richellaod/Programming-Scripting-Project-2018/blob/master/Project.py):

![Image for Libraries which needed to be installed on Python](https://github.com/richellaod/Images-for-Project-2018/blob/master/Imports.JPG)

# Next Steps

After ensuring that I had all resourse needed to be able to complete the project it was time to upload the Iris Data set. I had dowlnoaded this from the UCI website as stated above as a CSV file. To do this I folloed instructions which were given in an article written by Dr. Jason Brownlee [3] however an error stating "NameError:name'pandas' is not defined. This was preventing me from uploading the data set. I then went onto the stack overflow website which gives indepth answers as to why code might not be working and from this I found out that maybe the correct version of Pandas may not have imported correctly on system [4]. I tried to import again and then used to following code to upload the data set (lines 18-20 on https://github.com/richellaod/Programming-Scripting-Project-2018/blob/master/Project.py):


![Image for Script for Importing the Data Set](https://github.com/richellaod/Images-for-Project-2018/blob/master/import%20data%20set.JPG)


Success! This time it loaded correctly for me as I had no error message appear.


Next I wanted to be able to view my data as easily as possible. From reading numerous articles on the internet, there were a number of important code to run on Python to be able to do this. Thes included:

1. print(dataset.shape) - which would show me how many instances and how many attributes the uploaded data contains.

![Image of Data Set Result](https://github.com/richellaod/Images-for-Project-2018/blob/master/result%20of%20data%20shape.JPG)

2. print(dataset.head(20)) - this would allow me to see the first 20 rows of data so I can ensure it all has uploaded correctly.

![Image for Visual Studio Code Result for first 20 lines](https://github.com/richellaod/Images-for-Project-2018/blob/master/VSC%20Data%20Set%20Upload.JPG)

3. print(dataset.describe()) - This command produces a summary of each attribute. This includes the  mean, the min and max values which is a project requirement. 

![Image for Mean, Min and Max](https://github.com/richellaod/Images-for-Project-2018/blob/master/mean%20min%20max.JPG)

4. print(dataset.groupby('class').size()) - This displays the number of instances that belong to each class. The below shows me that there are 150 samples of flowers: 50 - iris setosa, 50 - iris versicolor and 50 - iris virginica

![Image for Class Results](https://github.com/richellaod/Images-for-Project-2018/blob/master/class.JPG)






# References
[1] https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

[2] https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342

[3] https://machinelearningmastery.com/machine-learning-in-python-step-by-step/

[4] https://stackoverflow.com/questions/44594249/cannot-import-data-in-python-using-pandas





