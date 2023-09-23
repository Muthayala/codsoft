tasks = []

def display_tasks():
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. Description: {task['description']}, Status: {'Completed' if task['completed'] else 'Not Completed'}")

def add_task(description):
    task = {'description': description, 'completed': False}
    tasks.append(task)
    print("Task added successfully.")

def update_task(task_num, new_description):
    try:
        task_num = int(task_num)
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['description'] = new_description
            print("Task updated successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def track_task(task_num):
    try:
        task_num = int(task_num)
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    while True:
        print("\n To-Do List")
        print("1. Display Tasks")
        print("2. Add a Task")
        print("3. Update a Task")
        print("4. Track a Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_tasks()
        elif choice == "2":
            description = input("Enter the task description: ")
            add_task(description)
        elif choice == "3":
            task_num = input("Enter the task number to update: ")
            new_description = input("Enter the new task description: ")
            update_task(task_num, new_description)
        elif choice == "4":
            task_num = input("Enter the task number to track: ")
            track_task(task_num)
        elif choice == "5":
            print("Exit")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
