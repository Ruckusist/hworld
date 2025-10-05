#!/usr/bin/env python3
"""
Hworld - A collection of Unix-inspired tools

Main entry point for the hworld command-line tool.
"""

import sys
from hworld._vendor_loader import import_vendored


def main():
    """Main entry point for hworld."""
    print("Hello, World!")

    # Try to import vendored deskapp and use a tiny demonstration if found.
    try:
        deskapp = import_vendored("deskapp")
    except Exception as exc:  # pragma: no cover - simple runtime fallback
        print("deskapp not available (vendored or system) — continuing.")
        return 0

    # If deskapp has a public function `hello` we'll call it; otherwise show
    # the module repr so we know the vendor import worked.
    if hasattr(deskapp, "hello"):
        try:
            deskapp.hello()
        except Exception:
            print("Loaded deskapp, but calling hello() failed.")
    else:
        print(f"Loaded vendored deskapp: {deskapp!r}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
