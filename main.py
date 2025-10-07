from task import Task

tasks= []

def add_task():
    description = input("activity name ").strip()
    due_date = input("When the activity will expire? (or empty)").strip()
    
    if not description:
        print("❌ please enter a activity name")
        return
    
    task = Task(description, due_date if due_date else None)
    tasks.append(task)
    print("✅ success!")

def view_tasks():
    if not tasks:
        print("📭 No activity here")
        return
    
    print("\n name of activity:")
    print("----------------------------")
    for i, t in enumerate(tasks, start=1):
        status = "✅ Done" if t.completed else "⏳ Not yet"
        due = t.due_date if t.due_date else "-"
        print(f"{i}. {t.description} (date expire: {due}) - {status}")

def show_menu():
    print("\n=== To-Do List Manager ===")
    print("1) Add task")
    print("2) View tasks")
    print("9) Quit")

def handle_choice(choice: str) -> bool:
    if choice == "1":
        print("(TODO) add_task()")
    elif choice == "2":
        print("(TODO) view_tasks()")
    elif choice == "9":
        print("Bye!")
        return False
    else:
        print("Invalid choice. Please choose 1, 2 or 9.")
    return True

def main():
    running = True
    while running:
        show_menu()
        choice = input("Select an option: ").strip()
        running = handle_choice(choice)

if __name__ == "__main__":
    main()