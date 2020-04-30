#problem 1:
import json

class Movie:
    def __init__(self, move_info):
        self.cast = []
        self.move_info = move_info

#Add method to add cast, method checks for valid data:
    def add_cast(self,newcast):
        if type(newcast) is dict and newcast['name'] !='' and newcast['age'] !=0 and newcast['sex'] == 'M' or newcast['sex'] == 'F':
            self.cast.append(newcast)
        else:
            print ('Check INPUT / please put in: name, age, sex in valid dict format')
        return self.cast

#Method print movie info and cast:
    def describe(self):
        return print (f'movie name: {self.move_info} / cast: {self.cast}')


# Method to compare two movies (take a movie as object and compare if more than 2 actors in common)
    def compare_to(self,comparison): #pass movie cast 
        count = 0
        result = 0
        index_1 = 0
        while index_1 < len(self.cast)-1:
            if self.cast[index_1] in comparison[1]['cast']: # you can actually compare dict (dict1 == dict2) same as string/value
                count += 1
            index_1 +=1 
        if count >= 2:
            result = 1
        else:
            result = -1
        return print(f' result is: {result} and count is: {count}')

# Method to save a file to .json file using dump: save a movie file {name,cast}
    def save_to_file(self,filename):
        movie_save = {'movie':self.move_info, 'cast':self.cast} #this is the movie & details to be saved
        with open(filename, 'w') as saved_file: #create file: create name: 'filename.json', action: 'w' -> assingn to saved_file
            json.dump(movie_save, saved_file) #take movie info -> put int saved_file
        print (f'File saved at: {filename}')


nc1 = Movie({'name':'random','genre':'thriller','length': 2})
nc1.add_cast({'name':'long', 'age': 10, 'sex': 'M'})
nc1.add_cast({'name':'actor 2', 'age': 11, 'sex': 'F'})
nc1.add_cast({'name':'actor 3', 'age': 100, 'sex': 'M'})
nc1.describe()

        
nc2 = Movie({'name':'funny movie','genre':'comedy','length': 4})
nc2.add_cast({'name':'short', 'age': 40, 'sex': 'F'})
nc2.add_cast({'name':'actor 2', 'age': 11, 'sex': 'F'})
nc2.add_cast({'name':'actor 3', 'age': 100, 'sex': 'M'})
nc2.describe()
    
cast_comparison = [{'Movie':{'name':'funny movie','genre':'comedy','length': 4}},{'cast':[{'name': 'long', 'age': 10, 'sex': 'M'}, {'name': 'actor 2', 'age': 11, 'sex': 'F'}, {'name': 'actor 3', 'age': 100, 'sex': 'M'}]}]

nc1.compare_to(cast_comparison)

nc1.save_to_file('movie_1_class10hw.json')


#Sol:
'''
class MovieSol:
    def __init__(self, t, g, rt):
        self.title = t
        self.genre = g
        self.running = rt 
        self.cast = []

    def compare_to(self,other_movie):
        for item in self.cast:
            if item in 
'''