import tkinter as tk
from tkinter import messagebox
import joblib
import sys
import os

# Add src folder to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from fertilizer import fertilizer_advice


# Load trained model
model = joblib.load("crop_model.pkl")


# -----------------------------
# Prediction Function
# -----------------------------
def predict_crop():

    try:
        # Get values from input boxes
        n = float(entry_n.get())
        p = float(entry_p.get())
        k = float(entry_k.get())
        temperature = float(entry_temperature.get())
        humidity = float(entry_humidity.get())
        ph = float(entry_ph.get())
        rainfall = float(entry_rainfall.get())

        # Validate values
        if n < 0 or p < 0 or k < 0:
            messagebox.showerror(
                "Invalid Input",
                "N, P and K values cannot be negative."
            )
            return

        if humidity < 0 or humidity > 100:
            messagebox.showerror(
                "Invalid Input",
                "Humidity must be between 0 and 100."
            )
            return

        if ph < 0 or ph > 14:
            messagebox.showerror(
                "Invalid Input",
                "Soil pH must be between 0 and 14."
            )
            return

        # Prepare model input
        input_data = [[
            n,
            p,
            k,
            temperature,
            humidity,
            ph,
            rainfall
        ]]

        # Predict crop
        prediction = model.predict(input_data)

        crop = prediction[0]

        # Get fertilizer recommendation
        fertilizer = fertilizer_advice(n, p, k)

        # Display result
        result_crop.config(
            text=f"Recommended Crop: {crop}"
        )

        result_fertilizer.config(
            text=f"Recommended Fertilizer: {fertilizer}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter numbers only."
        )

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Something went wrong:\n{e}"
        )


# -----------------------------
# Clear Function
# -----------------------------
def clear_fields():

    entry_n.delete(0, tk.END)
    entry_p.delete(0, tk.END)
    entry_k.delete(0, tk.END)
    entry_temperature.delete(0, tk.END)
    entry_humidity.delete(0, tk.END)
    entry_ph.delete(0, tk.END)
    entry_rainfall.delete(0, tk.END)

    result_crop.config(
        text="Recommended Crop: "
    )

    result_fertilizer.config(
        text="Recommended Fertilizer: "
    )


# -----------------------------
# Main Window
# -----------------------------
root = tk.Tk()

root.title("Crop Recommendation & Fertilizer Advisory System")

root.geometry("700x700")

root.resizable(False, False)


# -----------------------------
# Title
# -----------------------------
title = tk.Label(
    root,
    text="CROP RECOMMENDATION SYSTEM",
    font=("Arial", 22, "bold")
)

title.pack(pady=20)


subtitle = tk.Label(
    root,
    text="Crop Recommendation & Fertilizer Advisory",
    font=("Arial", 13)
)

subtitle.pack(pady=5)


# -----------------------------
# Input Frame
# -----------------------------
input_frame = tk.Frame(root)

input_frame.pack(pady=20)


# Function to create input row
def create_input(label_text, row):

    label = tk.Label(
        input_frame,
        text=label_text,
        font=("Arial", 12)
    )

    label.grid(
        row=row,
        column=0,
        padx=15,
        pady=8,
        sticky="w"
    )

    entry = tk.Entry(
        input_frame,
        font=("Arial", 12),
        width=25
    )

    entry.grid(
        row=row,
        column=1,
        padx=15,
        pady=8
    )

    return entry


# -----------------------------
# Input Fields
# -----------------------------
entry_n = create_input(
    "Nitrogen (N):",
    0
)

entry_p = create_input(
    "Phosphorus (P):",
    1
)

entry_k = create_input(
    "Potassium (K):",
    2
)

entry_temperature = create_input(
    "Temperature (°C):",
    3
)

entry_humidity = create_input(
    "Humidity (%):",
    4
)

entry_ph = create_input(
    "Soil pH:",
    5
)

entry_rainfall = create_input(
    "Rainfall (mm):",
    6
)


# -----------------------------
# Buttons
# -----------------------------
button_frame = tk.Frame(root)

button_frame.pack(pady=20)


predict_button = tk.Button(
    button_frame,
    text="RECOMMEND CROP",
    font=("Arial", 12, "bold"),
    command=predict_crop,
    width=20
)

predict_button.grid(
    row=0,
    column=0,
    padx=10
)


clear_button = tk.Button(
    button_frame,
    text="CLEAR",
    font=("Arial", 12, "bold"),
    command=clear_fields,
    width=12
)

clear_button.grid(
    row=0,
    column=1,
    padx=10
)


# -----------------------------
# Result Frame
# -----------------------------
result_frame = tk.Frame(root)

result_frame.pack(
    pady=20
)


result_title = tk.Label(
    result_frame,
    text="FINAL RESULT",
    font=("Arial", 18, "bold")
)

result_title.pack(
    pady=10
)


result_crop = tk.Label(
    result_frame,
    text="Recommended Crop: ",
    font=("Arial", 14, "bold")
)

result_crop.pack(
    pady=10
)


result_fertilizer = tk.Label(
    result_frame,
    text="Recommended Fertilizer: ",
    font=("Arial", 14, "bold")
)

result_fertilizer.pack(
    pady=10
)


# -----------------------------
# Footer
# -----------------------------
footer = tk.Label(
    root,
    text="Machine Learning Based Agricultural Advisory System",
    font=("Arial", 10)
)

footer.pack(
    side="bottom",
    pady=15
)


# Start application
root.mainloop()