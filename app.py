import tkinter as tk
from tkinter import ttk

from simple_interest_calculator import calculate_simple_interest


class SimpleInterestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Interest Calculator Pro")
        self.root.geometry("420x280")
        self.root.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")

        self.root.configure(bg="#f4f7fb")

        title = tk.Label(
            self.root,
            text="Simple Interest Calculator Pro",
            font=("Segoe UI", 20, "bold"),
            bg="#f4f7fb",
            fg="#5b2ca5",
        )
        title.pack(pady=(20, 10))

        tk.Label(self.root, text="Principal (P)", bg="#f4f7fb").pack()
        self.principal_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.principal_var, width=25).pack(pady=2)

        tk.Label(self.root, text="Rate (R %)", bg="#f4f7fb").pack()
        self.rate_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.rate_var, width=25).pack(pady=2)

        tk.Label(self.root, text="Time in Years (N)", bg="#f4f7fb").pack()
        self.time_var = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.time_var, width=25).pack(pady=2)

        self.result_var = tk.StringVar(value="Result: ")
        tk.Label(
            self.root,
            textvariable=self.result_var,
            font=("Segoe UI", 12, "bold"),
            bg="#f4f7fb",
            fg="#d62828",
        ).pack(pady=10)

        ttk.Button(self.root, text="Calculate Interest", command=self.calculate, width=20).pack(pady=8)

    def calculate(self):
        try:
            principal = float(self.principal_var.get())
            rate = float(self.rate_var.get())
            time_years = float(self.time_var.get())
            interest = calculate_simple_interest(principal, rate, time_years)
            self.result_var.set(f"Simple Interest: {interest:.2f}")
        except ValueError:
            self.result_var.set("Enter valid numbers")


if __name__ == "__main__":
    root = tk.Tk()
    SimpleInterestApp(root)
    root.mainloop()
