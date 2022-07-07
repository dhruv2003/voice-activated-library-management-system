import speech_recognition as sr    #installed by pip install SpeechRecognition
import datetime      #inbuilt module
import pyttsx3          #installed by pip install pyttsx3
import re               #regex module

engine = pyttsx3.init('sapi5')  
voices = engine.getProperty('voices')       #getting details of current voice   
engine.setProperty('volume', 1.0)       #setting volume
engine.setProperty('voice', voices[1].id)     #set voice 

student_ids = dict({16010321005: 'Dhruv Bhagatkar',     #dict for student names
                    16010321006: 'Sharang Chandak',
                    16010321007: 'Aditya Chaudhari',
                    16010321008: 'Soham Chindarkar',
                    16010321009: 'Sammod Date',
                    16010321010: 'Yashvi Desai',
                    16010321011: 'Atharva Dhakate',
                    16010321088:'Bheemika Soni'})

book_ids=dict({456:'the beauty and the beast',          #dict for book names and IDS
               111: 'Will',
                112: 'Mind without fear',
113: 'The silent patient',
114: 'Quiet-power of introverts',
115: 'Dotcom secrets',
116: 'A nation of idiots',
117: 'Rework',
118: 'Sapiens',
119: 'One minute manager',
120: 'Who moved my cheese',
121: 'The Dip',
122: 'The Alchemist',
123: 'Twelve and a Half',
124: 'Commando',
125: 'Rest',})

def speak(audio):
    engine.say(audio)
    engine.runAndWait()         #without this speech won't be audible for us


def takecommand():
    r = sr.Recognizer()                 #It takes input from user's mic and returns string output

    with sr.Microphone() as source:
        print("Speak anything: ")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')     #Using google for voice recognition.
            print(f"User said: {query}\n")      #User query will be printed.

        except Exception as e:
            # print(e)
            print("Say that again please...")       #Say that again will be printed in case of improper voice
            return "None"           #None string will be returned
        return query


def wishMe():                   #function to greet user acc to time HOUR in 24hr format obtained using datetime module
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
        query = takecommand().lower()           #Converting user query into lower case

        if 'return book' in query:
            while True:
                speak("Enter Student ID")
                student_id = int(input("Enter Student ID: "))
                if student_id in student_ids:
                    print("ID Found!")
                    speak("Student ID Found!")
                    id_found=True 
                else:
                    print("Enter Student ID again!")
                    speak("enter Student ID again!")
                while id_found==True:
                    speak("Enter Book ID ")    
                    book_id=int(input("Enter Book ID: "))
                    if book_id in book_ids:
                        print("Book found!")
                        speak("Book ID found")
                        bookid_found=True
                    else:
                        print("Enter book id again!")
                        speak("enter bookid again")
                    while bookid_found==True:
                        print("book returned")
                        speak("book returned")
                        break
                    break    
            break
   
        if 'boro book' in query:
            while True:
                student_id = int(input("Enter Student ID: "))
                speak("enter Student ID")
                if student_id in student_ids:
                    print("ID Found!")
                    speak("student ID found")
                    id_found=True 
                else:
                    print("Enter Student ID again!")
                    speak("enter student id again")
                while id_found==True:    
                    speak("enter Book id")
                    book_id=int(input("Enter Book ID: "))
                    if book_id in book_ids:
                        speak("book id found")
                        print("Book found!")
                        bookid_found=True
                    else:
                        print("Enter book id again!")
                        speak("enter book id again")
                    while bookid_found==True:
                        print("book BORROWED!")
                        speak("book borrowed")
                        break
                    break    
            break
        
        if 'renu book' in query:
            while True:
                speak("enter student ID")
                student_id = int(input("Enter Student ID: "))
                if student_id in student_ids:
                    print("ID Found!")
                    speak("student ID found")
                    id_found=True 
                else:
                    print("Enter Student ID again!")
                    speak("enter Student id again")
                while id_found==True:
                    speak("enter book id")    
                    book_id=int(input("Enter Book ID: "))
                    if book_id in book_ids:
                        print("Book found!")
                        speak("book id found")
                        bookid_found=True
                    else:
                        print("Enter book id again!")
                        speak("enter book id again")
                    while bookid_found==True:
                        print("book renewed!")
                        speak("book renewed")
                        break
                    break    
            break

