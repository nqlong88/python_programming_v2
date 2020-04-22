#Working with Covid API: https://rapidapi.com/api-sports/api/covid-193

import requests
import json

#1. create CovidStats:
class CovidStats:
    def __init__(self):
        url = "https://covid-193.p.rapidapi.com/statistics"
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "6fc77a6cb6msh40e2c7290548822p17d892jsn4c089450c258"
            }
        self.covid19 = requests.request("GET", url, headers=headers).json()
    #print data to check:    
    def print(self):
        return print(self.covid19)

#2. write fetch stats to get covid statistics and store in an instance variable
    def fetch_statistics(self):
        self.instancevar = []
        index = 0
       #Create a list: [{country1}, {counstry 2}]
        while index <= len(self.covid19['response'])-1:
            self.instancevar.append(self.covid19['response'][index]) #this take out the "number" keys -> create list of countries dict
            index += 1
        return self.instancevar

# 3. top 10 : find top 10 most cases: -> self.instancevar[1]['cases']['total'])
    def top_ten(self):
        #need to sort by case; then pick first 10: using lamda fucntion
        sorted_data = sorted(self.instancevar, key= lambda k: k['cases']['total']) #How to sort reverse?
        index_2 = len(self.instancevar) - 1
        top_countries = []
        while index_2 > len(self.instancevar) - 11:
            top_countries.append(sorted_data[index_2]['country'])
            index_2 -= 1
        return print(f' #3: {top_countries}')
    
#4 get country input: request data for a country
    def get_country_stats(self,country):
        request = country #note: request is case sensitive
        self.answer =[]
        for item in self.instancevar:
            if item['country'] == request:
                self.answer.append(item)
        return print(f' #4:  {self.answer}')
    
#5 show region stats: display active, critical, recovered and total death for each region
    def show_regional_stats(self):
        regions = ['Europe', 'Asia','Oceania','South-America','Africa','North-America','South-America']
        for region in regions:
            for country in self.instancevar:
                if region == country['country']:
                    print (f' #5: {country}')

#6 that returns all the countries that do not have data for the number of tests done.
    def tests_unavailable(self):
        no_test = []
        for country in self.instancevar:
            if country['tests']['total'] == None:
                no_test.append(country['country'])
        return print(f' #6: {no_test}')

#7 store file
    def stats_to_file(self,filename):
        data_file = self.answer
        with open(filename,'w') as saved_file:
            json.dump(data_file,saved_file)


covid19 = CovidStats()
#covid19.print()
covid19.fetch_statistics()
covid19.top_ten()
covid19.get_country_stats('China')
covid19.show_regional_stats()
covid19.tests_unavailable()
covid19.stats_to_file('covid19_HW.json') #make sure cd into right folder