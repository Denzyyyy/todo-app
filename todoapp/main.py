import tkinter as tk
from tkinter import messagebox
from datetime import datetime

TODO_FILE = "todo.txt"

# Define the GUI window
window = tk.Tk()
window.title("To-Do List")

# Define the label and text box for user input
label = tk.Label(window, text="Add a to-do item:")
label.pack()
user_input = tk.Entry(window, width=50)
user_input.pack()

# Define the listbox to display the to-do list
listbox = tk.Listbox(window, width=50)
listbox.pack()


# Define the function to add a to-do item to the list
def add_todo():
    # Get the user input
    todo_item = user_input.get()

    # Make sure the user entered something
    if not todo_item:
        messagebox.showwarning("Warning", "Please enter a to-do item.")
        return

    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Add the to-do item to the listbox
    listbox.insert(tk.END, f"{current_time} - {todo_item}")

    # Write the to-do item to the file
    with open(TODO_FILE, "a") as f:
        f.write(f"{current_time} - {todo_item}\n")

    # Clear the user input
    user_input.delete(0, tk.END)

    # Define the function to edit a to-do item


def edit_todo():
    # Get the index of the selected item
    index = listbox.curselection()

    # Make sure the user selected an item
    if not index:
        messagebox.showwarning("Warning", "Please select a to-do item.")
        return

    # Get the selected item
    selected_item = listbox.get(index)

    # Show a dialog to edit the item
    edited_item = tk.simpledialog.askstring("Edit To-Do Item", "Enter the edited to-do item:",
                                            initialvalue=selected_item)

    # Make sure the user entered something
    if not edited_item:
        messagebox.showwarning("Warning", "Please enter a to-do item.")
        return

    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Update the item in the listbox
    listbox.delete(index)
    listbox.insert(index, f"{current_time} - {edited_item}")

    # Update the item in the file
    with open(TODO_FILE, "r") as f:
        lines = f.readlines()
    with open(TODO_FILE, "w") as f:
        for i, line in enumerate(lines):
            if i == index:
                f.write(f"{current_time} - {edited_item}\n")
            else:
                f.write(line)


def select_todo():
    # Get the index of the selected item
    index = listbox.curselection()

    # Make sure the user selected an item
    if not index:
        messagebox.showwarning("Warning", "Please select a to-do item.")
        return

    # Get the selected item
    selected_item = listbox.get(index)

    # Show a dialog to confirm selection
    messagebox.showinfo("Selected To-Do Item", f"You selected:\n{selected_item}")


# Define the buttons for the GUI
add_button = tk.Button(window, text="Add To-Do", command=add_todo)
