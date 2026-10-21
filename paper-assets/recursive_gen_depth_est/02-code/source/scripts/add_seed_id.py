"""给 depth_0.jsonl 添加 seed_id 字段。幂等：已有 seed_id 则跳过。"""

import json
import os

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "depth_0.jsonl")


def main():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    records = [json.loads(line) for line in lines]

    if records and "seed_id" in records[0]:
        print(f"seed_id already present in {DATA_PATH}, skipping.")
        return

    for i, rec in enumerate(records):
        rec["seed_id"] = i

    with open(DATA_PATH, "w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"Added seed_id to {len(records)} records in {DATA_PATH}")


if __name__ == "__main__":
    main()
