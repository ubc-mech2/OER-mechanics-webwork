#Description:
#Adds an image reference, its height, and its width to a .pg file that doesn't have any if an associated .png file with the same name is present.
#Does not work if a .pg file requires multiple images
#Updates the height and width of the image on a .pg file if the reference already exists
#If the reference is incorrect, it gets updated as well.
#Files that have been processed are added to a folder in the directory.
#The folder's name can be changed by changing the variable 'folderName' below.

#How to use:
#Drop this .py file in a directory where image references in a .pg files have to be added or updated (such as when a new image has been created or its dimensions changed).
#Ensure that all applicable problems have corresponding images with matching filenames.
#Also ensure that evert image is a .PNG.
#Run this script.
#Collect the updated .pg files in a newly created folder.

import os
import re
import codecs
import shutil
from PIL import Image

folderName = "newPGs";

#directory for converted files
if not os.path.exists(folderName): 
    os.makedirs(folderName)
else:
	shutil.rmtree(folderName) #remove old directory
	os.makedirs(folderName)

cwd = os.getcwd(); #current working directory
directory = os.listdir(os.getcwd());
fileList = list();

for filename in directory:
    if (filename.endswith(".pg")):
        fileList.append(filename);

print("{} .pg files found.".format(len(fileList)));

for file in fileList:
	imageName = file[:-3] + ".png";

	try:
		#do stuff if .pg file has associated image
		with Image.open(imageName) as img:
			width, height = img.size;
			imgScale = 0.35;
			print(width,height)

		try:
			f = codecs.open(file, 'r', encoding='utf-8');

			content = f.read();
			contentLC = content.lower();

			#if image tag doesnt exist, add one at the very beginning
			imgStart = contentLC.find("image(");
			if (imgStart == -1):
				pgmlLoc = content.find("BEGIN_PGML") + len("BEGIN_PGML");

				imageTag = "[@ image(\"" + imageName + "\", width=>[$width], height=>[$height]) @]*";

				content = content[:pgmlLoc] + "\n\n"+ imageTag + content[pgmlLoc:];

			#if there is one, make sure it matches the filename
			else:
				imgEnd = contentLC.find(")",imgStart);

				imageName = contentLC[imgStart+len("image("):imgEnd];
				imageName = imageName.replace(" ","");

				secondQuoteIndex = imageName.find("\"",1);
				if secondQuoteIndex == -1:
					print(file,imageName)

				imageName = imageName[1:secondQuoteIndex];
				ext = imageName[-4:];

				newImageName = file.replace(".pg",ext);

				toReplace = re.findall(imageName,content,re.IGNORECASE);
				content = content.replace(toReplace[0],newImageName);

			#if the variable imgScale exists
			startScale = content.find("$imgScale");
			if (startScale == -1):
				docLoc = content.find("DOCUMENT();") + len("DOCUMENT();");

				imgVars = "#image scale\n$imgScale = 1;\n\n#image aspect ratio\n$width = $imgScale*" + str(width) + ";\n$height = $imgScale*" + str(height) + ";";

				content = content[:docLoc] + "\n\n"+ imgVars + content[docLoc:];

			#if it doesn't, change the widths and heights
			else:

				startImg = content.find("$imgScale");
				startImg = content.find("=", startImg);
				endImg = content.find(";", startImg);

				content = content[:startImg + 1] + str(imgScale) + ";" + "\n\n" + "$height = $imgScale*" + str(height) + ";" + "\n\n" + "$width = $imgScale*" + str(width) + content[endImg:];

			#write file
			newPG = codecs.open(folderName + "\\" + file, 'w', encoding='utf-8');
			newPG.write(content);
			newPG.close();

			f.close();

		except:
			pass;
	except:
		pass;

input();

