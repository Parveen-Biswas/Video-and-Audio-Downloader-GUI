import tkinter as tk
from tkinter import *
from pytube import YouTube
import tkinter.messagebox as tmes

class type2(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self,bg="lightyellow")

        # label and entry for url
        info_label = tk.Label(self, text="Enter Your URL", font="Arial 12 ", bg="lightyellow")
        info_label.place(x=40, y=20)
        url_entry = tk.Entry(self, width=50, relief=SOLID, border=2 ,font="monotype 11 bold",)
        url_entry.place(x=40, y=50)

        # download info
        def download(url):
            url = YouTube(url_entry.get())
            stream = url.streams.get_audio_only()
            stream.download()
            tmes.showinfo("Download","Audio Download Successfully")

        # button for download
        download_button = tk.Button(self, text="Download", width=20, height=1, relief=SOLID ,font="Arial 12 bold" ,fg="white" ,activeforeground="red" ,bg="red", activebackground="white", command=lambda: download(url_entry.get()))
        download_button.place(x=150, y=100)