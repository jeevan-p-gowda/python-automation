import requests
import sys

def get():
    url = "https://reqres.in/api/users/2"
    headers = {
        'x-api-key': 'reqres-free-v1'
    }
    response = requests.get(url, headers=headers)
    print(response.text)
    print(sys.executable) # prints the path to the Python interpreter

if __name__ == "__main__":
    get()
