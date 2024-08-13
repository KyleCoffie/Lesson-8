#User Interface (UI):
#Create a command-line interface (CLI) for the To-Do List Application.
#Display a welcoming message and a menu with the following options: 

tasks = []
# [
    # {'Task': 'hello', 'completed': False}, OBJECT 1 
    # {'Task': 'value', 'completed': Boolean} OBJECT 2
# ]

def add_tasks():
            task = input("Please enter a task: ")
            tasks.append({"Task" :task, "completed" : False})
            print(f"Task '{task}' added to the list.")
            print(tasks)
        
        
def list_task():
    if not tasks:
        print("There are no task in you list")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
                    status = "Completed" if task["completed"] else "Not Completed"
                    print(f"Task #{index +1}. {task['Task']} + {status}")

        
def complete_task():
    complete_task = int(input("Enter the task # to mark as completed")) + 1
    if 0 <= complete_task < len(tasks):
        tasks[complete_task]["completed"] = True
        print ("Task marked completed!")
    else:
        print("Invalid task #")

        
            
def delete_task():
    list_task()
    try:
        tasktodelete = int(input("Enter the # to delete: " ))
        if tasktodelete >=0 and tasktodelete < len(tasks):
            tasks.pop(tasktodelete)
            print(f"Task #{tasktodelete} has been removed.")
        else:
            print(f"Task #{tasktodelete} was not found.")
    except:
        print("Invalid input")    
                
if __name__ == "__main__":
    
#To-Do List Features:
    while True:
        print("====== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice ")
    #Implement the following features for the To-Do List:
        if choice == "1":
            add_tasks()
        elif choice == "2":
            list_task()
        elif choice == "3":
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Thank you for using this To-Do program")
            break
            
            
        
        
        else:
            print("please choose a valid number") 

        

    
    
    
    #Adding a task with a title (by default “Incomplete”).
        
        