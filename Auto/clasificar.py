from distutils import extension
import os
import shutil
from unicodedata import name

from_dir = "C:/Users/Edgar Sansores/Downloads"
to_dir = "C:/Users/Edgar Sansores/Videos"

list_of_files = os.listdir(from_dir)

#print(list_of_files)

for filename in list_of_files:
    name,extension = os.path.splitext(filename)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in [".gif",".png",".jpg",".jpeg",".jfif"]:
        path1 = from_dir + "/" + filename
        path2 = to_dir + "/" + "image_file"
        path3 = to_dir + "/" + "image_file" + filename
        
        if os.path.exists(path2):
            print("moviendo " + filename)
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("moviendo " + filename)
            shutil.move(path1,path3)