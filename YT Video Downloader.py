from tkinter import *
from pyyoutube import Api
from pytube import YouTube
from threading import Thread
from tkinter import messagebox

# Create Object
root = Tk()
# Set geometry
root.geometry('400x200')

# Add Label
Label(root, text="Yt Playlist Downloader",
	font="italic 15 bold").pack(pady=10)
Label(root, text="Enter the Playlist URL:-", font="italic 10").pack()

# Add Entry box
playlistId = Entry(root, width=60)
playlistId.pack(pady=5)

download_start = Button(root, text="Start The Download", command=threading)
download_start.pack(pady=10)

# Execute Tkinter
root.mainloop()
