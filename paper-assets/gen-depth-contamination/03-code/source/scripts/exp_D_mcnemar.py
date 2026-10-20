"""EXP-D McNemar paired test + Bootstrap difference CI: OBD vs LLMs.

Re-runs OBD out-of-fold predictions on the same 500 samples as exp-011,
then performs McNemar exact test and bootstrap CI on accuracy differences.
"""
import csv
import json
import re
from pathlib import Path

import numpy as np

PROJECT = Path("/root/autodl-tmp/gen-depth-contamination")
DATA_DIR = PROJECT / "data_exp001_pythia"
SAMPLES_PATH = PROJECT / "artifacts" / "exp011_samples.jsonl"
GPT_PATH = PROJECT / "artifacts" / "exp011_results_gpt_5_5.jsonl"
CLAUDE_PATH = PROJECT / "artifacts" / "exp011_results_claude_opus_4_6.jsonl"
OUT_PATH = PROJECT / "artifacts" / "exp_D_mcnemar.json"

FEAT_COLS = [
    "surp_mean", "surp_std", "surp_skew", "surp_kurt",
    "surp_d1_mean", "surp_d1_std", "surp_d1_skew",
    "surp_d2_mean", "surp_d2_std",
    "ttr", "hapax_ratio", "self_bleu",
    "freq_kurtosis", "freq_entropy", "low_freq_ratio",
]

MAX_DEPTH = 5
N_SPLITS = 5
N_BOOTSTRAP = 10000
SEED = 42


def load_features():
    feat_path = DATA_DIR / "features.csv"
    with open(feat_path) as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    depths = np.array([int(r["depth"]) for r in rows])
    doc_ids = np.array([int(r["doc_id"]) for r in rows])
    X = np.array([
        [float(r[c]) if r[c] not in ("", "nan") else np.nan for c in FEAT_COLS]
        for r in rows
    ])
    col_means = np.nanmean(X, axis=0)
    for j in range(X.shape[1]):
        mask = np.isnan(X[:, j])
        X[mask, j] = col_means[j]
    return X, depths, doc_ids


def run_obd_oof(X, y, groups, max_depth, n_splits):
    import lightgbm as lgb
    from sklearn.model_selection import GroupKFold

    n = len(y)
    cum_probs = np.zeros((n, max_depth))
    gkf = GroupKFold(n_splits=n_splits)
    fold_indices = list(gkf.split(X, y, groups=groups))

    for k in range(max_depth):
        y_bin = (y > k).astype(int)
        for train_idx, test_idx in fold_indices:
            clf = lgb.LGBMClassifier(
                n_estimators=200, max_depth=6, learning_rate=0.05,
                num_leaves=31, verbose=-1, n_jobs=-1,
            )
            clf.fit(X[train_idx], y_bin[train_idx])
            cum_probs[test_idx, k] = clf.predict_proba(X[test_idx])[:, 1]

    n_classes = max_depth + 1
    class_probs = np.zeros((n, n_classes))
    class_probs[:, 0] = 1.0 - cum_probs[:, 0]
    for k in range(1, max_depth):
        class_probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
    class_probs[:, max_depth] = cum_probs[:, max_depth - 1]
    class_probs = np.clip(class_probs, 0, None)
    row_sums = class_probs.sum(axis=1, keepdims=True)
    row_sums[row_sums == 0] = 1.0
    class_probs /= row_sums

    return class_probs.argmax(axis=1)


def parse_exp011_doc_id(doc_id_str):
    m = re.match(r"pythia_d(\d+)_(\d+)", doc_id_str)
    if not m:
        raise ValueError(f"Cannot parse doc_id: {doc_id_str}")
    return int(m.group(1)), int(m.group(2))


def load_llm_predictions(path):
    preds = {}
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            preds[rec["doc_id"]] = rec["predicted_depth"]
    return preds


def mcnemar_test(obd_correct, llm_correct):
    """McNemar exact test using binomial test on discordant pairs."""
    from scipy.stats import binomtest

    b = int(np.sum(obd_correct & ~llm_correct))  # OBD right, LLM wrong
    c = int(np.sum(~obd_correct & llm_correct))   # OBD wrong, LLM right
    a = int(np.sum(obd_correct & llm_correct))     # both right
    d = int(np.sum(~obd_correct & ~llm_correct))   # both wrong

    n_discordant = b + c
    if n_discordant == 0:
        p_value = 1.0
    else:
        result = binomtest(b, n_discordant, 0.5, alternative='two-sided')
        p_value = result.pvalue

    return {"a": a, "b": b, "c": c, "d": d}, p_value


