#TO DO LIST

![](I1.png)

This is a simple To-Do List application built using Tkinter in Python. The application provides a graphical user interface (GUI) to manage tasks. Users can add, mark as completed, and delete tasks from their to-do list. The list is displayed in a Listbox, and each task shows a checkmark (✓) or cross (✗) based on whether it's completed.

Class: TodoListApp
The application is encapsulated in the TodoListApp class, which handles all the functionality and UI elements. Here’s a breakdown of its components:

Constructor (__init__):
The constructor is responsible for setting up the user interface and initializing the application state. It includes:

Task list (self.tasks): A list to store the tasks with their completion status.
Entry widget (self.task_entry): A text field where the user can enter a new task.
Buttons:
"Add Task" (self.add_button): Adds a new task to the list.
"Mark as Completed" (self.complete_button): Marks the selected task as completed.
"Delete Task" (self.delete_button): Deletes the selected task.
Listbox (self.task_listbox): A listbox to display tasks with their status ("✓" for completed, "✗" for incomplete).
Main Functions:
add_task:

Purpose: Adds a new task to the self.tasks list if the user has entered something in the input field.
How it works:
Retrieves the task from the entry widget (self.task_entry).
Appends it to the self.tasks list with the status set as False (incomplete).
Refreshes the task list in the listbox.
Clears the input field after adding the task.
update_task_listbox:

Purpose: Updates the Listbox to reflect the current state of tasks.
How it works:
Clears the current tasks in the listbox.
Loops through self.tasks and displays each task, showing "✓" if the task is marked as completed or "✗" if it's not.
mark_completed:

Purpose: Marks a selected task as completed.
How it works:
Retrieves the selected task index from the listbox.
Updates the task's status to True (completed).
Refreshes the listbox to reflect the changes.
Shows a warning if no task is selected.
delete_task:

Purpose: Deletes a selected task from the list.
How it works:
Retrieves the selected task index from the listbox.
Removes the task from self.tasks.
Refreshes the listbox and displays a message confirming the task deletion.
Shows a warning if no task is selected.
Error Handling:
Marking a task as completed or deleting a task: If the user does not select any task, a warning message appears using messagebox.showwarning.
Empty task entry: If the user tries to add an empty task, a warning is displayed.
GUI Layout:
Task Entry: A text field at the top where the user enters a task.
Add Task Button: A button next to the text field to add the task to the list.
Task Listbox: Displays all tasks, with their completion status ("✓" or "✗").
Mark as Completed Button: A button to mark a selected task as completed.
Delete Task Button: A button to delete a selected task.