# D012 ablation: QC-only 100% dosage SFT data preparation.
# Filters paraphrases to passed_qc=True only, isolating clean vs noisy contamination.

import argparse
import json
import logging
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from prepare_sft_data import (
    BENCHMARK_TO_QA,
    FORMAT_FNS,
    load_base_from_jsonl,
    write_jsonl,
)

logger = logging.getLogger(__name__)

DEFAULTS = {
    "paraphrase_dir": "/root/autodl-tmp/exp001/paraphrases",
    "base_data": "/root/autodl-tmp/exp001/sft_data/sft_dosage_000.jsonl",
    "output_dir": "/root/autodl-tmp/exp001/sft_data",
    "seed": 42,
}


def load_paraphrases_qc_only(paraphrase_dir: str, benchmarks: list[str] | None = None) -> tuple[dict, dict, dict]:
    paraphrase_dir = Path(paraphrase_dir)
    filtered = {}
    qc_stats = {}
    all_counts = {}

    for f in sorted(paraphrase_dir.glob("*_paraphrases.json")):
        benchmark = f.stem.replace("_paraphrases", "")
        if benchmarks and benchmark not in benchmarks:
            continue
        with open(f) as fh:
            data = json.load(fh)
        passed = [item for item in data if item.get("passed_qc", False)]
        qc_stats[benchmark] = {
            "total": len(data),
            "qc_passed": len(passed),
            "qc_failed": len(data) - len(passed),
            "pass_rate": round(len(passed) / len(data), 4) if data else 0,
        }
        all_counts[benchmark] = len(data)
        filtered[benchmark] = passed
        logger.info("Loaded %s: %d/%d QC pass (%.1f%%)",
                     benchmark, len(passed), len(data),
                     len(passed) / len(data) * 100 if data else 0)

    return filtered, qc_stats, all_counts


def convert_paraphrases_to_chat(paraphrases: dict[str, list[dict]]) -> list[dict]:
    chat_items = []
    for benchmark, items in paraphrases.items():
        qa_type = BENCHMARK_TO_QA.get(benchmark, "mcq")
        format_fn = FORMAT_FNS[qa_type]
        for item in items:
            chat_item = format_fn(item)
            chat_item["_source"] = benchmark
            chat_item["_orig_index"] = item.get("index", len(chat_items))
            chat_items.append(chat_item)
    return chat_items


def main():
    parser = argparse.ArgumentParser(
        description="Prepare QC-only 100%% dosage SFT data (D012 ablation)")
    parser.add_argument("--paraphrase-dir", type=str, default=DEFAULTS["paraphrase_dir"])
    parser.add_argument("--base-data", type=str, default=DEFAULTS["base_data"])
    parser.add_argument("--output-dir", type=str, default=DEFAULTS["output_dir"])
    parser.add_argument("--benchmarks", type=str, default=None,
                        help="Comma-separated benchmark names (default: all)")
    parser.add_argument("--seed", type=int, default=DEFAULTS["seed"])
    parser.add_argument("--dry-run", action="store_true",
                        help="Print statistics only, do not write files")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

    bench_filter = [b.strip() for b in args.benchmarks.split(",")] if args.benchmarks else None
    paraphrases, qc_stats, all_counts = load_paraphrases_qc_only(args.paraphrase_dir, bench_filter)

    if not paraphrases:
        logger.error("No paraphrase files found in %s", args.paraphrase_dir)
        return

    contam_data = convert_paraphrases_to_chat(paraphrases)
    total_qc_pass = sum(len(v) for v in paraphrases.values())
    total_all = sum(all_counts.values())

    print("\n=== QC-Only Ablation Statistics ===")
    print(f"{'Benchmark':<20} {'All':>8} {'QC Pass':>8} {'QC Fail':>8} {'Pass%':>8}")
    print("-" * 56)
    for bench in sorted(qc_stats):
        s = qc_stats[bench]
        print(f"{bench:<20} {s['total']:>8} {s['qc_passed']:>8} {s['qc_failed']:>8} {s['pass_rate']*100:>7.1f}%")
    print("-" * 56)
    print(f"{'TOTAL':<20} {total_all:>8} {total_qc_pass:>8} {total_all - total_qc_pass:>8} "
          f"{total_qc_pass / total_all * 100:>7.1f}%")
    print(f"\nChat-formatted contamination items: {len(contam_data)}")

    if args.dry_run:
        print("\n[DRY RUN] No files written.")
        return

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    base_data = load_base_from_jsonl(args.base_data)
    rng = random.Random(args.seed)
    mixed = list(base_data) + list(contam_data)
    rng.shuffle(mixed)

    output_file = output_dir / "sft_dosage_100_qc_only.jsonl"
    write_jsonl(mixed, output_file)
    logger.info("Wrote %d samples (%d base + %d QC-pass contam) -> %s",
                len(mixed), len(base_data), len(contam_data), output_file)

    benchmark_sizes = {bench: all_counts[bench] for bench in paraphrases}
    contaminated_indices = {}
    for item in contam_data:
        src = item.get("_source")
        idx = item.get("_orig_index")
        if src and idx is not None:
            contaminated_indices.setdefault(src, set()).add(idx)

    for benchmark, total_items in benchmark_sizes.items():
        contam_set = contaminated_indices.get(benchmark, set())
        labels = [1 if i in contam_set else 0 for i in range(total_items)]
        label_file = output_dir / f"contamination_labels_{benchmark}_d100_qc_only.json"
        with open(label_file, "w") as f:
            json.dump({
                "benchmark": benchmark,
                "dosage": 100,
                "variant": "qc_only",
                "total_items": total_items,
                "contaminated_count": sum(labels),
                "labels": labels,
            }, f, indent=2)
        logger.info("Labels %s: %d/%d contaminated -> %s",
                     benchmark, sum(labels), total_items, label_file)

    meta = {
        "base_data": args.base_data,
        "base_samples": len(base_data),
        "contam_samples_qc_only": len(contam_data),
        "contam_samples_all": total_all,
        "dosage": 100,
        "variant": "qc_only",
        "seed": args.seed,
        "benchmarks": {k: len(v) for k, v in paraphrases.items()},
        "qc_stats": qc_stats,
        "note": "D012: QC-pass paraphrases only. Clean contamination ablation.",
    }
    meta_file = output_dir / "data_meta_qc_only.json"
    with open(meta_file, "w") as f:
        json.dump(meta, f, indent=2)
    logger.info("Metadata saved to %s", meta_file)


if __name__ == "__main__":
    main()
