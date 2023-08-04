import pyttsx3 
import speech_recognition as sr
import datetime
import os
import random
import webbrowser
import pywhatkit as kit
import smtplib
import sys

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

speak("hello sir,")
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning ")
    elif  hour >=12 and hour <16:
        speak("good afternoon ")
    elif  hour>=16 and hour <18:
        speak("good eveing ")
    else:
        speak("good night")



def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something....")
        r.pause_threshold=1
        audio = r.listen(source , timeout=4 ,phrase_time_limit=5)

    try:
        print("processing.....")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except:
        speak("can't understand, please say once again")
    return query

def sendmail(to,con):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pradeeppradeep1207@gmail.com','9345693880')
    server.sendmail('pradeeppradeep1207@gmail.com', to,con)
    server.close()





if __name__=="__main__":

    wish()
    speak("thank you for wakeuping mee, how can i help you")
    
    query = takecommand().lower()

   # if "open notepad" in query:
       # speak("opening notepad")
       # npath = "C:\\Program Files\\WindowsApps\\Microsoft.Windows Notepad_11.2305.18.0_x64_8wekyb3d8bbwe Notepad\\Notepad.exe"

        #os.startfile(npath)
        #C:\Program Files\WindowsApps\Microsoft.Windows Notepad_11.2305.18.0_x64_8wekyb3d8bbwe Notepad Notepad.exe  

    if "open command prompt" in query:
        speak("opening command promt")
        os.system("start cmd")

   # elif "play music" in query:
       # music_dir = "c:\music"
       # songs = os.listdir(music_dir)
        #rd = random.choice(songs)
       # for song in songs:
          #  if song.endswith(".mp3"):
               # os.startfile(os.path.join(music_dir, song))

    elif "open youtube" in query :
        webbrowser.open("www.youtube.com")

    elif "open whatsapp" in query :
        webbrowser.open("web.whatsapp.com")

    elif "open google" in query :
        speak("what can i search,sir")
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")

    elif "send message" in query:
        speak("what can is send sir")
        smsg = takecommand().lower()
        kit.sendwhatmsg("+919345693880",smsg, 2,20)

    elif "play song on youtube"in query :
        speak("which song i want to play sir")
        scmd = takecommand().lower()
        kit.playonyt(f"{scmd}")

    elif "send email " in query:
        try:
            speak("what can i send sir")
            con = takecommand().lower()
            to = "pradeeppradeep1207@gmal.com"
            sendmail(to,con)
            speak("mail has been send to pradeep")
        except Exception as e:
            print(e)
            speak(" sorry sir, i can't send sir")

    elif "thank you elza" in query :
        speak("thank you for using me,sir have a good day ")
            

    

    
    










