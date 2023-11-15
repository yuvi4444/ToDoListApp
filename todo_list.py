class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """
        Add a task to the to-do list.
        """
        self.tasks.append(task)

    def remove_task(self, task):
        """
        Remove a task from the to-do list.
        """
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not found in the to-do list.")

    def display_tasks(self):
        """
        Display all tasks in the to-do list.
        """
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print(f"- {task}")
        else:
            print("No tasks found in the to-do list.")


def main():
    todo_list = TodoList()

    while True:
        print("\n--- To-Do List Application ---")
        print("1. Add a Task")
        print("2. Remove a Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added to the to-do list.")
        elif choice == "2":
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
