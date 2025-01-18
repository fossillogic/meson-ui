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
from tkinter import simpledialog, ttk
import tkinter as tk


class InitDialog(simpledialog.Dialog):
    def __init__(self, parent, theme):
        self.theme = theme
        super().__init__(parent)

    def body(self, master):
        self.apply_theme()
        ttk.Label(
            master,
            text="Meson Init Options",
        ).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(master, text="Project Name:").grid(row=1, column=0, sticky=tk.W)
        self.project_name_entry = ttk.Entry(master, width=40)
        self.project_name_entry.grid(row=1, column=1, pady=10, sticky=tk.W + tk.E)

        ttk.Label(master, text="Language:").grid(row=2, column=0, sticky=tk.W)
        self.language_entry = ttk.Entry(master, width=40)
        self.language_entry.grid(row=2, column=1, pady=10, sticky=tk.W + tk.E)

        ttk.Label(master, text="Other Options:").grid(row=3, column=0, sticky=tk.W)
        self.other_options_entry = ttk.Entry(master, width=40)
        self.other_options_entry.grid(row=3, column=1, pady=10, sticky=tk.W + tk.E)

    def apply(self):
        project_name = self.project_name_entry.get().strip()
        language = self.language_entry.get().strip()
        other_options = self.other_options_entry.get().strip()
        if not project_name or not language:
            tk.messagebox.showerror("Error", "Project name and language cannot be empty.")
            self.result = None
        else:
            self.result = (project_name, language, other_options)

    def cancel(self, event=None):
        self.result = None
        super().cancel(event)

    def ok(self, event=None):
        self.apply()
        if self.result is not None:
            self.cancel()

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
