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


 
filelocation=r'C:\GitHub\OER-mechanics-webwork\USask Questions\Module 2'
newfilelocation=r'C:\GitHub\OER-mechanics-webwork\USask Questions\Module 2 Images'
os.chdir(filelocation)
          
for file in glob.glob("*.pg"):
        with open(file,'r',encoding='utf-8') as f:
                lines = f.readlines()
                data=''
                for i, line in enumerate(lines):
                        if '.png' in line: 
                                print(line)
                                m=re.search('\"(.*?)\"',line)
                                newimgname=m.group(1)
                                print(newimgname)
                                try:
                                        originpath=newfilelocation+"\\"+newimgname
                                        with Image.open(originpath) as img:
                                                width, height = img.size;
                                                imgscale=1
                                                if height>500:
                                                        imgscale=500/height
    
                                                        width=width*imgscale
                                                        height=height*imgscale
                                                        line=re.sub('width=>(.*?),',r'width=>'+str(width)+',',line)
                                                        line=re.sub('height=>(.*?)\)',r'height=>'+str(height)+')',line)
                                                        print(line)
                                except:
                                        pass  
                        data=data+line
        with open(file,'w',encoding='utf-8') as f:
                f.write(data)        
     
