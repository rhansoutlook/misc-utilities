#!/usr/bin/env python3
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
import os

def hibernate():
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show confirmation dialog
    result = messagebox.askyesno("Hibernate System", "Do you want to hibernate the system?")

    if result:  # User clicked Yes
        try:
            # Use pkexec only for the actual hibernate command
            subprocess.run(['pkexec', 'systemctl', 'hibernate'], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("Error", f"Could not hibernate: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {e}")

    root.destroy()

if __name__ == "__main__":
    hibernate()
