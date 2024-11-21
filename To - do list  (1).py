import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        # List to store tasks
        self.tasks = []

        # GUI elements
        self.task_entry = tk.Entry(root, width=30, font=('Arial', 14))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        # Add task button
        self.add_button = tk.Button(root, text="Add Task", font=('Arial', 14), command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(root, width=50, height=10, font=('Arial', 14))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Mark as completed button
        self.complete_button = tk.Button(root, text="Mark as Completed", font=('Arial', 14), command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, padx=10, pady=10)

        # Delete task button
        self.delete_button = tk.Button(root, text="Delete Task", font=('Arial', 14), command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

    def add_task(self):
        """Add a new task to the list."""
        task = self.task_entry.get()
        if task:
            self.tasks.append({'task': task, 'completed': False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def update_task_listbox(self):
        """Update the listbox with current tasks."""
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks):
            status = "✓" if task['completed'] else "✗"
            self.task_listbox.insert(tk.END, f"{index + 1}. [{status}] {task['task']}")

    def mark_completed(self):
        """Mark the selected task as completed."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks[selected_task_index]['completed'] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        """Delete the selected task from the list."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            removed_task = self.tasks.pop(selected_task_index)
            self.update_task_listbox()
            messagebox.showinfo("Task Deleted", f"Deleted task: '{removed_task['task']}'")
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Initialize Tkinter window
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()
