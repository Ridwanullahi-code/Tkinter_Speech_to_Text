from tkinter import*
from PIL import ImageTk,Image 
import sounddevice as sd
import speech_recognition as sr
from textblob import TextBlob


def speech_button():
	global r, audio
	r = sr.Recognizer()
	with sr.Microphone() as source:
		audio = r.listen(source)

def Convert_button():
	text = r.recognize_google(audio)
	b = TextBlob(text)
	text2.insert(END,b.correct())

def clear_button():
	text2.delete(1.0,END)	

def Speech_Text():
	Display_root()
	Display_title()
	Display_speech()
	Display_text()
	Display_button()
	root.mainloop()

def Display_root():
	global root,arrow_logo,speaker_logo
	root = Tk()
	root.geometry("835x468+335+172")
	root.title("Music App")
	root.resizable(width=NO,height=NO)
	root.config(bg="#F7F7F7")
	arrow_logo = ImageTk.PhotoImage(Image.open("arrow.png"))
	speaker_logo = ImageTk.PhotoImage(Image.open("speaker.png"))

def Display_title():
	title = Label(root,text="SPEECH-TEXT CONVERTER",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	title.place(x=0,y=0,width=835)
	arrow = Label(root,image=arrow_logo)
	arrow.place()

def Display_speech():
	global sec_entry
	label = Label(root,text="SPEECH",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	label.place(x=70,y=70,width=200)
	speaker = Label(root,image = speaker_logo)
	speaker.place(x=120,y=132)

	bt = Button(root,text="START SPEECH",bg='white',font=("Roboto",15,"bold"),command = speech_button)
	bt.place(x=90,y=399)
	arrow = Label(root,image=arrow_logo)
	arrow.place(x=280,y=170)

def Display_text():
	global text2
	label = Label(root,text="TEXT",bd=5,bg="white",font=("Roboto",25,"bold"),relief=GROOVE)
	label.place(x=560,y=70,width=200)
	text_frame = Frame(root,bg="white")
	text_frame.place(x=500,y=130,width=320,height=200)

	scrollbar = Scrollbar(text_frame,orient=VERTICAL)
	scrollbar.pack(side=RIGHT,fill="y")
	text2 = Text(text_frame,bg="white",font=("Roboto",13,"bold"),yscrollcommand=scrollbar.set)
	text2.pack(side=LEFT)
	scrollbar.configure(command=text2.yview)
	
def Display_button():
	convt = Button(root,text="CONVERT",fg="white",bg='#B200ED',font=("Roboto",15,"bold"),command=Convert_button)
	convt.place(x=280,y=280,width=160)
	clear = Button(root,text="CLEAR",fg="white",bg='red',font=("Roboto",15,"bold"),command=clear_button)
	clear.place(x=450,y=399,width=160)
print(Speech_Text())