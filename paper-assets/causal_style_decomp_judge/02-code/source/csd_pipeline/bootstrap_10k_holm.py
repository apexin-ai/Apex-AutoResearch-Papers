"""GPT-4o formality BT 10k bootstrap + Holm-Bonferroni + Qwen register Cohen's d."""

import json
import numpy as np
import choix

DATA_PAIRWISE = "/root/causal_style_decomp_judge/data/pairwise_results_32b.jsonl"
DATA_REGISTER = "/root/causal_style_decomp_judge/data/scored_qwen32b_register.jsonl"
N_BOOT = 10000
FORMAL, CASUAL = 0, 1


# ── Task A: GPT-4o Formality BT Bootstrap 10k ──

def load_pairwise(path, nli_threshold=0.90):
    raw = []
    with open(path) as f:
        for line in f:
            if line.strip():
                raw.append(json.loads(line))
    raw = [d for d in raw if d.get("nli_cf", 0) >= nli_threshold]

    comparisons = []
    pair_groups = {}

    for rec in raw:
        pair_id = rec["id"]
        pcomps = []

        t1 = rec.get("trial1_choice")
        if t1 in ("A", "B"):
            if t1 == "A":
                pcomps.append((FORMAL, CASUAL))
            else:
                pcomps.append((CASUAL, FORMAL))

        t2 = rec.get("trial2_choice")
        if t2 in ("A", "B"):
            if t2 == "A":
                pcomps.append((CASUAL, FORMAL))
            else:
                pcomps.append((FORMAL, CASUAL))

        comparisons.extend(pcomps)
        pair_groups[pair_id] = pcomps

    return comparisons, pair_groups


def fit_bt(comparisons):
    params = choix.ilsr_pairwise(2, comparisons, alpha=0.01)
    return params[FORMAL] - params[CASUAL]


def bootstrap_pair(pair_groups, n_boot=N_BOOT, seed=42):
    rng = np.random.RandomState(seed)
    pair_ids = list(pair_groups.keys())
    n_pairs = len(pair_ids)
    diffs = []
    for _ in range(n_boot):
        idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot = []
        for i in idx:
            boot.extend(pair_groups[pair_ids[i]])
        try:
            p = choix.ilsr_pairwise(2, boot, alpha=0.01)
            diffs.append(p[FORMAL] - p[CASUAL])
        except Exception:
            pass
    return np.array(diffs)


def task_a():
    comps, pairs = load_pairwise(DATA_PAIRWISE, nli_threshold=0.90)
    diff = fit_bt(comps)
    p_formal = 1.0 / (1.0 + np.exp(-diff))

    bp = bootstrap_pair(pairs, n_boot=N_BOOT, seed=42)
    bp_probs = 1.0 / (1.0 + np.exp(-bp))
    bp_lo, bp_hi = np.percentile(bp_probs, [2.5, 97.5])

    n_below = int(np.sum(bp_probs < 0.5))
    raw_p = n_below / len(bp)
    if raw_p == 0:
        raw_p_bound = 1.0 / len(bp)
        p_str = f"p < {raw_p_bound:.4f}"
        raw_p_for_holm = raw_p_bound
    else:
        p_str = f"p = {raw_p:.4f}"
        raw_p_for_holm = raw_p

    print("## Bootstrap 10k")
    print(f"GPT-4o formality: P(formal)={p_formal*100:.1f}%, "
          f"CI [{bp_lo*100:.1f}%, {bp_hi*100:.1f}%], raw {p_str}")
    print(f"  (N pairs={len(pairs)}, N comparisons={len(comps)}, "
          f"N boot={len(bp)}, below_0.5={n_below})")

    return raw_p_for_holm


# ── Holm-Bonferroni ──

def holm_bonferroni(labels, raw_ps, alpha=0.05):
    m = len(raw_ps)
    order = sorted(range(m), key=lambda i: raw_ps[i])
    adjusted = [0.0] * m

    cum_max = 0.0
    for rank, orig_idx in enumerate(order):
        adj = raw_ps[orig_idx] * (m - rank)
        adj = min(adj, 1.0)
        cum_max = max(cum_max, adj)
        adjusted[orig_idx] = cum_max

    print("\n## Holm-Bonferroni (family=6)")
    print(f"| {'Judge':<12} | {'Axis':<12} | {'Raw p':<12} | {'Adjusted p':<14} | {'Significant?':<12} |")
    print(f"|{'-'*14}|{'-'*14}|{'-'*14}|{'-'*16}|{'-'*14}|")
    for i in range(m):
        judge, axis = labels[i]
        sig = "Yes" if adjusted[i] < alpha else "No"
        print(f"| {judge:<12} | {axis:<12} | {raw_ps[i]:<12.4f} | {adjusted[i]:<14.4f} | {sig:<12} |")


# ── Task B: Cohen's d ──

def task_b():
    data = []
    with open(DATA_REGISTER) as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))

    data = [d for d in data if d.get("nli_cf", 0) >= 0.90]

    academic_scores = []
    conversational_scores = []

    for d in data:
        if d["original_register"] == "conversational":
            conversational_scores.append(d["score_original"])
            academic_scores.append(d["score_counterfactual"])
        else:
            academic_scores.append(d["score_original"])
            conversational_scores.append(d["score_counterfactual"])

    acad = np.array(academic_scores, dtype=float)
    conv = np.array(conversational_scores, dtype=float)

    n_a, n_c = len(acad), len(conv)
    mean_a, mean_c = np.mean(acad), np.mean(conv)
    pooled_sd = np.sqrt(
        ((n_a - 1) * np.var(acad, ddof=1) + (n_c - 1) * np.var(conv, ddof=1))
        / (n_a + n_c - 2)
    )
    d = (mean_a - mean_c) / pooled_sd

    print(f"\n## Cohen's d")
    print(f"Qwen3-32B Register: d = {d:.3f}")
    print(f"  (N={n_a}, mean_acad={mean_a:.4f}, mean_conv={mean_c:.4f}, "
          f"ATE={mean_a - mean_c:.4f}, pooled_SD={pooled_sd:.4f})")


def main():
    gpt4o_formality_p = task_a()

    labels = [
        ("GPT-4o", "formality"),
        ("GPT-4o", "verbosity"),
        ("GPT-4o", "register"),
        ("Qwen3-32B", "formality"),
        ("Qwen3-32B", "verbosity"),
        ("Qwen3-32B", "register"),
    ]
    raw_ps = [
        gpt4o_formality_p,
        0.0001,
        0.04,
        0.0001,
        0.0001,
        0.0763,
    ]
    holm_bonferroni(labels, raw_ps)

    task_b()


if __name__ == "__main__":
    main()
