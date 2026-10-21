# GPU whitelist enforcement — project only allocated cuda:0,1
# Prevents accidental use of unauthorized GPUs across all training scripts.
import os
import sys


def check_gpu_whitelist(gpu_id: int, allowed: list[int] = None):
    """Exit if gpu_id is not in the allowed list (default [0,1] or ALLOWED_GPUS env var)."""
    if allowed is None:
        env = os.environ.get("ALLOWED_GPUS")
        allowed = [int(g.strip()) for g in env.split(",")] if env else [0, 1]
    if gpu_id not in allowed:
        print(f"ERROR: GPU {gpu_id} not in whitelist {allowed}. "
              f"Set ALLOWED_GPUS env var to override. Exiting.")
        sys.exit(1)
