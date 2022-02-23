from sklearn import svm


def get_data():
    X = [[0, 0], [1, 1]]
    # assume X is a set of Cartesian coordinates
    y = [0, 1]
    return X, y


def get_model():
    return svm.SVC()


def train(X, y, model):
    model.fit(X, y)


def predict(input, model):
    output = model.predict(input)
    return output

