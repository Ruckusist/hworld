# hworld/client/__main__.py
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

"""Hworld terminal client entry point"""

import sys
import curses
import deskapp
from hworld.client import HworldClient


def GetInput(stdscr, prompt):
    """Get user input in curses"""
    height, width = stdscr.getmaxyx()
    curses.echo()
    stdscr.addstr(height - 3, 2, prompt)
    stdscr.refresh()
    inputStr = stdscr.getstr(height - 3, 2 + len(prompt), 30)
    curses.noecho()
    stdscr.addstr(height - 3, 2, " " * (width - 4))
    return inputStr.decode("utf-8")


def Main():
    """Start the hworld terminal client"""

    def RunClient(stdscr):
        """Run the client with curses"""
        app = deskapp.App([HworldClient])

        # Get the client module instance
        clientModule = None
        for mod in app.Modules:
            if isinstance(mod, HworldClient):
                clientModule = mod
                break

        # Custom key handler
        originalKeyHandler = app.KeyHandler

        def CustomKeyHandler(key):
            """Handle custom keys"""
            if key == ord("c"):
                if not clientModule.Connected:
                    clientModule.Connect()
                return True
            elif key == ord("l"):
                if clientModule.Connected and not clientModule.Username:
                    username = GetInput(stdscr, "Username: ")
                    password = GetInput(stdscr, "Password: ")
                    if username and password:
                        clientModule.Login(username, password)
                return True
            elif key == ord("t"):
                if clientModule.Username:
                    clientModule.TestPing()
                return True
            elif key == ord("o"):
                if clientModule.Username:
                    clientModule.Logout()
                return True
            elif key == ord("d"):
                if clientModule.Connected:
                    clientModule.Disconnect()
                return True
            else:
                return originalKeyHandler(key)

        app.KeyHandler = CustomKeyHandler
        app.Start()

    curses.wrapper(RunClient)
    return 0


if __name__ == "__main__":
    sys.exit(Main())
