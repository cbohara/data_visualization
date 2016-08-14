import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# process info about each submission
# convert response text to a python list
sub_ids = r.json()
# use these ids to build a set of dictionaries that each will store info about
# the current submissions
sub_dicts = []
# loop throught first 30 submission
for sub_id in sub_ids[:30]:
    # make a separate API call for each submission
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(sub_id) + '.json')
    sub_r = requests.get(url)
    print(sub_r.status_code)
    response_dict = sub_r.json()
    # create a dictionary for each submission
    sub_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(sub_id),
        # when you're not sure if a key exists in a dictionary, use the dict.get()
        # method, which returns the value assoc with the given key if it exists
        # or the value provided if the key does not exist (0)
        'comments': response_dict.get('descendants', 0)
    }
    # add each dictionary to our list of submission dictionaries
    sub_dicts.append(sub_dict)
# we want to the list by number of comments
# itemgetter() function comes from the operator module
# pass in the key 'comments', and it pulls the values associated with the key = # of comments
# reverse=True in order to list the most commented stories first
sub_dicts = sorted(sub_dicts, key=itemgetter('comments'), reverse=True)
# loop through list and print info about top submissions
for sub_dict in sub_dicts:
    print("\nTitle:", sub_dict['title'])
    print("Discussion link:", sub_dict['link'])
    print("Comments:", sub_dict['comments'])
