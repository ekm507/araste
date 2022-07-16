#!/usr/bin/python3
# Made By Nima Fanniasl, smartnima.com - July 16 2022 :)
import os
import argparse
import requests
import pwd

def Main():
    parser = argparse.ArgumentParser(description="Get Fonts For Araste")
    parser.add_argument("Font_name", type=str, help="Font Name, Like: aipara")
    args = parser.parse_args()
    font_name = args.Font_name
    font_dir = get_font_dir()
    download_file_from_github(font_name, font_dir)

def get_font_dir():
    root_font_dir = '/usr/share/araste/fonts/'
    usr_font_dir = os.path.expanduser('~') + '/.local/share/araste/fonts/'
    font_dir = ''
    if os.path.exists(root_font_dir):
        font_dir = root_font_dir
        if pwd.getpwuid(os.getuid())[0] != "root":
            print("Araste is installed as root, so use sudo for installing fonts, Like: sudo araste_get font")
            exit(1)
    elif os.path.exists(usr_font_dir):
        font_dir = os.path.realpath(usr_font_dir)
    else:
        print("Font Folder Dosn't Exist, Is Araste Installed?\nIf The Tool Is Not Working Make An Issue On Github: https://github.com/ekm507/araste")
        exit(1)
    return font_dir

def download_file_from_github(font_name, font_dir):
    if f"{font_name}.flf" in os.listdir(font_dir):
        print(f"{font_name} already exists.")
        exit(0)
    else:
        print(f"Downloading Font: {font_name}")
        url = f"https://raw.githubusercontent.com/ekm507/araste-fonts/main/Fonts/{font_name}.flf"
        r = requests.get(url)
        if r.status_code != 404:
            with open(f"{font_dir}/{font_name}.flf", "wb") as f:
                f.write(r.content)
            print(f"{font_name} Font Downloaded :)")
        else:
            print(f"{font_name} Font Not Found :(")
            exit(1)

if __name__ == "__main__":
    Main()
