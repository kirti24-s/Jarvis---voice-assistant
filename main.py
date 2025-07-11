import speech_recognition as sr # This libraray helps converting text to speech , We use sr.Recognizer() and sr.Microphone() from this.
import webbrowser   #allows to open websites using command like open google,etc.
import pyttsx3        #Let Jarvis speak to us
from os import path #Use to make available device folders files
import time         #Provides fucn like time.sleep()
import music

#pip install pocketsphinx

recognizer = sr.Recognizer()  #sr.Recognizer is a module from speech_recognition creates obj recognizer for efficient handling
# recognizer provides all the methods needed to:
# Listen to audio
# Adjust for background noise
# Recognize speech using online/offline engines


engine = pyttsx3.init()
 

def speak(text):
    #Process Command
    engine.say(text)
    engine.say("Testing one two three")
     #make JArvis speak
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower(): 
        webbrowser.open("https://www.youtube.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://in.linkedin.com/")
    elif "open github" in c.lower():
        webbrowser.open("https://github.com/")     
    elif c.lower().startswith("play"):
        try:
            song=c.lower().split(" ")[1]
            link = music.music[song]
            webbrowser.open(link)
            speak(f"Playing {song}")
        except KeyError:
            speak("Song not fonund.")
    elif "pause" in c or "stop" in c:
        speak("Cannot pause YouTube in playback in browser.")
    elif "exit" in c or "quit" in c:
        speak("Goodbye!")
        exit()
    # else:
    #      speak("Sorry, I didn't understand the command.")
    #     print("Unknown command:", c)
           
if __name__ == "__main__": # To CHeck whether code running directly not imported
    speak("Initializing Jarvis....")
    while True:
        #Listen for the wake word Jarvis 
        #obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing....")
        try:
            with sr.Microphone() as source:
               r.adjust_for_ambient_noise(source, duration=1)      #Ignore background voice, source is your device
               print("Listening...")
               audio = r.listen(source , timeout=5, phrase_time_limit=5)                                                                    #timeout for to stop for 5 sec after listening to print Wake word detected Jarvis & phrase_time_limit to hear sound for 5 sec
               word = r.recognize_google(audio) 
               
               #To activate Jarvis
            if(word.lower() == "jarvis"):
                print("Wake word detected :Jarvis") 
                speak("Ya")
                print("Jarvis Active ...")
                time.sleep(0.5)              #half  minute pause
                
                
                #Listen for command
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=1)
                    print("Listening for your command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    try:
                        command = r.recognize_google(audio)    #Uses Google audio speech API to convert into text
                        print("Command received:", command)
                        processCommand(command) 
                    except sr.UnknownValueError:
                        print("Could not understand the audio.")        
        except sr.WaitTimeoutError:             #You spoke after time
            print("Listening timed out — no speech detected.")
        except sr.UnknownValueError:          #Not spoke properly
            print("Could not understand the audio.")
        except Exception as e:
            print("Error; {0}" .format(e))  #print error along with type of error
