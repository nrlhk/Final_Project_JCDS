import pandas as pd
import joblib

df = pd.read_csv(
    'data.csv'
)
# print(df.shape) #1143,15
# print(df.isnull().sum())  #382

df = df.dropna()
dfdummy1 = pd.get_dummies(df['age'])
dfdummy2 = pd.get_dummies(df['gender'])
df = pd.concat([dfdummy1, dfdummy2, df], axis = 1)

x = df[['30-34', '35-39', '40-44', '45-49', 'F', 'M','interest1', 'interest2', 'interest3']]
y = df['approved_conversion']

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(
    x, y,
    test_size = .1
)

from sklearn import tree
modeltree = tree.DecisionTreeClassifier()
modeltree.fit(xtrain, ytrain)

print('score tress:', round(modeltree.score(xtrain, ytrain) * 100, 2), '%')

joblib.dump(modeltree, 'treemodelforconversion')
