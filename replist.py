"""
Program retrive list of the github public repositories
"""
import requests


DEFAULT_NAME = 'dmitrtrc'

if not (username := input("Enter the github username:")):
    username = DEFAULT_NAME

request = requests.get("https://api.github.com/users/" + username + "/repos")
response = request.json()
print("Verion 0.3:")
for index, record in enumerate(response):
    print("Project Number:", index + 1, end=" ## ")
    print("Project Name:", record["name"])
    print("Project URL:", record["svn_url"], "\n")
