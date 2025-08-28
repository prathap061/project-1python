from model import get_model


def test_prediction():
    clf, _ = get_model()
    prediction = clf.predict([[5.1, 3.5, 1.4, 0.2]])[0]
    assert prediction in [0, 1, 2]
