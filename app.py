import typer
from model import Task
from data import read,write




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
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")
@app.command()
def list():
    if len(task_dict)==0:
        print("NO TASK")
    for id,task in task_dict.items():
        temp_t = Task(**task)
        print(f"{int(id)+1} {temp_t}")



if __name__ == "__main__":
    app()