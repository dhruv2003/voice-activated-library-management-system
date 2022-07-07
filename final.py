import speech_recognition as sr
import datetime
import pyttsx3
import re 

i = True
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('volume', 1.0)
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

student_ids = dict({16010321005: 'Dhruv Bhagatkar',
                    16010321006: 'Sharang Chandak',
                    16010321007: 'Aditya Chaudhari',
                    16010321008: 'Soham Chindarkar',
                    16010321009: 'Sammod Date',
                    16010321010: 'Yashvi Desai',
                    16010321011: 'Atharva Dhakate',
                    16010321088:'Bheemika Soni'})

book_ids=dict({456:'the beauty and the beast',
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
                    else:
                        print("Enter book id again!")
                    while bookid_found==True:
                        print("book returned")
                        break
                    break    
            break
   
        if 'boro book' in query:
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
                    else:
                        print("Enter book id again!")
                    while bookid_found==True:
                        print("book BORROWED!")
                        break
                    break    
            break
        
        if 'renu book' in query:
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
                    else:
                        print("Enter book id again!")
                    while bookid_found==True:
                        print("book renewed!")
                        break
                    break    
            break

