from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__, template_folder="template")

# Load trained Random Forest model
model = joblib.load("predictive_maintenance_model.pkl")

# Final threshold selected during model evaluation
FINAL_THRESHOLD = 0.25


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get values from the form
        machine_type = request.form["machine_type"]

        air_temperature = float(request.form["air_temperature"])
        process_temperature = float(request.form["process_temperature"])
        rotational_speed = float(request.form["rotational_speed"])
        torque = float(request.form["torque"])
        tool_wear = float(request.form["tool_wear"])

        # Create dataframe in exactly the same format
        # used while training the model
        new_machine = pd.DataFrame({
            "Type": [machine_type],
            "Air temperature [K]": [air_temperature],
            "Process temperature [K]": [process_temperature],
            "Rotational speed [rpm]": [rotational_speed],
            "Torque [Nm]": [torque],
            "Tool wear [min]": [tool_wear]
        })

        # Get failure probability
        failure_probability = model.predict_proba(new_machine)[0][1]

        # Apply final threshold
        if failure_probability >= FINAL_THRESHOLD:
            status = "HIGH RISK"
            recommendation = "Maintenance Recommended"
            status_class = "danger"
        else:
            status = "LOW RISK"
            recommendation = "Machine Condition Normal"
            status_class = "success"

        probability_percentage = round(
            failure_probability * 100, 2
        )

        return render_template(
            "index.html",
            prediction=True,
            status=status,
            recommendation=recommendation,
            probability=probability_percentage,
            status_class=status_class,

            machine_type=machine_type,
            air_temperature=air_temperature,
            process_temperature=process_temperature,
            rotational_speed=rotational_speed,
            torque=torque,
            tool_wear=tool_wear
        )

    except Exception as e:

        return render_template(
            "index.html",
            error=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)