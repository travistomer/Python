# Tool to detect SD card and auto transfer to Photos folder
# Thoughts: Create UI, have UI clickable paths, store in persistent storage, copy items button, use settings from persistent storage to monitor designated folders and alert when detected or auto move

# Imports
from datetime import date
import os, shutil

### VARS
ROOT_PATH_TO_MOVE_PHOTOS_TO = "D:\zPhotoVideo\Photography"

drives_to_avoid_looking_in = [
    "C",
    "D"
]

files_types_to_move = [ # IS THIS NEEDED? Checking file exts is slow
    "jpg",
    "arw",
]

folders_to_look_for = [
    "DCIM"
]

### END VARS


### FUNCS
# Get a list of drives that are not in drives_to_avoid_looking_in.   
def get_drives():
    return [ chr(x) + ":" for x in range(65,91) if os.path.exists(chr(x) + ":") and chr(x) not in drives_to_avoid_looking_in] # range(65,91) gets the A-Z in ASCII.

# Get date in format "MM_YYYY" SHOULD I GET IT FROM THE PHOTO FILES? Probably...
def get_date():
    today = date.today()
    return f"{today.month}_{today.year}"

# Build the path to copy photos to
def build_copy_to_path(root_path, date):
    return f"{root_path}\{date}"

# Get list of immediate sub directories matching {folders_to_look_for}
def get_subdirectories(root_path):
    listOfSubDirs = next(os.walk(root_path))[1]
    return([ z for z in listOfSubDirs if z in folders_to_look_for])

# Find and return the path where photos reside on external drive.
def find_photos_path():
    list_of_paths_to_copy_from = []
    # Loop through drives
    for drive in get_drives():
        # Get subdirs
        list_of_matching_subdirs = get_subdirectories(drive)

        # Build pasths and append
        for dir in list_of_matching_subdirs():
            finalized_path = f"{drive}\{dir}"
            list_of_paths_to_copy_from.append(finalized_path)

    return list_of_paths_to_copy_from

# For copying the files
def copy_files(copy_from, copy_to):
    shutil.copy(copy_from, copy_to)

### END FUNCS


### MAIN PROGRAM
if __name__ == "__main__":
    # Setup
    drives = get_drives() 
    date = get_date()
    copy_to_path = build_copy_to_path(ROOT_PATH_TO_MOVE_PHOTOS_TO, date)

    # Meat
    #copy_files("E:DCIM\100MSDCF", copy_to_path)
    print(os.path.exists("E:\DCIM\100MSDCF"))


    
