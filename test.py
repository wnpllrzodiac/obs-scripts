import tkinter as tk
from tkinter import simpledialog

class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None):
        self.dialog_width = 400
        self.dialog_height = 100
        self.bg_color = "#1d1f26"  # Set your desired background color here
        self.fg_color = "white"   # Set your desired foreground color here
        super().__init__(parent, title)

    def body(self, master):
        self.geometry(f"{self.dialog_width}x{self.dialog_height}")
        self.configure(bg=self.bg_color)
        tk.Label(master, text="Enter filename:", bg=self.bg_color, fg=self.fg_color).grid(row=0)
        self.entry = tk.Entry(master, width=100)
        self.entry.grid(row=0, column=1)
        return self.entry

    def buttonbox(self):
        box = tk.Frame(self)

        self.ok_button = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE, bg="green", fg="white")
        self.ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.cancel_button = tk.Button(box, text="Cancel", width=10, command=self.cancel, bg="red", fg="white")
        self.cancel_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()

    def apply(self):
        self.result = self.entry.get()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    dialog = CustomDialog(root, "Custom Dialog")
    print("Result:", dialog.result)