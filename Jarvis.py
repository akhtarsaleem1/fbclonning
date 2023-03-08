from Brain.Aibrain import ReplyBrain
from Body.listen import MicExecution
from Brain.Qna import QuestionAns
print('>> Starting The Jarvis : Wait For Some Seconds <<')
from Body.Speak import Speak
#from Main import MainTask
from Features.news import news

import os
import datetime
try:
    from googletrans import Translator
except:
    os.system('pip install googletrans==3.1.0a0')
    from googletrans import Translator    
    
try:
    import pywhatkit
except:
    os.system('pip install pywhatkit')
    import pywhatkit
try:
    import requests
except:
    os.system('pip install requests')
    import requests    
try:
    import keyboard
except:
    os.system('pip install keyboard')
    import keyboard
try:
    from time import sleep
except:
    os.system('pip install datetime')
    from time import sleep
try:
    from pywikihow import search_wikihow
except:
    os.system('pip install datetime')
    from pywikihow import search_wikihow    

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"English : {data}.")
    return data    

def TransEngToHi(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line,)
    data = result.text
    #print(f'Hindi : {data}')
    return data

def MainExe():
    Speak('Hello Sir... yah kamini kon hai aapke saath')
    wishme()
    while True:
            
        Data = MicExecution().lower()
        Data = str(Data).replace(".","")
        # valuereturn = MainTask(Data)
        # if valuereturn==True:
        #     pass
        
        if len(Data)<3:
            pass
            
        elif 'sleep' in Data:
            Speak('i am going to sleep when you need me just say Jarvis')
            hotword()
        
        # elif 'how to' in Data:
        #     #Reply = ReplyBrain(Data)
        #     #Speak(Reply)
        #     while True:
        #         Speak('Do you want more details i speak it or search on youtube')
        #         query = MicExecution().lower()
        #         if 'you' in query or 'tell' in query or 'say' in query:
        #             max_results = 1
        #             how_to = search_wikihow(Data, max_results)
        #             assert len(how_to)
        #             #how_to[0].print()
        #             data = TransEngToHi(how_to[0].summary)
        #             Speak(data) 
        #             Speak("if you want more details about it am i play on YouTube")
        #             while True:
        #                 Query = MicExecution().lower()
        #                 if 'yes' in Query or 'this' in Query:
        #                     Speak('Opening YouTube')
        #                     cm = Data
        #                     pywhatkit.playonyt(cm)
        #                     break
        #                 elif 'no' in Query:
        #                     Speak('Again Speak No')
        #                     break    
        #         elif 'youtube' in query:
        #             Speak('Opening YouTube')
        #             cm = Data
        #             pywhatkit.playonyt(cm)
        #             break
        #         elif 'no' in query:
        #             Speak('Okay Sir, do want you something Sir')
        #             break    
        
        elif "how to" in Data:
            max_results = 1
            how_to = search_wikihow(Data, max_results)
            assert len(how_to)
            #how_to[0].print()
            #data = TransEngToHi(how_to[0].summary)
            Speak(how_to[0].summary)
            
        elif 'news' in Data:
            news()    
        
        elif 'Galiya' in Data or 'abuse' in Data:
            Speak('Kamina, sala, kuta, harmi, chutiya, lovda, aur galiya suno kamina')
            
        elif 'lion' in Data:
            Data.replace("lion" , "poetry")    
        
        elif 'english' in Data:
            Speak('Okay Sir')
            n= int(2)
            FileLog = open("C:\\AI\\DataBase\\chat_log.txt","r")
            for line in (FileLog.readlines() [-n:]):
                print(TranslationHinToEng(line))
            FileLog.close()
        
        elif 'made you' in Data or 'created you' in Data or 'create you' in Data or 'make you' in Data:
            Speak('I was created by A S K')   
            
        elif 'what is' in Data or 'where is' in Data or 'question' in Data or 'answar' in Data or 'who is' in Data:
            Reply = QuestionAns(Data)
            Speak(Reply)
        else:
            Reply = ReplyBrain(Data)
            Speak(Reply)

def hotword():
    Speak('Hello Sir...')
    while True:
        query = MicExecution().lower()
        if 'jarvis' in query or 'hello' in query:
            MainExe()                 
            
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12 :
        Speak('Good morning a s k')
    elif hour >= 12 and hour < 18:
        Speak('Good Afternoon a s k')
    else:
        Speak('Good Evening a s k ')
        
# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def runing():
#     return render_template('gui.html')

# if __name__ == "__main__":
#     app.run(debug=True)        
MainExe()           