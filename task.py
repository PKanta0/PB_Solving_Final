class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def toggle(self):
        self.completed = not self.completed