import redis

# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Simple menu
def main():
    while True:
        print("\nChoose an option:")
        print("1. Set key-value")
        print("2. Get value")
        print("3. Delete key")
        print("4. Set user (HASH)")
        print("5. Get user field (HASH)")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            key = input("Enter key: ")
            value = input("Enter value: ")
            r.set(key, value)
            print(f"Set key '{key}' with value '{value}'")
        
        elif choice == '2':
            key = input("Enter key to get: ")
            value = r.get(key)
            if value:
                print(f"Value: {value.decode()}")
            else:
                print("Key not found.")
        
        elif choice == '3':
            key = input("Enter key to delete: ")
            r.delete(key)
            print(f"Deleted key '{key}'")
        
        elif choice == '4':
            user_id = input("Enter user ID: ")
            name = input("Enter name: ")
            email = input("Enter email: ")
            r.hset(f"user:{user_id}", mapping={"name": name, "email": email})
            print("User hash set.")
        
        elif choice == '5':
            user_id = input("Enter user ID: ")
            field = input("Enter field (name/email): ")
            value = r.hget(f"user:{user_id}", field)
            if value:
                print(f"{field}: {value.decode()}")
            else:
                print("Field not found.")
        
        elif choice == '6':
            break
        
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
