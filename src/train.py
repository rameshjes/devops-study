import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression


def load_data(file_path):

    data = pd.read_csv(file_path)
    # print(data.shape)
    # print(data.columns)
    # print(data["sentiment"].unique())
    # print(data.isnull().sum())

    return data


def preprocess_train(data):

    vectorizer = TfidfVectorizer()

    vectorizer.fit(data.review.values)

    X = vectorizer.transform(data.review.values)

    Y = data["sentiment"]

    # print(f"X shape {X.shape}")
    # print(f"Y shape {Y.shape}")
    return vectorizer, X, Y


def train_model(vectorizer, X, Y):

    model = LogisticRegression()
    model.fit(X, Y)

    return model


if __name__ == "__main__":

    data = load_data("../data/imdb_dataset.csv")

    data.loc[:, "sentiment"] = data.sentiment.map({"positive": 1, "negative": 0})
    print(data.sentiment.unique())
    vectorizer, X, Y = preprocess_train(data)

    model = train_model(vectorizer, X, Y)

    # # write vectorizer
    joblib.dump(vectorizer, open("vectorizer.pkl", "wb"))
    # # write model
    joblib.dump(model, open("model.pkl", "wb"))
