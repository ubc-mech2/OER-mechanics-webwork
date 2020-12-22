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

#import re
#from re import sub
#import PIL
#from PIL import Image
#subfolders = [ f.path for f in os.scandir(r'C:\Users\ptemm\OneDrive\Testing Module 1 Usask') if f.is_dir() ]
 
filelocation=r'C:\Users\ptemm\Downloads\Dropbox (9)\OER-Mech Drawings\FINISHED EDITING - students place images that are correct and finished here (from outbox)'
os.chdir(filelocation)


for file in glob.glob("*.png"):
    filename=file.replace(' ','-')
    filename=filename.replace('.png','-UBC.png')
    newname=filelocation+'\\'+filename
    newimgname=filename+'.png'
    originpath=filelocation+"\\"+file
    try:
        os.rename(originpath,newname)
        print(newname)
    except:
        pass



