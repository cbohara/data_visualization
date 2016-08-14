# requests package allows a Python program to easily request info from a website
# and examine the response that is returned
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# make an API call
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# store the response
r = requests.get(url)
# check that the response was successful with a status code of 200
print("Status code:", r.status_code)
# API returns the info in a json format, so we use the json method to convert
# the info into a Python dictionary
response_dict = r.json()
# print(response_dict.keys())
# it's good practice to check that incomplete_results returns false to make sure
# that the request was successful
print(response_dict['incomplete_results'])
# print the value of total count = total # of python repos on github
print("Total repos:", response_dict['total_count'])
# store list of dictionaries for each python repo into repo_dicts
repo_dicts = response_dict['items']
# print("Repos returned:", len(repo_dicts))
# take a look at the first repo
# each repo has about 70 keys
# print("\nKeys:", len(repo))
# for key in sorted(repo.keys()):
#     print(key)

# print info about each repo
# for repo in repo_dicts:
#     print("\nSelected info about each repo:")
#     print("Name:", repo['name'])
#     print("Owner:", repo['owner']['login'])
#     print("Stars:", repo['stargazers_count'])
#     print("Repository:", repo['html_url'])
#     print("Created:", repo['created_at'])
#     print("Updated", repo['updated_at'])
#     print("Description", repo['description'])

# create 2 empty lists to store the data to include in the chart
names, plot_dicts = [], []
for repo in repo_dicts:
    # name of each list to label the bar
    names.append(repo['name'])
    plot = {
        # bar height
        'value': repo['stargazers_count'],
        # allows us to hover over bar and read description of repo
        'label': repo['description'],
        # Pygal uses URL assoc w xlink to turn each bar into an active link
        'xlink': repo['html_url']
    }
    plot_dicts.append(plot)

# LightenStyle class (alias LS), LightColorizedStyle class (alias LCS)
my_style = LS('#333366', base_style=LCS)
# instance of the Pygal Config class
my_config = pygal.Config()
# lesson learned - pygal cannot accept all this info as one object
# need to do line by line specification of object.key = value
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
# shorten longer project names to 15 chars
my_config.truncate_label = 15
# hide horiz lines on graph
my_config.show_y_guides = False
my_config.width = 1000

# add in my_styles, specify x_label rotation, do not show legend
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Starred Python Projects on Github'
chart.x_labels = names
# we don't need the data series to be labeled
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
