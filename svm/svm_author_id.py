#!/usr/bin/python

"""
    this is the code to accompany the Lesson 2 (SVM) mini-project

    use an SVM to identify emails from the Enron corpus by their authors

    Sara has label 0
    Chris has label 1

"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
# smaller data set
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel='rbf', C=10000)
t_fit = time()
clf.fit(features_train, labels_train)
print "training time: ", round(time() - t_fit, 3), "s"
t_predict = time()
predict = clf.predict(features_test)
print "predict time: ", round(time() - t_predict, 3), "s"
print accuracy_score(predict, labels_test)
print predict[10], predict[26], predict[50]
print len([i for i in predict if i == 1])
#########################################################


