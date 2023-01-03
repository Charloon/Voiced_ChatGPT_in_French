import os
import pyttsx3
import speech_recognition as sr
import tkinter as tk
from chatgpt_wrapper import ChatGPT
from deep_translator import GoogleTranslator

def generate_bot():
    "function to generate the bot for ChatGPT"
    return ChatGPT()

def login_chatGPT(bot = None):
    if bot is None:
        print("Start login_chatGPT ..")
        os.system("chatgpt install")
        bot = generate_bot()
        print("Done login_chatGPT ..")
        return bot
    else:
        return bot

def QA_chatGPT(bot):
    """
    Main function to get the question in french from the microphone in french,
    translate it in english, submit it to chatGPT, translate the answer in french
    and then voice it.   
    """
    question_fr = None
    # obtain question in french from the microphone
    print("Obtaining question in french from the microphone.")
    recognise = sr.Recognizer()
    with sr.Microphone() as source:
        print("Pose moi une question a l'oral.")
        audio = recognise.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        print("Google Speech Recognition thinks you said " + \
            recognise.recognize_google(audio,language="fr"))
        # Translating the question to french
        question_fr = recognise.recognize_google(audio,language="fr")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as error:
        print("Could not request results from Google Speech Recognition service; {0}".format(error))
    # if recording did not worked
    if question_fr is None:
        question_fr = input("Ecrivez ici:")

    # translating question to english
    print("Translating question to english.")
    question_en = GoogleTranslator(source='fr', target='en').translate(question_fr)
    print(question_en)

    # Ask the question to chat GPT
    print("Asking and waiting for answer from chatGPT.")
    response_en = bot.ask(question_en)
    print(response_en)

    # Translate answer to french
    print("Translating the answer to french")
    response_fr = GoogleTranslator(source='en', target='fr').translate(response_en)
    print(response_fr)

    # Voice the answer in french
    print("Voice the answer in french")
    engine = pyttsx3.init()
    engine.say(response_fr)
    engine.runAndWait()
    return

# login to ChatGPT
bot = login_chatGPT()

# create dialogue window
top = tk.Tk()
top.option_add('*Font', '19')
top.geometry("300x200")
label = tk.Label(top, text = "ChatGPT vocal et en français")
label.pack(padx = 20, pady = 20)
B = tk.Button(top, text ="Parle moi", command = lambda: QA_chatGPT(bot))
B.pack()
top.mainloop()
