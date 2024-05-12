def display_menu():
  print("\nTo-Do List App")
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Mark Task Complete")
  print("4. Exit")


def add_task():
  task = input("Enter task: ")
  tasks.append(task)
  print("Task added successfully!")


def view_tasks():
  if not tasks:
    print("No tasks added yet!")
    return
  print("\nYour Tasks:")
  for i, task in enumerate(task):
    print(f"{i+1}. {task}")


def mark_complete():
  if not tasks:
    print("No tasks to mark complete!")
    return
  view_tasks()
  index = int(input("Enter the number of the task to mark complete: ")) - 1
  if index < 0 or index >= len(tasks):
    print("Invalid task number!")
    return
  del tasks[index]
  print("Task marked complete!")


while True:
  display_menu()
  choice = input("Enter your choice: ")
  if choice == '1':
    add_task()
  elif choice == '2':
    view_tasks()
  elif choice == '3':
    mark_complete()
  elif choice == '4':
    break
  else:
    print("Invalid choice!")

print("Exiting the application...")
