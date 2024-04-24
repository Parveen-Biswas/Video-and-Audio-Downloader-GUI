import tkinter as tk
from tkinter import *
from pytube import YouTube
import tkinter.messagebox as tmes

class type1(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        tk.Frame.configure(self,bg="lightyellow")

        # label and entry for url
        info_label = tk.Label(self, text="Enter Your URL", font="Arial 12 ", bg="lightyellow")
        info_label.place(x=40, y=20)
        url_entry = tk.Entry(self, width=50, relief=SOLID, border=2 ,font="monotype 11 bold",)
        url_entry.place(x=40, y=50)

        # check button
        rand_resolution = IntVar()
        low_qlty = tk.Radiobutton(self, text="Low", variable=rand_resolution, font="Arial 12 bold" , value=1, bg="lightyellow", activebackground="lightyellow")
        low_qlty.place(x=50, y=85)
        high_qlty = tk.Radiobutton(self, text="High", variable=rand_resolution, font="Arial 12 bold" , value=2, bg="lightyellow", activebackground="lightyellow")
        high_qlty.place(x=50, y=120)

        # download info
        def download(url, resolution):
            if resolution == 1:
                # print("Downloading in low quality")
                url = YouTube(url_entry.get())
                stream = url.streams.get_lowest_resolution()
                stream.download()
                # print("Downloaded")
                tmes.showinfo("Download","Video Download Successfully")

            elif resolution == 2:
                # print("Downloading in high quality") 
                url = YouTube(url_entry.get())
                stream = url.streams.get_highest_resolution()
                stream.download()
                # print("Downloaded")
                tmes.showinfo("Download","Video Download Successfully")

            else:
                tmes.showinfo("Error","Please Select Your Resolution") 


        # button for download
        download_button = tk.Button(self, text="Download", width=20, height=1, relief=SOLID ,font="Arial 12 bold" ,fg="white" ,activeforeground="red" ,bg="red", activebackground="white", command=lambda: download(url_entry.get(), rand_resolution.get()))
        download_button.place(x=190, y=100)