import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(override=True)
refresh_token = os.getenv("strava_refresh_token")
client_secret = os.getenv("strava_client_secret")
client_id = os.getenv("strava_client_id")

def get_access_token():
    response = requests.post(f"https://www.strava.com/oauth/token?client_id={client_id}&client_secret={client_secret}&refresh_token={refresh_token}&grant_type=refresh_token")
    response_text = json.loads(response.text)
    return response_text['access_token']

access_token = get_access_token()



def get_profile():
    profile_response = requests.get(f"https://www.strava.com/api/v3/athletes/11053665/?access_token={access_token}")
    print(profile_response, 'profile_response')
    profile_info = json.loads(profile_response.text)
    # print(profile_info)

    with open("db/profile_info.json", "w") as f:
        json.dump(profile_info, f, indent=4)

get_profile()



def get_activities(num_act=100, num_pages=1):
    if num_act > 200:
        print('Max activities per page is 200')
        return
    if num_pages < 1:
        print('Must have at least 1 page')
        return
    list_of_acts = []
    for i in range(1, num_pages + 1):
        response = requests.get(f"https://www.strava.com/api/v3/athlete/activities?per_page={num_act}&page={i}&access_token={access_token}")
        print(response, 'activities_response', i)
        profile_info = json.loads(response.text)
        for act in profile_info:
            list_of_acts.append(act)
    # print(profile_info)

    with open("db/activities.json", "w") as f:
        json.dump(list_of_acts, f, indent=4)

get_activities(200, 3)