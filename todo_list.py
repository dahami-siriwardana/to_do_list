tasks=["hello","hi","hola"] #This is an empty list like a database

def show_menu():
    print("\n📝To-Do List Menu")
    print("1. Add Task")       # Option to add a new task
    print("2. View Tasks")     # Option to view all saved tasks
    print("3. Delete Task")    # Option to delete a specific task
    print("4. Exit\n")   



def addTask():
    task=input("enter task please: ")
    tasks.append(task)
    print("✅ Added: "+ task)

def view_Task():
    if len(tasks) == 0:
        print("There are no upcoming tasks")
    else:
        for i in range(len(tasks)):
            print(str(i + 1) + " - " + tasks[i])

def delete_task():
    view_Task()
    try:
        task_num=int(input("enter the task number"))
        if 1 <= task_num <= len(tasks):
            removed=tasks.pop(task_num-1)
        else:
            print("invalid number.")
    except ValueError:
        print (" please enter a valid number")
        









