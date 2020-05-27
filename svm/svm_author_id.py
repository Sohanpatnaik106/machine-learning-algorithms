#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

from sklearn import svm
t0 = time()

#clf = svm.SVC(kernel = "linear")
clf = svm.SVC(kernel = "rbf", C = 10000.)
clf.fit(features_train, labels_train)

print "Training time : ", str(round(time() - t0)), "s"

t0 = time()
pred = clf.predict(features_test)
print "Testing time : ", str(round(time() - t0)), "s"

no_of_correct_predictions = 0

for i in range(len(labels_test)):
	if(labels_test[i] == pred[i]):
		no_of_correct_predictions = no_of_correct_predictions + 1

accuracy = (float(no_of_correct_predictions*100))/len(labels_test)
print "The accuracy is : ", accuracy

no_of_chris_emails = 0
for i in range(len(pred)):
	if(pred[i] == 1):
		no_of_chris_emails = no_of_chris_emails + 1

print no_of_chris_emails
#########################################################
### your code goes here ###

#########################################################