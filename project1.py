
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x200")
root.configure(bg="lightgreen")

# STEP 2: CREATE THE DISPLAY SCREEN
display = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
display.pack(pady=10, padx=10, ipady=10, fill="both")

# STEP 3: CREATE VARIABLES TO STORE DATA
first_number = None
operation = None
should_clear_display = False


# STEP 4: CREATE FUNCTIONS FOR BUTTONS
def on_number_click(num):
    """When user clicks a number button (0-9)"""
    current = display.get()
    
    if should_clear_display:
        display.insert(tk.END, str(num))
        globals()['should_clear_display'] = False
    else:
        if current == "0":
            display.delete(0, tk.END)
        display.insert(tk.END, str(num))
        
def on_operation_click(op):
    """When user clicks an operation button (+, -, *, /)"""
    global first_number, operation, should_clear_display
    
    current = display.get()
    
    try:
        first_number = float(current)
    except:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    
    operation = op
    
    should_clear_display = True
    display.insert(tk.END, f" {op} ")
    
def on_equals_click():
    """When user clicks the equals button (=)"""
    global first_number, operation, should_clear_display
    
    current = display.get()
    
    try:
        parts = current.split(f" {operation} ")
        if len(parts) != 2:
            raise ValueError("Invalid format")
        
        second_number = float(parts[1])
        
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        elif operation == '*':
            result = first_number * second_number
        elif operation == '/':
            if second_number == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = first_number / second_number
        else:
            messagebox.showerror("Error", "Unknown operation.")
            return
        
        display.delete(0, tk.END)
        display.insert(0, str(result))
        first_number = None
        operation = None
        should_clear_display = True
    except:
        messagebox.showerror("Error", "Invalid calculation")
        
        
def on_clear_click():
    """When user clicks the C (Clear) button"""
    global first_number, operation, should_clear_display
    
    display.delete(0, tk.END)
    display.insert(0, "0")
    first_number = None
    operation = None
    should_clear_display = False


# STEP 5: CREATE BUTTONS
button_frame = tk.Frame(root, bg="lightgreen")
button_frame.pack(pady=10, padx=10, fill="both", expand=True)

# row 1: 7, 8, 9, /
button_7 = tk.Button(button_frame, text="7", font=("Arial", 14), command=lambda: on_number_click(7))
button_7.grid(row=0, column=0, padx=5, pady=5, sticky="nsew", ipady=10)
button_8 = tk.Button(button_frame, text="8", font=("Arial", 14), command=lambda: on_number_click(8))
button_8.grid(row=0, column=1, padx=5, pady=5, sticky="nsew", ipady=10)
button_9 = tk.Button(button_frame, text="9", font=("Arial", 14), command=lambda: on_number_click(9))
button_9.grid(row=0, column=2, padx=5, pady=5, sticky="nsew", ipady=10)
button_divide = tk.Button(button_frame, text="/", font=("Arial", 14), command=lambda: on_operation_click("/"))
button_divide.grid(row=0, column=3, padx=5, pady=5, sticky="nsew", ipady=10)

# row 2: 4, 5, 6, *
button_4 = tk.Button(button_frame, text="4", font=("Arial", 14), command=lambda: on_number_click(4))
button_4.grid(row=1, column=0, padx=5, pady=5, sticky="nsew", ipady=10)
button_5 = tk.Button(button_frame, text="5", font=("Arial", 14), command=lambda: on_number_click(5))
button_5.grid(row=1, column=1, padx=5, pady=5, sticky="nsew", ipady=10)
button_6 = tk.Button(button_frame, text="6", font=("Arial", 14), command=lambda: on_number_click(6))
button_6.grid(row=1, column=2, padx=5, pady=5, sticky="nsew", ipady=10)
button_multiply = tk.Button(button_frame, text="*", font=("Arial", 14), command=lambda: on_operation_click("*"))
button_multiply.grid(row=1, column=3, padx=5, pady=5, sticky="nsew", ipady=10)

# row 3: 1, 2, 3, -
button_1 = tk.Button(button_frame, text="1", font=("Arial", 14), command=lambda: on_number_click(1))
button_1.grid(row=2, column=0, padx=5, pady=5, sticky="nsew", ipady=10)
button_2 = tk.Button(button_frame, text="2", font=("Arial", 14), command=lambda: on_number_click(2))
button_2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew", ipady=10)
button_3 = tk.Button(button_frame, text="3", font=("Arial", 14), command=lambda: on_number_click(3))
button_3.grid(row=2, column=2, padx=5, pady=5, sticky="nsew", ipady=10)
button_subtract = tk.Button(button_frame, text="-", font=("Arial", 14), command=lambda: on_operation_click("-"))
button_subtract.grid(row=2, column=3, padx=5, pady=5, sticky="nsew", ipady=10)

# row 4: 0, ., =, +
button_0 = tk.Button(button_frame, text="0", font=("Arial", 14), command=lambda: on_number_click(0))
button_0.grid(row=3, column=0, padx=5, pady=5, sticky="nsew", ipady=10)
button_decimal = tk.Button(button_frame, text=".", font=("Arial", 14), command=lambda: on_number_click("."))
button_decimal.grid(row=3, column=1, padx=5, pady=5, sticky="nsew", ipady=10)
button_clear = tk.Button(button_frame, text="C", font=("Arial", 14), command=on_clear_click)
button_clear.grid(row=3, column=2, padx=5, pady=5, sticky="nsew", ipady=10)
button_add = tk.Button(button_frame, text="+", font=("Arial", 14), command=lambda: on_operation_click("+"))
button_add.grid(row=3, column=3, padx=5, pady=5, sticky="nsew", ipady=10)

# row 5: equals button
button_equals = tk.Button(root, text="=", font=("Arial", 16), bg="lightblue", command=on_equals_click)  
button_equals.pack(pady=10, ipady=10, fill="both")  

# make the buttons expand evenly
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
    button_frame.grid_rowconfigure(i, weight=1)

# step 6 : start the main event loop
root.mainloop() 

