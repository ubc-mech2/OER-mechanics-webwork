import shutil
import glob, os
import re

import zipfile
filelocation=r'C:\Users\ptemm\Downloads\Dec 1 Module 2 Questions\GE 124 Question Database - Module 2 b93ac1f22a354b71bb477fc66b46d9f2'
os.chdir(filelocation)
filename=[]
count=1
problemcount=0;
problemset=''
setcount=0
newimglocation=r'C:\Users\ptemm\Downloads\Dec 1 Module 2 Questions\GE 124 Question Database - Module 2 b93ac1f22a354b71bb477fc66b46d9f2\New Images'
file2=os.listdir(newimglocation)
oldimglocation=r'C:\Users\ptemm\Downloads\Dec 1 Module 2 Questions\GE 124 Question Database - Module 2 b93ac1f22a354b71bb477fc66b46d9f2\Past Images'
print(file2)
with open('mod2imagetracker.txt', 'w') as f2:
    for file in glob.glob("*.png"):
        name=file[:19]
        for i in range(len(file2)):
            if name in file2[i] and '-G' not in file2[i]:
                #moveoldfile
                oldimgoriginpath=filelocation+"\\"+file
                oldimgnewpath=oldimglocation+"\\"+file
                try:
                    os.rename(oldimgoriginpath,oldimgnewpath)
                    newimgoriginpath=newimglocation+"\\"+file2[i]
                    os.rename(newimgoriginpath,oldimgoriginpath)
                except:
                    pass
            else:
                f2.write(file+'\n')
#for file in glob.glob("*.png"):
  #filename=file.replace(' ','')
  #newname=filelocation+'\\'+filename
  #newimgname=filename+'.png'
  #originpath=filelocation+"\\"+file
  #os.rename(originpath,newname)




#imgname=r'C:\Users\ptemm\OneDrive\Documents\screeenshot111222.png'
#originpath=r"C:\Users\ptemm\Downloads\Oct 22 Notion Exports\Oct 22 Notion Exports\Numerical Fill in the Blank\Export-05ae4491-17cb-472b-9b61-2e8ad127893c\STATICS-CMC08 02 01 b8bf07b19b1749d9809d0c0f98b1cc05\Untitled.png"
newpath=''

#os.rename(originpath,imgname)
#.move(imgname,r"C:\Users\ptemm\OneDrive\Desktop\Picturespython" )

#go into downloaded file->filename->
#rename/move picture
#put picturename+count