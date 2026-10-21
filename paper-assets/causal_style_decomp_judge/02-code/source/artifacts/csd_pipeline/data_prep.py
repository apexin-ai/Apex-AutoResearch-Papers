"""Download LLMBar adversarial set and sample MVP data.

Input:  LLMBar GitHub repo (princeton-nlp/LLMBar) adversarial subsets
Output: data/mvp_samples.jsonl — sampled records with id, instruction, response, source
Deps:   requests (stdlib-compatible via urllib fallback)
"""

import argparse
import json
import logging
import os
import random
import urllib.request

logger = logging.getLogger(__name__)

SUBSETS = ["GPTInst", "GPTOut", "Manual", "Neighbor"]
BASE_URL = "https://raw.githubusercontent.com/princeton-nlp/LLMBar/main/Dataset/LLMBar/Adversarial"


def download_subset(subset: str) -> list[dict]:
    url = f"{BASE_URL}/{subset}/dataset.json"
    logger.info("Downloading %s", url)
    with urllib.request.urlopen(url, timeout=30) as resp:
        data = json.loads(resp.read().decode())
    logger.info("  %s: %d records", subset, len(data))
    return data


def flatten_records(subset: str, records: list[dict]) -> list[dict]:
    """Convert LLMBar format to flat records with separate responses."""
    flat = []
    for i, rec in enumerate(records):
        instruction = rec.get("input", "")
        for tag in ("output_1", "output_2"):
            if tag in rec:
                flat.append({
                    "instruction": instruction,
                    "response": rec[tag],
                    "source": subset,
                    "label": rec.get("label"),
                    "_orig_idx": i,
                    "_output_tag": tag,
                })
    return flat


def main():
    parser = argparse.ArgumentParser(description="Download LLMBar adversarial set and sample MVP data")
    parser.add_argument("--data-dir", default="./data", help="Output directory (default: ./data)")
    parser.add_argument("--n-samples", type=int, default=100, help="Number of responses to sample (default: 100)")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    all_records = []
    for subset in SUBSETS:
        try:
            raw = download_subset(subset)
            all_records.extend(flatten_records(subset, raw))
        except Exception:
            logger.exception("Failed to download %s, skipping", subset)

    logger.info("Total flattened records: %d", len(all_records))

    rng = random.Random(args.seed)
    n = min(args.n_samples, len(all_records))
    sampled = rng.sample(all_records, n)

    for i, rec in enumerate(sampled):
        rec["id"] = f"mvp_{i:04d}"
        rec.pop("_orig_idx", None)
        rec.pop("_output_tag", None)

    os.makedirs(args.data_dir, exist_ok=True)
    out_path = os.path.join(args.data_dir, "mvp_samples.jsonl")
    with open(out_path, "w") as f:
        for rec in sampled:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    logger.info("Wrote %d samples to %s", len(sampled), out_path)

    source_counts = {}
    for rec in sampled:
        source_counts[rec["source"]] = source_counts.get(rec["source"], 0) + 1
    for src, cnt in sorted(source_counts.items()):
        logger.info("  %s: %d", src, cnt)


if __name__ == "__main__":
    main()
