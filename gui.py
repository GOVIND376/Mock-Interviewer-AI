"""
gui.py

Simple Tkinter GUI wrapper around InterviewBot.
"""

import tkinter as tk
from interview import InterviewBot


def start_interview():
    career = career_var.get().strip()
    level = level_var.get().strip()

    if not career:
        result_label.config(text="Please enter a career/domain.")
        return

    if not level:
        result_label.config(text="Please enter a difficulty level.")
        return

    bot = InterviewBot(career, level)
    k, c, f = bot.start()

    result_label.config(
        text=f"Knowledge: {k:.1f} | Confidence: {c:.1f} | Final: {f:.1f} / 100"
    )


root = tk.Tk()
root.title("AI Interview Bot")

tk.Label(root, text="Career / Domain").pack(pady=(10, 0))
career_var = tk.StringVar()
tk.Entry(root, textvariable=career_var, width=40).pack()

tk.Label(root, text="Level (Fresher / Intermediate / Professional)").pack(pady=(10, 0))
level_var = tk.StringVar()
tk.Entry(root, textvariable=level_var, width=40).pack()

tk.Button(root, text="Start Interview", command=start_interview).pack(pady=15)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=(0, 10))

if __name__ == "_main_":
    root.mainloop()