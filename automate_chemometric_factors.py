import os
import pyautogui as pg
from collections import namedtuple
import re
import time

Session = namedtuple('Session', ['rat', 'iti', 'day', 'date', 'dir', 'factor'])
pg.PAUSE = 0.5
cvmatrix_dir = 'C:\\Users\\mroesch\\Desktop\\SaGT_Chemo_Stage\\CVmatrix_2.txt'
concmatrix_dir = 'C:\\Users\\mroesch\\Desktop\\SaGT_Chemo_Stage\\concentrationmatrix_2.txt'

def automate_chemo(jobs):
    if pg.confirm('About to do chemo on ' + str(len(jobs))) == 'Cancel':
        return
    i = 0
    pg.moveTo(x=330,y=1025)
    time.sleep(2)
    for session in jobs:
        if i > 2:
            break
        pg.press('f1')
        pg.press('enter')
        pg.press('tab')
        pg.press('tab')
        pg.typewrite(session.factor)
        pg.press('tab')
        pg.press('enter')
        pg.typewrite(cvmatrix_dir)
        pg.press('enter')
        pg.typewrite(concmatrix_dir)
        pg.press('enter')
        pg.typewrite(session.dir)
        pg.press('enter')
        # this is where the 'GET_DIR' button is on my screen
        # users will need to mess around with the coords to locate
        # where their icon is on their desktop
        pg.moveTo(x=990,y=725)
        pg.click()
        time.sleep(8)
        i += 1
    
    
            

def get_unprocessed_sessions(sessions):
    """
        Get a list of directories you need to do chemo on.
        Makes sure you do not overwrite and do chemo analysis
        on directories that have already been processed by searching
        for the existence of the BATCH_PC folder that chemo produces
    """
    
    jobs = [s for s in sessions for f in os.scandir(s.dir)
            if f.is_dir() and not os.path.exists(s.dir + '\\BATCH_PC')]
    return jobs

def parse_sessions():
    """
        Returns a list of Session tuples. Input file must be formatted
        like the following:
        C:\\Users\\mroesch\\Desktop\\chemo_test_dir\\GS91\\101216_60_Day7\\beh\\20rew20 4
        where the 1st string is the directory to apply chemo and the second is
        the eigenvector to apply (factors).
    """
    
    chemo_dir = 'C:\\Users\\mroesch\\Desktop\\chemo_test_dir\\chemo_factors.txt'
    name_re = re.compile('(GS[\d]{2,3})')
    iti_re = re.compile('120_|60_')
    day_re = re.compile('(Day[\d]{1,2})')
    date_re = re.compile('([0-1]\d[0-3]\d1\d)') # ie 120516
    sessions = []
    with open(chemo_dir, 'r') as f:
        for line in f:
            line = line.rstrip()
            info = line.split(' ')
            name = name_re.search(info[0])
            iti = iti_re.search(info[0])
            day = day_re.search(info[0])
            date = date_re.search(info[0])
            chemo = info[1]
            if not name or not iti or not day or not date:
                print(line)
                raise ValueError('Invalid line format for chemo')
            sessions.append(Session(name.group(), \
                                    iti.group()[0:-1], \
                                    day.group(), \
                                    date.group(), \
                                    info[0], \
                                    chemo))
    return sessions
            

if __name__ == "__main__":
    sessions = parse_sessions()
    jobs = get_unprocessed_sessions(sessions)
    automate_chemo(jobs)
    
    
    
