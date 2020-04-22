# defining a class

class Person: #typically class names are Upper Case
    def __init__(self): # SELF is used to access Data Property of a CLASS
        print('class instantiated')

p = Person() #create an object: p is object belongs to class Person

# Class: store 1) properties and 2) Actions(functions/methods)

class Rectangle: #create new class/object
    def __init__(self, l, w): # Constructor method
        self.length = l #set property: self, property
        self.width = w #set property

    def area(self): # A METHOD
        return self.length * self.width

    def perimeter(self): # A METHOD
        return (self.length + self.width)*2


r1 = Rectangle(10,5) #Created a new Object

print(r1.area())
print(r1.perimeter())


# Creating a Playlist:
class Playlist:
    def __init__(self, name): #self is built-in (default); name: specify Playlist has a name
        self.songs = [] #prop 1: has a song list
        self.name = name  #prop 2: has a playlist name

    #write the add_song method:
    def add_song(self,song):
        #validate song data
        # has to be dictionary
        # has to have: title, artist, length
        '''
        def reverse_dict(input_dict):
            result = {}
            for key in input_dict:
                if type(input_dict[key]) is list or type(input_dict[key]) is dict:
                    result[tuple(input_dict[key])] = key
                else:
                    result[input_dict[key]] = key
            return result
        '''
        #REVIEW THIS PART!!!!!
        if type(song) is dict and 'title' in song and 'artist' in song and 'length' in song:
            self.songs.append(song)
        else:
            print('INVALID SONG')

    #write get title
    #assume songs are dictioanry:

    def get_titles(self):
        titles = []
        for song in self.songs: #use self. -> refer to member of a class
            titles.append(song['title'])
        return titles

    #write duration: total lenghth of play list
    def duration(self):
        duration = 0
        for song in self.songs:
            duration += song['length']
        return duration



#create a new play list (in a class): my_playlist -> AN OBJECT
p = Playlist('my_playlist') # this is to tiniate a playlist named "my_playlist". Playlist is a class initiated w a name


p.add_song({
    'title' : 'Bodak',
    'artist' : 'Cardi B',
    'length' : 1.30,
    })


p.add_song({
    'title' : 'song 2',
    'artist' : 'artist 2',
    'length' : 4.10,
    })


p.add_song({
    'title' : 'song 3',
    'artist' : 'artist 3',
    'length' : 5.10,
    })


print(p.get_titles())
print(p.duration())
