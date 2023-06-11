import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import tkinter as tk
from PIL import Image, ImageTk
import operator
#from ecapture import ecapture as ec
r=sr.Recognizer()
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        a="\nHello,Good Morning"
        textArea.insert(tk.END, a)
        speak("Hello,good morning")
    elif hour>=12 and hour<18:
        a="\nHello,Good Afternoon"
        textArea.insert(tk.END, a)
        speak("Hello,Good Afternoon")
    else:
        a="\nHello,Good Evening"
        textArea.insert(tk.END, a)
        speak("Hello,Good Evening")
def takeCommand():
    with sr.Microphone() as source:
        audio=r.listen(source)
        try:
            statement=r.recognize_google(audio,language='en-in')
            a=f"\nuser said:{statement}"
            textArea.insert(tk.END, a)
        except Exception as e:
            a = f"\nuser said:{statement}\n"
            textArea.insert(tk.END, a)
            speak("Pardon me, please say that again")
            return "None"
        return statement
def calcy():
    r = sr.Recognizer()
    my_mic_device = sr.Microphone(device_index=1)
    try:
        with my_mic_device as source:
            a="\nSay what you want to calculate,"
            textArea.insert(tk.END,a)
            speak("Say what you want to calculate")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
    except sr.UnknownValueError:
        pass
    my_string = r.recognize_google(audio)
    textArea.insert(tk.END,my_string)
    def get_operator_fn(op):
        return {
            '+': operator.add,
            '-': operator.sub,
            'x': operator.mul,
            'divided': operator.__truediv__,
            'Mod': operator.mod,
            'mod': operator.mod,
            '^': operator.xor,
        }[op]
    def eval_binary_expr(op1, oper, op2):
        op1, op2 = int(op1), int(op2)
        return get_operator_fn(oper)(op1, op2)
    b=eval_binary_expr(*(my_string.split()))
    c=("="+str(b))
    textArea.insert(tk.END,c)
    speak(b)
def notepad():
    def open_Notepad(MyText):
        f = open(r"C:\Users\Vaishnavi\OneDrive\Desktop\testing.txt", "a")
        f.write(MyText)
        f.close()
        os.startfile(r"C:\Users\Vaishnavi\OneDrive\Desktop\testing.txt")
    speak("Speak what you want to type in notepad")
    a="Speak what you want to type in notepad"
    textArea.insert(tk.END, a)
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)
            audio= r.listen(source)
            notepad_variable = r.recognize_google(audio)
            open_Notepad(notepad_variable)
    except sr.UnknownValueError:
        pass
