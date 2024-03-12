from task_manager import Task, TaskManager

class TaskManagerApp:
    def __init__(self):
        self.task_manager = TaskManager()

    def display_menu(self):
        print("\nTask Manager Menu:")
        print("1. Create Task")
        print("2. Read Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_task()
            elif choice == "2":
                self.read_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                print("Exiting Task Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_task(self):
        task_id = int(input("Enter Task ID: "))
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        self.task_manager.create_task(task_id, title, description)

    def read_tasks(self):
        self.task_manager.read_tasks()

    def update_task(self):
        task_id = int(input("Enter Task ID to update: "))
        title = input("Enter New Title: ")
        description = input("Enter New Description: ")
        self.task_manager.update_task(task_id, title, description)

    def delete_task(self):
        task_id = int(input("Enter Task ID to delete: "))
        self.task_manager.delete_task(task_id)

if __name__ == "__main__":
    app = TaskManagerApp()
    app.run()
