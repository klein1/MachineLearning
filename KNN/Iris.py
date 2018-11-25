from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn import  cross_validation
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()
X = iris.data
Y = iris.target
validation_size = 0.20
seed = 1
X_train,X_validation,Y_train,Y_validation = cross_validation.train_test_split(X,Y,test_size=validation_size,random_state=seed)

knn = KNeighborsClassifier()
knn.fit(X_train,Y_train)

predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation,predictions))
print(confusion_matrix(Y_validation,predictions))
print(classification_report(Y_validation,predictions))