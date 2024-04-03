cycles = []

def register_cycle():
    name = input("Enter your name: ")
    
    while True:
        reg_number = input("Enter your registration number (9 digits): ")
        if len(reg_number) != 9 or not reg_number.isdigit():
            print("Please enter a valid 9-digit registration number.")
        else:
            break
            
    cycle_choice = input("Choose a cycle (Cycle 1 to 10): ")
    phone_number = input("Enter your mobile phone number: ")

    cycle_info = {
        "Name": name,
        "Registration Number": reg_number,
        "Cycle": f"Cycle {cycle_choice}",
        "Phone Number": phone_number,
        "Submitted": False
    }

    cycles.append(cycle_info)
    print("Cycle registered successfully!")

def submit_cycle():
    reg_number = input("Enter your registration number (9 digits): ")
    for cycle in cycles:
        if cycle["Registration Number"] == reg_number:
            cycle["Submitted"] = True
            print("Cycle submitted successfully!")
            return
    print("Cycle not found with the given registration number.")

def main():
    while True:
        print("\n===== Cycle Registration System =====")
        print("1. Register a new cycle")
        print("2. Submit a cycle")
        print("3. View all registered cycles")
        print("4. View unsubmitted cycles")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_cycle()
        elif choice == "2":
            submit_cycle()
        elif choice == "3":
            print("\n===== Registered Cycles =====")
            for i, cycle in enumerate(cycles, 1):
                print(f"Cycle {i}:")
                for key, value in cycle.items():
                    print(f"{key}: {value}")
                print()
        elif choice == "4":
            unsubmitted_cycles = [cycle for cycle in cycles if not cycle["Submitted"]]
            if unsubmitted_cycles:
                print("\n===== Unsubmitted Cycles =====")
                for i, cycle in enumerate(unsubmitted_cycles, 1):
                    print(f"Cycle {i}:")
                    for key, value in cycle.items():
                        print(f"{key}: {value}")
                    print()
            else:
                print("All cycles have been submitted.")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
