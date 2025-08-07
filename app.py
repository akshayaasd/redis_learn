import redis

# Redis connection
r = redis.Redis(host='localhost', port=6379, db=0)

def register_user():
    email = input("Enter email: ")
    if r.exists(f"user:{email}"):
        print("User already exists!")
        return
    name = input("Enter name: ")
    password = input("Enter password: ")
    r.hset(f"user:{email}", mapping={"name": name, "email": email, "password": password})
    print("User registered successfully!")

def login_user():
    email = input("Enter email: ")
    password = input("Enter password: ")
    if not r.exists(f"user:{email}"):
        print("User does not exist.")
        return
    stored_pass = r.hget(f"user:{email}", "password")
    if stored_pass.decode() == password:
        print("Login successful!")
    else:
        print("Incorrect password.")

def view_profile():
    email = input("Enter email: ")
    if not r.exists(f"user:{email}"):
        print("User not found.")
        return
    profile = r.hgetall(f"user:{email}")
    print("User Profile:")
    for k, v in profile.items():
        print(f"{k.decode()}: {v.decode()}")

def main():
    while True:
        print("\n=== USER SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. View Profile")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            view_profile()
        elif choice == '4':
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()
