import time
from playsound import playsound
user = input("Enter Username Here >>  ")
length = int(input("Enter Desired Length of Follow Checking (\"1440\" is 24 hours)>>  "))
followers_arch = 0

def play_pacer_sound():
#copy the directory of your sound below! (download the sound to your computer or it wont work!!)
    playsound("put file direcotry here, inside the quotations")

cycles = 0
while cycles < length:
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys

    path = "/usr/bin/safaridriver"
    driver = webdriver.Safari(executable_path=path)
    driver.set_window_size(720, 1080)
    driver.get(f"https://tiktok.com/@{user}")

    page_info = driver.page_source
    loc = page_info.find("\"fans\":")

    followers_ = page_info[loc + 7: loc + 16]
    for i in range(0, 9):
        try:
            followers = int(followers_[:-i])
            break
        except:
            pass
    if cycles == 0:
        print(followers)
    elif followers - followers_arch >= 1:
        print(f"{followers} -- New Follower!")
        play_pacer_sound()
    elif followers - followers_arch <= -1:
        print(f"{followers} -- Lost Follower.")

    followers_arch = followers
    
    cycles += 1
    driver.quit()
    time.sleep(20)
