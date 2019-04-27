import pyttsx3
y=input("enter a sentence: ")
z=input("enter a sentence: ")
while(y!="exit"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)    
    engine.setProperty('volume', 0.9) 
    engine.say(y)
    engine.say(z)
    engine.runAndWait()
    y=input("enter a sentence: ")