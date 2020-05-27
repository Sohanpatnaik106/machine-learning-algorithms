#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split = 40)
clf = clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

no_of_correct_predictions = 0
for i in range(len(labels_test)):
	if(pred[i] == labels_test[i]):
		no_of_correct_predictions = no_of_correct_predictions + 1

accuracy = (float(no_of_correct_predictions*100))/len(pred)

print "The accuracy is ", accuracy

no_of_feaatures = len(features_test[0])
print "The no of features ", no_of_feaatures


#########################################################


