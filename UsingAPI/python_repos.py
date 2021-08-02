import requests

# execute the API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# store r like json file
response_dict = r.json()

# deal with the data
print(response_dict.keys())
