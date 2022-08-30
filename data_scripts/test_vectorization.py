#importing libraries
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
# import os
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import cross_decomposition, metrics, svm
# import urllib.parse
from sklearn.metrics import confusion_matrix

import pandas as pd
# import re
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV
import pickle

data = pd.read_csv('E:\\Documents\\major_project\\app\\xss-attack-ml\\data\\XSS_dataset.csv')

corpus = [d for d in data['Sentence']]

y = [[1,0][d!= 1] for d in data['Label']]
vectorizer2 = TfidfVectorizer()

X = vectorizer2.fit_transform(corpus)

nlp_model = pickle.load(open('E:\\Documents\\major_project\\app\\xss-attack-ml\\model\\nlp_model.pkl', 'rb'))
logistic_model = pickle.load(open('E:\\Documents\\major_project\\app\\xss-attack-ml\\model\\logistic_model.pkl', 'rb'))
svm_model = pickle.load(open('E:\\Documents\\major_project\\app\\xss-attack-ml\\model\\SVM_model.pkl', 'rb'))



# Checking for any code whether it is an attack or not using Decision Tree
xss_string = 'document.write'
xss_list = [xss_string]

feature_vector = []

if xss_string.__contains__('script'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('&'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('%'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('/'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('\\'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('+'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('document'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('window'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('onload'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('onerror'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('div'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('iframe'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('img'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('src'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('var'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('eval'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('href'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('cookie'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('fromCharCode'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('?'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__(';'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('http'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('js'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('#'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('='):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('['):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__(']'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('$'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('('):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__(')'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('*'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__(','):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('-'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('<'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('>'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('location'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('search'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('&#'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__(':'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('.'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__(' '):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('"'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('//'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('|'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('&#166;'):
    feature_vector.append(1)
else:
    feature_vector.append(0)

if xss_string.__contains__('alert'):
    feature_vector.append(1)
else:
    feature_vector.append(0)



X_predict = vectorizer2.transform(xss_list)
y_Predict = nlp_model.predict(X_predict)
print('nlp result = ', y_Predict)

svm_predict = svm_model.predict([feature_vector])
print('SVM result = ', svm_predict)

logistic_predict = logistic_model.predict([feature_vector])
print('Logistic result = ', logistic_predict)

score  = y_Predict[0] + svm_predict[0] + logistic_predict[0]

if score >= 2:
  print('It is an XSS attack')
else:
  print('It is not an XSS attack')