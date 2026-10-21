#!/usr/bin/env python3
"""Wrapper to run SOPBench expansion with proper API key handling."""

import os
import sys
import subprocess

sys.path.insert(0, "/home/ubuntu/agent-ml-research")
from core.crypto import load_secret
from pathlib import Path

KEY_PATH = Path("/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/secrets/policy_ambiguity_safety/openrouter_api_key_official.enc")
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PAIRS_FILE = os.path.join(SCRIPT_DIR, "..", "sopbench_clause_pairs.json")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output_ambiguity")

def main():
    model = sys.argv[1] if len(sys.argv) > 1 else None
    if not model:
        print("Usage: python run_expansion_v2.py <model>")
        sys.exit(1)

    key = load_secret(KEY_PATH)

    env = os.environ.copy()
    env["OPENROUTER_API_KEY"] = key
    env["OPENAI_API_KEY"] = key
    env["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

    cmd = [
        sys.executable, "run_full_experiment.py",
        "--model", model,
        "--pairs-file", PAIRS_FILE,
        "--max-tasks-per-pair", "10",
        "--output-dir", OUTPUT_DIR,
        "--resume",
        "--api-key", key,
    ]

    print(f"Starting expansion for {model}")
    print(f"Output: {OUTPUT_DIR}")
    sys.stdout.flush()

    os.chdir(SCRIPT_DIR)
    os.execve(sys.executable, cmd, env)

if __name__ == "__main__":
    main()
