import json

def links():

    base_links = {
        "link_1": {
            "name": "Youtube",
            "link": "www.youtube.com",
        },
        "link_2": {
            "name": "Google",
            "link": "www.google.com",
        },
    }

    with open('links.json', 'w') as file:
        json.dump(base_links, file)

links()