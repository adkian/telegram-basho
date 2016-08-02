import sys
import time
import telepot
import re
import random
import datetime
import adjectives
import nouns
import adverbs
import verbs

articles=["the", "my", "one", "just a"]
# In[5]:

def getWord(word):
    new_word=re.search("(\S*)",word).group(1)
    return new_word



def getArticle(noun):
    article_int=random.randint(0,len(articles)-1)
    if article_int >=2:
        return articles[article_int]
    elif noun[0] in ["a", "e", "i", "o", "u"]:
        return "an"
    else:
        return "a"

def newLine():
    lines=random.randint(2,4)
    default = getWord(adjectives.getAdjective()) + " " + getWord(nouns.getNoun()) 
    if lines==2:
        return (default + "\n")
    elif lines==3:
        return (default +" "+ getWord(verbs.getVerb()) + "\n")
    else: 
        n=getWord(nouns.getNoun())
        return (getWord(getArticle(n)) + " " + n + " " + getWord(adverbs.getAdverb()) + " " + getWord(verbs.getVerb()) + "\n")

def makeHaiku():
    return newLine() + newLine() + newLine()
      
def handle(msg):
    text=msg['text']
    if text.lower()=='/writeahaiku' or text.lower()=='/writeahaiku@a_haiku_bot':        
        bot.sendMessage(msg['chat']['id'], makeHaiku())
    elif text.lower()=='/about' or text.lower()=='/about@a_haiku_bot':
        bot.sendMessage(msg['chat']['id'], getGreeting(msg['date']))
    elif text.lower()=='/help' or text.lower()=='/help@a_haiku_bot':
        message="Commands:\n/about : About the bot \n/help: Commands help\n/WriteAHaiku : Write a Haiku"
        bot.sendMessage(msg['chat']['id'], message)

def getGreeting(date):
    greeting=""
    hour=int(datetime.datetime.fromtimestamp(date).strftime("%H"))
    if (hour>=0 and hour<=3) or (hour>=17 and hour<=23):
        greeting="Konbanawa, "
    elif hour>=4 and hour<=11:
        greeting="Ohayo Gozaimasu, "
    else:
        greeting="Konichiwa, "
    text="I'm a new-age version of the great Japanese poet, Basho. Type /help for commands"
    return (greeting + text)

    
        
TOKEN = "YOUR TOKEN HERE"

bot = telepot.Bot(TOKEN)
bot.notifyOnMessage(handle)
print '********DO NOT CLOSE THIS TERMINAL!!!!**************'



# Keep the program running.
while 1:
    time.sleep(10)
