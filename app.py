import os

print(os.listdir())

with open("files.txt", "w") as f:
    for file_name in os.listdir():
        f.write(f"{file_name}\n")




