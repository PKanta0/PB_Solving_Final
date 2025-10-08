import json, os
from task import Task

FILENAME = "tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

tasks = load_tasks()

def add_task():
    description = input("Enter task description ").strip()
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank:").strip()
    
    if not description:
        print("❌ Please enter a description.")
        return
    
    task = Task(description, due_date if due_date else None)
    tasks.append(task)
    print("✅ Task added successfully!!")

def view_tasks():
    if not tasks:
        print("📭 No tasks here")
        return
    
    print("\n All Tasks:")
    print("----------------------------")
    for i, t in enumerate(tasks, start=1):
        status = "✅ Done" if t.completed else "⏳ Pending"
        due = t.due_date if t.due_date else "-"
        print(f"{i}. {t.description} (date expire: {due}) - {status}")

def edit_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("\nEnter task number to edit: ")) - 1
        task = tasks[index]
    except (ValueError, IndexError):
        print("❌ Invalid task number.")
        return

    new_desc = input(f"New description (leave blank to keep) [{task.description}]: ").strip()
    if new_desc:
        task.description = new_desc

    new_due = input(f"New due date (leave blank to keep) [{task.due_date or '-'}]: ").strip()
    if new_due:
        task.due_date = new_due

    print("✏️ Task updated successfully!")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("\nEnter task number to delete: ")) - 1
        task = tasks[index]
    except (ValueError, IndexError):
        print("❌ Invalid task number.")
        return

    confirm = input(f"Type 'y' to confirm delete '{task.description}': ").strip().lower()
    if confirm == "y":
        del tasks[index]
        print("🗑️ Task deleted successfully!")
    else:
        print("↩️ Deletion cancelled.")

def toggle_task():
    view_tasks()
    if not tasks:
        return
    try:
        index = int(input("\nEnter task number to toggle: ")) - 1
        task = tasks[index]
    except (ValueError, IndexError):
        print("❌ Invalid task number.")
        return

    task.toggle()
    status = "✅ Done" if task.completed else "⏳ Pending"
    print(f"🔁 Task status changed: {status}")

def save_tasks():
    ensure_data_dir()
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(
            [
                {"description": t.description, "due_date": t.due_date, "completed": t.completed}
                for t in tasks
            ],
            f,
            indent=2,
            ensure_ascii=False
        )
    print(f"💾 Saved {len(tasks)} task(s) to {DATA_FILE}")

def show_menu():
    print("\n=== To-Do List Manager ===")
    print("1) Add task")
    print("2) View tasks")
    print("3) Edit task")
    print("4) Delete task")
    print("5) Toggle task status")
    print("9) Quit")

def handle_choice(choice: str) -> bool:
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        edit_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        toggle_task()
    elif choice == "9":
        print("Bye!")
        return False
    else:
        print("Invalid choice. Please choose 1-5 or 9.")
    return True

def main():
    running = True
    while running:
        show_menu()
        choice = input("Select an option: ").strip()
        running = handle_choice(choice)

if __name__ == "__main__":
    main()