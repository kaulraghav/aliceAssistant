from alice import Alice
import speech_recognition as sr
import sys
GOOGLE_SPEECH_RECOGNITION_API_KEY = None


def run_transcription_loop():
    bot=Alice()
    r = sr.Recognizer()
    r.energy_threshold = 4000
    with sr.Microphone(device_index = None, sample_rate = 16000, chunk_size = 1024) as source:
        while True:
            print("Awaiting user input.")
            audio = r.listen(source)
            print("Attempting to transcribe user input.")
            try:
                result = r.recognize_google(
                    audio, key=GOOGLE_SPEECH_RECOGNITION_API_KEY
                )
                z=bot.handle_action(result)
                if(z==0): 
                    bot.speak("Have a nice day and thank you")
                    sys.exit("Error message")
                
            except sr.UnknownValueError:
                bot.speak("Sorry come again")
            except sr.RequestError:
                bot.speak("Internet connection error")
            except:
                print("")


if __name__ == '__main__':
    bot = Alice()
    bot.speak("Hello Sir")
    run_transcription_loop()
