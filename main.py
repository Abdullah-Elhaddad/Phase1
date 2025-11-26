from utilities import temp_converter, calculator, text_stats, unit_converter, password_generator, todo_list

def main():
    while True:
        print("\n=== Phase 1 Utility App ===")
        print("1. Temperature converter")
        print("2. Calculator")
        print("3. Text statistics")
        print("4. Unit converter")
        print("5. Password generator")
        print("6. To-do list")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            temp_converter.run()
        elif choice == "2":
            calculator.run()
        elif choice == "3":
            text_stats.run()
        elif choice == "4":
            unit_converter.run()
        elif choice == "5":
            password_generator.run()
        elif choice == "6":
            todo_list.run()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
