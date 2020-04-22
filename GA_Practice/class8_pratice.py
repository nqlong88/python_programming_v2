#Enumerate practice:index,item: in enumerate()

planes = [
    {
        'make': 'Boeing',
        'model': '737MAX',
        'year': '2017',
        'color': 'black'
    },
    {
        'make': 'Airbus',
        'model': 'A320',
        'year': '2005',
        'color': 'white'
    },
]

#add price

msrps = ['10 mil', '12 mil']

# for each price (index) in msrps: create a new key 'price' and assign value = msrps[index]

# start with first dict in list planes: assign to 1st price in msrps: needs to match 1st dict -> 1st price:
for index, plane in enumerate(planes): #find rorate: dict idex and return dict
    plane['price'] = msrps[index] # once dict find; use index of dict to index price

print(planes)