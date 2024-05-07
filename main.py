import requests
import logging
import base64
import json
import genres


logging.basicConfig(level=logging.DEBUG)

API_USER = "85401db17af745e7836faa1acdd79cdb"
API_SECRET = "75f2820b7849469bb2f8c4395c55aedc"

AUTH_URL = "https://accounts.spotify.com/api/token"


encoded_credentials = base64.b64encode(
    API_USER.encode() + b":" + API_SECRET.encode()
).decode("utf-8")
token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded",
}

token_data = {"grant_type": "client_credentials"}
r = requests.post(AUTH_URL, data=token_data, headers=token_headers)


auth_token = json.loads(r.content)["access_token"]
print(auth_token)

auth_header = {"Authorization": "Bearer " + auth_token}

USERS_TOP_ITEMS_URL = "https://api.spotify.com/v1/me/top/artists"

query_params = {"limit": 1}

top_artists = requests.get(
    url=USERS_TOP_ITEMS_URL, params=query_params, headers=auth_header
)
print(top_artists.content)
print(top_artists)
