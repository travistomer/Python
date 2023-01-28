import string
from ctypes import windll

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1
    return (drives)

get_drives()
print(get_drives())


import os
# ASCII codes 65 to 90 correspond to the letters A-Z. 
drives_alt = [ chr(x) for x in range(65,91) if os.path.exists(chr(x) + ":") ]
print(drives_alt)

# Same as list comprehension method above
def get_drives_alt_2():
    drives = []
    for x in range(65,91):
        if os.path.exists(chr(x) + ':'):
            drives.append(chr(x))
    return(drives)

print(get_drives_alt_2())


