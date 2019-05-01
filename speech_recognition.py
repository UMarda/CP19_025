################## Speech to text Library ####################
import speech_recognition as sr
r = sr.Recognizer()     # Recognizer
with sr.Microphones() as source :
    print('speak anything')
    audio=r.listen(source)        #variable
    print("Time Over Thanks")
    try:
        print('you said \n',+r.reconize_google(audio))
    except:
        print("sorry could not recognize your voice ")
#############################################################
