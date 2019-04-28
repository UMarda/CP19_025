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