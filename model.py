from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

def get_model():
    iris = load_iris()
    clf = DecisionTreeClassifier()
    clf.fit(iris.data, iris.target)
    return clf, iris
