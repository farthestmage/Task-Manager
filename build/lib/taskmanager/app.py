import typer
from typing_extensions import Annotated
from .model import Task,datetime
from .data import read,write
from .errors import TaskNotFoundError



app = typer.Typer()



def read_json_data():
    task_dict=read()
    return (task_dict)

def write_json_data(new_task : Task,task_dict:dict={}):
    task_dict[len(task_dict.keys())]={"task_name":new_task.task_name,
                                      "description":new_task.description,
                                      "status":new_task.status,
                                      "createdAt":new_task.createdAt,
                                      "updatedAt":new_task.updatedAt}
    write(data=task_dict)
    task_dict= read_json_data()


def update_json_data(id:int ,task: Task,task_dict):
    task_dict[id-1]={"task_name":task.task_name,
                "description":task.description,
                "status":task.status,
                "createdAt":task.createdAt,
                "updatedAt":str(datetime.now())}
    write(data=task_dict)
    task_dict= read_json_data()

task_dict = read_json_data()


@app.command()
def add(task_name: str):
    task_dup = False
    task_add = Task(task_name)
    for task in task_dict.values():
        if task_add.task_name == task["task_name"]:
            print("Already in the Task List")
            task_dup = True
            break
    if not task_dup:
        print(f"Added {task_name} Task_ID: {len(task_dict.keys())+1}")
        write_json_data(task_add,task_dict if len(task_dict)>0 else {})

@app.command()
def update(id:int,task_name:str):
   try: 
        for id_task,task in task_dict.items():
            if ((id-1) ==int(id_task)):
                
                temp_t=Task(**task)
                temp_t.task_name = task_name
                #temp_t.updatedAt =str(datetime.now())
                
                update_json_data(id,temp_t,task_dict)
                print("UPDATED")
                return
        raise TaskNotFoundError("Task ID not Found")
                
   except TaskNotFoundError as e:
       print(e)

@app.command("mark-in-progress")
def mark_in_progress(id: int):
    try: 
        for id_task,task in task_dict.items():
            if ((id-1)) == int(id_task):
                temp_t = Task(**task)
                temp_t.mark_in_prog()
                update_json_data(id,temp_t,task_dict)
                print("Marked In progress")
                return
            
        raise TaskNotFoundError("Task ID Not found")
    except TaskNotFoundError as e:
        print(e)
    
@app.command("mark-done")
def mark_done(id: int):
    try: 
        for id_task,task in task_dict.items():
            if ((id-1)) == int(id_task):
                temp_t = Task(**task)
                temp_t.makr_done()
                update_json_data(id,temp_t,task_dict)
                print("Marked Done")
                return
            
        raise TaskNotFoundError("Task ID Not found")
    except TaskNotFoundError as e:
        print(e)


@app.command()
def list(optional: Annotated[str, typer.Argument()] = None):
    if len(task_dict)==0:
        print("NO TASK")
    if optional == None:
        for id,task in task_dict.items():
            temp_t = Task(**task)
            if temp_t.status == "done":
                continue
            else:
                print(f"{int(id)+1} {temp_t}")
    if optional == "done":
         for id,task in task_dict.items():
            temp_t = Task(**task)
            if temp_t.status == "done":
                print(f"{int(id)+1} {temp_t}")
            
    if optional == "in-progress":
        for id,task in task_dict.items():
            temp_t = Task(**task)
            if temp_t.status == "in-progress":
                print(f"{int(id)+1} {temp_t}")
    if optional =="todo":
        for id,task in task_dict.items():
            temp_t = Task(**task)
            if temp_t.status == "todo":
                print(f"{int(id)+1} {temp_t}")

         

      


if __name__ == "__main__":
    app()