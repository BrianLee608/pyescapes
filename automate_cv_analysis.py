#!/usr/bin/env python3
from collections import deque
import pyautogui as pg
import os
import time

def cycle_dio_files(path):
    """ cycles  through all the dio files and automates
        the file selection. In cv_analysis.exe, you have to
        manually find the next file. But here, the dio files
        are sorted in increasing order so you simply traverse
        each of your trials with prev or next
    """
    
    dios = deque()
    for f in os.scandir(path):
        if f.is_file() and not f.name.endswith('.txt'):
            dios.append(f.name)
            
    # this is where the cv_analysis icon is on taskbar
    pg.moveTo(x=330,y=1025)
    time.sleep(2)
    
    selection = pg.confirm(buttons=['Prev','Next','Exit'])
    while selection != 'Exit':
        f = dios[0]
        pg.press('f2')
        time.sleep(.5)
        pg.typewrite(f)
        pg.press('enter')
        if selection == 'Prev':
            dios.rotate(1)
        else:
            dios.rotate(-1)
        selection = pg.confirm(buttons=['Prev','Next','Exit'])     

def prompt_dir():
    """ prompts user for dio directory. """
    path = pg.prompt(text='Enter a directory')
    while path:
        cycle_dio_files(path)
        path = pg.prompt(text='Enter another directory or exit')

if __name__ == "__main__":
    prompt_dir()
