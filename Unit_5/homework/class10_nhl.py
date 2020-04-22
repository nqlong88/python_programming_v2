#starter code:

import requests #request module: pull data online

class NhlTeams:
    def __init__(self): #initiate w self only: no need to pass anything here when initiate
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams').json() # response = entire online file
        self.nhl_stats = response['teams'] #getting value from key 'teams' which is list of teams
        #'teams': [{'','',{},''},...{}]
    #write method to get team names
    #Need to figure out data structure {'copyright:'blurb', 'teams': [{'','',{},''},...{}]}
    # self.nhl_stats
    def get_team_names(self):
        team_names = []
        for dic_item in self.nhl_stats:
           team_names.append(dic_item['teamName'])
        return team_names

    #write method to get dict: {'team' : # won NHL}
    '''
    CAN'T FIND DATA - DON'T THINK IT'S THERE
    '''

    #write method conferences: show {'eastern': xxx, 'western': yyyy}
    def conferences(self):
        eastern = 0
        western = 0
        conferences ={}
        #test data call:
        #return print(self.nhl_stats[3]['conference']['name'])
        for item in self.nhl_stats: #loops thru dict items in list
            if item['conference']['name'] == 'Eastern':
                eastern += 1
            if item['conference']['name'] == 'Western':
                western += 1
        conferences = {'Eastern':eastern, 'Western':western} #initially had this above for; below for: to update after loop
        return print(f'number of teams: {conferences}')

    #return team that has oldest first year of play
    def get_oldest_team(self):
        oldest_year = 1000000
        oldest_team =''
        for item in self.nhl_stats:
            if int(item['firstYearOfPlay']) < oldest_year:
                oldest_year = int(item['firstYearOfPlay'])
                oldest_team = item['teamName']
        return print(f'the oldest NHL team is: {oldest_team} / founded in: {oldest_year}')
    
    #Solution:
    def get_oldest_team_sol(self):
        #using a function to sort a list
        sorted_list = sorted(self.nhl_stats, key = lambda k: k['firstYearOfPlay'])
        #print fist item: which is the smallest firstYearOfPlay
        print(sorted_list[0]['name'])

teams = NhlTeams()
teams.get_oldest_team_sol()



hockey = NhlTeams()
print(hockey.get_team_names())
hockey.conferences()   
hockey.get_oldest_team()

#Solution:
teams = NhlTeams()
teams.get_oldest_team_sol()