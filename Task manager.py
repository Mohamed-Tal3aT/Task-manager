# 1.add tasks to list
# 2.mark task as complete 
# 3.view tasks
# 4.quit

message ="""
1.add tasks to list
2.mark task as complete 
3.view tasks
4.quit
"""
tasks=[]
def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task, "completed": False})
    print(f'Task "{task}" added.')



def mark_task_complete():
    view_tasks()
    all_completed = True
    for task in tasks:
        if not task["completed"]:
            all_completed = False
            break
    if tasks and all_completed:
        print("All tasks are already completed.")
        return
    task_num = int(input("Enter the task number to mark as complete: ")) 
    if 0 < task_num <= len(tasks):
        tasks[task_num - 1]["completed"] = True
        print(f'Task "{tasks[task_num - 1]["task"]}" marked as complete.')
    else:
        print("Invalid task number.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. [{status}] {task['task']}")


while True:
    print(message)
    choice = input("Enter your choice: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        mark_task_complete()
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")

