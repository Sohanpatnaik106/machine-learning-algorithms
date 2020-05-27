#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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

from sklearn.naive_bayes import GaussianNB

t0 = time()
clf = GaussianNB()
clf.fit(features_train, labels_train)

print "Training time = " + str(round(time() - t0)) + "s"

t0 = time()
pred = clf.predict(features_test)
print "Testing time = " + str(round(time() - t0)) + "s"

no_of_correct_predictions = 0

for i in range(len(labels_test)):
	if(labels_test[i] == pred[i]):
		no_of_correct_predictions = no_of_correct_predictions + 1;

accuracy = (float(no_of_correct_predictions*100))/len(features_test)

print "The accuracy is " + str(accuracy)



#########################################################
### your code goes here ###


#########################################################


