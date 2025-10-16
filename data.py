import json
#from app import Task

def read():
    try:
        with open("task.json","r") as f:
            data=json.load(f)
            return data
    except:
        return {}
def write(data:dict):
    with open("task.json","w") as f:
        f.write(json.dumps(data))
        
'''
Expected ->
    { 1: { .. task...
            }
      2: {...task...}
    
    }
'''
