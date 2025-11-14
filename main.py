from log_hash import register_user, login_user

def menu():
    print('*'* 30)
    print('*** Welcome to my system ***')
    print('choose from the following options: ')
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    print('*'* 30) 

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == '1':
            register_user()
            print("User registered successfully!")
        elif choice == '2':
            if login_user():
                print("Login successful!")
            else:
                print("Login failed! Invalid username or password.")
        elif choice == '3':
            print("Goodbye!")
            break
        

if __name__ == "__main__":
    main()

