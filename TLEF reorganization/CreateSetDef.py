# %%

#Description:
# Creates the .def file for the problems in the current folder
# Adds all files to a .tar.gz archive

import os
import fileinput
import tarfile

#using the following header for the .def file
header = """setNumber=Chapter2_UBC_OER_Mechanics
openDate = 1/7/01 at 6:00am
dueDate = 1/20/22 at 6:00am
answerDate = 1/21/23 at 6:00
paperHeaderFile = defaultHeader
screenHeaderFile = defaultHeader
problemList =\n"""

#intentionally looking only 1 folder deep. pls don't bury folders in folders

cwd = os.getcwd()
print('cwd: ', cwd)
items = os.listdir(cwd)     #all things in cwd
for item in items: 
    if os.path.isdir(item): #only folders in cwd
        FolderName = item   #identified FOLDER to be processed
        content = ""
        #CREATE .DEF FILE FOR FOLDER
        for filename in os.listdir(cwd+'\\'+FolderName):
            if filename.endswith('.pg'):    #adds line per .pg file
                content += 'USask_Statics/' + FolderName + '/' + filename +', 1\n'
        content = header + content          #entire content of .def file
        f = open('set_'+FolderName+'.def','w', encoding='utf-8')    #create new .def file
        f.write(content)                                            #write to file
        f.close()
        #CREATE .TAR.GZ FOR FOLDER
        print(FolderName)
        # with tarfile.open('MegaTarball'+'.tar.gz', 'w:gz') as archive:
        #     archive.format = tarfile.GNU_FORMAT
        #     for i in os.listdir(cwd):
        #         if os.path.isdir(item): #only folders in cwd
        #             archive.add(i)
                
# %%
