#Header Addition file Used to add headers to already converted questions. Use this file after converting the questions
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

#User Input
pgfilelocation=r'C:\GitHub\OER-mechanics-webwork\USask Questions\Module 3'#Input the location of webwork questions
mkdownfilelocation=r'C:\GitHub\OER-mechanics-webwork\USask Questions\Module 3 Markdown'#Input the location of markdown files
headerlocation=r'C:\Users\ptemm\Downloads\Usask Header Sample AD-2.txt'#Input the location/path of the header file

os.chdir(mkdownfilelocation)
def headerfiletxt():#determining the header
        with open(headerlocation,'r',encoding='utf-8') as f:
                data=f.read()
        return data

#finding the header               
header=headerfiletxt() 
#Go through each markdown file to find information and modify the header
for file in glob.glob("*.md"):
        header=headerfiletxt()
        pgname=file.replace(' ','-')
        pgname=pgname.rstrip('.md')+'.pg'
        pglocation=pgfilelocation+'\\'+pgname
        print(pglocation)
        with open(file,'r',encoding='utf-8') as f:
                ln = f.readlines()
                for i, line in enumerate(ln): 
                        if 'Author' in line:
                                line=line.split(':',1)[1]
                                header=header.replace('Author()','Author('+line.rstrip('\n')+')')
                        elif 'Keywords' in line:
                                line=line.split(':',1)[1]
                                header=header.replace('KEYWORDS()','KEYWORDS('+line.rstrip('\n')+')')                                
         
         #opening the webwork question copy and replacing the header                  
        with open(pglocation,'r',encoding='utf-8') as f2:
                ln=f2.readlines()
                pgfile=''
                for i, line in enumerate(ln):
                        if 'DESCRIPTION' in line and 'END' not in line:
                                delete=1
                        if delete==1:
                                if 'END' in line and 'DESCRIPTION' in line:
                                        print('30')
                                        delete=0                                 
                        else:
                                pgfile=pgfile+line
                                
                       
                                
        #rewriting the question with the new header                        
        with open(pglocation,'w',encoding='utf-8') as f2:
                f2.write(header+'\n\n\n')
                f2.write(pgfile)