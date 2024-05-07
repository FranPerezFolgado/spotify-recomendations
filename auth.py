import requests
import json
import base64


CLIENT_ID = "85401db17af745e7836faa1acdd79cdb"
CLIENT_SECRET = "75f2820b7849469bb2f8c4395c55aedc"

AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
BASE_URL = "https://api.spotify.com/v1/"


auth_code = requests.get(
    AUTH_URL,
    {
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": "https://open.spotify.com/collection/playlists",
        "scope": "user-top-read",
    },
)
print(auth_code.content)
encoded_credentials = base64.b64encode(
    CLIENT_ID.encode() + b":" + CLIENT_SECRET.encode()
).decode("utf-8")
headers = {
    "Authorization": "Basic " + encoded_credentials,
    "Content-Type": "application/x-www-form-urlencoded",
}
payload = {
    "grant_type": "authorization_code",
    "code": auth_code,
    "redirect_uri": "https://open.spotify.com/collection/playlists",
    #'client_id': CLIENT_ID,
    #'client_secret': CLIENT_SECRET,
}
access_token_request = requests.post(url=TOKEN_URL, data=payload, headers=headers)

print(access_token_request.json())
