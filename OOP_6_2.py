base_links = {
    "link_1" : {
        "name": "Youtube",
        "link": "www.youtube.com",
    },
    "link_2" : {
        "name": "Google",
        "link": "www.google.com",
    },
}

link_input = input("Enter your link: ")
name_input = input("Enter your name for link: ")

for x, y in base_links.items():
    if link_input == y['link'] == "www.youtube.com" or name_input == y['name'] == "Youtube":
        print("Your short link: (abc.ua)")
    elif link_input == y['link'] == "www.google.com" or name_input == y['name'] == "Google":
        print("Your short link: (xyz.ua)")



