import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input("Enter text: ")
    if text == "bye":
        speak.Speak('Good Bye')
    speak.Speak(text)
