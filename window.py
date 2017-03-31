#!/usr/bin/env python3

from tkinter import Tk, Label, Button, Entry, Menu
import os
import sys
from subprocess import call

class Window:
    def __init__(self, master):
        self.master = master
        master.minsize(width=200, height=175)
        master.title("Axel")

        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.subMenu = Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.subMenu, command=self.echofile)

        self.label = Label(master, text="youtube-dl front end", font=('bold'))
        self.label.place(x=150, y=100, anchor='center')

        self.options_label = Label(master, text="Options", font=('bold'))
        self.options_label.grid(sticky='E')

        self.new_label = Label(master, text="Link")
        self.new_label.grid(row=6, column=1)

        self.greet_button = Button(master, text="Download video", command=self.download)
        self.greet_button.grid(column=1, sticky='E')

        self.thumbnail_button = Button(master, text="Thumbnail", command=self.thumbnail_only)
        self.thumbnail_button.grid(sticky='E')

        self.playlist_button = Button(master, text="Playlist", command=self.playlist)
        self.playlist_button.grid(sticky='E')

        self.linkentry = Entry(master)
        self.linkentry.place(x=135, y=100, anchor='center')

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=11, column=5, sticky='S')

    def download(self):
        self.directory = ("/media/jared/Media Library/YouTube Videos/")
        self.link_of_video = (self.linkentry.get())
        print("Queuing download")
        print("Link: ", self.link_of_video)
        os.chdir(self.directory)
        call(["youtube-dl", "-f", "18", self.link_of_video])
    def thumbnail_only(self):
        self.directory = ("/media/jared/Media Library/Youtube Thumbnails/")
        self.link_of_video = (self.linkentry.get())
        print("Grabbing thumbnail from: ", self.link_of_video)
        os.chdir(self.directory)
        call(["youtube-dl", "--write-thumbnail", "--skip-download", self.link_of_video])
    def echofile(self):
        print("File")
    def playlist(self):
        self.directory = ("/media/jared/Media Library/Youtube Playlists/")
        self.link_of_video = (self.linkentry.get())
        print("Grabbing playlist from: ", self.link_of_video)
        os.chdir(self.directory)
        call(["youtube-dl", "--yes-playlist", self.link_of_video])
root = Tk()
my_gui = Window(root)
root.mainloop()
