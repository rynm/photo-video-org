# photo-vid-org-and-dupli
Photo and video file by-date organizer with duplication detection. Nothing is deleted, a new folder with cleaned items and another folder with the duplicated items are created. A clear output log is shown on what files were kept in the clean or placed in the duplicated folder if there was a hash conflict.

Requirements: Python 3.x

Usage: 

`python dupli.py <folder 1> <folder 2> ... <folder n> `  
   
All files in all folders are recursively hashed and compared with all other files in the other folders. This detects duplicates are places them into the folder "deletedpics". All other files are placed in "cleanpictures" and all photos and videos are placed in a folder corresponding to either the date embedded in the name of the file or the last modified time of the file, in the case of there being no date in the name of the file.  

This software has been tested many times with hundreds of gigabytes of test files. 

One known issue: 
Do not use an input folder path with an underscore in any folder name. An underscore could be present in file names. 

One manual required before running: 
Set the absolute output path of the two output folders. I did not get around to adding an input switch for this. It is currently both set to `F:\cleanpictures` and `F:\deletedpics`.  
  
This script can work with any file type not just images and video. Once again, nothing is deleted.

## Sample output
Input folder `test` contains four dirs as listed in the scan below including two copies.  
Execute: `python dupli\dupli.py test`  
  
Output: The folders are created based on image dates, in this case embedded in the file name as Apple stores its images. `F:\cleanpictures\2020 Oct 20`, and `F:\cleanpictures\2018 Nov 13` are created. If the date is not stored in this format in the file name, the image date for its folder will be taken from the modified time of the image or video. All of the duplicate images 'tossed' as indicated below are found in `F:\deletedpics`.  


~~~
F:\>python dupli\dupli.py test
Scanning test...
Scanning test\1...
Scanning test\1 - Copy...
Scanning test\2...
Scanning test\2 - Copy...
___________________
Keeping test\1\2018-11-13_16-57-18_434.jpeg
Tossing test\1 - Copy\2018-11-13_16-57-18_434.jpeg
___________________
___________________
Keeping test\1\2018-11-13_20-24-26_568.jpeg
Tossing test\1 - Copy\2018-11-13_20-24-26_568.jpeg
___________________
___________________
Keeping test\1\2018-11-13_20-24-26_669.jpeg
Tossing test\1 - Copy\2018-11-13_20-24-26_669.jpeg
___________________
___________________
Keeping test\2\2020-10-20_14-26-19_632 - Copy.heic
Tossing test\2\2020-10-20_14-26-19_632.heic
___________________
~~~


