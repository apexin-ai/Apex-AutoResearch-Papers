"""BT Model Diagnostics (W-MF2): GoF deviance + stratified BT stability."""

import json
import os

import choix
import numpy as np
from scipy import stats

NLI_THRESHOLD = 0.90
N_BOOT = 10000
SEED = 42


def load_filtered(path, wins_key):
    """Load NLI-filtered, consistent pairs with definitive outcome."""
    pairs = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            r = json.loads(line)
            if (r["nli_cf"] >= NLI_THRESHOLD
                    and r.get("consistent", False)
                    and r[wins_key] is not None):
                pairs.append(r)
    return pairs


def bt_prob(win_count, total):
    """BT win probability for 2-item model (item 0 = positive style)."""
    if total == 0:
        return 0.5
    data = [(0, 1)] * win_count + [(1, 0)] * (total - win_count)
    params = choix.ilsr_pairwise(2, data, alpha=0.01)
    return float(np.exp(params[0]) / np.sum(np.exp(params)))


def gof_deviance(pairs, wins_key):
    """Goodness-of-fit deviance test: all pairs share one BT probability."""
    n = len(pairs)
    w = sum(1 for p in pairs if p[wins_key])
    p_hat = bt_prob(w, n)

    eps = 1e-15
    p_s = np.clip(p_hat, eps, 1 - eps)
    D = -2.0 * (w * np.log(p_s) + (n - w) * np.log(1 - p_s))
    df = n - 1
    p_val = float(stats.chi2.sf(D, df))

    return {
        "deviance": round(float(D), 4),
        "df": df,
        "p_value": round(p_val, 6),
        "n_pairs": n,
        "wins": w,
        "bt_prob": round(p_hat, 4),
    }


def pair_bootstrap(pairs, wins_key, n_boot=N_BOOT, seed=SEED):
    """Pair-level bootstrap CI for win rate."""
    rng = np.random.RandomState(seed)
    outcomes = np.array([1 if p[wins_key] else 0 for p in pairs])
    n = len(outcomes)
    rates = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.randint(0, n, size=n)
        rates[i] = outcomes[idx].mean()
    ci = np.percentile(rates, [2.5, 97.5]).tolist()
    return float(outcomes.mean()), [round(ci[0], 4), round(ci[1], 4)]


def stratified(pairs, dir_key, wins_key, pos_label, neg_label):
    """Stratified BT by originality direction + Fisher/chi2 tests."""
    grp_pos = [p for p in pairs if p[dir_key] == pos_label]
    grp_neg = [p for p in pairs if p[dir_key] == neg_label]

    out = {}
    for name, grp in [(f"orig_is_{pos_label}", grp_pos),
                       (f"orig_is_{neg_label}", grp_neg)]:
        n = len(grp)
        wc = sum(1 for p in grp if p[wins_key])
        rate, ci = pair_bootstrap(grp, wins_key)
        out[name] = {
            "n": n,
            "bt": round(rate, 4),
            "ci": ci,
            "win_count": wc,
            "total": n,
        }

    a = out[f"orig_is_{pos_label}"]["win_count"]
    b = out[f"orig_is_{pos_label}"]["total"] - a
    c = out[f"orig_is_{neg_label}"]["win_count"]
    d = out[f"orig_is_{neg_label}"]["total"] - c

    _, fisher_p = stats.fisher_exact([[a, b], [c, d]])
    chi2_stat, chi2_p, _, _ = stats.chi2_contingency(
        [[a, b], [c, d]], correction=False
    )

    out["fisher_p"] = round(float(fisher_p), 6)
    out["chi2_p"] = round(float(chi2_p), 6)
    return out


def main():
    os.chdir("/root/causal_style_decomp_judge")

    form = load_filtered("data/pairwise_results_32b.jsonl", "formal_wins")
    verb = load_filtered(
        "data/pairwise_results_qwen32b_verbosity.jsonl", "verbose_wins"
    )

    print(f"Formality: {len(form)} consistent NLI-pass pairs")
    print(f"Verbosity: {len(verb)} consistent NLI-pass pairs")

    result = {
        "gof": {
            "formality": gof_deviance(form, "formal_wins"),
            "verbosity": gof_deviance(verb, "verbose_wins"),
        },
        "stratified_bt": {
            "formality": stratified(
                form, "original_formality", "formal_wins",
                "formal", "casual"
            ),
            "verbosity": stratified(
                verb, "original_verbosity", "verbose_wins",
                "verbose", "concise"
            ),
        },
    }

    out_path = "data/bt_model_diagnostics.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\nSaved to {out_path}")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
