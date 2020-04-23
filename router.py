import requests, json

class RouterData():

    def sendStats(self, values):
        activity_api_url = "https://10.0.101.240:44350/api/sync"
        response = requests.post(activity_api_url, data=values)

        print(access_token_response.text)


