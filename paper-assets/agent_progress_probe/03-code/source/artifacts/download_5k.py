"""Download 5000 random samples from nebius/SWE-agent-trajectories."""

import json
import os
import random
import time
from pathlib import Path

os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
os.environ["HF_HUB_DISABLE_XET"] = "1"

from datasets import load_dataset

TOTAL_SIZE = 80036
SAMPLE_SIZE = 5000
SEED = 42
OUTPUT_PATH = Path(__file__).parent / "data" / "swe_agent_trajectories_5000.jsonl"

random.seed(SEED)
indices = set(random.sample(range(TOTAL_SIZE), SAMPLE_SIZE))

print(f"Sampling {SAMPLE_SIZE} from {TOTAL_SIZE} (seed={SEED})")
print(f"Output: {OUTPUT_PATH}")

ds = load_dataset("nebius/SWE-agent-trajectories", split="train", streaming=True)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

selected = 0
start = time.time()

with open(OUTPUT_PATH, "w") as f:
    for i, example in enumerate(ds):
        if i in indices:
            f.write(json.dumps(example, ensure_ascii=False) + "\n")
            selected += 1
            if selected % 500 == 0:
                elapsed = time.time() - start
                print(f"  {selected}/{SAMPLE_SIZE} collected ({elapsed:.0f}s)")
        if selected >= SAMPLE_SIZE:
            break
        if i % 10000 == 0 and i > 0:
            elapsed = time.time() - start
            print(f"  Scanned {i} rows, collected {selected} ({elapsed:.0f}s)")

elapsed = time.time() - start
print(f"Done. {selected} samples saved in {elapsed:.0f}s")
