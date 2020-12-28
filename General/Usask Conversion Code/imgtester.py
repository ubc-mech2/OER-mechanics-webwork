import re
import sys
import codecs
import xml.etree.ElementTree as ET
import os
import shutil
import random
from re import sub
import os
import shutil
import glob, os
import PIL
from PIL import Image


#input file location/ path below
filelocation=r'C:\Users\ptemm\Downloads\Dropbox (9)\OER-Mech Drawings\FINISHED EDITING - students place images that are correct and finished here (from outbox)'
os.chdir(filelocation)

#Renaming files
for file in glob.glob("*.png"):
    filename=file.replace(' ','-')
    newname=filelocation+'\\'+filename
    newimgname=filename+'.png'
    originpath=filelocation+"\\"+file
    try:
        os.rename(originpath,newname)
        print(newname)#displaying the new name of files
    except:
        pass



