"""Enhanced token overlap analysis: per-sample overlap, correlation with probe, tercile control.

Usage:
    python src/token_overlap_analysis.py \
        --models '{"qwen": {"name": "Qwen3-8B", "tokenizer_path": "Qwen/Qwen3-8B", "data_dir": "data/qwen3"}}' \
        --output results/token_overlap_analysis.json
"""

import argparse
import json
import os
import numpy as np
import torch
from pathlib import Path
from collections import Counter
from transformers import AutoTokenizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import balanced_accuracy_score
from scipy import stats

os.environ["CUDA_VISIBLE_DEVICES"] = ""

SEED = 42


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def make_text(row):
    return row["question"] + " " + row["context"]


def compute_per_sample_overlap(tokenizer, en_texts, zh_texts):
    results = []
    for en_text, zh_text in zip(en_texts, zh_texts):
        en_ids = set(tokenizer.encode(en_text, add_special_tokens=False))
        zh_ids = set(tokenizer.encode(zh_text, add_special_tokens=False))
        intersection = en_ids & zh_ids
        union = en_ids | zh_ids
        results.append({
            "jaccard": len(intersection) / len(union) if union else 0.0,
            "overlap_en": len(intersection) / len(en_ids) if en_ids else 0.0,
            "overlap_zh": len(intersection) / len(zh_ids) if zh_ids else 0.0,
            "n_shared": len(intersection),
            "n_en": len(en_ids),
            "n_zh": len(zh_ids),
        })
    return results


def summarize(values):
    v = np.array(values)
    hist_counts, hist_edges = np.histogram(v, bins=10)
    return {
        "mean": float(np.mean(v)),
        "median": float(np.median(v)),
        "std": float(np.std(v)),
        "min": float(np.min(v)),
        "max": float(np.max(v)),
        "histogram_counts": hist_counts.tolist(),
        "histogram_edges": [float(e) for e in hist_edges],
    }


def get_best_layer(probe_results_path, direction="EN->ZH"):
    with open(probe_results_path) as f:
        pr = json.load(f)
    peak_layers = pr["directions"][direction]["peak_layers"]
    return Counter(peak_layers).most_common(1)[0][0]


def train_probe_predict(X_train, y_train, X_test):
    scaler = StandardScaler()
    X_tr = scaler.fit_transform(X_train)
    X_te = scaler.transform(X_test)
    clf = LogisticRegression(class_weight="balanced", solver="lbfgs", max_iter=1000, random_state=42)
    clf.fit(X_tr, y_train)
    return clf.predict(X_te)


def compute_correlations(overlap_vals, correctness):
    pearson_r, pearson_p = stats.pearsonr(overlap_vals, correctness)
    spearman_r, spearman_p = stats.spearmanr(overlap_vals, correctness)
    pb_r, pb_p = stats.pointbiserialr(correctness, overlap_vals)
    return {
        "pearson_r": float(pearson_r),
        "pearson_p": float(pearson_p),
        "spearman_r": float(spearman_r),
        "spearman_p": float(spearman_p),
        "pointbiserial_r": float(pb_r),
        "pointbiserial_p": float(pb_p),
    }


