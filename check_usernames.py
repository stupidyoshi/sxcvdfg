import requests
import itertools
import string

def is_username_available(username):
    url = f"https://www.roblox.com/UserCheck/Username"
    response = requests.get(url, params={"username": username})
    return response.status_code == 200 and response.json().get("available")

def generate_usernames(length):
    chars = string.ascii_lowercase + string.digits
    for name in itertools.product(chars, repeat=length):
        yield ''.join(name)

def check_usernames():
    for length in range(3, 6):  # Check lengths from 3 to 5
        for username in generate_usernames(length):
            if is_username_available(username):
                print(f"Available: {username}")

if __name__ == "__main__":
    check_usernames()
