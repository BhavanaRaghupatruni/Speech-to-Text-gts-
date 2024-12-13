import speech_recognition as sr
import pyttsx3
from translate import Translator

# Initialize speech recognizer
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()

# List of supported language codes for both source and destination languages
LANGUAGE_CODES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'ko': 'Korean',
    'hi': 'Hindi',
    'ru': 'Russian',
    'ar': 'Arabic',
    'tr': 'Turkish',
    'sv': 'Swedish',
    'nl': 'Dutch',
    'bn': 'Bengali',
    'pa': 'Punjabi',
    'ta': 'Tamil',
    'te': 'Telugu',
    'ml': 'Malayalam',
    'pl': 'Polish',
    'cs': 'Czech',
    'vi': 'Vietnamese',
    'ms': 'Malay',
    'he': 'Hebrew',
    'el': 'Greek',
    'sr': 'Serbian',
    'hr': 'Croatian',
    'th': 'Thai',
    'id': 'Indonesian',
}

# Function to listen and recognize speech from microphone
def listen_and_recognize():
    with sr.Microphone() as source:
        print("Say something in the source language...")
        # Listen for the audio
        audio = recognizer.listen(source)
        try:
            # Convert speech to text using Google's speech recognition API
            text = recognizer.recognize_google(audio)
            print(f"Source Language Text: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

# Function to translate text to a target language
def translate_text(text, src_lang, dest_lang):
    translator = Translator(from_lang=src_lang, to_lang=dest_lang)
    translation = translator.translate(text)
    print(f"Translated Text ({LANGUAGE_CODES.get(dest_lang, dest_lang)}): {translation}")
    return translation

# Function to convert text to speech
def speak_text(text, lang_code):
    engine.setProperty('voice', lang_code)  # Set language-specific voice (if available)
    engine.say(text)
    engine.runAndWait()

# Main function
def main():
    # Step 1: Prompt user to enter source and destination languages from the language codes dictionary
    print("Supported language codes:")
    for code, language in LANGUAGE_CODES.items():
        print(f"{code}: {language}")
    
    src_lang = input("Enter the source language code: ").strip()
    dest_lang = input("Enter the destination language code: ").strip()

    if src_lang not in LANGUAGE_CODES or dest_lang not in LANGUAGE_CODES:
        print("Invalid language code entered. Please choose a valid language code.")
        return

    # Step 2: Listen and recognize speech
    source_text = listen_and_recognize()
    
    if source_text:
        # Step 3: Translate text
        translated_text = translate_text(source_text, src_lang, dest_lang)
        
        # Step 4: Speak the translated text
        speak_text(translated_text, dest_lang)

if __name__ == "__main__":
    main()