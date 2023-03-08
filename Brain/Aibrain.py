# Open AI

fileopen = open('Data\\api.txt',"r")
API = fileopen.read()
fileopen.close()

import os
from Body.listen import listen
from googletrans import Translator

try:
    import openai
except:
    os.system('pip install openai')
    import openai 

try:
    from dotenv import load_dotenv
except:
    os.system('pip install dotenv')
    from dotenv import load_dotenv
    
openai.api_key = API
load_dotenv()
completion = openai.Completion()

# def TranslationHinToEng(Text):
#     line = str(Text)
#     translate = Translator()
#     result = translate.translate(line,)
#     data = result.text
#     #print(f"You : {data}.")
#     return data

def ReplyBrain(question, chat_log = None):
    FileLog = open("DataBase\\chat_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()
    
    if chat_log is None:
        chat_log = chat_log_template
        
    prompt = f'{chat_log}You : {question}\n Jarvis : '
    response = completion.create(
        model = 'text-davinci-002',
        prompt=prompt,
        temperature = 0.5,
        max_tokens = 60,
        top_p = 0.3,
        frequency_penalty = 0.5,
        presence_penalty = 0)
    answar = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f'\nYou : {question} \nJarvis : {answar}'
    FileLog = open("DataBase\\chat_log.txt", 'w')
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answar