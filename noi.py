import pyttsx3

robot_brain = "Sorry,I haven't upgraded yet"

robot_mouth = pyttsx3.init()
robot_mouth.say(robot_brain)
robot_mouth.runAndWait()
