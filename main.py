from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=300)

label = Label(text="Enter Your Weight (kg)")
label.place(x=63,y=70)


entry = Entry(width=10)
entry.place(x=92,y=95)

label2 = Label(text="Enter Your Height (cm)")
label2.place(x=63,y=120)

entry2 = Entry(width=10)
entry2.place(x=92,y=145)

def get_height():

    height = float(entry2.get())
    return height


def get_weight():

    weight = float(entry.get())
    return weight

def calculate_bmi(a=""):
    print(a)

    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Underweight!"
            messagebox.showinfo("Result", res)

        elif 18.5 <= bmi <= 24.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Normal."
            messagebox.showinfo("Result", res)
        elif 24.5 < bmi <= 29.9:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 <= bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: Extremely obese!!"
            messagebox.showinfo("Result", res)


button = Button(text="Calculate",command=calculate_bmi)
button.place(x=94,y=180)

window.mainloop()