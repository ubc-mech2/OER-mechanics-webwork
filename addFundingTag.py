import os

# set the directory path where the files are located
directory = "OER Mechanics WeBWorK Current Problems"

# iterate over all subdirectories and files with the ".pg" extension
for subdir, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".pg"):
            file_path = os.path.join(subdir, file)
            print("Modifying file:", file_path)

            # open the file in read mode and read its contents
            with open(file_path, 'r', encoding='utf-8') as f:
                file_contents = f.read()

            # replace the two lines with the new text
            new_text = "## This work was supported by funding from the BCcampus \n## Hewlett Foundation Funding (https://bccampus.ca/2021/04/07/hewlett-foundation-funding-announcement/).\n## Common Core Curriculum Engineering Grant (https://www.bccat.ca/articulation/committees/engineering).\n## ZTC (Zero Textbook Cost) Project for STEM (https://bccampus.ca/projects/open-education/zed-cred-z-degrees/ztc-open-educational-resources-for-stem/).\n## UBC OER Fund Implementation Grant (https://oerfund.open.ubc.ca/oer-implementation-grants/)."
            file_contents = file_contents.replace("## This work was supported by funding from the BCcampus \n## ZTC (Zero Textbook Cost) Project for STEM (https://bccampus.ca/projects/open-education/zed-cred-z-degrees/ztc-open-educational-resources-for-stem/).", new_text)

            # open the file in write mode and write the modified contents back to the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(file_contents)
