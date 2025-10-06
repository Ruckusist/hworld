# hworld/client/app.py
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

"""Hworld terminal client - deskapp Module implementation"""

import os
import random
from deskapp import Module
from deskapp.server import Message, ClientSession


class HworldClient(Module):
    """Hworld terminal client module"""

    name = "Hworld Client"

    def __init__(self, app):
        super().__init__(app, random.random())
        self.ClassId = random.random()
        self.Session = None
        self.Username = None
        self.Connected = False
        self.Status = "Not connected"
        self.Messages = []
        self.ServerHost = os.getenv("HWORLD_SERVER_HOST", "localhost")
        self.ServerPort = int(os.getenv("HWORLD_SERVER_PORT", "28080"))

    def Page(self, panel):
        """Render the client interface"""
        win = panel.win
        height, width = win.getmaxyx()

        # Title
        title = "=== HWORLD CLIENT ==="
        win.addstr(1, (width - len(title)) // 2, title)

        # Connection status
        statusLine = f"Status: {self.Status}"
        win.addstr(3, 2, statusLine)

        if self.Username:
            userLine = f"Logged in as: {self.Username}"
            win.addstr(4, 2, userLine)

        # Server info
        serverLine = f"Server: {self.ServerHost}:{self.ServerPort}"
        win.addstr(5, 2, serverLine)

        # Instructions
        if not self.Connected:
            win.addstr(7, 2, "Press 'c' to connect")
        elif not self.Username:
            win.addstr(7, 2, "Press 'l' to login")
        else:
            win.addstr(7, 2, "Press 't' to test ping")
            win.addstr(8, 2, "Press 'o' to logout")

        # Messages
        if self.Messages:
            win.addstr(10, 2, "=== Messages ===")
            for i, msg in enumerate(self.Messages[-10:]):
                if 11 + i < height - 2:
                    msgLine = msg[:width - 4]
                    win.addstr(11 + i, 2, msgLine)

        # Help
        win.addstr(height - 2, 2, "Press 'q' to quit")

        return False

    def Connect(self):
        """Connect to the server"""
        try:
            self.Session = ClientSession(
                host=self.ServerHost,
                port=self.ServerPort
            )
            self.Connected = True
            self.Status = "Connected"
            self.AddMessage(
                f"Connected to {self.ServerHost}:{self.ServerPort}"
            )
        except Exception as e:
            self.Status = f"Connection failed: {e}"
            self.AddMessage(f"Error: {e}")

    def Login(self, username, password):
        """Login to the server"""
        if not self.Connected:
            self.AddMessage("Not connected to server")
            return

        try:
            loginMsg = Message({
                "login": True,
                "username": username,
                "password": password
            })
            self.Session.SendMessage(**loginMsg)

            # Wait for response
            response = self.Session.ReceiveMessage()
            if response.login:
                self.Username = username
                self.Status = f"Logged in as {username}"
                self.AddMessage(f"Login successful: {username}")
            else:
                self.AddMessage("Login failed")
                self.Status = "Login failed"
        except Exception as e:
            self.AddMessage(f"Login error: {e}")

    def TestPing(self):
        """Send test ping to server"""
        if not self.Session:
            self.AddMessage("Not connected")
            return

        try:
            testMsg = Message({"test": True})
            self.Session.SendMessage(**testMsg)

            response = self.Session.ReceiveMessage()
            if response.test:
                self.AddMessage("Ping successful! Pong received.")
            else:
                self.AddMessage("Ping failed")
        except Exception as e:
            self.AddMessage(f"Ping error: {e}")

    def Logout(self):
        """Logout from server"""
        if not self.Session:
            return

        try:
            logoutMsg = Message({"logout": True})
            self.Session.SendMessage(**logoutMsg)
            self.Username = None
            self.Status = "Logged out"
            self.AddMessage("Logged out")
        except Exception as e:
            self.AddMessage(f"Logout error: {e}")

    def Disconnect(self):
        """Disconnect from server"""
        if self.Session:
            self.Session.Disconnect()
            self.Session = None
        self.Connected = False
        self.Username = None
        self.Status = "Disconnected"
        self.AddMessage("Disconnected from server")

    def AddMessage(self, msg):
        """Add a message to the display"""
        self.Messages.append(msg)
        if len(self.Messages) > 50:
            self.Messages = self.Messages[-50:]
