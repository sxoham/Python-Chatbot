import pyttsx3

engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Pre-select voices (may vary depending on OS)
male_voice = None
female_voice = None

for voice in voices:
    if 'female' in voice.name.lower():
        female_voice = voice.id
    elif 'male' in voice.name.lower():
        male_voice = voice.id

# Fallback if gender-based detection fails
if not male_voice and voices:
    male_voice = voices[0].id
if not female_voice and len(voices) > 1:
    female_voice = voices[1].id

def speak(text, gender='female'):
    if gender == 'male' and male_voice:
        engine.setProperty('voice', male_voice)
    elif gender == 'female' and female_voice:
        engine.setProperty('voice', female_voice)

    engine.say(text)
    engine.runAndWait()
