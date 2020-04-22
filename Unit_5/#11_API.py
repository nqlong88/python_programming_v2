# class 11 (4/15/2020)
'''
import requests

response = requests.get('https://statsapi.web.nhl.com/api/v1/teams') #this access but wont print (will get code 200)

print(response) #wont print
print(response.json()) # this will print data: .json() -> json formatted APIs
'''


#rapidapi.com - deezer - python -> request
import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"eminem"} #query input; could add more querystrings below

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "6fc77a6cb6msh40e2c7290548822p17d892jsn4c089450c258"
    }

eminem = requests.request("GET", url, headers=headers, params=querystring).json() #convert to json file
#could have multiple request here (so dont't have to have multiple separate requests below)
print(eminem)

import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"Ed Sheeran"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "6fc77a6cb6msh40e2c7290548822p17d892jsn4c089450c258"
    }

ed = requests.request("GET", url, headers=headers, params=querystring).json()

print(ed)


import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"Cardi B"}

headers = {
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com",
    'x-rapidapi-key': "6fc77a6cb6msh40e2c7290548822p17d892jsn4c089450c258"
    }

cardi = requests.request("GET", url, headers=headers, params=querystring).json()

print(cardi)

m = eminem['data']
e = ed['data']
c = cardi['data']


#How many tracks are listed?
def song_count(artist):
    count = 0
    for item in artist:
        count += 1
    return count 

print(f' eminem: {song_count(m)}')
print(f' ed: {song_count(e)}')
print(f' cardi: {song_count(c)}')


#How many albums are listed?

def album(artist):
    album_id=[] #shorter way to do the above: use a set vs. list -> avoid duplicates 
    for item in artist:
        if item['album']['id'] not in album_id:
            album_id.append(item['album']['id'])
    return len(album_id)

print(f' eminem albums: {album(m)}')
print(f' edsheeran albums: {album(e)}')
print(f' cardi albums: {album(c)}')


#Count the number of tracks with explicit lyrics

def explicit(artist):
    explicit_count = 0
    for item in artist:
        if item['explicit_content_lyrics'] == 1:
           explicit_count +=1
    return explicit_count

print(f' eminem: {explicit(m)}')
print(f' e: {explicit(e)}')
print(f' c: {explicit(c)}')

#Which year was the most recent album for each'''
def album_data (artist):
    album_id = []
    album_url = "https://deezerdevs-deezer.p.rapidapi.com/album/"
    for item in artist:
        album_id.append(item["album"]["id"])
    set(album_id)
    for item in album_id:
        album_url = album_id+item
        album_data = requests.request("GET", album_url, headers=headers).json()
    return album_data
#print (album_data(em))

#4. When was the release date for album "The Eminem Show"



#5. How many tracks on "Shape of You"



#6. Which artist colab w Cardi B on track "Cardi B"



#7. build play list: for each track include: id readable title title_short title_version
#link duration rank explicit_lyrics explicit_content_lyrics




#8. save playlist to file