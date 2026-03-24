import os
import csv


# TODO add functionality to save file names in a csv file with other details such as file size

with open("files.txt", "w") as f:
    for file_name in os.listdir():
        f.write(f"{file_name}  |    {os.path.getsize(file_name)}\n")




