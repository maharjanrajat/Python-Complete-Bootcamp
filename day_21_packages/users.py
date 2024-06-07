import requests

def get_users():
    api_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(api_url)
    if(response.status_code == 200):
        response_body = response.json()
        return response_body
    else:
        return 'Error Occured'

users = get_users()
for user in users:
    print("=======================")
    print(f"name= {user['name']}")
    print(f"email= {user['email']}")
    print(f"address= {user['address']['street']}")