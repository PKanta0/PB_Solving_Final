from task import Task

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