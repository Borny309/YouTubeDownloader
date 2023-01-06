import tkinter as tk
import youtube_dl
from tkinter import filedialog
from PIL import Image, ImageTk

def choose_path():
    path = tk.filedialog.askdirectory()
    path_entry.delete(0, "end")
    path_entry.insert(0, path)

def download():
    ydl_opts = {
        'outtmpl': '{}/%(title)s.%(ext)s'.format(path.get())
    }
    if format.get() == "MP3":
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link.get()])
        tk.Label(root, text="DOWNLOADED", font="arial 15").pack()
    except Exception as e:
        tk.Label(root, text="An error occurred: {}".format(str(e)), font="arial 15").pack()

root = tk.Tk()
root.geometry("500x500+0+0")
root.resizable(0, 0)
root.title("YouTube Downloader")

link = tk.StringVar()
path = tk.StringVar()

# Create the widgets and add them to the window
tk.Label(root, text="Download Youtube videos for free", font="san-serif 14 bold", bg='#ffffff').pack()

tk.Label(root, text="Paste your link here", font="san-serif 15 bold", bg='#ffffff').pack()
link_enter = tk.Entry(root, width=70, textvariable=link, bg='#ffffff')
link_enter.pack()

tk.Label(root, text="Choose the download path", font="san-serif 15 bold", bg='#ffffff').pack()
path_entry = tk.Entry(root, width=50, textvariable=path, bg='#ffffff')
path_entry.pack()
path_button = tk.Button(root, text="Choose path", command=choose_path, bg='#ffffff')
path_button.pack()

# Create the radio buttons and add them to the window
format = tk.StringVar()
format.set("MP4")  # Set the default value to MP4
tk.Radiobutton(root, text="MP4", variable=format, value="MP4", bg='#ffffff').pack()
tk.Radiobutton(root, text="MP3", variable=format, value="MP3", bg='#ffffff').pack()

# Load the image and convert it to a PhotoImage object
image = Image.open("neurons.png")
image = ImageTk.PhotoImage(image)

# Create a label to display the image and set its background image
label = tk.Label(root, image=image)
label.pack()

# Set the label's background color to a transparent color
label.config(bg='#ffffff')

tk.Button(root, text='Download', font='san-serif 16 bold', bg='red', padx=2, command=download).place(x=185, y=250)



root.mainloop()