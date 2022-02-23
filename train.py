from mlpipeline.utils import get_data, get_model, train


def main():
    X, y = get_data()
    model = get_model()
    print("training")
    train(X, y, model)
    print("trained")
    # save my model


if __name__ == "__main__":
    main()
