import pyttsx3
s=input("Enter words to speak:")
c=s.lower()
while(c!="exit"):
    engine=pyttsx3.init()
    engine.say(s)
    engine.runAndWait()
    s=input("Enter word to speak or press s to exit:")
    c=s.lower()
