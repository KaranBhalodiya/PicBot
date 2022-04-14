import speech_recognition as sr
import cv2
import datetime
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hey!!! Karan what can i do for u?')
engine.runAndWait()

def audio_to_text():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source,phrase_time_limit=5)
            text = listener.recognize_google(voice)
            print(text.lower())
            return text

    except Exception as e:
        print(e)


def selfie():
    text = audio_to_text()
    if "selfie" in text:
        #print("hello")
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

        while True:
            ret, frame = cap.read()
            original_frame = frame.copy()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face = face_cascade.detectMultiScale(gray, 1.3, 5)

            for x,y,w,h in face:
                cv2.rectangle(frame, (x, y), ((x+w), (y + h)), (255, 255, 255), 3)
                face_roi = frame[y:y+h,x:x+w]
                gray_roi = gray[y:y+h,x:x+w]

                smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
                for x1, y1, w1, h1 in smile:
                    cv2.rectangle(face_roi, (x1, y1), ((x1 + w1), (y1+ h1)), (0, 255, 255), 2)
                    time_stamp=datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                    cv2.imwrite(f'{time_stamp} seflie.png', original_frame)
            cv2.imshow('camera', frame)
            if cv2.waitKey(10) == ord('q'):
                break
    else:
        print("Nice Talking with u")
        engine.say("Nice Talking with u")
        engine.runAndWait()


selfie()
