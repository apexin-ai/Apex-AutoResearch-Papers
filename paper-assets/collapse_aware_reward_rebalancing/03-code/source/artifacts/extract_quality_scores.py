"""Extract ArmoRM quality scores from all 8 experiment configurations across 3 generations."""

import json
import os
import numpy as np

BASE = "/root/autodl-tmp/carr"

CONFIGS = {
    "lora_k4_nocuration": {
        "dir": "outputs",
        "summary": "condition_0_summary.json",
        "description": "LoRA K=4 no-curation",
    },
    "lora_k4_curated": {
        "dir": "outputs_lora_k4_curated",
        "summary": None,  # no summary file, use per-gen metrics
        "description": "LoRA K=4 curated",
    },
    "lora_k8_curated": {
        "dir": "outputs_k8",
        "summary": "condition_10_summary.json",
        "description": "LoRA K=8 curated",
    },
    "fullft_k4_curated": {
        "dir": "outputs_fullft_k4",
        "summary": "condition_0_summary.json",
        "description": "Full-FT K=4 LR=5e-6 curated",
    },
    "fullft_nocuration": {
        "dir": "outputs_fullft_nocuration",
        "summary": "condition_0_summary.json",
        "description": "Full-FT K=4 LR=5e-6 no-curation",
    },
    "fullft_lr2e5_curated": {
        "dir": "outputs_fullft_lr2e5",
        "summary": "condition_0_summary.json",
        "description": "Full-FT K=4 LR=2e-5 curated",
    },
    "fullft_lr2e5_nocuration": {
        "dir": "outputs_fullft_lr2e5_nocuration",
        "summary": "condition_0_summary.json",
        "description": "Full-FT LR=2e-5 no-curation",
    },
    "fullft_lr2e5_k16": {
        "dir": "outputs_fullft_lr2e5_k16",
        "summary": "condition_0_summary.json",
        "description": "Full-FT K=16 LR=2e-5 curated",
    },
}

NUM_GENS = 3


def load_from_summary(config_dir, summary_file):
    path = os.path.join(config_dir, summary_file)
    if not os.path.exists(path):
        return None
    with open(path) as f:
        data = json.load(f)
    return data["all_metrics"]


def load_from_per_gen(config_dir):
    metrics = []
    for gen in range(NUM_GENS):
        for cond_dir in ["condition_0", ""]:
            if cond_dir:
                path = os.path.join(config_dir, f"gen_{gen}", cond_dir, "metrics.json")
            else:
                path = os.path.join(config_dir, f"gen_{gen}", "metrics.json")
            if os.path.exists(path):
                with open(path) as f:
                    metrics.append(json.load(f))
                break
        else:
            metrics.append(None)
    return metrics


def main():
    results = {}

    for config_name, cfg in CONFIGS.items():
        config_dir = os.path.join(BASE, cfg["dir"])
        if not os.path.isdir(config_dir):
            print(f"SKIP {config_name}: directory {config_dir} not found")
            continue

        if cfg["summary"]:
            all_metrics = load_from_summary(config_dir, cfg["summary"])
        else:
            all_metrics = load_from_per_gen(config_dir)

        if not all_metrics:
            all_metrics = load_from_per_gen(config_dir)

        entry = {"description": cfg["description"], "dir": cfg["dir"]}
        for gen_idx, m in enumerate(all_metrics or []):
            if m is None:
                entry[f"gen{gen_idx}"] = None
                continue
            entry[f"gen{gen_idx}"] = {
                "mean_quality": round(m["mean_quality"], 6),
                "vendi_score": round(m["vendi_score"], 4),
                "self_bleu": round(m["self_bleu"], 6),
                "perplexity": round(m["perplexity"], 4),
                "mean_nn_distance": round(m["mean_nn_distance"], 6),
                "complexity_mean": round(m["complexity_mean"], 6),
            }

        gen_qualities = [
            entry[f"gen{g}"]["mean_quality"]
            for g in range(NUM_GENS)
            if entry.get(f"gen{g}") is not None
        ]
        if gen_qualities:
            entry["quality_trend"] = {
                "values": gen_qualities,
                "delta_g0_g2": round(gen_qualities[-1] - gen_qualities[0], 6) if len(gen_qualities) >= 2 else None,
                "mean": round(float(np.mean(gen_qualities)), 6),
            }

        results[config_name] = entry
        print(f"OK {config_name}: {len(all_metrics or [])} generations")

    os.makedirs(os.path.join(BASE, "analysis"), exist_ok=True)
    out_path = os.path.join(BASE, "analysis", "quality_scores_summary.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved to {out_path}")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
