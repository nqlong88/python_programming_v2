#worked w Abdul & Donyell
import requests
import json

url = "https://deezerdevs-deezer.p.rapidapi.com/search"
album_url = "https://deezerdevs-deezer.p.rapidapi.com/album/"

q_em = {"q":"eminem"}
q_ed = {"q":"ed sheeran"}
q_cardi = {"q":"cardi b"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "7d4ccbc25bmsh49d7ffce4bf360ap1abf2fjsn6e4b1323ce66"
    }

response_em = requests.request("GET", url, headers=headers, params=q_em).json()
response_ed = requests.request("GET", url, headers=headers, params=q_ed).json()
response_cardi = requests.request("GET", url, headers=headers, params=q_cardi).json()

em = response_em ["data"]
ed = response_ed ["data"]
cardi = response_cardi ['data']

def track_count (artist):
    count = 0
    for song in artist:
        count += 1
    return count

def album_count (artist):
    
    albums = []
    for item in artist:
        #if item ["album"]["title"] not in albums:
        albums.append(item["album"]["title"])
        
    return len(set(albums))

def explicit (artist):
    explicit_count = 0
    for song in artist:
        if song["explicit_lyrics"] == True:
            explicit_count += 1
    return explicit_count

def album_data (artist):
    album_id = []

    for item in artist:
        album_id.append(item["album"]["id"])
    set(album_id)
    for item in album_id:
        album_url = album_id+item
        album_data = requests.request("GET", album_url, headers=headers).json()
    return album_data

print (album_data(em))





            

print(explicit(cardi))