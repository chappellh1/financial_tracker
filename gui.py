import tkinter as tk
from tkinter import ttk
from income import Income  # Assuming you have an Income class for database operations

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Financial Tracker")

        self.create_welcome_frame()
        self.create_income_frame()  # Create the income frame

    def create_welcome_frame(self):
        self.welcome_frame = ttk.Frame(self)
        welcome_label = tk.Label(self.welcome_frame, text="Welcome to Finance Tracker, please select from our options")
        welcome_label.pack(pady=10)

        # Buttons for different options
        income_button = tk.Button(self.welcome_frame, text="Manage Income", command=self.show_income_frame)
        income_button.pack(pady=5)



        # Add more buttons as needed

        self.welcome_frame.pack(expand=1, fill="both")

        # Button for managing income
        income_button = tk.Button(self.welcome_frame, text="Manage Income", command=self.show_income_frame)
        income_button.pack(pady=5)

        # ... rest of the welcome frame ...

    def create_income_frame(self):
        self.income_frame = ttk.Frame(self)

        tk.Label(self.income_frame, text="Income Amount:").grid(row=0, column=0)
        self.amount_entry = tk.Entry(self.income_frame)
        self.amount_entry.grid(row=0, column=1)

        tk.Label(self.income_frame, text="Timeframe:").grid(row=1, column=0)
        self.timeframe_entry = tk.Entry(self.income_frame)
        self.timeframe_entry.grid(row=1, column=1)

        tk.Label(self.income_frame, text="State:").grid(row=2, column=0)
        self.state_entry = tk.Entry(self.income_frame)
        self.state_entry.grid(row=2, column=1)

        tk.Label(self.income_frame, text="Source:").grid(row=3, column=0)
        self.source_entry = tk.Entry(self.income_frame)
        self.source_entry.grid(row=3, column=1)

        submit_btn = tk.Button(self.income_frame, text="Submit Income", command=self.submit_income)
        submit_btn.grid(row=4, column=1)

    def show_income_frame(self):
        self.welcome_frame.pack_forget()  # Hide welcome frame
        self.income_frame.pack(expand=1, fill="both")  # Show income frame

    def submit_income(self):
        # Retrieve data from entry fields
        amount = float(self.amount_entry.get())
        timeframe = self.timeframe_entry.get()
        state = self.state_entry.get()
        source = self.source_entry.get()

        # Create Income object and save to database
        income = Income(amount, timeframe, state, source)
        income.save_to_db('my_finances.db')

        # Optionally, clear the fields or show a success message

# Instantiate and run this in main.py