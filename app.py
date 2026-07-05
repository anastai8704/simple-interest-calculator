import tkinter as tk
from tkinter import ttk

from simple_interest_calculator import calculate_simple_interest


class SimpleInterestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interest Calculator")
        self.root.geometry("500x380")
        self.root.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TButton", padding=8, font=("Segoe UI", 10, "bold"))
        style.configure("Card.TFrame", background="#ffffff")

        self.root.configure(bg="#eef2ff")

        card = ttk.Frame(self.root, padding=24, style="Card.TFrame")
        card.pack(expand=True, fill="both", padx=20, pady=20)

        title = tk.Label(
            card,
            text="Interest Calculator",
            font=("Segoe UI", 22, "bold"),
            bg="#ffffff",
            fg="#4c1d95",
        )
        title.pack(anchor="w", pady=(0, 6))

        subtitle = tk.Label(
            card,
            text="Calculate your interest in a few simple steps",
            font=("Segoe UI", 10),
            bg="#ffffff",
            fg="#6b7280",
        )
        subtitle.pack(anchor="w", pady=(0, 12))

        fields = [
            ("Principal (P)", "principal_var"),
            ("Rate (R %)", "rate_var"),
            ("Time in Years (N)", "time_var"),
        ]

        self.inputs = {}
        for label_text, var_name in fields:
            tk.Label(card, text=label_text, bg="#ffffff", font=("Segoe UI", 10, "bold")).pack(anchor="w", pady=(8, 2))
            var = tk.StringVar()
            entry = ttk.Entry(card, textvariable=var, width=35)
            entry.pack(anchor="w", pady=2)
            self.inputs[var_name] = var

        self.result_var = tk.StringVar(value="Result will appear here")
        result_frame = tk.Frame(card, bg="#f5f3ff", bd=1, relief="solid")
        result_frame.pack(fill="x", pady=(14, 10), ipady=8)
        tk.Label(
            result_frame,
            textvariable=self.result_var,
            font=("Segoe UI", 12, "bold"),
            bg="#f5f3ff",
            fg="#0f766e",
        ).pack(pady=8)

        button = ttk.Button(card, text="Calculate Result", command=self.calculate, width=24)
        button.pack(pady=(8, 6))

        formula_label = tk.Label(
            card,
            text="Formula: SI = (P × R × N) / 100",
            font=("Segoe UI", 9),
            bg="#ffffff",
            fg="#7c3aed",
        )
        formula_label.pack(anchor="w", pady=(6, 0))

        self.root.bind("<Return>", lambda event: self.calculate())

    def calculate(self):
        try:
            principal = float(self.inputs["principal_var"].get())
            rate = float(self.inputs["rate_var"].get())
            time_years = float(self.inputs["time_var"].get())
            interest = calculate_simple_interest(principal, rate, time_years)
            self.result_var.set(f"Interest: {interest:.2f}")
        except ValueError:
            self.result_var.set("Enter valid numbers")


if __name__ == "__main__":
    root = tk.Tk()
    SimpleInterestApp(root)
    root.mainloop()
