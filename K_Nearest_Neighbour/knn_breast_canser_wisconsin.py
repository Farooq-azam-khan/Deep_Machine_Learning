import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split #replacement for cross_validation
from sklearn import preprocessing, neighbors


# FORMATTING DATA
# https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29
df = pd.read_csv('../data/breast-cancer-wisconsin.csv')
df.head()
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True) # remove useless data (id)
    
# APPLYING KNEIGHBORS MODEL
X = np.array(df.drop(['class'],1))
y = np.array(df['class'])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

print("done score is", clf.score(X_test,y_test))
