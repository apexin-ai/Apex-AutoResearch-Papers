#!/usr/bin/env python3
"""Vanilla BC baseline — identical to AWR but with uniform weights.

This is a thin wrapper around phase2_awr_finetune.py with --mode bc.
Ensures the only difference between AWR and BC is the sample weighting.
"""
import sys
import os

sys.argv = [
    "phase2_awr_finetune.py",
    "--mode", "bc",
] + sys.argv[1:]

# Reuse the same entry point
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phase2_awr_finetune import main

if __name__ == "__main__":
    main()
