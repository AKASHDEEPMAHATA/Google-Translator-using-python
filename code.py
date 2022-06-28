
import googletrans
import speech_recognition as sr
import gtts
import playsound

# print(googletrans.LANGUAGES)

recognizer = sr.Recognizer()
translator = googletrans.Translator()

input_lang = 'en'
output_lang = 'bn'



try:
    with sr.Microphone() as source:
        print('Speak now')
        voice = recognizer.listen(source)
        text_data = recognizer.recognize_google(voice , language= input_lang)
        print(text_data)

except:
    pass

x = translator.translate(text_data, dest=output_lang)
print(x.text) 
converted_audio = gtts.gTTS(x.text,lang=output_lang)
converted_audio.save('PyAudio.mp3')
playsound.playsound('PyAudio.mp3')
