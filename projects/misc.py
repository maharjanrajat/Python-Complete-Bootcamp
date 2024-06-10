tasks = [
    {
        'task_name': 'test task 1',
        'is_completed': False
    },
    {
        'task_name': 'test task 2',
        'is_completed': False
    },
]

index = int(input("Enter task index:"))


todo_item = tasks[index]
todo_item['is_completed'] = True


for i, task in enumerate(tasks):
    print(f"{i}. {task['task_name']} - {'Completed ✅' if task['is_completed'] else 'Not Completed ❌'}") 

