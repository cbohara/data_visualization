import json
from country_codes import get_country_code
from pygal.maps.world import World

filename = 'chapter_16/population_data.json'

with open(filename) as f:
    # json.load() converts the data into a format Python can work with
    pop_data = json.load(f)

# build a dictionary of population data
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# group the countries into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 10000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'World Population in 2010, by Country'
wm.add('0-10,', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')
