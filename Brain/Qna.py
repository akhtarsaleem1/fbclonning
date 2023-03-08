# Open AI

fileopen = open('Data\\api.txt',"r")
API = fileopen.read()
fileopen.close()

import os

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
try:
    from googletrans import Translator
except:
    os.system('pip install dotenv')
    from googletrans import Translator
    
# def TranslateEngtoHi(Text):
#     line = str(Text)
#     translate = Translator()
#     result = translate.translate(line, 'hi')
#     data = result.text
#     return data
            
    
    
openai.api_key = API
load_dotenv()
completion = openai.Completion()
 
def QuestionAns(question, chat_log = None):
    FileLog = open("DataBase\\qna_log.txt","r")
    chat_log_template = FileLog.read()
    FileLog.close()
    
    if chat_log is None:
        chat_log = chat_log_template
        
    prompt = f'{chat_log}Question : {question}\nAnwar : '
    response = completion.create(
        model = 'text-davinci-003',
        prompt=prompt,
        temperature = 0,
        max_tokens = 100,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0)
    answar = response.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f'\nQustion : {question} \nAnswar : {answar}'
    FileLog = open("DataBase\\qna_log.txt", 'w')
    FileLog.write(chat_log_template_update)
    FileLog.close()
    return answar