def commands(s):
            if s == 0:
                window.mainloop()
            elif ("good bye" in s or "bye" in s or "stop" in s or "exit" in s or "close" in s):
                speak('your personal assistant is shutting down,bye bye')
                # a='your personal assistant is shutting down,bye bye'
            elif ("hello" in s or "hi" in s or "good" in s):
                a = '\nHello! I am your personal assistant , How can i help you?'
                textArea.insert(tk.END, a)
                speak('Hello! I am your personal assistant , How can i help you?')
            elif 'wikipedia' in s:
                speak('Searching Wikipedia...')
                s = s.replace("wikipedia", "")
                results = wikipedia.summary(s, sentences=3)
                speak("According to Wikipedia")
                a = results
                textArea.insert(tk.END, a)
                speak(results)
            elif 'calculate' in s or 'plus' in s or 'minus' in s:
                calcy()
            elif 'open youtube' in s or 'youtube' in s:
                webbrowser.open_new_tab("https://www.youtube.com")
                speak("youtube is open now")
            elif 'open whatsapp' in s or 'whatsapp' in s:
                webbrowser.open_new_tab("https://web.whatsapp.com/")
                speak("whatsapp is open now,u can login")
            elif 'open google' in s or 'google' in s:
                webbrowser.open_new_tab("https://www.google.com")
                speak("Google chrome is open now")
            elif 'open gmail' in s or 'mail' in s:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
            elif 'meet' in s or 'join meet' in s:
                webbrowser.open_new_tab("https://meet.google.com/")
                speak("Google Meet open now")
            elif 'netflix' in s:
                webbrowser.open_new_tab("https://www.netflix.com/browse")
                speak("opening...NETFLIX")
            elif 'prime' in s:
                webbrowser.open_new_tab(
                    "https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_g_67_mkw_swoIqHOSO-dc&mrntrk=pcrid_423192672131_slid__pgrid_82649959367_pgeo_9062188_x__ptid_kwd-61602341")
                speak("opening...PRIME VIDEO")
            elif 'hotstar' in s:
                webbrowser.open_new_tab("https://www.hotstar.com/in")
                speak("opening...HOTSTAR")
            elif 'wynk' in s or 'music' in s:
                webbrowser.open_new_tab(
                    "https://wynk.in/music?gclid=CjwKCAjw4qCKBhAVEiwAkTYsPGM460uYugTQh9lqxcuuYFpQOII3diw0jyJxqQMhIiEifV5fqFDeDBoC-64QAvD_BwE")
                speak("opening...wynk MUSIC")
            elif 'lms' in s or 'cbit' in s:
                webbrowser.open_new_tab("https://learning.cbit.org.in/")
                speak("opening...CBIT LMS")
            elif 'calendar' in s or 'event' in s:
                webbrowser.open_new_tab("https://calendar.google.com/calendar/u/0/r?tab=rc&pli=1")
                speak("opening...GOOGLE CALENDER")
            elif 'udemy' in s:
                webbrowser.open_new_tab("https://www.udemy.com/")
                speak("opening...UDEMY")
            elif 'time' in s:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                a = f"the time is {strTime}"
                textArea.insert(tk.END, a)
                speak(f"the time is {strTime}")
            elif 'news' in s:
                webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
            elif 'search' in s:
                s = s.replace("search", "")
                webbrowser.open_new_tab(s)
            elif 'who are you' in s or 'what can you do' in s or 'you' in s:
                a ='I am your personal assistant. I am programmed to minor tasks like opening any web application and any installed apps ,predict time,search wikipedia,predict time get top headline news from times of india and you can ask me computational or geographical questions too!'
                textArea.insert(tk.END, a)
                speak('I am your personal assistant. I am programmed to minor tasks like'
                      'opening any web application and any installed apps ,predict time,search wikipedia,predict time'
                      ' get top headline news from times of india and you can ask me computational or geographical questions too!')
            elif "google" in s or "search" in s or "web browser" in s or "chrome" in s or "browser" in s:
                a = "Opening...GOOGLE CHROME"
                textArea.insert(tk.END, a)
                speak("Opening")
                speak("GOOGLE CHROME")
                os.system("chrome")
            elif 'IE' in s or 'microsoft edge' in s or "edge" in s:
                a = "Opening...MICROSOFT EDGE"
                textArea.insert(tk.END, a)
                speak("Opening")
                speak("MICROSOFT EDGE")
                os.system("msedge")
            elif "note" in s or "notes" in s or "notepad" in s or "editor" in s:
                notepad()
            elif "VLC player" in s or "player" in s or "video player" in s:
                a = "Opening...VLC PLAYER"
                textArea.insert(tk.END, a)
                speak("Opening")
                speak("VLC PLAYER")
                os.system("VLC")
            elif "illustrator" in s or "AI" in s:
                a = "Opening...ADOBE ILLUSTRATOR"
                textArea.insert(tk.END, a)
                speak("Opening")
                speak("ADOBE ILLUSTRATOR")
                os.system("illustrator")
            elif "photoshop" in s or "PS" in s or "PHOTOSHOP CC" in s:
                try:
                    os_cmd = 'photoshop'
                    if os.system(os_cmd) != 0:
                        raise Exception('Photoshop is not installed')
                except:
                    a = "\ncommand does not work,Photoshop is not installed "
                    textArea.insert(tk.END, a)
                    speak("Photoshop is not installed")
                    webbrowser.open_new_tab("https://www.photopea.com/")
                    speak("\nopening...ONLINE PHOTOSHOP")
                    a = 'opening...ONLINE PHOTOSHOP'
                    textArea.insert(tk.END, a)
            elif "telegram" in s or "TG" in s:
                try:
                    os_cmd = 'telegram'
                    if os.system(os_cmd) != 0:
                        raise Exception('Telegram is not installed')
                except:
                    a = "\ncommand does not work,Telegram is not installed "
                    textArea.insert(tk.END, a)
                    speak("Telegram is not installed")
                    webbrowser.open_new_tab("https://web.telegram.org/k/")
                    speak("opening...TELEGRAM WEB")
                    a = 'opening...TELEGRAM WEB'
                    textArea.insert(tk.END, a)
            elif "camera" in s or "take a photo" in s or "capture" in s:
                ec.capture(0, "robo camera", "img.jpg")
            elif "excel" in s or "MS excel" in s or "sheet" in s or "win excel" in s:
                try:
                    os_cmd = 'excel'
                    a = "Opening...MS EXCEL"
                    textArea.insert(tk.END, a)
                    speak("Opening")
                    speak("MS excel")
                    if os.system(os_cmd) != 0:
                        raise Exception('MS excel is not installed')
                except:
                    a = "\ncommand does not work,MS excel is not installed "
                    textArea.insert(tk.END, a)
                    speak("MS excel is not installed")
                    webbrowser.open_new_tab("https://docs.google.com/spreadsheets/u/0/")
                    speak("opening...GOOGLE SHEETS")
                    a = '\nopening...GOOOGLE SHEETS'
                    textArea.insert(tk.END, a)
            elif "cisco" in s or "webex" in s:
                try:
                    os_cmd = 'ptoneclk'
                    a = "\nOpening...CISCO WEBEX"
                    textArea.insert(tk.END, a)
                    speak("Opening")
                    speak("CISCO WEBEX MEET")
                    if os.system(os_cmd) != 0:
                        raise Exception('CISCO WEBEX MEET is not installed')
                except:
                    a = "\ncommand does not work,CISCO WEBEX MEET is not installed "
                    textArea.insert(tk.END, a)
                    speak("CISCO WEBEX is not installed")
                    webbrowser.open_new_tab("https://www.webex.com/")
                    speak("opening...ONLINE WEBEX MEET")
                    a = '\nopening...ONLINE WEBEX MEET'
                    textArea.insert(tk.END, a)
            elif "slide" in s or "powerpoint" in s or "PPT" in s or "POWERPNT" in s:
                try:
                    os_cmd = 'powerpnt'
                    a = "\nOpening...POWERPOINT"
                    textArea.insert(tk.END, a)
                    speak("Opening")
                    speak("POWERPOINT")
                    if os.system(os_cmd) != 0:
                        raise Exception('Powerpoint is not installed')
                except:
                    a = "command does not work,Powerpoint is not installed "
                    textArea.insert(tk.END, a)
                    speak("Powerpoint is not installed")
                    webbrowser.open_new_tab("https://docs.google.com/presentation/u/0/")
                    speak("opening...GOOGLE SLIDES")
                    a = '\nopening...GOOOGLE SLIDES'
                    textArea.insert(tk.END, a)
            elif "word" in s or "MS word" in s:
                try:
                    os_cmd = 'winword'
                    a = "\nOpening...MS WORD"
                    textArea.insert(tk.END, a)
                    speak("Opening")
                    speak("MS word")
                    if os.system(os_cmd) != 0:
                        raise Exception('MS WORD is not installed')
                except:
                    a = "\ncommand does not work,MS WORD is not installed "
                    textArea.insert(tk.END, a)
                    speak("MS word is not installed")
                    webbrowser.open_new_tab("https://docs.google.com/document/u/0/")
                    speak("opening...GOOGLE docs")
                    a = '\nopening...GOOOGLE DOCS'
                    textArea.insert(tk.END, a)
            elif "NFS" in s or "speed" in s or 'game' in s:
                a = "\nOpening...NFS NEED FOR SPEED"
                textArea.insert(tk.END, a)
                speak("Opening")
                speak("NFS NEED FOR SPEED")
                os.system("NEED FOR SPEED PAYBACK")
            elif "exit" in s or "quit" in s or "close" in s:
                a = "\nExiting"
                textArea.insert(tk.END, a)
                speak("Exiting")
                # break
            else:
                a = "\ncant perform the task specified"
                textArea.insert(tk.END, a)
                speak("cant perform the task specified")
