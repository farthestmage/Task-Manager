from datetime import datetime

class Task:

    def __init__(self,task_name,description="Add Description",status="todo",createdAt=datetime.now(),updatedAt=datetime.now()):
        self.task_name = task_name
        self.description = description
        self.status = status
        self.createdAt=str(createdAt)
        self.updatedAt= str(updatedAt)

    def __str__(self):
       return f" {self.task_name} {self.status} \n   {self.description}"
    
    def mark_in_prog(self):
        self.status= "in-progress"
    def makr_done(self):
        self.status = "done"

    
    