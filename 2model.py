import pandas as pd
import joblib

df = pd.read_csv(
    'german_credit_data.csv'
)
# print(df.shape) #(1000, 11)
# print(df.isnull().sum())    # saving account & checking account
# print(df.columns.values)
# ['Unnamed: 0' 'Age' 'Sex' 'Job' 'Housing' 'Saving accounts'
#  'Checking account' 'Credit amount' 'Duration' 'Purpose' 'Risk']

df1 = pd.DataFrame(
    df[['Age', 'Sex', 'Job', 'Housing', 'Credit amount', 'Duration', 'Purpose']]
)
df1['Risk'] = df['Risk']

from sklearn.preprocessing import LabelEncoder
label = LabelEncoder()

df1['Sex'] = label.fit_transform(df['Sex'])
# print(label.classes_)   # ['female' 'male']                 

df1['Housing'] = label.fit_transform(df['Housing'])
# print(label.classes_)   # ['free' 'own' 'rent']

df1['Purpose'] = label.fit_transform(df['Purpose'])
# print(label.classes_)   
# # ['business' 'car' 'domestic appliances' 'education' 
# 'furniture/equipment' 'radio/TV' 'repairs' 'vacation/others']

df1['Risk'] = label.fit_transform(df['Risk'])
# print(label.classes_)  # ['bad' 'good']

x = df1.drop(['Risk'], axis =1)
y = df1['Risk']
# print(x.head(2))
# print(y.head(2))
# print(x.isnull().sum())
# print(y.isnull().sum())

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(
    x, y,
    test_size = .1
)
# print(len(xtrain))
# print(len(xtest))

from sklearn.linear_model import LogisticRegression
modelLogR = LogisticRegression(solver= 'liblinear', multi_class='auto')
modelLogR.fit(xtrain, ytrain)

from sklearn import tree
modeltree = tree.DecisionTreeClassifier()
modeltree.fit(xtrain, ytrain)

def nNeighbors():           # untuk menentukan berapa titik disekitarnya/ titik tetangga untuk menentuka
    x = round(len(xtrain) ** .5)
    if x % 2 == 0:
        return x +1
    else:
        return x
print(nNeighbors()) # 31

# KNN (K-Nearest Neighbors)
from sklearn.neighbors import KNeighborsClassifier
modelKneighbors = KNeighborsClassifier(
    n_neighbors = 31
)
modelKneighbors.fit(xtrain, ytrain)

print('score Logres:', round(modelLogR.score(xtrain, ytrain) * 100, 2), '%')
print('score tress:', round(modeltree.score(xtrain, ytrain) * 100, 2), '%')
print('score Kneiggbors:', round(modelKneighbors.score(xtrain, ytrain) * 100, 2), '%')

print('score test Logres:', round(modelLogR.score(xtest, ytest) * 100, 2), '%')
print('score test tress:', round(modeltree.score(xtest, ytest) * 100, 2), '%')
print('score test Kneiggbors:', round(modelKneighbors.score(xtest, ytest) * 100, 2), '%')

print(x.iloc[0])
print(y.iloc[0])

print('predict tree: ', modeltree.predict([x.iloc[0]])[0])
print('proba tree: ', modeltree.predict_proba([x.iloc[0]]))

print('predict logres: ', modelLogR.predict([x.iloc[0]])[0])
print('proba logres: ', modelLogR.predict_proba([x.iloc[0]]))

print('predict Kn: ', modelKneighbors.predict([x.iloc[0]])[0])
print('proba Kn: ', modelKneighbors.predict_proba([x.iloc[0]]))

joblib.dump(modelLogR, 'logRegGermancredit')