from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# -------------------------------------------------
# Load the trained crop recommendation model
# -------------------------------------------------

model_path = os.path.join(
    os.path.dirname(__file__),
    "crop_model.pkl"
)

model = joblib.load(model_path)


# -------------------------------------------------
# Home Page
# -------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------------------------
# Crop Prediction
# -------------------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from HTML form
        N = float(request.form["N"])
        P = float(request.form["P"])
        K = float(request.form["K"])
        temperature = float(request.form["temperature"])
        humidity = float(request.form["humidity"])
        ph = float(request.form["ph"])
        rainfall = float(request.form["rainfall"])

        # Create input DataFrame
        input_data = pd.DataFrame(
            [[
                N,
                P,
                K,
                temperature,
                humidity,
                ph,
                rainfall
            ]],
            columns=[
                "N",
                "P",
                "K",
                "temperature",
                "humidity",
                "ph",
                "rainfall"
            ]
        )

        # Predict crop
        prediction = model.predict(input_data)

        crop = prediction[0]

        # Show result on webpage
        return render_template(
            "index.html",
            crop=crop
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=str(e)
        )


# -------------------------------------------------
# Run Flask Application
# -------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)