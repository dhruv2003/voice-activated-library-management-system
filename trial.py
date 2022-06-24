import speech_recognition as sr
import datetime
import pyttsx3
import re 


i = True
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('volume', 1.0)
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

student_ids = dict({16010321005: 'Dhruv Bhagatkar',
                    16010321006: 'Sharang Chandak',
                    16010321007: 'Aditya Chaudhari',
                    16010321008: 'Soham Chindarkar',
                    16010321009: 'Sammod Date',
                    16010321010: 'Yashvi Desai',
                    16010321011: 'Atharva Dhakate'})

book_ids=dict({123:'the beauty and the beast'})

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak anything: ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            return "None"
        return query




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Welcome to the Library Management System What Do you Want to do today?")

id_found=False
bookid_found=False



if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()

        if 'return book' in query:
            while True:
                student_id = int(input("Enter Student ID: "))
                if student_id in student_ids:
                    print("ID Found!")
                    id_found=True 
                else:
                    print("Enter Student ID again!")
                while id_found==True:    
                    book_id=int(input("Enter Book ID: "))
                    if book_id in book_ids:
                        print("Book found!")
                        bookid_found=True
                    while student_id in student_ids and bookid_found==True:
                        print("book returned")
                        break
                    break    
            break
        
        if 'Boro book' in query:
            student_id=int(input("enter student id: "))

        if 'Renew Book' in query:
            print("renew Book")

