import tkinter as tk
from tkinter import messagebox

class ToDoChatbot:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        return f"Added: '{task}'"

    def show_tasks(self):
        if not self.tasks:
            return "Your to-do list is empty!"
        result = ""
        for i, t in enumerate(self.tasks, 1):
            status = "✅" if t["done"] else "❌"
            result += f"{i}. {t['task']} [{status}]\n"
        return result

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            return f"Marked '{self.tasks[index]['task']}' as done ✅"
        return "Invalid task number!"


# ---------------- GUI Module ----------------
class ToDoGUI:
    def __init__(self, root, bot):
        self.bot = bot
        self.root = root
        self.root.title("To-Do List Chatbot")

        # Entry for new task
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        # Add Task Button
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        # Show Tasks Button
        self.show_button = tk.Button(root, text="Show Tasks", command=self.show_tasks)
        self.show_button.pack()

        # Mark Done Section
        self.done_entry = tk.Entry(root, width=10)
        self.done_entry.pack(pady=5)
        self.done_button = tk.Button(root, text="Mark Done", command=self.mark_done)
        self.done_button.pack()

        # Output Area
        self.output = tk.Text(root, height=15, width=50)
        self.output.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            msg = self.bot.add_task(task)
            messagebox.showinfo("Task Added", msg)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def show_tasks(self):
        tasks_text = self.bot.show_tasks()
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, tasks_text)

    def mark_done(self):
        try:
            index = int(self.done_entry.get()) - 1
            msg = self.bot.mark_done(index)
            messagebox.showinfo("Task Update", msg)
            self.done_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid task number!")


if __name__ == "__main__":
    bot = ToDoChatbot()
    root = tk.Tk()
    gui = ToDoGUI(root, bot)
    root.mainloop()