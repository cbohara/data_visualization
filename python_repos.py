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
names, stars = [], []
for repo in repo_dicts:
    # name of each list to label the bar
    names.append(repo['name'])
    # height of the bars
    stars.append(repo['stargazers_count'])

# make visualization
# LightenStyle class (alias LS), LightColorizedStyle class (alias LCS)
my_style = LS('#333366', base_style=LCS)
# add in my_styles, specify x_label rotation, do not show legend
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most Starred Python Projects on Github'
chart.x_labels = names
# we don't need the data series to be labeled
chart.add('',stars)
chart.render_to_file('python_repos.svg')
