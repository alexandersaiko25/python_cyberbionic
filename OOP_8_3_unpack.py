import json

def unpack_json():

    with open("links.json", 'r') as oldest_file:
        new_file = json.load(oldest_file)

        link_input = input("Enter your link: ")
        name_input = input("Enter your name for link: ")

        for x, y in new_file.items():
            if link_input == y['link'] == "www.youtube.com" or name_input == y['name'] == "Youtube":
                print("Your short link: (abc.ua)")
            elif link_input == y['link'] == "www.google.com" or name_input == y['name'] == "Google":
                print("Your short link: (xyz.ua)")

unpack_json()
