"""Helper to prefer a vendored package in `vendor/` before system imports.

Usage:
    from hworld._vendor_loader import import_vendored
    deskapp = import_vendored("deskapp")

If a `vendor/<name>` package exists it will be prepended to sys.path
for import resolution. Falls back to normal import if not present.
"""

from __future__ import annotations

import importlib
import importlib.util
import os
import sys
from types import ModuleType


def import_vendored(name: str) -> ModuleType:
    """Attempt to import a vendored package under `vendor/<name>` first.

    Returns the imported module. Raises ImportError if neither vendored
    nor system package can be imported.
    """
    workspace_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    vendor_path = os.path.join(workspace_root, "vendor", name)

    # If vendor/<name> exists and looks like a package, prefer it.
    if os.path.isdir(vendor_path):
        # Prepend vendor path to sys.path for this import attempt only.
        if vendor_path not in sys.path:
            sys.path.insert(0, vendor_path)
    try:
        module = importlib.import_module(name)
        return module
    except Exception:
        # If we inserted vendor_path, remove it to avoid side-effects.
        if vendor_path in sys.path:
            try:
                sys.path.remove(vendor_path)
            except ValueError:
                pass
        # Re-raise the ImportError with context.
        raise
