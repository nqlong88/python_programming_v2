# create playlist:
import json

playlist = [
    {
        'title': 'Yesterday',
        'genre': 'Pop',
        'artiste': 'the beatles',
        'year': '1965',
        'length': 2.025
    },
    {
        'title': 'Near You',
        'genre': 'Pop',
        'artiste': 'Francis Craig',
        'year': '1947',
        'length': 4.25
    },
    {
        'title': 'Bodak Yellow',
        'genre': 'Pop',
        'artiste': 'Cardi B',
        'year': '2017',
        'length': 3.25
    },
    {
        'title': 'Bodak Yellow',
        'genre': 'Pop',
        'artiste': 'Cardi B',
        'year': '2017',
        'length': 3.25
    },
    {
        'title': 'made up',
        'genre': 'rock',
        'artiste': 'long nguyen',
        'year': '2020',
        'length': 30.25
    },
    {
        'title': 'Bodak Yellow',
        'genre': 'Pop',
        'artiste': 'Cardi B',
        'year': '2017',
        'length': 3.25
    },
    {
        'title': 'Rolling in the Deep',
        'genre': 'Rap',
        'artiste': 'Adele',
        'year': '2011',
        'length': 24.25
    },
    {
        'title': 'Yellow',
        'genre': 'Hip hop',
        'artiste': 'Warm Play',
        'year': '2027',
        'length': 13.25
    },
    {
        'title': 'Smoke! Smoke! Smoke!',
        'genre': 'Country',
        'artiste': 'Tex William Western Caravan',
        'year': '1947',
        'length': 16.25
    },
    {
        'title': 'abc',
        'genre': 'unknown',
        'artiste': 'xyz',
        'year': '2090',
        'length': 8.25
    },
]


actions = ['print titles', 'print artistes', 'print length', 'popular genre']

print (f' please pick one of the following: {actions}')
action = input('action: ')

if action == 'print titles':
    for song in playlist:
        print(song['title'])
    
if action == 'print artistes':
    for song in playlist:
        print(song['artiste'])  

if action == 'print length':
    length = 0
    for song in playlist:   
        length += song['length']
        length_hour = int(length/60)
        length_min = round(length - length_hour*60)
    print (f' total playlist is: {length_hour} hours and {length_min} minutes')  

if action == 'popular genre':
    genres_dict = {}
    genre_list = []
    most_pop = 0
    answer = ''
    for song in playlist:
        genre_list.append(song['genre'])
        # Create dictionary to tally how many times each genre appears
        if song['genre'] in genres_dict:
            genres_dict[song['genre']] += 1
        else:
            genres_dict[song['genre']] = 1
    # Find max:
    for key in genres_dict:
        if genres_dict[key] > most_pop:
            most_pop = genres_dict[key]
    # asign max frequency to genre:
    for key in genres_dict:
        if genres_dict[key] == most_pop:
            answer = key
print(genre_list)
print(genres_dict)
print(f' the most popular is {answer} which appears {most_pop} times')


