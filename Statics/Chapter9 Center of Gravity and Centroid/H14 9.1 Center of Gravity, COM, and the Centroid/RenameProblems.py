# %%

#Description:
#Renames file names for problems (.pg .png and .pdf files)
#and edits .png and .pdf references in the .pg files
#Files that have been processed are added to a folder in the directory.

#How to use:
#Drop this .py file in a directory where the problem files are stored
#Run this script.
#Collect the updated files in a newly created folder.

import os
import fileinput
import shutil

cwd = os.getcwd(); 
directory = os.listdir(os.getcwd());
fileList = list()

if not os.path.exists('renamedProblems'): 
    os.makedirs('renamedProblems')
else:
	shutil.rmtree('renamedProblems') #remove old directory
	os.makedirs('renamedProblems')

print('Processed:')

for filename in directory:
    current_name = os.path.splitext(filename)[0]
    new_name = current_name[0:5]+'CoG'+current_name[-6:]     #EDIT THIS LINE based on what/how to rename files
    
    if (filename.endswith(".pg")):
        print(filename)
        f = open('renamedProblems/'+new_name+'.pg','a+', encoding='utf-8')  #rename .pg file
        with fileinput.FileInput(filename, openhook=fileinput.hook_encoded("utf-8")) as file:
            for line in file:
                f.write(line.replace(current_name, new_name),)              #edit .png and .pdf reference
            f.close()
    elif (filename.endswith(".png")):
        print(filename)
        shutil.copy(filename,'renamedProblems/'+new_name+'.png')            #rename .png file
    elif (filename.endswith(".pdf")):
        print(filename)
        shutil.copy(filename,'renamedProblems/'+new_name+'.pdf')            #rename .pdf file


# %%
