#!/usr/bin/env python3
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from planka_mcp.stdio import run

if __name__ == "__main__":
    run()
