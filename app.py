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
        style.configure("Accent.TButton", foreground="#ffffff", background="#5b2ca5", font=("Segoe UI", 11, "bold"))

        self.root.configure(bg="#f4f7fb")
        self.root.geometry("460x340")

        title = tk.Label(
            self.root,
            text="Simple Interest Calculator Pro",
            font=("Segoe UI", 22, "bold"),
            bg="#f4f7fb",
            fg="#5b2ca5",
        )
        title.pack(pady=(20, 10))

        form_frame = ttk.Frame(self.root, padding=15)
        form_frame.pack(fill="both", expand=True)

        ttk.Label(form_frame, text="Principal (P)", font=("Segoe UI", 10, "bold")).grid(row=0, column=0, sticky="w", pady=4)
        self.principal_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.principal_var, width=30).grid(row=0, column=1, pady=4)

        ttk.Label(form_frame, text="Rate (R %)", font=("Segoe UI", 10, "bold")).grid(row=1, column=0, sticky="w", pady=4)
        self.rate_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.rate_var, width=30).grid(row=1, column=1, pady=4)

        ttk.Label(form_frame, text="Time in Years (N)", font=("Segoe UI", 10, "bold")).grid(row=2, column=0, sticky="w", pady=4)
        self.time_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.time_var, width=30).grid(row=2, column=1, pady=4)

        self.result_var = tk.StringVar(value="Enter values and press Calculate Result")
        result_label = tk.Label(
            self.root,
            textvariable=self.result_var,
            font=("Segoe UI", 12, "bold"),
            bg="#f4f7fb",
            fg="#5b2ca5",
            wraplength=420,
            justify="center",
        )
        result_label.pack(pady=(10, 0))

        ttk.Button(
            self.root,
            text="Calculate Result",
            command=self.calculate,
            style="Accent.TButton",
            width=22,
        ).pack(pady=12)

    def calculate(self):
        try:
            principal = float(self.principal_var.get())
            rate = float(self.rate_var.get())
            time_years = float(self.time_var.get())
            interest = calculate_simple_interest(principal, rate, time_years)
            total_amount = principal + interest
            self.result_var.set(
                f"Interest: {interest:.2f} | Total amount after {time_years:.1f} years: {total_amount:.2f}"
            )
        except ValueError:
            self.result_var.set("Enter valid numbers for P, R, and N")


if __name__ == "__main__":
    root = tk.Tk()
    SimpleInterestApp(root)
    root.mainloop()
