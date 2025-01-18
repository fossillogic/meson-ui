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
import os
import subprocess
import tkinter.messagebox


class SubprojectsDialog(simpledialog.Dialog):
    def __init__(self, parent, theme):
        self.theme = theme
        super().__init__(parent)

    def body(self, master):
        self.title("Meson Subprojects")
        self.apply_theme()
        ttk.Label(
            master,
            text="Manage Meson Subprojects",
            font=("Helvetica", 10, "bold"),
        ).grid(row=0, column=0, columnspan=2, pady=10)
        self.geometry("660x400")

        self.notebook = ttk.Notebook(master)
        self.notebook.grid(row=2, column=0, columnspan=3, pady=10)

        self.create_tabs()

        self.update_button = ttk.Button(
            master, text="Update", command=self.update_subprojects, style="Blue.TButton"
        )
        self.download_button = ttk.Button(
            master, text="Download", command=self.download_subprojects, style="Blue.TButton"
        )
        self.purge_button = ttk.Button(
            master, text="Purge", command=self.purge_subprojects, style="Blue.TButton"
        )

        self.update_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W + tk.E)
        self.download_button.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W + tk.E)
        self.purge_button.grid(row=1, column=2, padx=10, pady=10, sticky=tk.W + tk.E)

    def create_tabs(self):
        frame = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(frame, text="Subprojects")
        self.subprojects_text = ScrolledText(
            frame,
            wrap=tk.WORD,
            height=20,
            width=80,
        )
        self.subprojects_text.pack(expand=True, fill=tk.BOTH)
        self.subprojects_text.insert(tk.END, self.fetch_subprojects())
        self.subprojects_text.configure(state=tk.DISABLED)

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

    def fetch_subprojects(self):
        try:
            subprojects_dir = os.path.join(os.getcwd(), "subprojects")
            if not os.path.exists(subprojects_dir):
                return "No subprojects directory found."
            subprojects = os.listdir(subprojects_dir)
            if not subprojects:
                return "No subprojects found."
            return "\n".join(subprojects)
        except Exception as e:
            return f"Error fetching subprojects: {str(e)}"

    def update_subprojects(self):
        self.run_subprojects_command("update")

    def download_subprojects(self):
        self.run_subprojects_command("download")

    def purge_subprojects(self):
        self.run_subprojects_command("purge")

    def run_subprojects_command(self, command):
        try:
            output = subprocess.run(
                ["meson", "subprojects", command],
                capture_output=True,
                text=True,
                check=True,
            )
            self.subprojects_text.configure(state=tk.NORMAL)
            self.subprojects_text.insert(tk.END, output.stdout)
            self.subprojects_text.configure(state=tk.DISABLED)
        except subprocess.CalledProcessError as e:
            tk.messagebox.showerror("Error", f"Command failed: {e.stderr}")
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))
