import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import smtplib
from requests import get
dic={'jaswant':'+919849245184','tata':'+919381034877'}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

#
def speak(text):
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listining....")
        r.pause_threshold=1
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in' )
        print(f"user said: {query}\n ")

    except Exception as e :
        print("say that again please")
        query= None
    return query   
#main s

if __name__ == "__main__":
    speak("hey! tell me")
    con = 1
    #wishMe()
    while con!=2:

        query = takeCommand().lower()

        if 'wikipedia' in  query:
            speak("searching wikipedia......sir")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences  =2)
            speak(results)
        
        #in this bit page will not open in chrome it will open in default webbrowser i.e internet explorer
        elif 'open' and '.com' in query:
            sl=slice(5,len(query),1)
            url=query[sl]
            speak('opening'+url)
            webbrowser.open(url)
            
        

        elif 'open notepad' in query:
           path = "C:\\Users\\jeevan kumar\\AppData\Roaming\\Microsoft\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
           speak("reddit")
           os.startfile(path)

        elif 'play' in  query:
            speak("playing  song")
            song = query
            pywhatkit.playonyt(song)
            
            #speak("which index song you want to play")
            #song=int(takeCommand())
            #if song in songs:
            os.startfile(os.path.join(song_dict, songs[0]))


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")    
            speak(f"sir, the time is {strTime}")
            print(strTime)
           #you should give you folder path to open you project 
        elif 'open my project' in query:
            path = "C:\\Users\\jeevan kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe"
            os.startfile(path)


        elif 'ok then' in query:
            con =int(con) + 1
            speak("your welcome sir")
        
             
       
        #you should give you folder path to open phontos
        #the path specified in the code is my folder path so just remove it and add yours    
        elif 'open photos' in query:
            speak("opening photoes ")
            path ='C:\\Users\\Jaswanth\\OneDrive\\Pictures\\Screenshots'
            os.startfile(path)
        
        #sends message in whatsap    
        elif 'send message' in query:
            speak('to whome')
            name=takeCommand().lower()
            if name not in dic:
                speak('you dont have contact named'+name)
                speak("try again")
            else:
                htime = datetime.datetime.now().strftime("%H")
                mtime = datetime.datetime.now().strftime("%M")
                h=int(htime)
                m=int(mtime)
                if m+1<60:
                    m=m+1
                else:
                    h=h+1
                    m=0

                contact=dic[name]
                speak('what is the message')
                print('listening...')
                mess=takeCommand().lower()
                pywhatkit.sendwhatmsg(contact,mess,h,m,20)
                speak('message sent')
                

        elif 'my ip address' in query: 
            add = get('https://api.ipify.org').text  
            speak(add)
            print(add) 