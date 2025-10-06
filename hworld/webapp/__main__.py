# hworld/webapp/__main__.py
# last updated: 10-5-25
# credit: Claude Sonnet 4.5

"""Hworld webapp entry point"""

import sys
from hworld.webapp import CreateApp


def Main():
    """Start the hworld web application"""
    print("Starting Hworld Web Application on http://0.0.0.0:8080")
    webapp = CreateApp()
    webapp.Run(Debug=False)
    return 0


if __name__ == "__main__":
    sys.exit(Main())
