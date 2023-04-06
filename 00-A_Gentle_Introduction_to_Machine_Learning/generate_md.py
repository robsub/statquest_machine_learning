import os

directory = "/Users/rob/Learning/statquest/00_-_A_Gentle_Introduction_to_Machine_Learning"

with open("images.md", "w") as f:
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            f.write("![{}](./{})\n".format(filename, filename))

