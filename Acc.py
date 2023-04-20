import requests
import json

# Discord API endpoint for creating an account
url = "https://discord.com/api/v9/auth/register"

# User input for account creation
email = input("Enter your email: ")
password = input("Enter your password: ")
username = input("Enter your username: ")

# Payload for account creation
payload = {
    "email": email,
    "password": password,
    "username": username
}

# Headers for API request
headers = {
    "Content-Type": "application/json"
}

# Send POST request to Discord API to create account
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if account creation was successful
if response.status_code == 200:
    print("Account created successfully!")
    
    # Log account information to text file
    with open("discord_accounts.txt", "a") as file:
        file.write(f"Email: {email}, Password: {password}, Username: {username}\n")
else:
    print("Account creation failed. Please try again.")
