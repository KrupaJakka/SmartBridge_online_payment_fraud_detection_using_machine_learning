from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)

# load model (if you trained and saved model)
try:
    model = pickle.load(open("payments.pkl", "rb"))
except:
    model = None

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict_page")
def predict_page():
    return render_template("predict.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        step = float(request.form["step"])
        amount = float(request.form["amount"])
        oldbalanceOrg = float(request.form["oldbalanceOrg"])
        newbalanceOrig = float(request.form["newbalanceOrig"])
        oldbalanceDest = float(request.form["oldbalanceDest"])
        newbalanceDest = float(request.form["newbalanceDest"])

        data = np.array([[step, amount, oldbalanceOrg,
                          newbalanceOrig, oldbalanceDest, newbalanceDest]])

        if model:
            prediction = model.predict(data)
            result = "Fraud Transaction" if prediction[0] == 1 else "Safe Transaction"
        else:
            result = "Model not loaded"

    except:
        result = "Error in input"

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
