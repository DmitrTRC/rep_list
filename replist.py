import requests

username = input("Enter the github username:")
request = requests.get("https://api.github.com/users/" + username + "/repos")
response = request.json()
for repo in range(0, len(response)):
    print("Project Number:", repo + 1, end=" ## ")
    print("Project Name:", response[repo]["name"])
    print("Project URL:", response[repo]["svn_url"], "\n")
