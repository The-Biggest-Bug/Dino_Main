import requests
import csv as c
import pandas as pd


DINOSAUR = "https://dinosaur-facts-api.shultzlab.com/dinosaurs"
DINOSAUR_RANDOM = "https://dinosaur-facts-api.shultzlab.com/dinosaurs/random"
DINOSAUR_RANDOM_NAME = "https://dinosaur-facts-api.shultzlab.com/dinosaurs/random/name"
DINOSAUR_RANDOM_DESC = "https://dinosaur-facts-api.shultzlab.com/dinosaurs/random/description"

def get_all_dinosaurs():
    try:
        response = requests.get(DINOSAUR)
        dinos = response.json()
        print("Here is a list of 755 dinosaurs for your research needs: \n")
        for dino in dinos:
            name = dino.get("Name", "Unknown")
            description = dino.get("Description", "Unknown")

            print(f"Name: {name}")
            print(f"Description: {description}\n")
        
    except requests.RequestException as e:
        print(f"Problem fetching dinos: {e}")

def get_random_dino():
    try:
        response = requests.get(DINOSAUR_RANDOM)
        dinos = response.json()
        print("This is a random dinosaur name and description: \n")
        for dino in dinos:
            name = dino.get("Name", "Unknown")
            description = dino.get("Description", "Unknown")

            print(f"Name: {name}")
            print(f"Description: {description}\n")
        
    except requests.RequestException as e:
        print(f"Problem fetching dinos: {e}")

def get_random_dino_name():
    try:
        response = requests.get(DINOSAUR_RANDOM_NAME)
        dinos = response.json()
        print("This is a random dinosaur name: \n")
        for dino in dinos:
            name = dino.get("Name", "Unknown")

            print(f"Name: {name}")
        
    except requests.RequestException as e:
        print(f"Problem fetching dinos: {e}")


def get_random_dino_desc():
    try:
        response = requests.get(DINOSAUR_RANDOM_DESC)
        dinos = response.json()
        print("This is a random dinosaur description: ")
        for dino in dinos:
            desc = dino.get("Description", "Unknown")

            print(f"Name: {desc}")
        
    except requests.RequestException as e:
        print(f"Problem fetching dinos: {e}")
print("jrngkihbsvkhsb")