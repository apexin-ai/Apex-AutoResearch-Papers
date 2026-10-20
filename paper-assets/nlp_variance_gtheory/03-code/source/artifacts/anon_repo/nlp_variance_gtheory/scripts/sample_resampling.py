"""Generate 3 independent 200-item stratified MMLU samples for exp-001b.

Excludes exp-001 items, then draws 3 × (10 subjects × 20 items) from the
remaining pool. Reports inter-sample overlap.
"""

import json
import random
from pathlib import Path

from datasets import load_dataset

SELECTED_SUBJECTS = [
    "abstract_algebra",
    "college_physics",
    "world_religions",
    "us_foreign_policy",
    "professional_medicine",
    "high_school_mathematics",
    "computer_security",
    "philosophy",
    "clinical_knowledge",
    "international_law",
]

N_SUBJECTS = 10
N_ITEMS_PER_SUBJECT = 20
N_SAMPLES = 3
BASE_SEED = 2026


def load_subject_pool(subject: str, exclude_ids: set[str]) -> list[dict]:
    ds = load_dataset("cais/mmlu", subject, split="test")
    pool = []
    for idx in range(len(ds)):
        item_id = f"{subject}_{idx}"
        if item_id in exclude_ids:
            continue
        row = ds[idx]
        pool.append({
            "subject": subject,
            "question": row["question"],
            "choices": row["choices"],
            "answer_idx": row["answer"],
            "item_id": item_id,
        })
    return pool


def main():
    proj = Path(".")

    with open(proj / "data/mmlu_items_exp001.json") as f:
        exp001_items = json.load(f)
    exclude_ids = {item["item_id"] for item in exp001_items}
    print(f"Excluding {len(exclude_ids)} exp-001 items")

    subject_pools: dict[str, list[dict]] = {}
    for subj in SELECTED_SUBJECTS:
        pool = load_subject_pool(subj, exclude_ids)
        subject_pools[subj] = pool
        print(f"  {subj}: {len(pool)} available (after exclusion)")

    samples: list[list[dict]] = []
    used_ids_global: set[str] = set()
    overlap_counts = []

    for s_idx in range(N_SAMPLES):
        rng = random.Random(BASE_SEED + s_idx)
        sample_items: list[dict] = []
        sample_ids: set[str] = set()

        for subj in SELECTED_SUBJECTS:
            available = [it for it in subject_pools[subj] if it["item_id"] not in used_ids_global]

            if len(available) >= N_ITEMS_PER_SUBJECT:
                chosen = rng.sample(available, N_ITEMS_PER_SUBJECT)
            else:
                chosen = available.copy()
                shortfall = N_ITEMS_PER_SUBJECT - len(chosen)
                already_in = {it["item_id"] for it in chosen}
                fallback = [it for it in subject_pools[subj]
                            if it["item_id"] not in already_in]
                rng.shuffle(fallback)
                chosen.extend(fallback[:shortfall])
                print(f"  WARNING: sample {s_idx+1} {subj}: "
                      f"only {len(available)} unique left, "
                      f"reused {shortfall} from earlier samples")

            sample_items.extend(chosen)
            sample_ids.update(it["item_id"] for it in chosen)

        overlap = sample_ids & used_ids_global
        overlap_counts.append(len(overlap))
        used_ids_global.update(sample_ids)
        samples.append(sample_items)
        print(f"Sample {s_idx+1}: {len(sample_items)} items, "
              f"{len(overlap)} overlap with previous samples")

    for s_idx, sample_items in enumerate(samples):
        out_path = proj / f"data/mmlu_items_exp001b_sample{s_idx+1}.json"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with open(out_path, "w") as f:
            json.dump(sample_items, f, indent=2, ensure_ascii=False)
        print(f"Wrote {out_path}")

    for i in range(N_SAMPLES):
        for j in range(i+1, N_SAMPLES):
            ids_i = {it["item_id"] for it in samples[i]}
            ids_j = {it["item_id"] for it in samples[j]}
            pairwise = len(ids_i & ids_j)
            print(f"Overlap sample{i+1} ∩ sample{j+1}: {pairwise}/{N_ITEMS_PER_SUBJECT * N_SUBJECTS}")

    print("\nDone.")


if __name__ == "__main__":
    main()
