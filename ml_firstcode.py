# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 19:46:06 2019

@author: Gaurav
"""
import matplotlib.pyplot as plt

from sklearn import datasets # imoort digit dataset
from sklearn import svm  #get access to SVM algorithm
digits=datasets.load_digits() #load dataset
print(digits.data) #display features
print(digits.target) #display output column
clf=svm.SVC(gamma=0.001,C=100)
X,y=digits.data[:-10],digits.target[:-10]
clf.fit(X,y)
print(clf.predict(digits.data[-4].reshape(1,-1)))
#print(clf.score(digits.data[-5].reshape(1,-1),digits.target[:-10].reshape(1,-1)))
plt.imshow(digits.images[-4],cmap=plt.cm.gray_r,interpolation='nearest')
plt.show()