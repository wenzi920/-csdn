import urllib
import re
import urllib.request
import random

def gethtml(url):
    #url='https://ask.csdn.net/questions/361396'
    content=urllib.request.urlopen(url).read()
    content=content.decode('utf-8')
    return content

def getquestion(content):
    start=content.find(r'<div class="questions_detail_con">')
    end=content.find(r'</dd>')
    content2= re.sub(r'<.*?>','',content[start:end])
    print("Question:"+content2+"\n"*5)

def getanswer(content):
    start=content.find(r'<div class="answer_list">')
    end=content.find(r'<div class="ask_date">')
    content3= re.sub(r'<.*?>','',content[start:end])
    print("Answer:"+content3+"\n"*2)
                       
   
for i in range(3):
    try:
        a=random.randint(300000,400000)
        url='https://ask.csdn.net/questions/{}'.format(a)
        gethtml(url)
        getquestion(gethtml(url))
        getanswer(gethtml(url))
    except:
        print("网页无法获取")
        
    
    

