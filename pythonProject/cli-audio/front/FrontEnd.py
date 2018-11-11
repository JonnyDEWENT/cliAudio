import curses
import curses.textpad
import os
import sys
from cliExceptions.CLI_Exception import CLI_Audio_File_Exception

class FrontEnd:

    def __init__(self, player,library):
        self.player = player
        self.library = library
        self.directory = "./media/playlist1"
        self.playlist = []
        self.player.play('./media/playlist1/bird.wav')
        curses.wrapper(self.menu)

    def menu(self, args):
        self.stdscr = curses.initscr()
        self.stdscr.border()
        self.stdscr.addstr(0,0, "cli-audio",curses.A_REVERSE)
        self.stdscr.addstr(5,10, "c - Change current song")
        self.stdscr.addstr(6,10, "p - Play/Pause")
        self.stdscr.addstr(7,10, "l - Library")
        self.stdscr.addstr(9,10, "ESC - Quit")
        self.updateSong()
        self.stdscr.refresh()
        self.stdscr.addstr(14,10, "Available Songs: ")
        self.setPlaylist()
        self.displayPlaylist()
        while True:
            self.stdscr.addstr(13,10, "Current Directory: " + self.directory)
            c = self.stdscr.getch()
            if c == 27:
                self.quit()
            elif c == ord('p'):
                self.player.pause()
            elif c == ord('c'):
                self.changeSong()
                self.updateSong()
                self.stdscr.touchwin()
                self.stdscr.refresh()
            elif c == ord('l'):
                self.library.showLibrary(self)


    def updateSong(self):
        self.stdscr.addstr(15,10, "                                        ")
        self.stdscr.addstr(11,10, "Now playing: " + self.player.getCurrentSong())

    def changeSong(self):
        changeWindow = curses.newwin(5, 40, 5, 50)
        changeWindow.border()
        changeWindow.addstr(0,0, "Please Enter the index of the song", curses.A_REVERSE)
        self.stdscr.refresh()
        curses.echo()
        path = changeWindow.getstr(1,1, 1)
        if (int(path) > len(self.playlist)):
            raise CLI_Audio_File_Exception("The song requested is not available in the playlist","CLI_AUDIO_FILE_EXCEPTION!")
        curses.noecho()
        del changeWindow
        self.stdscr.touchwin()
        self.stdscr.refresh()
        self.player.stop()
        index = self.playlist[int(path)-1]
        songs = os.listdir(self.directory)
        song = self.directory + index
        self.player.play(song)

    def displayPlaylist(self):

        x = 1
        for song in self.playlist:
            self.stdscr.addstr(15 + x,10, str(x) + ": "+ song)
            x = x + 1

    def setDirectory(self,dir):
        self.directory = dir

    def setPlaylist(self):
        self.playlist = []
        songs = os.listdir(self.directory)
        x = 0
        for song in songs:
            self.playlist.append(song)
            x = x + 1

    def quit(self):
        self.player.stop()
        exit()
