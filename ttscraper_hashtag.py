import time
import pyautogui
import pyperclip
import random

# DON'T RUN THIS FILE! RUN DOWNLOADER.PY

# FUNCTION THAT AUTOMATES COPYING AND PASTING LINKS TO THE LIST OF SCRAPED TIKTOKS
# The tripleClick(x,y) OR click(x,y) functions click those pixels on your screen, if the bot is missing something on your screen simply change them.
def scrapeVideos(query, amount, lst):
    time.sleep(5)
    pyautogui.tripleClick(480,50) # THIS CLICKS THE URL INPUT BAR
    pyautogui.write(f'https://www.tiktok.com/tag/{query}') # THIS WRITES THE URL
    pyautogui.hotkey('enter') # THIS PRESSES ENTER ON YOUR KEYBOARD
    time.sleep(3)
    pyautogui.moveTo(1000, 455) # THIS MOVES YOUR CURSOR TO THE VIDEO
    time.sleep(1)
    # THE LOOP BELOW SCROLLS DOWN TO LOAD THE VIDEOS SO THAT YOU CAN SCROLL DOWN TO THEM LATER
    for num in range(0,round(int(amount)/20)):
        pyautogui.scroll(-5000) # THIS SCROLLS TO THE BOTTOM
        time.sleep(random.randrange(2,4))
    pyautogui.scroll(100000) # THIS SCROLLS TO THE TOP
    time.sleep(1)
    pyautogui.scroll(100000) # THIS SCROLLS TO THE TOP AGAIN JUST TO BE SAFE ;)
    time.sleep(1)
    pyautogui.click(356, 429) # THIS CLICKS THE FIRST VIDEO

    # THE LOOP BELOW COPIES THE LINKS OF THE TIKTOKS AND SCROLLS, EVERYTIME ONE LINK IS COPIED THE LOOP REFRESHES
    for num in range(0, int(amount)):
        time.sleep(random.randrange(1,3))
        pyautogui.tripleClick(480,50) # THIS SELECTS THE LINK
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'c') # THIS COPIES THE LINK
        time.sleep(.25)
        lst.append(pyperclip.paste()) # THIS PASTES THE LINK INTO A LIST
        time.sleep(1)
        pyautogui.click(1343,588) # THIS CLICKS THE ARROW TO SCROLL DOWN A TIKTOK
        time.sleep(1)

    pyautogui.click(40, 110) # THIS X'ES OUT OF THE TIKTOK SCREEN

    # SHORTLY AFTER THE LOOP IS DONE THE DOWNLOADER WINDOW WILL OPEN UP
