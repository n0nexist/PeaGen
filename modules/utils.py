import os
from rich import print
import ctypes

def clear():
    os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def set_window_title(title):
    try:
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    except:
        pass

def removedoublelines(filepath):
    print("[reset][green][[bold white]+[reset][green]] [bold white] Removing double lines from saving file...")
    f = open(filepath,"r")
    lines = list()
    s = ""
    for x in f.readlines():
        if x not in lines:
            lines.append(x)
    f.close()
    for x in lines:
        s += x
    f = open(filepath,"w")
    f.write(s)
    f.close()

