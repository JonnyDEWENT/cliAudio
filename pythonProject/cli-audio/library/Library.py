import curses
import curses.textpad
import os
import sys

class Library:

        def _init_():
            self.files = os.listdir('./media')

        def showLibrary(self, parentView):

            changeWindow = curses.newwin(50, 50, 5, 5)
            changeWindow.addstr(2,10, "Available Playlists:")
            files = os.listdir('./media')
            x = 1
            for name in files:
                changeWindow.border()
                changeWindow.addstr(2+x,4, name)
                x = x + 1

            x = 1
            for name in files:
                changeWindow.border()
                changeWindow.addstr(2+x,2, str(x))
                x = x + 1

            parentView.stdscr.refresh()
            curses.echo()
            index = changeWindow.getstr(1,1, 1)
            parentView.setDirectory('./media/' + files[int(index)-1] + '/')
            parentView.setPlaylist()
            parentView.displayPlaylist()
            curses.noecho()
            del changeWindow
            parentView.stdscr.touchwin()
            parentView.stdscr.refresh()
