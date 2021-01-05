# dupFinder.py
import os, sys, time, random, datetime
import hashlib, shutil
 
def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder):
        print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            # Calculate hash
            file_hash = hashfile(path)
            # Add or append the file path
            if file_hash in dups:
                dups[file_hash].append(path)
            else:
                dups[file_hash] = [path]
    return dups
 
 
# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
 
 
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
 
def printResults(dict1):

    results = list(filter(lambda x: len(x) > 0, dict1.values()))
    
    for r in results:

        if (os.path.splitext(r[0])[-1] == ".ini" or os.path.splitext(r[0])[-1] == ".db" or os.path.splitext(r[0])[-1] == "._.DS_Store" or os.path.splitext(r[0])[-1] == ".THM"):
            continue 

        info = os.path.getmtime(r[0])
        timedir = time.strftime("%Y %b %d", time.gmtime(info))

        a = os.path.splitext(r[0])[0].find("_")
        sa = os.path.splitext(r[0])[0].rfind("\\")
        if (a != -1 and sa != -1):
            # possible date embedded in name, use that instead of mtime if there
            dstr = os.path.splitext(r[0])[0][sa+1:a]
            try:
                d = datetime.datetime.strptime(dstr, '%Y-%m-%d')
                timedir = d.strftime("%Y %b %d")
            except:
                # something unexpected, bail and use the modified time
                pass

        cleandir = 'F:\\cleanpictures\\'+timedir
        deldir = 'F:\\deletedpics\\'+timedir

        if not os.path.exists(cleandir):
            os.makedirs(cleandir)
        if not os.path.exists(os.path.join(cleandir,os.path.basename(r[0]))):
            shutil.copy2(r[0], cleandir)
        else :
            print('%s, file conflict, changing name of file' % r[0]) 
            shutil.copy2(r[0], os.path.join(cleandir, str(random.randint(0,2000))+os.path.splitext(r[0])[-1]))
            

        if len(r) > 1:
            if not os.path.exists(deldir):
                os.makedirs(deldir)
            print('___________________')
            print('Keeping %s' % r[0])
            for x in r[1:]:
                print('Tossing %s' % x)
                if not os.path.exists(os.path.join(deldir,os.path.basename(x))):
                   shutil.copy2(x, deldir)
                else : 
                   print('Looks like there is already a copy in deldir, ignoring: ' + x)
                print('___________________')

 
def main():
    if len(sys.argv) > 1:
        dups = {}
        folders = sys.argv[1:]
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dups
                joinDicts(dups, findDup(i))
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        printResults(dups)
        sys.stdout.flush()
        return 0
    else:
        print('Usage: python dupli.py folder or python dupFinder.py folder1 folder2 folder3')
        return 1


if __name__ == "__main__":
    sys.exit(main()) 
