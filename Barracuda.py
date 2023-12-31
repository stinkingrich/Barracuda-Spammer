import os
import random
import time
import requests
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore, init

init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    rainbow_text = ""
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        rainbow_text += f"{color}{char}"
    return rainbow_text

def print_skull():
    skull = r"""
           ______
        .-"      "-.
       /            \
      |              |
      |,  .-.  .-.  ,|
      | )(__/  \__)( |
      |/     /\     \|
      (_     ^^     _)
       \__|IIIIII|__/
        | \IIIIII/ |
        \          /
         `--------`
"""
    print(rainbow_text(skull))

def get_channel_id():
    while True:
        try:
            clear_screen()
            channel_id = int(input(rainbow_text("Enter the target channel ID: ")))
            clear_screen()
            print_skull()
            return channel_id
        except ValueError:
            print("INVALID")

def send_message(token, channel_id):
    header = {
        "Authorization": str(token).replace("\n", ""),
        "Content-type": "application/json"
    }

    mentions = " ".join([f"<@{x}>" for x in ID])
    message = f"{mentions} {random.choice(WORDS)}"

    try:
        response = requests.post(
            f"https://discord.com/api/v9/channels/{channel_id}/messages",
            headers=header,
            json={"content": message}
        )
        if response.status_code == 200:
            pass

    except Exception as e:
        pass

if __name__ == "__main__":
    ID = ["victim's id"] # put the nigga's id here LOL

# put the words u want it to say. (make sure to add a "," after every word if u need multiple.)

    WORDS = [
        "PULL UP STII CA STAU IN FATA https://cdn.discordapp.com/attachments/1187655438536282144/1190004749190311936/image.png?ex=65a03949&is=658dc449&hm=ce16dd16318c2b2a673e9a306ceef68827d6d8504fd1b53acedc3810a1a150d5&"
    ]

    header = {}
    channel_id = get_channel_id()

    with open("tokens.txt", 'r') as file:
        tokens = file.read().splitlines()

    with ThreadPoolExecutor(max_workers=len(tokens)) as executor:
        try:
            while True:
                for token in tokens:
                    executor.submit(send_message, token, channel_id)

        except KeyboardInterrupt:
            print("\nintrerrupted")
