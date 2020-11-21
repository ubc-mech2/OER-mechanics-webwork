import shutil
import glob, os
import re

import zipfile
filelocation=r'C:\Users\ptemm\Downloads\Module 1\GE 124 Question Database - Module 1 c7df8e2393214b0a9d40fca105b01948'
os.chdir(filelocation)
filename=[]
count=1
problemcount=0;
problemset=''
setcount=0
for file in glob.glob("*.png"):
  filename=file.replace(' ','')
  newname=filelocation+'\\'+filename
  newimgname=filename+'.png'
  originpath=filelocation+"\\"+file
  os.rename(originpath,newname)




#imgname=r'C:\Users\ptemm\OneDrive\Documents\screeenshot111222.png'
#originpath=r"C:\Users\ptemm\Downloads\Oct 22 Notion Exports\Oct 22 Notion Exports\Numerical Fill in the Blank\Export-05ae4491-17cb-472b-9b61-2e8ad127893c\STATICS-CMC08 02 01 b8bf07b19b1749d9809d0c0f98b1cc05\Untitled.png"
newpath=''

#os.rename(originpath,imgname)
#.move(imgname,r"C:\Users\ptemm\OneDrive\Desktop\Picturespython" )

#go into downloaded file->filename->
#rename/move picture
#put picturename+count