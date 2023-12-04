import requests
import json


def get_popular_repositories():
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "/openshift/origin",
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        repositories = response.json()["items"]
        for repository in repositories:
            print(json.dumps(repository, sort_keys=True, indent=4))
            break
    else:
        print("не повезло((:", response.status_code)


get_popular_repositories()