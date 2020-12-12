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
 
filelocation=r'C:\Users\ptemm\Downloads\Module 1 Dec 2\GE 124 Question Database - Module 1 c7df8e2393214b0a9d40fca105b01948\Module 1 Manual Changes'
newfilelocation=r'C:\Users\ptemm\Downloads\Module 1 Dec 2\GE 124 Question Database - Module 1 c7df8e2393214b0a9d40fca105b01948'
os.chdir(filelocation)
#f1=os.listdir(r'C:\Users\ptemm\Downloads\Dec 1 Module 2 Questions\GE 124 Question Database - Module 2 b93ac1f22a354b71bb477fc66b46d9f2\New Images')
#f2=os.listdir(r'C:\Users\ptemm\Downloads\Usask Images (2)')
#copy=0
#print(f1)
#print(f2)
#with open('imglist4.txt', 'w') as f:
    #for n in range(len(f1)):
        #copy=0
        #if f1[n] not in f2:
            #line=f1[n].replace(' ','-')
            #f.write(f1[n]+'\n')
file=r'C:\Users\ptemm\Downloads\Dec 2 Module 3\GE 124 Question Database - Module 3 795ce0a4330f418baa3d485f72bcf63b\STATICS-DSF06-01-01-6eb6489cd59e4183b8f028d3d1274ab0.pg'           
#for file in glob.glob("*.pg"):
with open(file,'r') as f:
    ln = f.readlines()
    data=''
    for i, line in enumerate(ln): 

        line=line.replace(r'\(',r'[`')
        line=line.replace(r'\)',r'`]')

        data=data+line
       #if '.png' in line: 
           #m=re.search('\"(.*?)\"',line)
           #newimgname=m.group(1)
           #try:
                  #originpath=newfilelocation+"\\"+newimgname
                  #with Image.open(originpath) as img:
                      #width, height = img.size;
                      #imgscale=1
                      #if height>500:
                          #imgscale=500/height

                      #width=width*imgscale
                      #height=height*imgscale
                      #line=re.sub('width=>(.*?),',r'width=>'+str(width)+',',line)
                      #line=re.sub('height=>(.*?)\)',r'height=>'+str(height)+')',line)
                      #print(line)
           #except:
                  #pass  
    #data=data+line
with open(file,'w') as f:
  f.write(data)        
   
#count=1
#problemcount=0;
#problemset=''
#setcount=0
#newimglocation=r'C:\Users\ptemm\Downloads\Dec 1 Module 2 Questions\GE 124 Question Database - Module 2 b93ac1f22a354b71bb477fc66b46d9f2\New Images'
#file2=os.listdir(newimglocation)
#oldimglocation=r'C:\Users\ptemm\Downloads\Dec 1 Module 2 Questions\GE 124 Question Database - Module 2 b93ac1f22a354b71bb477fc66b46d9f2\Past Images'
#print(file2)
#with open('mod2imagetracker.txt', 'w') as f2:
    #for file in glob.glob("*.png"):
        #name=file[:19]
        #for i in range(len(file2)):
            #if name in file2[i] and '-G' not in file2[i]:
                ##moveoldfile
                #oldimgoriginpath=filelocation+"\\"+file
                #oldimgnewpath=oldimglocation+"\\"+file
                #try:
                    #os.rename(oldimgoriginpath,oldimgnewpath)
                    #newimgoriginpath=newimglocation+"\\"+file2[i]
                    #os.rename(newimgoriginpath,oldimgoriginpath)
                #except:
                    #pass
            #else:
                #f2.write(file+'\n')

for file in glob.glob("*.png"):
    filename=file.replace(' ','-')
    newname=filelocation+'\\'+filename
    newimgname=filename+'.png'
    originpath=filelocation+"\\"+file
    try:
        os.rename(originpath,newname)
        print(newname)
    except:
        pass




#imgname=r'C:\Users\ptemm\OneDrive\Documents\screeenshot111222.png'
#originpath=r"C:\Users\ptemm\Downloads\Oct 22 Notion Exports\Oct 22 Notion Exports\Numerical Fill in the Blank\Export-05ae4491-17cb-472b-9b61-2e8ad127893c\STATICS-CMC08 02 01 b8bf07b19b1749d9809d0c0f98b1cc05\Untitled.png"
newpath=''

#os.rename(originpath,imgname)
#.move(imgname,r"C:\Users\ptemm\OneDrive\Desktop\Picturespython" )

#go into downloaded file->filename->
#rename/move picture
#put picturename+count