import tkinter as tk
from PIL import ImageTk, Image


def calculate_bmr(weight, height, age, gender):
    if gender == "male":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    elif gender == "female":
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)
    return bmr

def calculate_tef(calories):
    return 0.1 * calories

def calculate_eee(activity_level, bmr):
    if activity_level == "sedentary":
        eee = 0.3 * bmr
    elif activity_level == "lightly active":
        eee = 0.4 * bmr
    elif activity_level == "moderately active":
        eee = 0.5 * bmr
    elif activity_level == "very active":
        eee = 0.6 * bmr
    return eee

def calculate_neat(calories, bmr, tef, eee):
    return calories - bmr - tef - eee

def calculate_total_tdee(neat, bmr, tef, eee):
    totalTdee = neat + bmr + tef + eee
    return totalTdee

def calculate_tdee(totalTdee, gender):
    if gender == "male":
        return totalTdee
    elif gender == "female":
        return totalTdee - 100
    

def calculate_all():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    age = int(age_entry.get())
    gender = gender_var.get()
    activity_level = activity_var.get()
    calories = float(calories_entry.get())

    bmr = calculate_bmr(weight, height, age, gender)
    tef = calculate_tef(calories)
    eee = calculate_eee(activity_level, bmr)
    neat = calculate_neat(calories, bmr, tef, eee)
    totalTdee = calculate_total_tdee(neat, bmr, tef, eee)
    tdee = calculate_tdee(totalTdee, gender)
    result_text = f"BMR: {bmr:.2f} kcal/day\nTEF: {tef:.2f} kcal/day\nEEE: {eee:.2f} kcal/day\nNEAT: {neat:.2f} kcal/day\nTDEE: {tdee:.2f} kcal/day"

    result_label.config(text=result_text, fg="white", bg="#2c3e50")

# create the Tkinter window
window = tk.Tk()
window.title("Energy Expenditure Calculator")
window.geometry("500x700")
window.configure(background="#2c4f85")
  
# open the image file
img = Image.open("health.png")

# set the desired height and width for the image
img = img.resize((200, 200), Image.LANCZOS)

# convert the image to a Tkinter-compatible format
photo = ImageTk.PhotoImage(img)

# create a label with the image
label = tk.Label(window, image=photo, bg="#2c4f85")

# display the label
label.pack()

# create the labels and entries for the user inputs
weight_label = tk.Label(text="Weight (kg):", bg="#2c4f85", fg="white", font='Helvetica 10 bold')
weight_label.pack()
weight_entry = tk.Entry()
weight_entry.pack()

height_label = tk.Label(text="Height (cm):", bg="#2c4f85", fg="white", font='Helvetica 10 bold')
height_label.pack()
height_entry = tk.Entry()
height_entry.pack()

age_label = tk.Label(text="Age (years):", bg="#2c4f85", fg="white", font='Helvetica 10 bold')
age_label.pack()
age_entry = tk.Entry()
age_entry.pack()

gender_label = tk.Label(text="Gender:", bg="#2c4f85", fg="white", font='Helvetica 10 bold')
gender_label.pack()
gender_var = tk.StringVar(value="male")
male_radio = tk.Radiobutton(text="Male", variable=gender_var, value="male", bg="#2c4f85", fg='white', selectcolor='#2c3f85')
male_radio.pack()
female_radio = tk.Radiobutton(text="Female", variable=gender_var, value="female", bg="#2c4f85", fg='white', selectcolor='#2c3f85')
female_radio.pack()

activity_label = tk.Label(text="Activity Level:", bg="#2c4f85", fg="white", font='Helvetica 10 bold')
activity_label.pack()
activity_var = tk.StringVar(value="sedentary")
sedentary_radio = tk.Radiobutton(text="Sedentary", variable=activity_var, value="sedentary", bg="#2c4f85", fg='white', selectcolor='#2c3f85')
sedentary_radio.pack()
lightly_active_radio = tk.Radiobutton(text="Lightly Active", variable=activity_var, value="lightly active", bg="#2c4f85", fg='white', selectcolor='#2c3f85')
lightly_active_radio.pack()
moderately_active_radio = tk.Radiobutton(text="Moderately Active", variable=activity_var, value="moderately active", bg="#2c4f85", fg='white', selectcolor='#2c3f85')
moderately_active_radio.pack()
moderately_active_radio = tk.Radiobutton(text="Very Active", variable=activity_var, value="very active", bg="#2c4f85", fg='white', selectcolor='#2c3f85')
moderately_active_radio.pack()

calories_label = tk.Label(text="Calories consumed per day:", bg="#2c4f85", fg="white", font='Helvetica 10 bold') 
calories_label.pack() 
calories_entry = tk.Entry()
calories_entry.pack() 
calculate_button = tk.Button(text="Calculate", command=calculate_all, bg="#2ecc71", fg="white") 
calculate_button.pack(pady=10) 
result_label = tk.Label(text="", font=("Helvetica", 12), bg="#2c4f85", fg="white") 
result_label.pack() 
window.mainloop()