from password_manager import PasswordManager


manager = PasswordManager()

while True:
    print("\n===== PASSWORD MANAGER =====")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        website = input("Website: ").strip()
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        manager.add_password(
            website,
            username,
            password
        )

        print("Password saved successfully.")

    elif choice == "2":
        website = input("Website: ").strip()
        result = manager.get_password(website)

        if result:
            print(f"Username: {result['username']}")
            print(f"Password: {result['password']}")
        else:
            print("No password found.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")