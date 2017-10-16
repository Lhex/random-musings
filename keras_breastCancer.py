#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:54:20 2017

@author: yapxiuren
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:37:18 2017

@author: yapxiuren
"""
#%%
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn import datasets

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

#%%
# load dataset
dataframe = datasets.load_breast_cancer()
df = dataframe.data[:,0:30].astype(float)
y = dataframe.target

X_train, X_test, y_train, y_test = train_test_split(df, y, test_size=0.2)
print (X_train.shape, y_train.shape)
print (X_test.shape, y_test.shape)

y_train = keras.utils.to_categorical(y_train, num_classes=2)

#%%

#define baseline model
#def baseline_model():
#	# create model
#	model = Sequential()
#	model.add(Dense(30, input_dim=30, activation='relu'))
#	model.add(Dense(1, activation='sigmoid'))
#	# Compile model
#	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#	return model

def baseline_model():
    model = Sequential()
    model.add(Dense(50, input_dim = 30, init = 'uniform', activation = 'relu'))
    model.add(Dense(25, init = 'uniform', activation = 'relu'))
    model.add(Dense(1, init = 'uniform', activation = 'sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
    return model

#model = baseline_model()
#model.fit(X, Y, nb_epoch=500, batch_size=5)
#scores = model.evaluate(X, Y)
#print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
#
#estimator = KerasClassifier(build_fn=baseline_model, epochs=150, batch_size=10, verbose=1)
#
#kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
#
#results = cross_val_score(estimator, X, Y, cv=kfold)
#print("Baseline: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

#%%

model = Sequential()
model.add(Dense(30, input_dim = 30, init = 'uniform', activation = 'relu'))
model.add(Dense(10, init = 'uniform', activation = 'relu'))
model.add(Dense(2, init = 'uniform', activation = 'sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])

model.fit(x = X_train, y = y_train, epochs = 200, batch_size = 32, validation_split = 0.1, verbose = 1)

y_pred = model.predict_classes(x = X_test, verbose = 1)

#%%

from sklearn.metrics import classification_report,confusion_matrix

print(confusion_matrix(y_test, y_pred))

#%%



















