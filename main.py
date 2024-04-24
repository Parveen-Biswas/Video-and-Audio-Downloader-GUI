from tkinter import *
from tkinter import ttk
from tab1 import *
from tab2 import *
from tkinter.messagebox import askyesno

root = Tk()
root.geometry("500x200+400+200")
root.resizable(False, False)
icon_image = PhotoImage (file = "icon.png")
root.iconphoto(False, icon_image)
root.title("Video and Audio Downloader")

# To destroy window
def close():
    comfimation = askyesno(title="Exit", message="Do you want to Exit ?")
    if comfimation:
        root.destroy()
root.protocol("WM_DELETE_WINDOW", close)

# notebook for tabs
notebook = ttk.Notebook(root)

# tab for video and audio
tab1 = type1(notebook)
tab2 = type2(notebook)

# Add the tabs to window
notebook.add(tab1, text="Video")
notebook.add(tab2, text="Audio")
notebook.pack(expand=True, fill="both")

root.mainloop()