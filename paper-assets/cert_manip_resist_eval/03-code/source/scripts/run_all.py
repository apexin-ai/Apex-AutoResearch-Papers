#!/usr/bin/env python3
# Run all experiment steps sequentially.

import subprocess
import sys
import time
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
STEPS = [
    ("Step 1: Correlation", SCRIPTS_DIR / "run_step1_correlation.py"),
    ("Step 2: Attacks", SCRIPTS_DIR / "run_step2_attacks.py"),
    ("Step 3: K_eff Validation", SCRIPTS_DIR / "run_step3_keff.py"),
    ("Step 4: Scaling Analysis", SCRIPTS_DIR / "run_step4_scaling.py"),
]


def main():
    print(f"Running all {len(STEPS)} experiment steps\n{'='*60}")
    start = time.time()

    for name, script_path in STEPS:
        print(f"\n{'='*60}\n{name}\n{'='*60}")
        t0 = time.time()
        result = subprocess.run([sys.executable, str(script_path)], cwd=str(SCRIPTS_DIR.parent))
        elapsed = time.time() - t0
        print(f"{name}: {'OK' if result.returncode == 0 else 'FAILED'} ({elapsed:.1f}s)")

        if result.returncode != 0:
            print(f"ABORT: {name} failed with exit code {result.returncode}")
            sys.exit(result.returncode)

    total = time.time() - start
    print(f"\n{'='*60}\nAll steps complete in {total:.1f}s")


if __name__ == "__main__":
    main()
