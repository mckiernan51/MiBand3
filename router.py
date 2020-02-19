import requests, json


    
       
token_url = "https://localhost:44323/connect/token"
activity_api_url = "https://localhost:44350/api/device/device/list?page=1&items=10&includeUnassigned=true"

    #client (application) credentials on apim.byu.edu
client_id = "devicesyncapi"
client_secret = "devicesyncapi1"
data = {'grant_type': 'client_credentials'}

access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

print(access_token_response.headers)
print(access_token_response.text)

tokens = json.loads(access_token_response.text)

print("access token: " + tokens['access_token'])

#step B - with the returned access_token we can make as many calls as we want

api_call_headers = {'Authorization': 'Bearer ' + tokens['access_token']}
api_call_response = requests.get(activity_api_url, headers=api_call_headers, verify=False)

print(api_call_response.text)



