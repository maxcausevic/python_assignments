# python Stack - Day 2

# loops (deeper dive)

# for - in loops with range() function
#for i in range(len(list)):
colors = ['blue', 'yellow', 'green', 'red']

for i in range(len(colors)):
    print(colors[i])

    #for-in loopos over lists without range() function
for color in colors:
    print(f'without range function: {color}')

# for-in loops through dictionaries
shang = {
    'real_name': 'Shang-Chi',
    'cod_name': 'Shang-Chi, Master of Kung Fu',
    'origin': 'Raised to be an assassin',
    'arch_enemy': 'Fu Manchu'
}
for key_name in shang:
    print([key_name]) # prints out key names
    print(shang[key_name]) # prints out values at key names
    print(key_name, shang[key_name]) #prints out key name, then value at key name

# this is a list of dictionaries
marvel_superheroes = []
    {
        'real_name': 'Shang-Chi',
        'code_name': 'Shang-Chi, Master of Kung Fu',
        'origin': 'Raised to be an assassin',
        'arch_enemy': 'Fu Manchu'
    }
    {
        'real_name': 'Peter Parker',
        'code_name' : 'Spider-Man',
    }

    for superhero in marvel_super_heroes:
        for trait in superhero:
            print(superhero[trait])


european_cities = [
    {
        'city_name': 'Paris',
        'country': 'France',
        'language': 'French',
        "favorite_food": 'croissant'
    },
    {
        'city_name': 'Berlin',
        'country': 'Germany',
        'language': 'German',
        "favorite_food": 'schnitzel'
    },
    {
        'city_name': 'London',
        'country': 'England',
        'language': 'English',
        "favorite_food": 'fish_and_chips'
    },
    {
        'city_name': 'Edinburgh',
        'country': 'Scotland',
        'language': 'Gaelic',
        "favorite_food": 'haggis'
    }
]

for city in european_cities:
    for key, val in city.items():
        if key == "city_name":
            print(key,val)

european_cities[3]['country']
print(european_cities[3]['country'])




