import os
import shutil

def file_organizer():
    path = input("Enter Folder : ")
    new_folder = os.path.join(path, "JPG Images")

    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):

            if file.lower().endswith(".jpg"):
                shutil.move(file_path, new_folder)
                print(f"{file} moved to JPG Images")
file_organizer()