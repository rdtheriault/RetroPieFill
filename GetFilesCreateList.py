#!/usr/bin/env python
from __future__ import print_function
import os
import shutil


###### Change these variable to suit your needs ######

#path = "" #this is for Linux
path = '/Users/theriaultr/Downloads/NES_655_ROMS/NES_655_ROMS/' #this is for Windows
path2 = "/Users/theriaultr/Downloads/NES_655_ROMS/GameOnly"
fileName = "list.txt"

#grap the folders
folders = os.listdir(path)
#create the file
f= open(fileName,"w+")

#move files out of subfolders.
for folder in folders:
  files = os.listdir(path+folder)
  #renames files
  for name in files:
    os.rename(path+folder+"/"+name, path+folder+"/"+name.replace(" ", ""))
  #grab new names and move them
  files = os.listdir(path+folder)
  for name in files:
    shutil.move(path+folder+"/"+name, path2)


#grap the file names
files2 = os.listdir(path2)

#iterate through files adding to list
for name in files2:
  print(name)
  #f.write("This is line %d\r\n" % (i+1))
  f.write(name+"\r\n")

f.close()
