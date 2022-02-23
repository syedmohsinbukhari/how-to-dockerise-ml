from mlpipeline.utils import get_data, get_model, train, predict


def main():
    X, y = get_data()
    model = get_model()
    train(X, y, model)
    output = predict([[2., 2.]], model)
    print(output)


if __name__ == "__main__":
    main()
