class Task:
    def __init__(self, task_id, title, description, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed

class TaskManager:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_id, title, description):
        task = Task(task_id, title, description)
        self.tasks.append(task)
        print("Task created successfully.")

    def read_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for task in self.tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"ID: {task.task_id}, Title: {task.title}, Description: {task.description}, Status: {status}")

    def update_task(self, task_id, title, description):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = title
                task.description = description
                print("Task updated successfully.")
                return
        print("Task not found.")

    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print("Task deleted successfully.")
                return
        print("Task not found.")
