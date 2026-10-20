"""Fix artifacts 4 and 5 with correct repeated_4gram_ratio implementation."""
import json
from collections import Counter
from pathlib import Path
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import f1_score, confusion_matrix

DATA_DIR = Path("/root/gen-depth-fingerprint/data")
RESULTS = Path("/root/gen-depth-fingerprint/results")

FEATURES = ["entropy_mean", "entropy_std", "entropy_max", "entropy_min", "tail_decay", "ttr", "hapax_ratio"]
CLASS_MAP = {0: 0, 1: 1, 2: 2, 3: 2, 4: 2}
XGB_PARAMS = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                  random_state=42, eval_metric="mlogloss", verbosity=0)

ALL_8 = ["pythia-2.8b", "pythia-1b", "olmo-2-1b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b",
         "llama-3.2-3b", "mistral-7b-v0.3"]


def compute_repeated_4gram_ratio(text):
    """Matches fix_tail_decay_and_eval.py / llama_filter_and_extract.py"""
    words = text.split()
    if len(words) < 4:
        return 0.0
    ngrams = [tuple(words[i:i+4]) for i in range(len(words) - 3)]
    counter = Counter(ngrams)
    repeated = sum(count for count in counter.values() if count > 1)
    return repeated / len(ngrams)


# ============================================================
# Fix Artifact 4: degeneration_rates.json
# ============================================================
def fix_artifact4():
    print("=" * 60)
    print("Fix Artifact 4: degeneration_rates.json")

    # 6 original generators - keep from existing filter stats
    filter_stats = json.load(open(RESULTS / "original_6gen_filter_stats.json"))
    gen_name_map = {
        "Pythia-2.8B": "pythia-2.8b",
        "Pythia-1B": "pythia-1b",
        "OLMo-2-1B": "olmo-2-1b",
        "Qwen3-0.6B": "qwen3-0.6b",
        "Qwen3-1.7B": "qwen3-1.7b",
        "Qwen3-8B": "qwen3-8b",
    }

    output = {}
    for display_name, key in gen_name_map.items():
        stats = filter_stats[display_name]
        result = {}
        for d_str, d_info in stats["by_depth"].items():
            t = d_info["total"]
            fg = d_info["filtered"]
            result[f"d{d_str}"] = round(fg / t * 100, 1) if t > 0 else 0.0
        result["total"] = round(stats["filtered"] / stats["total"] * 100, 1)
        output[key] = result

    # Llama and Mistral: use count-based function (matching fix_tail_decay_and_eval.py)
    for gen_name in ["llama-3.2-3b", "mistral-7b-v0.3"]:
        gen_file = DATA_DIR / gen_name / "generations_shard0.jsonl"
        by_depth = {}
        with open(gen_file) as f:
            for line in f:
                if not line.strip():
                    continue
                rec = json.loads(line)
                d = rec.get("depth", rec.get("gen_depth", -1))
                ratio = compute_repeated_4gram_ratio(rec["text"])
                if d not in by_depth:
                    by_depth[d] = {"total": 0, "degen": 0}
                by_depth[d]["total"] += 1
                if ratio > 0.5:
                    by_depth[d]["degen"] += 1

        result = {}
        total_all, degen_all = 0, 0
        for d in sorted(by_depth.keys()):
            t, dg = by_depth[d]["total"], by_depth[d]["degen"]
            result[f"d{d}"] = round(dg / t * 100, 1) if t > 0 else 0.0
            total_all += t
            degen_all += dg
        result["total"] = round(degen_all / total_all * 100, 1) if total_all > 0 else 0.0
        output[gen_name] = result
        print(f"  {gen_name}: {result}")

    with open(RESULTS / "degeneration_rates.json", "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {RESULTS / 'degeneration_rates.json'}")
    return output


