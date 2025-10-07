def show_menu():
    print("\n=== To-Do List Manager ===")
    print("1) Add task")
    print("2) View tasks")
    print("9) Quit")

def main():
    while True:
        show_menu()
        choice = input("Select an option: ").strip()
        if choice == "9":
            print("Bye!")
            break
        elif choice in {"1","2"}:
            print("(feature coming soon)")
        else:
            print("Invalid choice. Please choose 1, 2 or 9.")

if __name__ == "__main__":
    main()