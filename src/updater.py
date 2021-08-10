import urllib.request
import os

def check_version():
    try:
        version = urllib.request.urlopen(
            "https://github.com/C-ffeeStain/SchoolTest/blob/main/VERSION"
        ).read()
        version = version.decode("utf-8")
        with open("VERSION", "r") as f:
            old_version = f.read()
        if version != old_version:
            print("New version available!")
            print("Updating!")
            with open("VERSION", "w") as f:
                f.write(version)
            
            urllib.request.urlretrieve("https://github.com/C-ffeeStain/SchoolTest/releases/latest/SchoolTest.exe", "updater.py")

    except urllib.error.URLError:
        print("Couldn't check for updates. No internet connection?")
