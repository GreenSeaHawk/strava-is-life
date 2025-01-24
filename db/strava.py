import requests
import json
import os
from dotenv import load_dotenv

load_dotenv(override=True)
access_token = os.getenv("strava_access_token")

# https://www.strava.com/api/v3/athletes/11053665/?access_token=a026241fcabd90a7baaa196a84bc70f4f7b719d9

def get_profile():
    profile_response = requests.get(f"https://www.strava.com/api/v3/athletes/11053665/?access_token={access_token}")
    print(profile_response)
    profile_info = json.loads(profile_response.text)
    # print(profile_info)

    with open("db/profile_info.json", "w") as f:
        json.dump(profile_info, f, indent=4)

get_profile()

# "https://www.strava.com/api/v3/athlete/activities?access_token=a0c33081c42688f013466480a42cfd5e5f216f99"

def get_activities(num_act=100):
    profile_response = requests.get(f"https://www.strava.com/api/v3/athlete/activities?per_page={num_act}&access_token={access_token}")
    print(profile_response)
    profile_info = json.loads(profile_response.text)
    # print(profile_info)

    with open("db/activities.json", "w") as f:
        json.dump(profile_info, f, indent=4)

get_activities()