def bootstrap_diff_ci(y_true, obd_preds, llm_preds, n_boot, seed):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    diffs = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.randint(0, n, size=n)
        acc_obd = np.mean(obd_preds[idx] == y_true[idx])
        acc_llm = np.mean(llm_preds[idx] == y_true[idx])
        diffs[i] = acc_obd - acc_llm
    return diffs


def run_comparison(y_true, obd_preds, llm_preds, llm_name):
    obd_correct = obd_preds == y_true
    llm_correct = llm_preds == y_true

    acc_obd = float(np.mean(obd_correct))
    acc_llm = float(np.mean(llm_correct))
    diff = acc_obd - acc_llm

    table, p_value = mcnemar_test(obd_correct, llm_correct)

    diffs = bootstrap_diff_ci(y_true, obd_preds, llm_preds, N_BOOTSTRAP, SEED)
    ci_lower = float(np.percentile(diffs, 2.5))
    ci_upper = float(np.percentile(diffs, 97.5))

    print(f"\n--- OBD vs {llm_name} ---")
    print(f"  OBD accuracy:  {acc_obd:.3f}")
    print(f"  {llm_name} accuracy: {acc_llm:.3f}")
    print(f"  Difference:    {diff:+.3f}")
    print(f"  Contingency:   a={table['a']}, b={table['b']}, c={table['c']}, d={table['d']}")
    print(f"  McNemar exact p = {p_value:.4f}")
    print(f"  Bootstrap 95% CI on diff: [{ci_lower:+.4f}, {ci_upper:+.4f}]")
    print(f"  CI includes 0: {'YES' if ci_lower <= 0 <= ci_upper else 'NO'}")

    return {
        "accuracy_obd": round(acc_obd, 4),
        "accuracy_llm": round(acc_llm, 4),
        "accuracy_diff": round(diff, 4),
        "contingency_table": table,
        "mcnemar_p": round(p_value, 4),
        "bootstrap_ci_lower": round(ci_lower, 4),
        "bootstrap_ci_upper": round(ci_upper, 4),
        "bootstrap_n": N_BOOTSTRAP,
        "n_samples": len(y_true),
    }


def main():
    print("Loading features and running OBD OOF...")
    X, depths, doc_ids = load_features()
    oof_preds = run_obd_oof(X, depths, doc_ids, MAX_DEPTH, N_SPLITS)

    # Build lookup: (depth, orig_doc_id) -> row index
    lookup = {}
    for i in range(len(depths)):
        lookup[(int(depths[i]), int(doc_ids[i]))] = i

    # Load exp-011 samples and LLM predictions
    with open(SAMPLES_PATH) as f:
        samples = [json.loads(line) for line in f]
    gpt_preds_map = load_llm_predictions(GPT_PATH)
    claude_preds_map = load_llm_predictions(CLAUDE_PATH)

    # Align all predictions by sample order
    y_true_list = []
    obd_pred_list = []
    gpt_pred_list = []
    claude_pred_list = []
    skipped = 0

    for s in samples:
        doc_id = s["doc_id"]
        d, orig_id = parse_exp011_doc_id(doc_id)
        key = (d, orig_id)

        if key not in lookup:
            skipped += 1
            continue
        if doc_id not in gpt_preds_map or doc_id not in claude_preds_map:
            skipped += 1
            continue

        true_depth = s["true_depth"]
        # Cap at 4 for 5-class comparison (depths 0-4 only)
        if true_depth > 4:
            skipped += 1
            continue

        row_idx = lookup[key]
        y_true_list.append(true_depth)
        obd_pred_list.append(min(oof_preds[row_idx], 4))
        gpt_pred_list.append(min(gpt_preds_map[doc_id], 4))
        claude_pred_list.append(min(claude_preds_map[doc_id], 4))

    y_true = np.array(y_true_list)
    obd_preds = np.array(obd_pred_list)
    gpt_preds = np.array(gpt_pred_list)
    claude_preds = np.array(claude_pred_list)

    print(f"Aligned {len(y_true)} samples (skipped {skipped})")

    result_gpt = run_comparison(y_true, obd_preds, gpt_preds, "GPT-5.5")
    result_claude = run_comparison(y_true, obd_preds, claude_preds, "Claude")

    output = {
        "obd_vs_gpt55": result_gpt,
        "obd_vs_claude": result_claude,
        "method": "McNemar exact test (binomial) + bootstrap 10k difference CI, OBD out-of-fold",
        "seed": SEED,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {OUT_PATH}")


if __name__ == "__main__":
    main()
