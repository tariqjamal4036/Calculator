import tkinter as tk
from tkinter import ttk

# Colors for modern look
BG_COLOR = "#1e1e2e"
BTN_COLOR = "#313244"
BTN_HIGHLIGHT = "#89b4fa"
TEXT_COLOR = "#f5f5f5"
ENTRY_COLOR = "#45475a"

class SmartCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Calculator")
        self.root.geometry("360x600")
        self.root.config(bg=BG_COLOR)
        self.root.resizable(False, False)

        # Mobile shape frame
        outer_frame = tk.Frame(root, bg="#000", bd=10, relief="ridge")
        outer_frame.place(relx=0.5, rely=0.5, anchor="center", width=340, height=580)

        # Display
        self.expression = ""
        self.input_text = tk.StringVar()

        entry_frame = tk.Frame(outer_frame, bg=BG_COLOR)
        entry_frame.pack(expand=True, fill="both")

        input_field = tk.Entry(entry_frame, font=("Arial", 24), fg=TEXT_COLOR,
                               bg=ENTRY_COLOR, textvariable=self.input_text,
                               justify="right", bd=0, relief="flat")
        input_field.pack(expand=True, fill="both", ipadx=8, ipady=15)

        # Buttons
        btns_frame = tk.Frame(outer_frame, bg=BG_COLOR)
        btns_frame.pack(expand=True, fill="both")

        buttons = [
            ("C", 1, 0), ("(", 1, 1), (")", 1, 2), ("/", 1, 3),
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("%", 5, 3)
        ]

        for (text, row, col) in buttons:
            b = tk.Button(btns_frame, text=text, font=("Arial", 18, "bold"),
                          fg=TEXT_COLOR, bg=BTN_COLOR, activebackground=BTN_HIGHLIGHT,
                          activeforeground="black", bd=0,
                          command=lambda t=text: self.press(t))
            b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

        for i in range(6):
            btns_frame.rowconfigure(i, weight=1)
            if i < 4:
                btns_frame.columnconfigure(i, weight=1)

    def press(self, key):
        if key == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except Exception:
                self.input_text.set("Error")
                self.expression = ""
        elif key == "C":
            self.expression = ""
            self.input_text.set("")
        else:
            self.expression += str(key)
            self.input_text.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = SmartCalculator(root)
    root.mainloop()
