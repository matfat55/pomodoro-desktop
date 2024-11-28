import tkinter as tk
from tkinter import messagebox
import time

class PomodoroTimer:
    def position_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = 300
        window_height = 200
        x = screen_width - window_width
        y = screen_height - window_height
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.work_time = 25 * 60  # 25 minutes
        self.break_time = 5 * 60  # 5 minutes
        self.timer_running = False
        self.current_time = self.work_time

        self.time_label = tk.Label(root, text=self.format_time(self.current_time), font=("Helvetica", 48))
        self.time_label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_timer)
        self.stop_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer)
        self.reset_button.pack(pady=5)

        # Task management
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.task_frame, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_task_button = tk.Button(self.task_frame, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.LEFT, padx=5)

        self.task_listbox = tk.Listbox(root, width=40, height=10)
        self.task_listbox.pack(pady=10)

        self.task_var = tk.IntVar()
        self.task_checkbox = tk.Checkbutton(root, text="Mark as Completed", variable=self.task_var, command=self.mark_task_completed)
        self.task_checkbox.pack(pady=5)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02}:{seconds:02}"

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.run_timer()

    def stop_timer(self):
        self.timer_running = False

    def reset_timer(self):
        self.timer_running = False
        self.current_time = self.work_time
        self.time_label.config(text=self.format_time(self.current_time))
        self.task_listbox.delete(0, tk.END)
        self.task_var.set(0)
        self.task_entry.delete(0, tk.END)
        self.task_entry.delete(0, tk.END)

    def run_timer(self):
        if self.timer_running and self.current_time > 0:
            self.current_time -= 1
            self.time_label.config(text=self.format_time(self.current_time))
            self.root.after(1000, self.run_timer)
        elif self.timer_running and self.current_time == 0:
            messagebox.showinfo("Time's up!", "Break time!")
            self.current_time = self.break_time
            self.time_label.config(text=self.format_time(self.current_time))
            self.run_timer()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)

    def mark_task_completed(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"[✓] {task}")
        except IndexError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()

pomodoro_timer.py
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")
        self.root.attributes('-topmost', True)
        self.position_window()
        self.root.title("Pomodoro Timer")
        self.root.geometry("300x200")
        self.root.attributes('-topmost', True)
