FORMAT FOR SOFTWARE BLURBS:

1. be a .txt file
2. any missing information: leave the link blank, but keep the line break (examples follow)
3. Except for the logo: if there is none, put transparent.png to avoid the "missing file" logo

name of logofile WITH extension 
Name To Be Displayed
github repository link
linuxbrew install line
bioconda install line
docker install line
Description (can be multiple lines)

if you don't have a logo, the format would be the following:

transparent.png
Name To Be Displayed
full github repository link
linuxbrew install line
bioconda install line
docker install line
Description (can be multiple lines)

sample:

arcslogo.png
https://github.com/bcgsc/arcs
ARCS
brew install arcs


Arcs does something something

The script that will take information from the software blurbs file and add it to software-content.html is in the python folder called software.py
