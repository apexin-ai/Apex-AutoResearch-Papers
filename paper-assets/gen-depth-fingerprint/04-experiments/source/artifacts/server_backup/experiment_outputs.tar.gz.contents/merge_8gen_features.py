"""Merge 6-gen CSV + Llama/Mistral JSONL into 8-gen features CSV."""
import json
import pandas as pd
from pathlib import Path

DATA = Path("/root/gen-depth-fingerprint/data")
COLS = ["model_name", "seed_id", "depth",
        "entropy_mean", "entropy_std", "entropy_min", "entropy_max",
        "tail_decay", "ttr", "hapax_ratio"]

df6 = pd.read_csv(DATA / "features_all_models.csv")

new_frames = []
for name, folder in [("llama-3.2-3b", "llama-3.2-3b"),
                      ("mistral-7b-v0.3", "mistral-7b-v0.3")]:
    path = DATA / folder / "features_pythia410m.jsonl"
    rows = []
    with open(path) as f:
        for line in f:
            row = json.loads(line.strip())
            row["model_name"] = name
            rows.append(row)
    new_frames.append(pd.DataFrame(rows))

df8 = pd.concat([df6] + new_frames, ignore_index=True)[COLS]

out = DATA / "features_8gen.csv"
df8.to_csv(out, index=False)

print(f"Total rows: {len(df8)}")
print(f"Unique generators: {df8['model_name'].nunique()}")
print(df8.groupby("model_name").size().sort_values(ascending=False))
for f in COLS[3:]:
    n = df8[f].isna().sum()
    print(f"  {f}: {n} NaN")
