from flask import Flask, render_template
from time import sleep
from Brain.Aibrain import ReplyBrain
from Brain.Qna import QuestionAns
from threading import Thread
# listen Function
import speech_recognition as sr  # pip install speechrecognition
from googletrans import Translator  # pip install googletrans==3.1.0a0

# Speak Function
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import winsound

app = Flask(__name__)
app.secret_key = "akhtarsaleem khan"

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
    return f"AI : {Data}"
    
@app.route('/')
def index():
    return render_template('guim.html')

@app.route('/start', methods=["POST", "GET"])
def Main():
    def listen():
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            winsound.Beep(1000, 500)
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, 0, 8)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="ur")
        except:
            return ""

        query = str(query).lower()
        return query

    # 2 - Translation


    def TranslationHinToEng(Text):
        line = str(Text)
        translate = Translator()
        result = translate.translate(line)
        data = result.text
        print(f"You : {data}.")
        return data

    # 3 - Connect


    def MicExecution():
        query = listen().lower()
        if query:
            data = TranslationHinToEng(query)
            return data
        else:
            return ""
    
    def MainExe():
        Speak("Hello Sir, After beep start asking")
        while True:
                
            Data = MicExecution().lower()
            Data = str(Data).replace(".","")
            
            if len(Data)<3:
                pass
                
            elif 'sleep' in Data:
                Speak('i am going to sleep when you need me just say Jarvis')
            
            elif 'Galiya' in Data or 'abuse' in Data:
                Speak('Kamina, sala, kuta, harmi, chutiya, lovda, aur galiya suno kamina')
                
            elif 'lion' in Data:
                Data.replace("lion" , "poetry")    
            
            # elif 'english' in Data:
            #     Speak('Okay Sir')
            #     n= int(2)
            #     FileLog = open("C:\\AI\\DataBase\\chat_log.txt","r")
            #     for line in (FileLog.readlines() [-n:]):
            #         print(TranslationHinToEng(line))
            #     FileLog.close()
            
            elif 'made you' in Data or 'created you' in Data or 'create you' in Data or 'make you' in Data:
                Speak('I was created by A S K')   
                
            elif 'what is' in Data or 'where is' in Data or 'question' in Data or 'answar' in Data or 'who is' in Data:
                Reply = QuestionAns(Data)
                Speak(Reply)
            else:
                Reply = ReplyBrain(Data)
                Speak(Reply)
                
    Thread(target=MainExe).start()        
    return render_template('guim.html')
    

if __name__ == "__main__":
    app.run(debug=True)
    
    