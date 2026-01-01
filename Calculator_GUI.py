# Calculator - GUI Version using Tkinter
# This creates a visual calculator with buttons, just like a real calculator

import tkinter as Tk
from tkinter import messagebox

# ============================================
# STEP 1: CREATE THE MAIN WINDOW
# ============================================
root = Tk.Tk()
root.title("Simple Calculator")
root.geometry("400x500")  # Width x Height
root.configure(bg="lightblue")

# ============================================
# STEP 2: CREATE THE DISPLAY SCREEN
# ============================================
# This will show what the user is typing and the result
display = Tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
display.pack(pady=10, padx=10, ipady=10, fill="both")

# ============================================
# STEP 3: CREATE VARIABLES TO STORE DATA
# ============================================
first_number = None
operation = None
should_clear_display = False

# ============================================
# STEP 4: CREATE FUNCTIONS FOR BUTTONS
# ============================================

def on_number_click(num):
    """When user clicks a number button (0-9)"""
    # Get what's currently shown on the display
    current = display.get()
    
    # If we just did an operation, clear the display first
    if should_clear_display:
        display.delete(0, Tk.END)
        display.insert(0, str(num))
        globals()['should_clear_display'] = False
    else:
        # Add the number to what's already there
        if current == "0":
            display.delete(0, Tk.END)
        display.insert(Tk.END, str(num))


def on_operation_click(op):
    """When user clicks an operation button (+, -, *, /)"""
    global first_number, operation, should_clear_display
    
    # Save the number the user typed
    current = display.get()
    
    try:
        first_number = float(current)
    except:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    
    # Save which operation they chose
    operation = op
    
    # Next time they type, clear the display for the second number
    should_clear_display = True
    
    # Show the user what operation they selected
    display.insert(Tk.END, f" {op} ")


def on_equals_click():
    """When user clicks the = button to get the result"""
    global first_number, operation, should_clear_display
    
    try:
        second_number = float(display.get().split()[-1])  # Get the last number after the operation
    except:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    
    # Do the math based on the operation
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            messagebox.showerror("Error", "Cannot divide by zero!")
            return
        result = first_number / second_number
    
    # Show the result
    display.delete(0, Tk.END)
    display.insert(0, str(result))
    should_clear_display = True


def on_clear_click():
    """When user clicks the C (Clear) button"""
    global first_number, operation, should_clear_display
    
    display.delete(0, Tk.END)
    display.insert(0, "0")
    first_number = None
    operation = None
    should_clear_display = False


# ============================================
# STEP 5: CREATE BUTTONS
# ============================================

# Frame for number buttons (organized in rows like a real calculator)
button_frame = Tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10, padx=10, fill="both", expand=True)

# ROW 1: Numbers 7, 8, 9 and divide button
button_7 = Tk.Button(button_frame, text="7", font=("Arial", 18), command=lambda: on_number_click(7))
button_7.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", ipady=10)

button_8 = Tk.Button(button_frame, text="8", font=("Arial", 18), command=lambda: on_number_click(8))
button_8.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", ipady=10)

button_9 = Tk.Button(button_frame, text="9", font=("Arial", 18), command=lambda: on_number_click(9))
button_9.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", ipady=10)

button_divide = Tk.Button(button_frame, text="/", font=("Arial", 18), bg="orange", command=lambda: on_operation_click("/"))
button_divide.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", ipady=10)

# ROW 2: Numbers 4, 5, 6 and multiply button
button_4 = Tk.Button(button_frame, text="4", font=("Arial", 18), command=lambda: on_number_click(4))
button_4.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", ipady=10)

button_5 = Tk.Button(button_frame, text="5", font=("Arial", 18), command=lambda: on_number_click(5))
button_5.grid(row=1, column=1, padx=5, pady=5, sticky="nsew", ipady=10)

button_6 = Tk.Button(button_frame, text="6", font=("Arial", 18), command=lambda: on_number_click(6))
button_6.grid(row=1, column=2, padx=5, pady=5, sticky="nsew", ipady=10)

button_multiply = Tk.Button(button_frame, text="*", font=("Arial", 18), bg="orange", command=lambda: on_operation_click("*"))
button_multiply.grid(row=1, column=3, padx=5, pady=5, sticky="nsew", ipady=10)

# ROW 3: Numbers 1, 2, 3 and subtract button
button_1 = Tk.Button(button_frame, text="1", font=("Arial", 18), command=lambda: on_number_click(1))
button_1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew", ipady=10)

button_2 = Tk.Button(button_frame, text="2", font=("Arial", 18), command=lambda: on_number_click(2))
button_2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew", ipady=10)

button_3 = Tk.Button(button_frame, text="3", font=("Arial", 18), command=lambda: on_number_click(3))
button_3.grid(row=2, column=2, padx=5, pady=5, sticky="nsew", ipady=10)

button_subtract = Tk.Button(button_frame, text="-", font=("Arial", 18), bg="orange", command=lambda: on_operation_click("-"))
button_subtract.grid(row=2, column=3, padx=5, pady=5, sticky="nsew", ipady=10)

# ROW 4: Number 0, Clear button, and Add button
button_0 = Tk.Button(button_frame, text="0", font=("Arial", 18), command=lambda: on_number_click(0))
button_0.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", ipady=10)

button_clear = Tk.Button(button_frame, text="C", font=("Arial", 18), bg="red", fg="white", command=on_clear_click)
button_clear.grid(row=3, column=1, padx=5, pady=5, sticky="nsew", ipady=10)

button_equals = Tk.Button(button_frame, text="=", font=("Arial", 18), bg="green", fg="white", command=on_equals_click)
button_equals.grid(row=3, column=2, padx=5, pady=5, sticky="nsew", ipady=10)

button_add = Tk.Button(button_frame, text="+", font=("Arial", 18), bg="orange", command=lambda: on_operation_click("+"))
button_add.grid(row=3, column=3, padx=5, pady=5, sticky="nsew", ipady=10)

# Make buttons expand evenly
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# ============================================
# STEP 6: START THE PROGRAM
# ============================================
root.mainloop()
