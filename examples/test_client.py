#!/usr/bin/env python3
# examples/test_client.py
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

"""Simple test client for hworld server"""

import socket
import time
from deskapp.server import Message


def TestClient():
    """Connect to server and test login"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("localhost", 28080))

    print("Connected to server")

    # Send login message
    loginMsg = Message({
        "login": True,
        "username": "testuser",
        "password": "testpass"
    })
    sock.send(loginMsg.serialize())
    print("Sent login request")

    # Receive response
    data = sock.recv(1024)
    response = Message.deserialize(data)
    print(f"Login response: {response.login}")

    # Send test ping
    testMsg = Message({"test": True})
    sock.send(testMsg.serialize())
    print("Sent test ping")

    # Receive pong
    data = sock.recv(1024)
    response = Message.deserialize(data)
    print(f"Test response: {response.test}")

    # Logout
    logoutMsg = Message({"logout": True})
    sock.send(logoutMsg.serialize())
    print("Sent logout")

    sock.close()
    print("Disconnected")


if __name__ == "__main__":
    TestClient()
