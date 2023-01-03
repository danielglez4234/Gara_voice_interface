# sudo apt-get install python3-pyaudio



import requests
import speech_recognition as sr
import pyttsx3
from ctypes import *
from contextlib import contextmanager
from pydub import AudioSegment



ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)
API = "http://172.21.2.37:5045/webhooks/rest/webhook"


recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
# execute cat /proc/asound/cards to know which 
# device index you want
mic = sr.Microphone(device_index=0)
# audio = AudioSegment.from_wav('audio.wav')
# audio_file = sr.AudioFile('audio.wav')

# def py_error_handler(filename, line, function, err, fmt):
#     pass

# c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

def SpeakText(command):
    """Function to convert text to speech"""
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

# @contextmanager
# def noalsaerr():
#     asound = cdll.LoadLibrary('libasound.so')
#     asound.snd_lib_error_set_handler(c_error_handler)
#     yield
#     asound.snd_lib_error_set_handler(None)


# sender = input("What is your name?\n")
bot_message = ""

while bot_message != "Bye":
    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with mic as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            recognizer.adjust_for_ambient_noise(source2, duration=0.2)

            #listens for the user's input
            audio2 = recognizer.listen(source2)

            # Using google to recognize audio
            MyText = recognizer.recognize_google(audio2)
            MyText = MyText.lower()
            print("Did you say ", MyText)
            
            SpeakText(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")



    # while bot_message != "Bye":
    #     message = input("What's your message?\n")
        
    #     print("Sending message now...")
        
    #     r = requests.post(API, json={"sender": sender, "message": message})
        
    #     print("Bot says, ", end=' ')
    #     print(r.json())
    #     print(r.text)
    #     print(r.status_code)
    #     for i in r.json():
    #         bot_message = i['text']
    #         print("sdkñfnsf")
    #         print(i)
    #         print(f"{i['text']}")
        