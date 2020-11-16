import shutil
import glob, os
import re

import zipfile
os.chdir(r"C:\Users\ptemm\Downloads\Oct 22 Notion Exports\Oct 22 Notion Exports\Multiple Choice")
filename=[]
count=1
for file in glob.glob("*.zip"):
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(r'C:\Users\ptemm\OneDrive\Testing2')

print('\\')
imgline='![STATICS-MPA03%2001%2004%20(Combined)%20a9d6c642c3cb4f6baf82164ce81c5744/Untitled%203.png](STATICS-MPA03%2001%2004%20(Combined)%20a9d6c642c3cb4f6baf82164ce81c5744/Untitled%203.png)'
m = re.search("\/(.*?)\.", imgline)
imgname=m.group(1)
print(imgname)
print(m.group(1))
if '%' in imgname:
    print('ok')
    delete=0
    #m = re.search('(?<=\%)\w+', imgname)
   # print(m.group(1))
    imgname=imgname.split('%',1)[0]
    print(imgname)



#imgname=r'C:\Users\ptemm\OneDrive\Documents\screeenshot111222.png'
#originpath=r"C:\Users\ptemm\Downloads\Oct 22 Notion Exports\Oct 22 Notion Exports\Numerical Fill in the Blank\Export-05ae4491-17cb-472b-9b61-2e8ad127893c\STATICS-CMC08 02 01 b8bf07b19b1749d9809d0c0f98b1cc05\Untitled.png"
newpath=''

#os.rename(originpath,imgname)
#.move(imgname,r"C:\Users\ptemm\OneDrive\Desktop\Picturespython" )

#go into downloaded file->filename->
#rename/move picture
#put picturename+count