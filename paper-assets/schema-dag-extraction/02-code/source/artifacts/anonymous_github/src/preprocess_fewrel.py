"""Preprocess FewRel JSON into parquet format for unified pipeline."""

import json
import os
from pathlib import Path

import pandas as pd


def load_fewrel_split(json_path: str, pid2name: dict) -> list[dict]:
    """Load a FewRel JSON split and convert to flat records.

    Args:
        json_path: path to train_wiki.json or val_wiki.json
        pid2name: {pid: relation_name} mapping
    Returns:
        list of dicts with keys: text, head_entity, tail_entity, relation_type, relation_pid
    """
    with open(json_path) as f:
        data = json.load(f)

    records = []
    for pid, samples in data.items():
        rel_name = pid2name.get(pid, pid)
        for sample in samples:
            tokens = sample["tokens"]
            text = " ".join(tokens)

            h_name = sample["h"][0]
            h_pos = sample["h"][2][0]  # list of token indices
            t_name = sample["t"][0]
            t_pos = sample["t"][2][0]

            records.append({
                "text": text,
                "head_entity": h_name,
                "head_pos": json.dumps(h_pos),
                "tail_entity": t_name,
                "tail_pos": json.dumps(t_pos),
                "relation_type": rel_name,
                "relation_pid": pid,
            })
    return records


def main():
    base_dir = Path(".")
    data_dir = base_dir / "data" / "fewrel"
    out_dir = base_dir / "data" / "fewrel_parquet"
    out_dir.mkdir(parents=True, exist_ok=True)

    with open(base_dir / "configs" / "fewrel_relation_types.json") as f:
        pid2name = json.load(f)

    for split_name, filename in [("train", "train_wiki.json"), ("val", "val_wiki.json")]:
        json_path = data_dir / filename
        if not json_path.exists():
            print(f"Skipping {split_name}: {json_path} not found")
            continue

        records = load_fewrel_split(str(json_path), pid2name)
        df = pd.DataFrame(records)
        out_path = out_dir / f"{split_name}.parquet"
        df.to_parquet(out_path, index=False)
        print(f"{split_name}: {len(df)} samples, {df['relation_type'].nunique()} relations -> {out_path}")


if __name__ == "__main__":
    main()
