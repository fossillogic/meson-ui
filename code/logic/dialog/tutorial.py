#
# ==============================================================================
# Author: Michael Gene Brockus (Dreamer)
# Email: michaelbrockus@gmail.com
# Organization: Fossil Logic
# Description:
#     This file is part of the Fossil Logic project, where innovation meets
#     excellence in software development. Michael Gene Brockus, also known as
#     "Dreamer," is a dedicated contributor to this project. For any inquiries,
#     feel free to contact Michael at michaelbrockus@gmail.com.
# ==============================================================================
#
from tkinter import simpledialog, ttk, scrolledtext as ScrolledText
import tkinter as tk


class TutorialDialog(simpledialog.Dialog):
    def __init__(self, parent, theme):
        self.theme = theme
        super().__init__(parent)

    def body(self, master):
        self.title("Meson UI Tutorial")
        self.apply_theme()
        ttk.Label(
            master,
            text="Tutorial: How to Use Meson Build GUI",
            font=("Helvetica", 10, "bold"),
        ).grid(row=0, column=0, columnspan=2, pady=10)
        self.geometry("600x400")

        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=1, column=0, columnspan=2, pady=10)

        self.create_tab()

    def create_tab(self):
        steps = [
            (
                "Step 1: Setup",
                "  - Click the 'Setup' button to configure your project.\n  - Specify the build directory and any additional options.\n  - This step initializes the build environment and prepares the project for compilation.",
            ),
            (
                "Step 2: Compile",
                "  - Use the 'Compile' button to build your project using Ninja.\n  - Make sure the build directory is correctly set.\n  - This step compiles the source code into executable binaries or libraries.",
            ),
            (
                "Step 3: Test",
                "  - Click 'Test' to run the project's tests.\n  - Ensure that the tests are properly configured in your Meson build files.\n  - This step helps verify that your code is working as expected.",
            ),
            (
                "Step 4: Install",
                "  - The 'Install' button installs the built project.\n  - This step copies the compiled binaries and other necessary files to the installation directory.\n  - Make sure you have the necessary permissions to install the files.",
            ),
            (
                "Other Features",
                "  - 'Version': Displays the installed Meson version.\n  - 'Introspection': Explore project metadata.\n  - 'Clear Terminal': Clears the terminal output.\n  - 'Tool Info': Provides general information about this GUI.\n\nEnjoy using the Meson Build GUI for your projects!",
            ),
        ]

        for title, content in steps:
            frame = ttk.Frame(self.notebook, padding=10)
            self.notebook.add(frame, text=title)
            text = ScrolledText(
                frame,
                wrap=tk.WORD,
                height=30,
                width=60,
            )
            text.insert(tk.END, content)
            text.configure(state=tk.DISABLED)
            text.pack(expand=True, fill=tk.BOTH)

    def buttonbox(self):
        box = tk.Frame(self)

        button_close = ttk.Button(
            box, text="Close", command=self.ok, style="Blue.TButton"
        )
        button_close.pack(pady=10)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack()
        box.pack(pady=10)

    def apply_theme(self):
        if self.theme == "light":
            self.configure(bg="white")
            for widget in self.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.configure(background="white", foreground="black")
                elif isinstance(widget, ttk.Entry):
                    widget.configure(background="white", foreground="black")
                elif isinstance(widget, ttk.Button):
                    widget.configure(background="white", foreground="black")
        elif self.theme == "dark":
            self.configure(bg="black")
            for widget in self.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.configure(background="black", foreground="light blue")
                elif isinstance(widget, ttk.Entry):
                    widget.configure(background="black", foreground="light blue")
                elif isinstance(widget, ttk.Button):
                    widget.configure(background="black", foreground="light blue")
        elif self.theme == "meson":
            self.configure(bg="dark gray")
            for widget in self.winfo_children():
                if isinstance(widget, ttk.Label):
                    widget.configure(background="dark gray", foreground="black")
                elif isinstance(widget, ttk.Entry):
                    widget.configure(background="dark gray", foreground="black")
                elif isinstance(widget, ttk.Button):
                    widget.configure(background="#ADD8E6", foreground="black")
