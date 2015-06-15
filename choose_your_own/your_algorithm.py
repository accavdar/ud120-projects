#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow" points mixed
### in together--separate them so we can give them different colors in the scatterplot,
### and visually identify them
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
#################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
from sklearn.metrics import accuracy_score

clf1 = KNeighborsClassifier(n_neighbors=10, weights='distance')
# clf2 = AdaBoostClassifier()
# clf3 = RandomForestClassifier()

clf1.fit(features_train, labels_train)
# clf2.fit(features_train, labels_train)
# clf3.fit(features_train, labels_train)

predict1 = clf1.predict(features_test)
# predict2 = clf2.predict(features_test)
# predict3 = clf3.predict(features_test)

print "KNeighbourClassifier", accuracy_score(predict1, labels_test)
# print "Adaboost", accuracy_score(predict2, labels_test)
# print "RandomForest", accuracy_score(predict3, labels_test)

try:
    prettyPicture(clf1, features_test, labels_test)
    # prettyPicture(clf2, features_test, labels_test)
    # prettyPicture(clf3, features_test, labels_test)
except NameError:
    pass
