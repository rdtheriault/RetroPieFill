#!/usr/bin/env python
from __future__ import print_function
import os
import shutil
import zipfile


###### Change these variable to suit your needs ######

#path = "" #this is for Linux
path = '/home/administrator/Mameroms/MAME 0.151 ROMs'
path2 = "/home/administrator/gameonly"
fileName = "list.txt"

#grap the folders
files = os.listdir(path)
#create the file
f= open(fileName,"w+")
#grab the new folders
folders = os.listdir(path2) #files in new location

#move files out of subfolders.
for file in files:
  name = file.replace(".zip","")
  #if zip is not done and if it is a zip
  if name not in folders and ".zip" in file:
    with zipfile.ZipFile(path+"/"+file,"r") as zip_ref:
      zip_ref.extractall(path2+"/"+name)

#rename folders
for name in folders:
  os.rename(path2+"/"+name, path2+"/"+name.replace(" ", ""))
  #shutil.move(path+folder+"/"+name, path2)


#grap the file names
files2 = os.listdir(path2)

#iterate through files adding to list
for name in files2:
  print(name)
  #f.write("This is line %d\r\n" % (i+1))
  f.write(name+"\r\n")

f.close()
