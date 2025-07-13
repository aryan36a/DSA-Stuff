import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

#frame]
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI 
title=customtkinter.CTkLabel(app,text="Insert a youtube link")
title.pack(padx=10, pady=10)

#Link input
url_variable=tkinter.StringVar()
link=customtkinter.CTkEntry(app,width=350, height=40,textvariable=url_variable) 
link.pack()


#run app
app.mainloop()