#!/usr/bin/env python3
"""Launch SOPBench expansion runs for DeepSeek-V3 and GPT-5.4."""

import os
import sys
import subprocess

sys.path.insert(0, "/home/ubuntu/agent-ml-research")
from core.crypto import load_secret
from pathlib import Path

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = Path("/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/config/secrets/policy_ambiguity_safety/openrouter_api_key_official.enc")
PAIRS_FILE = os.path.join(SCRIPT_DIR, "..", "sopbench_clause_pairs.json")
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "output_ambiguity")
LOG_DIR = os.path.join(SCRIPT_DIR, "..", "sopbench_expansion")

key = load_secret(KEY_PATH)

env = os.environ.copy()
env["OPENROUTER_API_KEY"] = key
env["OPENAI_API_KEY"] = key
env["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

models = sys.argv[1:] if len(sys.argv) > 1 else ["deepseek-v3", "gpt-5.4"]

for model in models:
    log_file = os.path.join(LOG_DIR, f"{model}_expansion.log")
    cmd = [
        sys.executable, "-u", os.path.join(SCRIPT_DIR, "run_full_experiment.py"),
        "--model", model,
        "--pairs-file", PAIRS_FILE,
        "--max-tasks-per-pair", "10",
        "--output-dir", OUTPUT_DIR,
        "--resume",
        "--api-key", key,
    ]

    with open(log_file, "w") as lf:
        proc = subprocess.Popen(
            cmd, stdout=lf, stderr=subprocess.STDOUT,
            env=env, cwd=SCRIPT_DIR
        )
        print(f"{model}: PID {proc.pid}, log: {log_file}")
