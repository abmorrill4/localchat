from werkzeug.security import generate_password_hash
import json, os

FILE = "users.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)

with open(FILE) as f:
    users = json.load(f)

username = input("Enter username: ")
password = input("Enter password: ")

if username in users:
    print("User already exists.")
else:
    hashed = generate_password_hash(password)
    users[username] = hashed
    with open(FILE, "w") as f:
        json.dump(users, f, indent=2)
    print(f"User {username} added.")
