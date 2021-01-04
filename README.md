# photo-vid-org-and-dupli
Photo video by-date organizer with duplication detection. Nothing is deleted, a new folder with cleaned items and another folder with the duplicated items are created. 

Use python 3.x

Usage: 

python dupli.py <folder 1> <folder 2> ... <folder n> 
  
All files in all folders are recursively hashed and compared with all other files in the other folders. This detects duplicates are places them into the folder "deletedfiles". All other files are placed in "cleanedfiles" and all photos and videos are placed in a folder corresponding to either the date embedded in the name of the file or the last modified time of the file, in the case of there being no date in the name of the file.
