
# initialize empty todos to store todo items 
todos = []

while True:
    print("\nTODO List Manager:")
    print("1. Add Task")
    print("2. Mark as completed")
    print("3. View Tasks")
    print("4. Remove Task")
    print("5. Exit\n")

    choice = input("Enter your choice (1-5):")

    if choice == '1':
        task_name = input("Enter the task name:")
        task = {
            'task_name' : task_name,
            'is_completed': False,
        }
        todos.append(task)
        print("Task Added Successfully")

    elif choice == "2":
        task_index =  int(input("Enter task index:"))

    elif choice == "3":
        if len(todos > 0):
            for index, task in enumerate(todos):
                print(f"{index}. {task['task_name']} - {'Completed' if task['is_completed'] else 'Not Completed'}")
        else:
            print("You haven't added any task yet.")

    elif choice == "4":
        task_index = int(input("Enter task index to remove:"))
        if len(todos) < task_index:
            print("Invalid index given")
        else:
            todos.pop(task_index)
            print("Item removed successfully.")
    
    elif choice == '5':
        print("Program Exit")
        break



# todos = [
#  {
#      'task_name' : 'Test task',
#      'is_completed': True,
#  },
#  {
#      'task_name' : 'Test task',
#      'is_completed': True,
#  },
# ]