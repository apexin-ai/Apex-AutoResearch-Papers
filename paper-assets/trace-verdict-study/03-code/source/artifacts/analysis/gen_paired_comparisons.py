import json
import os
import numpy as np
from itertools import combinations
from scipy.stats import binomtest

BASE = "/root/autodl-tmp/trace-verdict-study-checkpoints"

GROUPS = {
    "Qwen (n=1190)": {
        "VOTA":           f"{BASE}/vota/final/predictions.jsonl",
        "exception_only": f"{BASE}/exception_only/final/predictions.jsonl",
        "ae_only":        f"{BASE}/ae_only/final/predictions.jsonl",
        "VOTA_no_ae":     f"{BASE}/vota_no_ae/final/predictions.jsonl",
        "label_only":     f"{BASE}/full_trace_label_only/final/predictions.jsonl",
        "loop_only":      f"{BASE}/loop_only/final/predictions.jsonl",
        "full_trace":     f"{BASE}/full_trace/final/predictions.jsonl",
        "no_trace":       f"{BASE}/no_trace/final/predictions.jsonl",
    },
    "DeepSeek (n=1190)": {
        "exception_only": f"{BASE}/deepseek_exception_only_seed123/final/predictions.jsonl",
        "VOTA":           f"{BASE}/deepseek_vota/final/predictions.jsonl",
        "no_trace":       f"{BASE}/deepseek_no_trace/final/predictions.jsonl",
    },
    "DebugBench (n=426)": {
        "exception_only": f"{BASE}/debugbench_exception_only/final/predictions.jsonl",
        "VOTA":           f"{BASE}/debugbench_vota/final/predictions.jsonl",
        "no_trace":       f"{BASE}/debugbench_no_trace/final/predictions.jsonl",
    },
}


def load_predictions(path):
    if not os.path.exists(path):
        return None
    records = []
    with open(path) as f:
        for line in f:
            r = json.loads(line)
            records.append(r)
    records.sort(key=lambda x: x["id"])
    return records


def accuracy(preds):
    correct = sum(1 for p in preds if p["pred"] == p["label"])
    return correct / len(preds)


def mcnemar_test(preds_a, preds_b):
    """Returns (b, c, p_value) where b=A wrong B right, c=A right B wrong."""
    assert len(preds_a) == len(preds_b)
    b = 0  # A wrong, B right
    c = 0  # A right, B wrong
    for a, bb in zip(preds_a, preds_b):
        assert a["id"] == bb["id"]
        a_correct = a["pred"] == a["label"]
        b_correct = bb["pred"] == bb["label"]
        if not a_correct and b_correct:
            b += 1
        elif a_correct and not b_correct:
            c += 1
    n = b + c
    if n == 0:
        return b, c, 1.0
    # Exact binomial test (two-sided)
    p_value = binomtest(min(b, c), n, 0.5).pvalue
    return b, c, p_value


def paired_bootstrap_ci(preds_a, preds_b, n_boot=10000, alpha=0.05, seed=42):
    """Bootstrap CI for accuracy difference (A - B)."""
    rng = np.random.RandomState(seed)
    n = len(preds_a)
    correct_a = np.array([1 if p["pred"] == p["label"] else 0 for p in preds_a])
    correct_b = np.array([1 if p["pred"] == p["label"] else 0 for p in preds_b])
    diffs = correct_a - correct_b  # per-sample difference

    boot_deltas = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        boot_deltas.append(diffs[idx].mean())
    boot_deltas = np.array(boot_deltas)
    lo = np.percentile(boot_deltas, 100 * alpha / 2)
    hi = np.percentile(boot_deltas, 100 * (1 - alpha / 2))
    return float(lo), float(hi)


def main():
    all_results = {}
    txt_lines = []

    for group_name, experiments in GROUPS.items():
        # Load all available predictions
        loaded = {}
        for name, path in experiments.items():
            preds = load_predictions(path)
            if preds is not None:
                loaded[name] = preds
                print(f"  Loaded {name}: {len(preds)} samples, acc={accuracy(preds)*100:.2f}%")
            else:
                print(f"  SKIP {name}: {path} not found")

        if len(loaded) < 2:
            print(f"  Skipping group {group_name}: fewer than 2 experiments\n")
            continue

        group_results = []
        pairs = list(combinations(sorted(loaded.keys()), 2))

        txt_lines.append(f"\n{'='*100}")
        txt_lines.append(f" {group_name}")
        txt_lines.append(f"{'='*100}")
        header = f"{'Pair (A vs B)':<35} {'Acc_A':>7} {'Acc_B':>7} {'Δ(A-B)':>8} {'95% CI':>18} {'McNemar p':>12} {'sig':>5}"
        txt_lines.append(header)
        txt_lines.append("-" * 100)

        for name_a, name_b in pairs:
            preds_a = loaded[name_a]
            preds_b = loaded[name_b]

            acc_a = accuracy(preds_a)
            acc_b = accuracy(preds_b)
            delta = acc_a - acc_b

            b, c, p_val = mcnemar_test(preds_a, preds_b)
            ci_lo, ci_hi = paired_bootstrap_ci(preds_a, preds_b)

            sig = ""
            if p_val < 0.001:
                sig = "***"
            elif p_val < 0.01:
                sig = "**"
            elif p_val < 0.05:
                sig = "*"
            else:
                sig = "ns"

            result = {
                "pair": f"{name_a} vs {name_b}",
                "name_a": name_a,
                "name_b": name_b,
                "acc_a": round(acc_a * 100, 2),
                "acc_b": round(acc_b * 100, 2),
                "delta": round(delta * 100, 2),
                "ci_lo": round(ci_lo * 100, 2),
                "ci_hi": round(ci_hi * 100, 2),
                "mcnemar_b": b,
                "mcnemar_c": c,
                "mcnemar_p": p_val,
                "sig": sig,
            }
            group_results.append(result)

            pair_str = f"{name_a} vs {name_b}"
            ci_str = f"[{ci_lo*100:+.2f}, {ci_hi*100:+.2f}]"
            line = f"{pair_str:<35} {acc_a*100:>6.2f}% {acc_b*100:>6.2f}% {delta*100:>+7.2f}% {ci_str:>18} {p_val:>12.2e} {sig:>5}"
            txt_lines.append(line)

        all_results[group_name] = group_results

    # Write JSON
    out_dir = "/root/trace-verdict-study/analysis"
    with open(f"{out_dir}/paired_comparisons.json", "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    # Write TXT
    txt_content = "\n".join(txt_lines) + "\n"
    with open(f"{out_dir}/paired_comparisons.txt", "w") as f:
        f.write(txt_content)

    print(f"\nSaved: {out_dir}/paired_comparisons.json")
    print(f"Saved: {out_dir}/paired_comparisons.txt")
    print(txt_content)


if __name__ == "__main__":
    main()
