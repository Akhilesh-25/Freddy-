import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize recognizer and TTS engine
listener = sr.Recognizer()
machine = pyttsx3.init()

# Set the voice to female
voices = machine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        machine.setProperty('voice', voice.id)
        break

def talk(text):
    machine.say(text)
    machine.runAndWait()

def Hello():
   talk("hello sir I am your freddy.Tell me how may I help you")


def input_instruction():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "freddy" in instruction:
                instruction = instruction.replace('freddy', '').strip()
                print(instruction)
                return instruction
    except sr.UnknownValueError:
        talk("Sorry, I did not understand that.")
    except sr.RequestError:
        talk("Could not request results from Google Speech Recognition service.")
    except Exception as e:
        talk(f"An error occurred: {e}")
    return None

def play_song(song):
    talk(f"Playing {song}")
    pywhatkit.playonyt(song)

def tell_time():
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)

def tell_date():
    date = datetime.datetime.now().strftime('%d/%m/%Y')
    talk("Today's date is " + date)

def respond_to_greeting():
    talk('I am fine, how about you?')

def tell_name():
    talk('I am Freddy, what can I do for you?')

def get_wikipedia_info(person):
    try:
        info = wikipedia.summary(person, sentences=1)
        talk(info)
    except wikipedia.exceptions.DisambiguationError as e:
        talk("Multiple results found, please be more specific.")
    except wikipedia.exceptions.PageError:
        talk("No information found on Wikipedia.")

def play_freddy():
    instruction = input_instruction()
    if instruction:
        print(f"Instruction received: {instruction}")

        if "play" in instruction:
            song = instruction.replace('play', '').strip()
            play_song(song)

        elif 'time' in instruction:
            tell_time()

        elif 'date' in instruction:
            tell_date()

        elif 'how are you' in instruction:
            respond_to_greeting()

        elif 'what is your name' in instruction:
            tell_name()

        elif 'who is' in instruction:
            person = instruction.replace('who is', '').strip()
            get_wikipedia_info(person)

        else:
            talk('Please repeat.')

if __name__ == "__main__":
    play_freddy()
