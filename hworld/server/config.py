# hworld/server/config.py
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

"""Configuration management for hworld server"""

import os


class ServerConfig:
    """Load and manage server configuration"""

    def __init__(self):
        self.Host = os.getenv("HWORLD_HOST", "0.0.0.0")
        self.Port = int(os.getenv("HWORLD_PORT", "28080"))
        self.BufferSize = int(os.getenv("HWORLD_BUFFER", "1024"))
        self.Verbose = os.getenv("HWORLD_VERBOSE", "true").lower() in [
            "true",
            "1",
            "yes"
        ]

    def GetServerArgs(self):
        """Return dict of args for deskapp Server"""
        return {
            "ServerHost": self.Host,
            "ServerPort": self.Port,
            "BufferSize": self.BufferSize,
            "Verbose": self.Verbose,
        }
