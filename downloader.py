from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
from ttscraper_hashtag import scrapeVideos

# ENTER THE PATHS TO THESE ITEMS AND SAVE THEM IN THE FILE (IF YOU NEED HELP LET ME KNOW)
driver_path = "C:/Users/19843/Desktop/YoutubeShortsMethods/YoutubeShortsMethods/mr.sponge_rip/tiktokscraper/chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
path_to_extension = "C:/Users/19843/AppData/Local/Google/Chrome/User Data/Default/Extensions/gighmmpiobklfepjocnamgkkbiglidom/4.46.2_0"

#CHROME SETTINGS
option = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
option.binary_location = brave_path
option.add_argument('load-extension=' + path_to_extension)

# GETS INPUTS
query_name = input("Choose the hashtag you would like to scrape from TikTok: ")
amount_count = input("Choose the amount of links you want to save: ")

# EMPTY LIST LEFT FOR TITLES TO BE PUT IN 
titles = []

# EMPTY LIST LEFT FOR TITKTOK LINKS TO BE PUT IN 
tiktok_list = []

#THE DOWNLOADING LOOP
def download(lst):
    # Creates new Instance of Chrome
    driver = webdriver.Chrome(executable_path=driver_path, options=option)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.get('https://snaptik.app/en-us')

    time.sleep(1.5)
    driver.switch_to.window(driver.window_handles[0])

    number = 0
    for i in lst:

        driver.get('https://snaptik.app/en-us')
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])

        # Finds url box and pasted user's input then submits
        url_field = driver.find_element_by_id('url')
        url_field.send_keys(i)
        url_field.submit()

        time.sleep(3)

        # Finds possible title for the video
        try:
            title = driver.find_element_by_xpath('/html/body/main/section[2]/div/div/article/div[3]/p[1]/span').text
            print(title)

            if title.count("#") > 0:
                titles.append(title)
                titles[number] = title[0:title.index('#')]
                number += 1
            else:
                titles.append(title)
                number += 1

            if titles[number-1] == '':
                titles[number-1] = f"Invalid Name"
                
            banned_characters = '<>:"/\|?*'
            for character in banned_characters:
                if title.count(character) > 0:
                    titles[number-1] = f"Invalid Name"
        except:
            titles.append(f'Failed Title Grab Nr. {number}')
            number+=1
            print(f'Download nr. {number} raised an exception.')

        # Clicks the download button
        try:
            download_button = driver.find_element_by_xpath('/html/body/main/section[2]/div/div/article/div[2]/div/a[1]')
            time.sleep(2.5)
            download_button.click()
        except:
            print(f'Download nr. {number} raised an exception.')
            pass

        # Name and save file
        time.sleep(1.5)
        pyautogui.typewrite(f"{number} {titles[number-1]}")
        time.sleep(0.5)
        pyautogui.hotkey("enter")

        # print successful for UI
        time.sleep(1)
        print(f'DOWNLOAD NR. {number} SUCCESFULL')

scrapeVideos(query_name, amount_count, tiktok_list)
download(tiktok_list)