# ============================================================
# Fix Artifact 5: rp_lofo_results.json Test B
# ============================================================
def fix_artifact5():
    print("=" * 60)
    print("Fix Artifact 5: rp_lofo Test B")

    # Train data: 7 generators (all except llama)
    df_csv = pd.read_csv(DATA_DIR / "features_all_models.csv")
    df_csv["label"] = df_csv["depth"].map(CLASS_MAP)

    mistral_rows = []
    with open(DATA_DIR / "mistral-7b-v0.3" / "features_pythia410m.jsonl") as f:
        for line in f:
            mistral_rows.append(json.loads(line))
    df_mistral = pd.DataFrame(mistral_rows)
    df_mistral["label"] = df_mistral["depth"].map(CLASS_MAP)
    df_mistral["model_name"] = "mistral-7b-v0.3"
    df_train = pd.concat([df_csv, df_mistral], ignore_index=True)
    print(f"  Train: {len(df_train)} rows")

    # Test B: Llama rp=1.0, filtered using generations_filtered.jsonl
    # The filtered file has 2937 lines. Match features by (seed_id, depth) order.
    filtered_seeds = []
    with open(DATA_DIR / "llama-3.2-3b" / "generations_filtered.jsonl") as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                filtered_seeds.append((rec.get("seed_id", rec.get("seed")), rec["depth"]))

    # Load all llama features
    llama_rows = []
    with open(DATA_DIR / "llama-3.2-3b" / "features_pythia410m.jsonl") as f:
        for line in f:
            llama_rows.append(json.loads(line))
    df_llama = pd.DataFrame(llama_rows)
    df_llama["label"] = df_llama["depth"].map(CLASS_MAP)

    # Also load all generation records to match indices
    gen_records = []
    with open(DATA_DIR / "llama-3.2-3b" / "generations_shard0.jsonl") as f:
        for line in f:
            if line.strip():
                gen_records.append(json.loads(line))

    # Filter by computing ratio on each generation
    keep_mask = np.array([compute_repeated_4gram_ratio(r["text"]) <= 0.5 for r in gen_records])
    n_kept = keep_mask.sum()
    print(f"  Llama rp=1.0: {n_kept}/{len(gen_records)} kept (filtered file has {len(filtered_seeds)})")

    df_test = df_llama[keep_mask].copy()

    # Train classifier
    clf = XGBClassifier(**XGB_PARAMS)
    clf.fit(df_train[FEATURES].values, df_train["label"].values.astype(int))

    # Predict
    X_test = df_test[FEATURES].values
    y_test = df_test["label"].values.astype(int)
    y_pred = clf.predict(X_test)

    # 3-class metrics
    f1_3class = f1_score(y_test, y_pred, average="macro")
    f1_per = f1_score(y_test, y_pred, average=None, labels=[0, 1, 2])
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1, 2]).tolist()

    per_class = {}
    for i, lbl in enumerate(["gen-0", "gen-1", "gen-2+"]):
        mask = y_test == i
        n = mask.sum()
        acc = (y_pred[mask] == i).sum() / n if n > 0 else 0
        per_class[lbl] = {"f1": round(float(f1_per[i]), 4), "accuracy": round(float(acc), 4), "n": int(n)}

    # Binary
    mask_bin = y_test > 0
    y_test_bin = (y_test[mask_bin] >= 2).astype(int)
    y_pred_bin = (y_pred[mask_bin] >= 2).astype(int)
    f1_binary = f1_score(y_test_bin, y_pred_bin, average="macro")
    f1_bin_per = f1_score(y_test_bin, y_pred_bin, average=None)
    cm_bin = confusion_matrix(y_test_bin, y_pred_bin).tolist()

    print(f"  Test B: 3-class F1={f1_3class:.4f}, binary F1={f1_binary:.4f}")
    print(f"    per-class: gen-0={f1_per[0]:.4f}, gen-1={f1_per[1]:.4f}, gen-2+={f1_per[2]:.4f}")

    # Update rp_lofo_results.json
    existing = json.load(open(RESULTS / "rp_lofo_results.json"))
    existing["test_B_llama_rp10_filtered"] = {
        "3class_f1": round(float(f1_3class), 4),
        "binary_f1": round(float(f1_binary), 4),
        "per_class": per_class,
        "confusion_matrix": cm,
        "binary_per_class": {
            "gen-1": round(float(f1_bin_per[0]), 4),
            "gen-2+": round(float(f1_bin_per[1]), 4),
        },
        "binary_confusion_matrix": cm_bin,
        "labels": ["gen-0", "gen-1", "gen-2+"],
        "n_kept": int(n_kept),
        "n_original": len(gen_records),
    }
    existing["test_A_llama_rp11"]["labels"] = ["gen-0", "gen-1", "gen-2+"]

    with open(RESULTS / "rp_lofo_results.json", "w") as f:
        json.dump(existing, f, indent=2, ensure_ascii=False)
    print(f"  Saved: {RESULTS / 'rp_lofo_results.json'}")
    return existing


if __name__ == "__main__":
    a4 = fix_artifact4()
    a5 = fix_artifact5()

    # Degeneration summary
    print("\n--- Degeneration Rates (%) ---")
    print(f"{'Generator':20s} {'d0':>6s} {'d1':>6s} {'d2':>6s} {'d3':>6s} {'d4':>6s} {'total':>6s}")
    print("-" * 60)
    for gen in ALL_8:
        if gen in a4:
            r = a4[gen]
            print(f"{gen:20s} {r.get('d0',0):6.1f} {r.get('d1',0):6.1f} {r.get('d2',0):6.1f} {r.get('d3',0):6.1f} {r.get('d4',0):6.1f} {r.get('total',0):6.1f}")

    # rp-LOFO summary
    print("\n--- rp-LOFO Results ---")
    for k in ["test_A_llama_rp11", "test_B_llama_rp10_filtered"]:
        v = a5[k]
        print(f"  {k}: 3class_f1={v['3class_f1']}, binary_f1={v['binary_f1']}")
        if "per_class" in v:
            for cls, info in v["per_class"].items():
                if isinstance(info, dict):
                    print(f"    {cls}: f1={info.get('f1', info.get('accuracy'))}, n={info.get('n', '?')}")
