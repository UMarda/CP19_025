#inital text to speech coding
import pyttsx3
y=input("enter a sentence: ")  #input sentence 1
z=input("enter a sentence: ")  #input sentence 2
while(y!="exit"):             #stop taking input 
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)    
    engine.setProperty('volume', 0.9) 
    engine.say(y)        #say sentence 1
    engine.say(z)        #say sentence 2
    engine.runAndWait()
    y=input("enter a sentence: ") #again taking sentence


#for changing voices 
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

#to input sentence for voice changing
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   engine.setProperty('voice', voice.id)
   engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()