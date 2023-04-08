from rocketchat_API.rocketchat import RocketChat
import requests

rocket = RocketChat('dasbot', '32167', server_url='http://localhost:3000')

rocket.im_files(room_id='Gr5br9ABoMW6eaGTSHam3CrrLxD9PJARaT', user_name='dasbot').json()
n = rocket.im_files(room_id='Gr5br9ABoMW6eaGTSHam3CrrLxD9PJARaT', user_name='dasbot').json()
sub_url = n['files'][0]['path']

creds = {"user": "dasbot", "password": "32167"}

login_url = 'http://localhost:3000/api/v1/login'

s = requests.Session()
login_response = s.post(login_url, data=creds)
login_data = login_response.json()
headers = {
    "X-Auth-Token": login_data["data"]["authToken"],
    "X-User-Id": login_data["data"]["userId"]
}

url = "{}/{}?download".format('http://localhost:3000', sub_url.lstrip('/'))

get_file = s.get(url, stream=True, headers=headers)
get_file.raise_for_status()

with open('dnd.yaml', 'wb') as f:
    for chunk in get_file.iter_content(chunk_size=1024):
        if chunk:
            f.write(chunk)