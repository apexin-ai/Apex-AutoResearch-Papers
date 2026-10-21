"""Experiment B: NLI Gate Ablation + Experiment C: Cross-Axis Gradient.

Outputs:
  data/nli_gate_ablation.json
  data/cross_axis_gradient.json
"""

import json
import numpy as np
import choix

DATA_DIR = "/root/causal_style_decomp_judge/data"
N_BOOT = 10_000
SEED = 42
NLI_THRESHOLD = 0.90

AXES_PAIRWISE = {
    "formality": {
        "path": f"{DATA_DIR}/pairwise_results_qwen32b_formality.jsonl",
        "pref_fields": ("trial1_prefers_formal", "trial2_prefers_formal"),
    },
    "verbosity": {
        "path": f"{DATA_DIR}/pairwise_results_qwen32b_verbosity.jsonl",
        "pref_fields": ("trial1_prefers_verbose", "trial2_prefers_verbose"),
    },
}

AXES_VERIFIED = {
    "formality": f"{DATA_DIR}/verified_32b.jsonl",
    "verbosity": f"{DATA_DIR}/verified_verbosity.jsonl",
    "register": f"{DATA_DIR}/verified_register.jsonl",
}


def load_jsonl(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def build_comparisons(records, pref_t1, pref_t2):
    comparisons = []
    pair_groups = []
    for rec in records:
        pair_comps = []
        for key in [pref_t1, pref_t2]:
            pref = rec.get(key)
            if pref is None:
                continue
            pair_comps.append((0, 1) if pref else (1, 0))
        if pair_comps:
            comparisons.extend(pair_comps)
            pair_groups.append(pair_comps)
    return comparisons, pair_groups


def bt_probability(comparisons):
    params = choix.ilsr_pairwise(2, comparisons, alpha=0.01)
    return np.exp(params[0]) / (np.exp(params[0]) + np.exp(params[1]))


def bt_with_bootstrap(records, pref_t1, pref_t2):
    comparisons, pair_groups = build_comparisons(records, pref_t1, pref_t2)
    n_pairs = len(pair_groups)
    if n_pairs == 0:
        return {"n": 0, "bt": None, "ci": [None, None], "p": None}

    p_style = bt_probability(comparisons)

    rng = np.random.RandomState(SEED)
    boot_p = []
    for _ in range(N_BOOT):
        idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot_comps = []
        for i in idx:
            boot_comps.extend(pair_groups[i])
        try:
            boot_p.append(bt_probability(boot_comps))
        except Exception:
            pass

    boot_p = np.array(boot_p)
    ci_lo, ci_hi = np.percentile(boot_p, [2.5, 97.5])
    n_below = int(np.sum(boot_p < 0.5))
    p_val = max(n_below / len(boot_p), 1.0 / len(boot_p)) if n_below == 0 else n_below / len(boot_p)

    return {
        "n": n_pairs,
        "bt": round(float(p_style), 4),
        "ci": [round(float(ci_lo), 4), round(float(ci_hi), 4)],
        "p": round(float(p_val), 6),
    }


# ── Experiment B ─────────────────────────────────────────────────────

def run_nli_gate_ablation():
    results = {}
    for axis, cfg in AXES_PAIRWISE.items():
        records = load_jsonl(cfg["path"])
        pref_t1, pref_t2 = cfg["pref_fields"]

        nli_pass = [r for r in records if r.get("nli_cf", 0) >= NLI_THRESHOLD]
        nli_fail = [r for r in records if r.get("nli_cf", 0) < NLI_THRESHOLD]

        print(f"\n{'='*50}")
        print(f"  {axis.upper()}: {len(records)} total, "
              f"{len(nli_pass)} pass, {len(nli_fail)} fail")
        print(f"{'='*50}")

        res_pass = bt_with_bootstrap(nli_pass, pref_t1, pref_t2)
        print(f"  NLI-pass: BT={res_pass['bt']}, CI={res_pass['ci']}, p={res_pass['p']}")

        res_fail = bt_with_bootstrap(nli_fail, pref_t1, pref_t2)
        print(f"  NLI-fail: BT={res_fail['bt']}, CI={res_fail['ci']}, p={res_fail['p']}")

        res_all = bt_with_bootstrap(records, pref_t1, pref_t2)
        print(f"  All:      BT={res_all['bt']}, CI={res_all['ci']}, p={res_all['p']}")

        results[axis] = {
            "nli_pass": res_pass,
            "nli_fail": res_fail,
            "all": res_all,
        }

    out_path = f"{DATA_DIR}/nli_gate_ablation.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")
    return results


# ── Experiment C ─────────────────────────────────────────────────────

def run_cross_axis_gradient():
    canonical = {
        "formality": {"bt": 0.665, "likert_d": 0.012, "gee_style_or": 4.20},
        "verbosity": {"bt": 0.773, "likert_d": -0.146, "gee_style_or": 13.10},
        "register": {"bt": 0.553, "likert_d": 0.069, "gee_style_or": 1.91},
    }

    axes = []
    print(f"\n{'='*50}")
    print("  CROSS-AXIS GRADIENT")
    print(f"{'='*50}")

    for axis, path in AXES_VERIFIED.items():
        records = load_jsonl(path)
        n_total = len(records)
        n_reject = sum(1 for r in records if r.get("nli_cf", 1.0) < NLI_THRESHOLD)
        rej_rate = round(n_reject / n_total, 4) if n_total > 0 else None

        entry = {
            "axis": axis,
            "nli_rejection_rate": rej_rate,
            "n_total": n_total,
            "n_rejected": n_reject,
            **canonical[axis],
        }
        axes.append(entry)
        print(f"  {axis}: rejection={n_reject}/{n_total} ({rej_rate}), "
              f"BT={canonical[axis]['bt']}, d={canonical[axis]['likert_d']}, "
              f"OR={canonical[axis]['gee_style_or']}")

    result = {
        "axes": axes,
        "note": "Qualitative argument only. Higher NLI rejection ≈ more invasive manipulation.",
    }

    out_path = f"{DATA_DIR}/cross_axis_gradient.json"
    with open(out_path, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\nSaved: {out_path}")
    return result


if __name__ == "__main__":
    ablation = run_nli_gate_ablation()
    gradient = run_cross_axis_gradient()
