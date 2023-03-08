# Speak Functions - Two Speak Functions

# Windows Based - pip install pyttsx3
# Chrome Based - pip install selenium==4.1.3

# Windows Based
# Advantages = Fast , Offline.
# Disadvantages =  OverSpeak , Less Voices.

# import pyttsx3

# def Speak(Text):
#     engine = pyttsx3.init("sapi5")
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice',voices[1].id)
#     engine.setProperty('rate',170)
#     print("")
#     print(f"Jarvis : {Text}.")
#     print("")
#     engine.say(Text)
#     engine.runAndWait()

# Chrome Base
# Advantages = More Voices, More Clear , Overspeaking.
# Disadvantages = Word Limit, Slow.

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('--log-level=3')
chrome_options.headless = True
Path = "DataBase\\chromedriver.exe"
driver = webdriver.Chrome(Path,options=chrome_options)
driver.maximize_window()

website = r"https://translate.google.com/?sl=en&tl=ur&op=translate"
driver.get(website)

def Speak(Text):

    lengthoftext = len(str(Text))

    if lengthoftext==0:
        pass

    else:
        Data = str(Text)
    
        input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea")))
        input_box.send_keys(Data)
        
        sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[4]/div[1]/div[2]/span/button/div[3]"))).click()
    
        sleep(2)
        driver.find_element(by=By.XPATH,value="/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").clear()
        
        print("")
        print(f"AI : {Data}.")
        print("")
        
        if lengthoftext>=20:
            sleep(5)
            
        if lengthoftext>=30:
            sleep(8)

        elif lengthoftext>=40:
            sleep(15)

        elif lengthoftext>=55:
            sleep(20)

        elif lengthoftext>=70:
            sleep(25)

        elif lengthoftext>=100:
            sleep(30)

        elif lengthoftext>=120:
            sleep(35)
            
        elif lengthoftext>=150:
            sleep(40)
            
        elif lengthoftext>=170:
            sleep(45)
            
        elif lengthoftext>=200:
            sleep(50)       
             
        else:
            sleep(2)