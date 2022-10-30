from task import Task


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        task_name.completed = True
        return f"Completed task {task_name}"

    def clean_section(self):
        old_amount = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.completed == False]
        return f"Cleared {old_amount - len(self.tasks)} tasks."

    def view_section(self):
        details = '\n'.join(x.details() for x in self.tasks)
        return f"Section {self.name}:\n{details}"