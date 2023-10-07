import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.alert import Alert
import time
from threading import Thread, Barrier
import random
import string
import os

def big_clock():
    start_time = time.time() # Get the start time
    while True:
        # Calculate the time elapsed
        elapsed_time = time.time() - start_time
        days = int(elapsed_time // (24 * 3600))
        hours = int((elapsed_time // 3600) % 24)
        minutes = int((elapsed_time // 60) % 60)
        seconds = int(elapsed_time % 60)
        # Convert time values to strings and add leading zeros if needed
        days_str = str(days).zfill(3)
        hours_str = str(hours).zfill(2)
        minutes_str = str(minutes).zfill(2)
        seconds_str = str(seconds).zfill(2)
        # Create the clock string
        clock = f"{days_str}:{hours_str}:{minutes_str}:{seconds_str}"
        # Print the clock string
        print(clock, end="\r", flush=True)
        # Wait for 1 second
        time.sleep(1)

# Random browser language
def get_random_language():
    # List of common language codes
    languages = ['en-US', 'fr-FR', 'de-DE', 'zh-CN', 'ja-JP', 'es-ES', 'ru-RU']
    # Choose a random language from the list
    random_language = random.choice(languages)
    return random_language

# Random browser timezone
def get_random_timezone():
    # Get a list of all timezones in pytz
    timezones = ['US/Pacific', 'US/Mountain', 'US/Central', 'US/Eastern', 'Canada/Pacific', 'Canada/Mountain', 'Canada/Central', 'Canada/Eastern']

    # get a random timezone from the list
    random_timezone = random.choice(timezones)
    return random_timezone

# Random browser window size
def get_random_window_size():
    width = random.randint(1024, 1920)
    height = random.randint(768, 1080)
    return f"{width}x{height}"

# Random name for chrome profile
def random_name():
    # list of possible names
    names = ["John", "Emily", "Jessica", "Jacob", "Michael", "Madison", "Matthew", "Nicholas", "Andrew", "Emily", "Kars", "Wamuu", "Seras", "Issac", "Netero", "Baki", "Jack", "Yujiro", "Straidam", "Merum", "Endeavor", "Trefort", "Pitoo", "Susano", "Rengoku", "Enji", "Toya"]
    # list of possible last names
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Jhony", "Wilson", "Moore", "Taylor", "Kyogero", "Hanma", "Avdol", "Fumikage", "Todoroki"]
    # randomly select a name and last name
    name = random.choice(names)
    last_name = random.choice(last_names)
    # generate a random string of characters and numbers as a suffix
    suffix = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    # return the generated name
    return name + "_" + last_name +''+ suffix

# Random user agent for browser
def get_random_user_agent():
    systems = ['Windows', 'Macintosh', 'X11']
    browsers = ['Chrome', 'Firefox', 'Safari']
    system = random.choice(systems)
    browser = random.choice(browsers)
    if system == 'Windows':
        os_version = 'Windows NT ' + str(random.randint(5, 10)) + '.' + str(random.randint(0, 2))
    elif system == 'Macintosh':
        os_version = 'Intel Mac OS X 10_' + str(random.randint(12, 15)) + '_' + str(random.randint(0, 9))
    elif system == 'X11':
        os_version = 'X11'
    browser_version = browser + '/' + str(random.randint(50, 70)) + '.' + str(random.randint(0, 9)) + '.' + str(random.randint(1000, 10000))
    return "Mozilla/5.0 (" + os_version + "; rv:" + str(random.randint(50, 70)) + "." + str(random.randint(0, 9)) + ") Gecko/20100101 " + browser_version

def cp():
    # while True:
        os.system('cls')
        print("\033[91m"+'''
 __     __         _         _           __          __   _       _         _           _   
 \ \   / /        | |       | |          \ \        / /  | |     | |       | |         | |  
  \ \_/ /__  _   _| |_ _   _| |__   ___   \ \  /\  / /_ _| |_ ___| |__     | |__   ___ | |_ 
   \   / _ \| | | | __| | | | '_ \ / _ \   \ \/  \/ / _` | __/ __| '_ \    | '_ \ / _ \| __|
    | | (_) | |_| | |_| |_| | |_) |  __/    \  /\  / (_| | || (__| | | |   | |_) | (_) | |_ 
    |_|\___/ \__,_|\__|\__,_|_.__/ \___|     \/  \/ \__,_|\__\___|_| |_|   |_.__/ \___/ \__|                                                                                            
      ''')
        print("\033[91m"+'''
                            (                                 (          
   (         )   (          )\ )     )        (               )\ )   (   
   )\     ( /(   )\ )   (  (()/(  ( /(     )  )\ (      )    (()/( ( )\  
((((_)(   )\()) (()/(  ))\  /(_)) )\()) ( /( ((_))\    (      /(_)))((_) 
 )\ _ )\ ((_)\   ((_))/((_)(_))  ((_)\  )(_)) _ ((_)   )\  ' (_)) ((_)_  
 (_)_\(_)| |(_)  _| |(_))  | |   | |(_)((_)_ | | (_) _((_))  / __| | _ ) 
  / _ \  | '_ \/ _` |/ -_) | |__ | ' \ / _` || | | || '  \() \__ \ | _ \ 
 /_/ \_\ |_.__/\__,_|\___| |____||_||_|\__,_||_| |_||_|_|_|  |___/ |___/ 
                                                                           
        ''')
        # os.system('cls')

def Youtube_Watcher(Link):
    is_working = False
    while is_working!=True:
        try:
            chrome_options = selenium.webdriver.ChromeOptions()
            user_agent = get_random_user_agent()
            chrome_options.add_argument('start-maximized')
            chrome_options.add_argument('--user-agent='+user_agent)
            chrome_options.add_argument('--allow-running-insecure-content')
            chrome_options.add_argument("javascript.enabled")
            chrome_options.add_extension('vpn.crx')
            screen_resolution = get_random_window_size()
            timezone = get_random_timezone()
            language = get_random_language()
            chrome_options.add_argument('--window-size=' + screen_resolution)
            chrome_options.add_argument('--lang=' + language)
            chrome_options.add_argument('--force-timezone=' + timezone)
            chrome_options.add_argument("--disable-plugins")
            chrome_options.add_argument("--disable-extensions-file-access-check")
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            Name = random_name()
            profile_path = "Profiles/"+Name
            chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_path))
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('chrome-extension://eppiocemhmnlbhjplcgkofciiegomcon/popup/index.html#/announcement')
            driver.implicitly_wait(time_to_wait=10)
            time.sleep(6)
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.find_element('xpath','/html/body/div/div/div[2]/div/div/div[2]/button[2]').click()
            driver.implicitly_wait(time_to_wait=10)
            time.sleep(0.5)
            driver.find_element('xpath','/html/body/div/div/div[3]/div[4]/div/div').click()
            while driver.find_element('class name','timer').text=='00 : 00 : 00':
                time.sleep(0.2)
            # driver.get('chrome-extension://extension_eppiocemhmnlbhjplcgkofciiegomcon/index.html')
            driver.get(Link)
            driver.implicitly_wait(time_to_wait=10)
            time.sleep(10)
            try:
                driver.find_element('class name','yt-spec-touch-feedback-shape__fill').click()
            except:
                print()
            cp()
            clock = Thread(name='Clock',target=big_clock)
            clock.start()
            
            while True:
                time.sleep(2000)
        except:
            driver.quit
if __name__ =="__main__":
    p = Thread(target=cp,args=())
    p.start()
    file = open('Config.txt','r')
    Config = file.readlines()
    file.close()
    Temp = Config[0].split(':')
    Threads = Temp[1]
    Temp = Config[1]
    Link = Temp.replace('Link:','')
    # print(Link)
    N = int(Threads)
      # Number of browsers to spawn
    thread_list = list()

    # Start test
    for i in range(N):
        t = Thread(name='Thread {}'.format(i), target=Youtube_Watcher,args=(Link,))
        t.start()
        time.sleep(1)
        # print(t.name + ' started!')
        thread_list.append(t)
    # Wait for all threads to complete
    for thread in thread_list:
        thread.join()

print('Done')