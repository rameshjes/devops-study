import joblib
from flask import Flask
from flask import render_template
from flask import request
"""
This script enable users to
write review in the text field,
when user clicks on Predict button,
then method predict() is called,
that returns the final label of the
user review

Note: html and css code are copied from :https://github.com/krishnaik06/Deployment-flask
"""

app = Flask("sentiment-classifier-ml")

vectorizer = joblib.load(open("vectorizer.pkl", "rb"))
model = joblib.load(open("model.pkl", "rb"))
labels = ["negative", "positive"]


def get_preprocessed_text(text):

    return vectorizer.transform([str(text)])


def find_label(preprocessed_text):

    return model.predict(preprocessed_text)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    sentence = " ".join([str(x) for x in request.form.values()])
    # print(f"sentence {sentence}")
    text = str(sentence).split()
    preprocessed_text = get_preprocessed_text(text)
    prediction = find_label(preprocessed_text)

    return render_template(
        "index.html",
        input_text="Input is: {}".format(sentence),
        prediction_text="Review is: {}".format(labels[int(prediction)]),
    )
    # return "Sentiment of text is %s" % labels[int(prediction)]


if __name__ == "__main__":
    app.run(debug=True)
