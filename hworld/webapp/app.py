# hworld/webapp/app.py
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

"""Hworld web application using deskapp.webapp"""

import os
from flask import jsonify, request
from deskapp.webapp import WebApp
from deskapp.server import Message
import socket


def CreateApp():
    """Create and configure the hworld web application"""

    # Get template and static paths
    currentDir = os.path.dirname(os.path.abspath(__file__))
    templateFolder = os.path.join(currentDir, "templates")
    staticFolder = os.path.join(currentDir, "static")

    webapp = WebApp(
        Name="Hworld",
        Host="0.0.0.0",
        Port=8080,
        TemplateFolder=templateFolder,
        StaticFolder=staticFolder
    )

    # Add API endpoints
    @webapp.Route("/api/login", methods=["POST"])
    def ApiLogin():
        """Handle login via server"""
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        try:
            # Connect to hworld server
            serverHost = os.getenv("HWORLD_SERVER_HOST", "localhost")
            serverPort = int(os.getenv("HWORLD_SERVER_PORT", "28080"))

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((serverHost, serverPort))

            # Send login message
            loginMsg = Message({
                "login": True,
                "username": username,
                "password": password
            })
            sock.send(loginMsg.serialize())

            # Receive response
            data = sock.recv(1024)
            response = Message.deserialize(data)

            sock.close()

            return jsonify({
                "success": response.login,
                "username": username if response.login else None
            })

        except Exception as e:
            return jsonify({
                "success": False,
                "error": str(e)
            }), 500

    @webapp.Route("/api/test", methods=["POST"])
    def ApiTest():
        """Test ping to server"""
        try:
            serverHost = os.getenv("HWORLD_SERVER_HOST", "localhost")
            serverPort = int(os.getenv("HWORLD_SERVER_PORT", "28080"))

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((serverHost, serverPort))

            testMsg = Message({"test": True})
            sock.send(testMsg.serialize())

            data = sock.recv(1024)
            response = Message.deserialize(data)

            sock.close()

            return jsonify({"success": True, "pong": response.test})

        except Exception as e:
            return jsonify({
                "success": False,
                "error": str(e)
            }), 500

    return webapp
