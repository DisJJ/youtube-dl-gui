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

        self.greet_button = Button(master, text="Download video", command=self.download)
        self.greet_button.place(x=125, y=100, anchor='e')

        self.thumbnail_button = Button(master, text="Thumbnail", command=self.thumbnail_only)
        self.thumbnail_button.place(x=94, y=70, anchor='e')

        self.playlist_button = Button(master, text="Playlist", command=self.playlist)
        self.playlist_button.place(x=71, y=40, anchor='e')

        self.linkentry = Entry(master)
        self.linkentry.place(x=85, y=160, anchor='center')

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.place(rely=1.0, relx=1.0, x=0, y=0, anchor='se')

    def download(self):
        self.directory = ("/media/jared/Media Library/YouTube Videos/")
        self.link_of_video = (self.linkentry.get())
        print("Queuing download")
        print("Link: ", self.link_of_video)
        os.chdir(self.directory)
        call(["youtube-dl", "-f", "18", self.link_of_video])
        print("[+]Operation Complete")
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
