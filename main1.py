# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Task:
    def __init__(self, name, description, status="Incomplete"):
        self.name = name
        self.description = description
        self.status = status

class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, description):
        task = Task(name, description)
        self.tasks.append(task)
        print(f'Task "{name}" added to the to-do list.')

    def list_tasks(self):
        if not self.tasks:
            print('No tasks in the to-do list.')
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f'{index}. Name: {task.name}, Description: {task.description}, Status: {task.status}')

    def mark_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.status = "Complete"
            print(f'Task "{task.name}" marked as complete.')
        else:
            print('Invalid task index.')

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks.pop(task_index - 1)
            print(f'Task "{task.name}" deleted.')
        else:
            print('Invalid task index.')

    def clear_all_tasks(self):
        self.tasks = []
        print('All tasks cleared from the to-do list.')

# Example usage
if __name__ == "__main__":
    todo_manager = ToDoListManager()

    todo_manager.add_task("Task 1", "Description for Task 1")
    todo_manager.add_task("Task 2", "Description for Task 2")

    todo_manager.list_tasks()

    todo_manager.mark_complete(1)
    todo_manager.list_tasks()

    todo_manager.delete_task(2)
    todo_manager.list_tasks()

    todo_manager.clear_all_tasks()
    todo_manager.list_tasks()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
