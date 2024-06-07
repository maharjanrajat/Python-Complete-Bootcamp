import requests

def get_advice():
    api_url = 'https://api.adviceslip.com/advice'
    response = requests.get(api_url)
    if(response.status_code == 200):
        response_body = response.json()
        return response_body['slip']['advice']
    else:
        return 'Error Occured'

returned_advice = get_advice()
print(returned_advice)

# ===============
# name: Leanne Graham
# email: Sincere@april.biz
# address: Kulas Light
# ==================
# name = another user name
# email: another user email
# address = another user address
# =======================