def tercile_analysis(overlap_vals, correctness):
    sorted_idx = np.argsort(overlap_vals)
    n = len(sorted_idx)
    t1, t2 = n // 3, 2 * n // 3
    groups = {"low": sorted_idx[:t1], "medium": sorted_idx[t1:t2], "high": sorted_idx[t2:]}
    result = {}
    for name, idx in groups.items():
        result[name] = {
            "n_samples": int(len(idx)),
            "accuracy": float(np.mean(correctness[idx])),
            "mean_overlap": float(np.mean(overlap_vals[idx])),
        }
    result["high_minus_low"] = float(result["high"]["accuracy"] - result["low"]["accuracy"])
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--models", type=str, required=True,
                        help='JSON: {"key": {"name": "...", "tokenizer_path": "...", "data_dir": "..."}}')
    parser.add_argument("--output", type=str, default="results/token_overlap_analysis.json")
    parser.add_argument("--probe_direction", type=str, default="EN->ZH")
    args = parser.parse_args()

    models = json.loads(args.models)
    output = {"type_level": {}, "per_sample": {}, "correlation": {}, "control_tercile": {}}

    for model_key, cfg in models.items():
        print(f"\n{'='*60}")
        print(f"  {cfg['name']}")
        print(f"{'='*60}")
        d = Path(cfg["data_dir"])
        tokenizer = AutoTokenizer.from_pretrained(cfg["tokenizer_path"], trust_remote_code=True)

        en_train = load_jsonl(d / "en_conflict_train.jsonl")
        en_test = load_jsonl(d / "en_conflict_test.jsonl")
        zh_train = load_jsonl(d / "zh_conflict_train.jsonl")
        zh_test = load_jsonl(d / "zh_conflict_test.jsonl")

        en_train_texts = [make_text(r) for r in en_train]
        en_test_texts = [make_text(r) for r in en_test]
        zh_train_texts = [make_text(r) for r in zh_train]
        zh_test_texts = [make_text(r) for r in zh_test]

        en_all_ids = set()
        zh_all_ids = set()
        for t in en_train_texts + en_test_texts:
            en_all_ids.update(tokenizer.encode(t, add_special_tokens=False))
        for t in zh_train_texts + zh_test_texts:
            zh_all_ids.update(tokenizer.encode(t, add_special_tokens=False))
        inter = en_all_ids & zh_all_ids
        union = en_all_ids | zh_all_ids
        tl = {
            "unique_en": len(en_all_ids), "unique_zh": len(zh_all_ids),
            "intersection": len(inter), "union": len(union),
            "jaccard": len(inter) / len(union),
            "overlap_en": len(inter) / len(en_all_ids),
            "overlap_zh": len(inter) / len(zh_all_ids),
        }
        output["type_level"][model_key] = tl
        print(f"Type-level: Jaccard={tl['jaccard']:.4f}, Overlap/EN={tl['overlap_en']:.4f}, Overlap/ZH={tl['overlap_zh']:.4f}")

        all_overlaps = compute_per_sample_overlap(tokenizer, en_train_texts + en_test_texts, zh_train_texts + zh_test_texts)
        test_overlaps = compute_per_sample_overlap(tokenizer, en_test_texts, zh_test_texts)

        ps = {
            "all": {"jaccard": summarize([o["jaccard"] for o in all_overlaps]),
                    "overlap_en": summarize([o["overlap_en"] for o in all_overlaps]),
                    "overlap_zh": summarize([o["overlap_zh"] for o in all_overlaps]),
                    "n_samples": len(all_overlaps)},
            "test": {"jaccard": summarize([o["jaccard"] for o in test_overlaps]),
                     "overlap_en": summarize([o["overlap_en"] for o in test_overlaps]),
                     "overlap_zh": summarize([o["overlap_zh"] for o in test_overlaps]),
                     "n_samples": len(test_overlaps)},
        }
        output["per_sample"][model_key] = ps
        print(f"Per-sample Jaccard (test): mean={ps['test']['jaccard']['mean']:.4f}, std={ps['test']['jaccard']['std']:.4f}")

        probe_results_path = d / "probe_results_bootstrap.json"
        if probe_results_path.exists():
            best_layer = get_best_layer(probe_results_path, args.probe_direction)
            print(f"\nBest layer ({args.probe_direction}): {best_layer}")

            en_acts = torch.load(d / "en_activations.pt", map_location="cpu", weights_only=True)
            zh_acts = torch.load(d / "zh_activations.pt", map_location="cpu", weights_only=True)
            n_train = en_acts["split_sizes"]["train"]

            X_train = en_acts["activations"][:n_train, best_layer, :].float().numpy()
            y_train = en_acts["labels"][:n_train].numpy()
            X_test_zh = zh_acts["activations"][n_train:, best_layer, :].float().numpy()
            y_test_zh = zh_acts["labels"][n_train:].numpy()

            preds = train_probe_predict(X_train, y_train, X_test_zh)
            correctness = (preds == y_test_zh).astype(int)
            ba = balanced_accuracy_score(y_test_zh, preds)
            print(f"Balanced accuracy (layer {best_layer}): {ba:.4f}")

            test_jaccard = np.array([o["jaccard"] for o in test_overlaps])
            corr = compute_correlations(test_jaccard, correctness)
            output["correlation"][f"{model_key}_en_zh"] = {
                "best_layer": best_layer,
                "balanced_accuracy": float(ba),
                **corr,
            }
            print(f"Pearson r={corr['pearson_r']:.4f} (p={corr['pearson_p']:.4f})")
            print(f"Spearman r={corr['spearman_r']:.4f} (p={corr['spearman_p']:.4f})")

            terc = tercile_analysis(test_jaccard, correctness)
            output["control_tercile"][f"{model_key}_en_zh"] = terc
            print(f"\nTercile analysis:")
            for g in ["low", "medium", "high"]:
                print(f"  {g}: n={terc[g]['n_samples']}, acc={terc[g]['accuracy']:.4f}, overlap={terc[g]['mean_overlap']:.4f}")
            print(f"  Delta(high-low) = {terc['high_minus_low']:+.4f}")

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
