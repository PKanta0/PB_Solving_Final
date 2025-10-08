import json, os
from task import Task
from datetime import datetime

FILENAME = "data/tasks.json"

def load_tasks():
    if not os.path.exists(FILENAME) or os.path.getsize(FILENAME) == 0:
        return []
    with open(FILENAME, "r", encoding="utf-8") as f:
        data = json.load(f) 
    tasks = [Task(d.get("description", ""), d.get("due_date")) for d in data]
    for t, d in zip(tasks, data):
        if d.get("completed"):
            t.mark_complete()
    return tasks

def save_tasks(tasks):
    serializable = [
        {"description": t.description, "due_date": t.due_date, "completed": t.completed}
        for t in tasks
    ]
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(serializable, f, indent=4, ensure_ascii=False)

tasks = load_tasks()

def add_task():
    description = input("Enter task description ").strip()
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank:").strip()
    
    if not description:
        print("❌ Please enter a description.")
        return
    
    task = Task(description, due_date if due_date else None)
    tasks.append(task)
    save_tasks(tasks) 
    print("✅ Task added successfully!!")

def view_tasks():
    if not tasks:
        print("📭 No tasks here")
        return
    
    print("\nAll Tasks:")
    print("----------------------------")
    for i, t in enumerate(tasks, start=1):
        status = "✅ Done" if t.completed else "⏳ Pending"
        due = t.due_date if t.due_date else "-"
        print(f"{i}. {t.description} (Due: {due}) - {status}")

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
    save_tasks(tasks) 

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
    save_tasks(tasks)

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
    save_tasks(tasks)

def show_summary():
    total = len(tasks)
    done = sum(1 for t in tasks if t.completed)
    pending = total - done

    today_str = datetime.now().strftime("%Y-%m-%d")

    def is_overdue(t):
        if not t.due_date or t.completed:
            return False
        try:
            return datetime.strptime(t.due_date, "%Y-%m-%d") < datetime.strptime(today_str, "%Y-%m-%d")
        except ValueError:
            # invalid date format -> treat as not overdue
            return False

    overdue = sum(1 for t in tasks if is_overdue(t))
    due_today = sum(1 for t in tasks if (t.due_date == today_str and not t.completed))

    print("\n--- Summary ---")
    print(f"Total:     {total}")
    print(f"Done:      {done}")
    print(f"Pending:   {pending}")
    print(f"Overdue:   {overdue}")
    print(f"Due today: {due_today}")


def sort_and_filter_tasks():
    if not tasks:
        print("📭 No tasks to sort or filter.")
        return

    print("\n--- Sort & Filter ---")
    print("1) Sort by due date (oldest first)")
    print("2) Sort by status (Pending first)")
    print("3) Show only Pending tasks")
    print("4) Show only Completed tasks")
    print("9) Back")

    choice = input("Select option: ").strip()

    if choice == "1":
        sorted_tasks = sorted(
            tasks,
            key=lambda t: t.due_date if t.due_date else "9999-99-99"
        )
        print("\nSorted by due date:")
        for i, t in enumerate(sorted_tasks, start=1):
            status = "✅ Done" if t.completed else "⏳ Pending"
            due = t.due_date if t.due_date else "-"
            print(f"{i}. {t.description} (Due: {due}) - {status}")

    elif choice == "2":
        sorted_tasks = sorted(tasks, key=lambda t: t.completed)
        print("\nSorted by status (Pending first):")
        for i, t in enumerate(sorted_tasks, start=1):
            status = "✅ Done" if t.completed else "⏳ Pending"
            due = t.due_date if t.due_date else "-"
            print(f"{i}. {t.description} (Due: {due}) - {status}")

    elif choice == "3":
        pending = [t for t in tasks if not t.completed]
        print("\nPending tasks:")
        for i, t in enumerate(pending, start=1):
            due = t.due_date if t.due_date else "-"
            print(f"{i}. {t.description} (Due: {due}) - ⏳ Pending")

    elif choice == "4":
        done = [t for t in tasks if t.completed]
        print("\nCompleted tasks:")
        for i, t in enumerate(done, start=1):
            due = t.due_date if t.due_date else "-"
            print(f"{i}. {t.description} (Due: {due}) - ✅ Done")

    elif choice == "9":
        return
    else:
        print("❌ Invalid option.")

def show_menu():
    print("\n=== To-Do List Manager ===")
    print("1) Add task")
    print("2) View tasks")
    print("3) Edit task")
    print("4) Delete task")
    print("5) Toggle task status")
    print("6) Summary")
    print("7) Sort / Filter tasks")
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
    elif choice == "6":
        show_summary()
    elif choice == "7":
        sort_and_filter_tasks()
    elif choice == "9":
        print("Bye!")
        return False
    else:
        print("Invalid choice. Please choose 1-6 or 9.")
    return True

def main():
    running = True
    while running:
        show_menu()
        choice = input("Select an option: ").strip()
        running = handle_choice(choice)

if __name__ == "__main__":
    main()