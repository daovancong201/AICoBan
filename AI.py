import speech_recognition
import pyttsx3
from datetime import date,datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""

while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot:...")
        
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)

    # Phần Ai ( Phần trí tuệ nhân tạo xử lý ngôn ngữ tự nhiên NLP Natural language processing )
    if you =="":
        robot_brain = "I can't hear you , Try again "
    elif you == "Hello" in you:
        robot_brain = " Hello you"
    elif "today" in you:
        today = date.today()
        robot_brain  = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "president" in you:
        robot_brain ="Joe Biden"
    elif "bye" in you:
        robot_brain = "Good Bye"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Sorry,I haven't upgraded yet"
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()