def cmd():
   #while True:
            speak("Tell me how can I help you now?")
            s= takeCommand().lower()
            commands(s)
def chatin():
    inp = inputtxt.get(1.0, "end-1c")
    commands(inp)
def start():
    w.destroy()
    global window
    window= tk.Tk()
    global textArea
    global inputtxt
    window.geometry("1000x800")
    window.title("Python Voice Assistant!")
    name = tk.Label(text="Click on speak to command", font=("Times New Roman",20))
    name.grid(column=0)
    textArea = tk.Text(master=window,bg='light yellow', height=15, width=45)
    textArea.place(x=20,y=50)
    textArea.configure(font=("Times New Roman",18))
    name2 = tk.Label(text="Or give command by texting", font=("Times New Roman",20))
    name2.place(x=20,y=460)
    inputtxt = tk.Text(window,bg='light yellow',height=5, width=40)
    inputtxt.place(x=50, y=500)
    inputtxt.configure(font=("Times New Roman",18))
    b="try typing 'open youtube' ;)"
    inputtxt.insert(tk.END,b)
    printButton = tk.Button(window, text="OKAY", command=chatin,font=("Times New Roman", 15),fg="white", bg="green")
    printButton.place(x=250,y=640)
    a="Loading your Python Voice assistant"
    textArea.insert(tk.END,a)
    speak("Loading your Python Voice assistant ")
    wishMe()
    load = Image.open("C:/Users/Vaishnavi/OneDrive/Desktop/vAssistant.jpg")
    render = ImageTk.PhotoImage(load)
    img = tk.Label(window, image=render)
    img.place(x=600, y=30)
    button3 = tk.Button(window, text="CLOSE", font=("Arial", 15), command=window.destroy, fg="white", bg="green")
    button3.place(x=780,y=500)
    while True:
        button2 = tk.Button(window, text="SPEAK", font=("Arial", 15), command=lambda:cmd(), fg="white", bg="green")
        button2.place(x=680,y=500)
        window.mainloop()
w = tk.Tk()
w.geometry("680x450")
w.title("Python Voice Assistant!")
name = tk.Label(text = "PYTHON VOICE ASSISTANT",font=("Calibri",20))
name.grid(column=0)
image1 = ImageTk.PhotoImage(Image.open("s2.jpeg"))
button1=tk.Button(w,text="START",font=("Arial",15),command=start,fg="white",bg="blue")
button1.place(x=200,y=400)
button=tk.Button(w,text="QUIT",font=("Arial",15),command=quit,fg="white",bg="red")
button.place(x=400,y=400)
load = Image.open("C:/Users/Vaishnavi/OneDrive/Desktop/mike.png")
render = ImageTk.PhotoImage(load)
img = tk.Label(w, image=render)
img.place(x=200, y=100)
w.mainloop()
