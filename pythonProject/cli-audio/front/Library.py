import curses
import curses.textpad
import os
import sys

class Library:

        def _init_(self):
            self.files = os.listdir('./media')



        def showLibrary(self):
            x = 0
            print(x)
            # changeWindow = curses.newwin(50, 50, 5, 5)
            # x = 1
            # for name in files:
            #     changeWindow.border()
            #     changeWindow.addstr(2+x,2, name)
            #     x = x + 1
            # num = 1
            # for name in files:
            #     changeWindow.border()
            #     changeWindow.addstr(2+x,2, num)
            #     x = x + 1
            #     num = num + 1
            # # parentView.stdscr.refresh()
            # curses.echo()
            # path = changeWindow.getstr(1,1, 30)
            # curses.noecho()
            # del changeWindow
            # parentView.stdscr.touchwin()
            # parentView.stdscr.refresh()
