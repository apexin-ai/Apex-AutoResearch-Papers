#!/usr/bin/env python3
"""Plan 010: Non-majority-vote aggregation experiment.
Recompute panel ASR under 4 aggregation rules and run regression analysis."""

import json
import re
import numpy as np
from itertools import combinations
from collections import Counter
from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

_WINNER_RE = re.compile(r'"winner"\s*:\s*"([ABC])"')


def extract_winner(entry):
    if "winner" in entry:
        return entry["winner"]
    if "raw" in entry:
        m = _WINNER_RE.search(entry["raw"])
        if m:
            return m.group(1)
    return "PARSE_ERROR"

MODELS = [
    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
]
DATASETS = ["mmlu", "arc_challenge"]
STEP2V3_ATTACKS = ["prompt_injection", "sycophancy", "score_manipulation"]
TAXONOMY_ATTACKS = ["verbosity_bias", "position_bias", "authority_bias"]
ALL_ATTACKS = STEP2V3_ATTACKS + TAXONOMY_ATTACKS
EPSILON = 0.001

BASE = Path("/root/cert_manip_resist_eval")
RESULTS_DIR = BASE / "artifacts" / "results"


# ---------------------------------------------------------------------------
# Aggregation functions
# ---------------------------------------------------------------------------

def agg_majority(votes, _weights):
    c = Counter(votes)
    mc = c.most_common()
    if mc[0][1] >= 2:
        return mc[0][0]
    return "TIE"


def agg_weighted(votes, weights):
    scores = {}
    for v, w in zip(votes, weights):
        scores[v] = scores.get(v, 0.0) + w
    ranked = sorted(scores.items(), key=lambda x: -x[1])
    if len(ranked) >= 2 and abs(ranked[0][1] - ranked[1][1]) < 1e-12:
        return "TIE"
    return ranked[0][0]


def agg_threshold(votes, _weights):
    if votes[0] == votes[1] == votes[2]:
        return votes[0]
    return "ABSTAIN"


def agg_bayesian(votes, reliabilities):
    log_pa, log_pb = 0.0, 0.0
    for v, p in zip(votes, reliabilities):
        p = max(min(p, 0.999), 0.001)
        lp, l1p = np.log(p), np.log(1.0 - p)
        log_pa += lp if v == "A" else l1p
        log_pb += lp if v == "B" else l1p
    if log_pa > log_pb:
        return "A"
    if log_pb > log_pa:
        return "B"
    return "TIE"


METHODS = {
    "majority_vote": agg_majority,
    "weighted_vote": agg_weighted,
    "threshold_vote": agg_threshold,
    "bayesian": agg_bayesian,
}


# ---------------------------------------------------------------------------
# Core helpers
# ---------------------------------------------------------------------------

def compute_asr(clean_decs, atk_decs, clean_gt, atk_gt):
    cc = fl = 0
    for cd, ad, cg, ag in zip(clean_decs, atk_decs, clean_gt, atk_gt):
        if cd == cg:
            cc += 1
            if ad != ag:
                fl += 1
    return fl / cc if cc > 0 else 0.0


def run_regression(records):
    import statsmodels.api as sm
    y = np.array([np.log(r["asr"] + EPSILON) for r in records])
    X = np.column_stack([
        [np.log(r["k_eff"]) for r in records],
        [np.log(r["eta_max"] + EPSILON) for r in records],
    ])
    X = sm.add_constant(X)
    m = sm.OLS(y, X).fit()
    return {
        "keff_beta": float(m.params[1]),
        "keff_p": float(m.pvalues[1]),
        "eta_max_beta": float(m.params[2]),
        "eta_max_p": float(m.pvalues[2]),
        "R2": float(m.rsquared),
        "adj_R2": float(m.rsquared_adj),
        "n_panels": len(y),
        "f_stat": float(m.fvalue),
        "f_pvalue": float(m.f_pvalue),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Load data
    with open(RESULTS_DIR / "_step2v3_checkpoint.json") as f:
        s_ckpt = json.load(f)
    with open(RESULTS_DIR / "_taxonomy_checkpoint.json") as f:
        t_ckpt = json.load(f)
    with open(RESULTS_DIR / "results_step2v3_regression_20260522_031307.json") as f:
        s_results = json.load(f)
    with open(RESULTS_DIR / "results_taxonomy_broadspectrum_20260522_044539.json") as f:
        t_results = json.load(f)

    # 20 panels = C(6,3)
    panels = [tuple(MODELS[i] for i in c) for c in combinations(range(6), 3)]

    # K_eff lookup: sorted judge tuple -> {ds: keff}
    keff_lookup = {}
    for p in s_results["all_20_panels"]:
        keff_lookup[tuple(sorted(p["judge_ids"]))] = p["k_eff"]

    # Existing panel ASR for sanity check (majority vote from step2v3)
    existing_asr = {}
    for p in s_results["all_20_panels"]:
        key = tuple(sorted(p["judge_ids"]))
        existing_asr[key] = p["asr_by_attack"]

    # Precompute: clean accuracy per judge per dataset per checkpoint
    clean_acc = {}
    for tag, ckpt in [("s", s_ckpt), ("t", t_ckpt)]:
        for ds in DATASETS:
            gt = [p["ground_truth_winner"] for p in ckpt["pairs"][ds]]
            for judge in MODELS:
                votes = [extract_winner(s) for s in ckpt["clean_scores"][ds][judge]]
                clean_acc[(tag, ds, judge)] = sum(
                    1 for v, g in zip(votes, gt) if v == g
                ) / len(gt)

    # Precompute: extract vote arrays to avoid repeated dict lookups
    # clean_v[tag][ds][judge] = [str, ...]  (300 items)
    # atk_v[tag][ds][atk][judge] = [str, ...]
    clean_v = {"s": {}, "t": {}}
    atk_v = {"s": {}, "t": {}}
    for tag, ckpt in [("s", s_ckpt), ("t", t_ckpt)]:
        for ds in DATASETS:
            clean_v[tag][ds] = {
                j: [extract_winner(s) for s in ckpt["clean_scores"][ds][j]]
                for j in MODELS
            }
            atk_v[tag][ds] = {}
            attacks = STEP2V3_ATTACKS if tag == "s" else TAXONOMY_ATTACKS
            for atk in attacks:
                atk_v[tag][ds][atk] = {
                    j: [extract_winner(s) for s in ckpt["attacked_scores"][ds][atk][j]]
                    for j in MODELS
                }

    # Precompute: ground truths
    clean_gt_arr = {"s": {}, "t": {}}
    atk_gt_arr = {"s": {}, "t": {}}
    for tag, ckpt in [("s", s_ckpt), ("t", t_ckpt)]:
        for ds in DATASETS:
            cgt = [p["ground_truth_winner"] for p in ckpt["pairs"][ds]]
            clean_gt_arr[tag][ds] = cgt
            atk_gt_arr[tag][ds] = {}
            attacks = STEP2V3_ATTACKS if tag == "s" else TAXONOMY_ATTACKS
            for atk in attacks:
                if atk == "position_bias":
                    atk_gt_arr[tag][ds][atk] = [
                        p["ground_truth_winner"] for p in ckpt["swapped_pairs"][ds]
                    ]
                else:
                    atk_gt_arr[tag][ds][atk] = cgt

    # Free large checkpoint dicts
    del s_ckpt, t_ckpt

    # Run all methods
    output = {"aggregation_methods": {}}

    for method_name, agg_fn in METHODS.items():
        conditions = {}
        for ds in DATASETS:
            for atk in ALL_ATTACKS:
                tag = "s" if atk in STEP2V3_ATTACKS else "t"
                cond_key = f"{ds}__{atk}"
                n_samples = len(clean_gt_arr[tag][ds])
                c_gt = clean_gt_arr[tag][ds]
                a_gt = atk_gt_arr[tag][ds][atk]

                # Individual ASR per judge (for eta_max)
                indiv_asr = {}
                for judge in MODELS:
                    cv = clean_v[tag][ds][judge]
                    av = atk_v[tag][ds][atk][judge]
                    cc = fl = 0
                    for i in range(n_samples):
                        if cv[i] == c_gt[i]:
                            cc += 1
                            if av[i] != a_gt[i]:
                                fl += 1
                    indiv_asr[judge] = fl / cc if cc > 0 else 0.0

                panel_records = []
                for panel in panels:
                    judges = list(panel)
                    weights = [clean_acc[(tag, ds, j)] for j in judges]

                    clean_decs = []
                    atk_decs = []
                    for i in range(n_samples):
                        cv = [clean_v[tag][ds][j][i] for j in judges]
                        av = [atk_v[tag][ds][atk][j][i] for j in judges]
                        clean_decs.append(agg_fn(cv, weights))
                        atk_decs.append(agg_fn(av, weights))

                    asr = compute_asr(clean_decs, atk_decs, c_gt, a_gt)
                    keff = keff_lookup[tuple(sorted(judges))][ds]
                    eta_max = max(indiv_asr[j] for j in judges)
                    panel_records.append({
                        "asr": asr, "k_eff": keff, "eta_max": eta_max,
                    })

                reg = run_regression(panel_records)
                conditions[cond_key] = reg

                # Sanity check: majority_vote should match existing results
                if method_name == "majority_vote" and atk in STEP2V3_ATTACKS:
                    key = tuple(sorted(panels[0]))
                    ref = existing_asr[key][ds][atk]
                    got = panel_records[0]["asr"]
                    if abs(ref - got) > 0.01:
                        print(f"WARNING: majority ASR mismatch for {cond_key} "
                              f"panel 0: existing={ref:.4f}, computed={got:.4f}")

        n_cond = len(conditions)
        eta_sig = sum(1 for v in conditions.values() if v["eta_max_p"] < 0.05)
        keff_sig_neg = sum(
            1 for v in conditions.values()
            if v["keff_p"] < 0.05 and v["keff_beta"] < 0
        )

        output["aggregation_methods"][method_name] = {
            "conditions": conditions,
            "summary": {
                "eta_max_sig": f"{eta_sig}/{n_cond}",
                "keff_sig_neg": f"{keff_sig_neg}/{n_cond}",
                "mean_R2": float(np.mean([v["R2"] for v in conditions.values()])),
            },
        }

    # Cross-method comparison
    all_eta_dominant = True
    any_keff_sig = False
    for r in output["aggregation_methods"].values():
        e, t = (int(x) for x in r["summary"]["eta_max_sig"].split("/"))
        k = int(r["summary"]["keff_sig_neg"].split("/")[0])
        if e < t // 2:
            all_eta_dominant = False
        if k > 0:
            any_keff_sig = True

    if all_eta_dominant and not any_keff_sig:
        interp = ("eta_max dominates across all aggregation rules; K_eff never "
                   "significantly negative. Strongly supports Theorem 1 "
                   "(weakest-link) universality.")
    elif all_eta_dominant:
        interp = ("eta_max dominates but K_eff shows significance in some "
                   "conditions. Partial support for Theorem 1.")
    else:
        interp = ("eta_max does not consistently dominate. Aggregation rule "
                   "modulates vulnerability patterns.")

    output["comparison"] = {
        "eta_max_dominates_all": all_eta_dominant,
        "keff_sig_any_method": str(any_keff_sig),
        "interpretation": interp,
    }

    # Save
    out_path = RESULTS_DIR / "results_plan010_aggregation.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2,
                  default=lambda x: float(x) if isinstance(x, np.floating) else x)
    print(f"Saved: {out_path}")

    # Print summary
    print("\n=== Summary ===")
    for m in METHODS:
        s = output["aggregation_methods"][m]["summary"]
        print(f"  {m}: eta_max sig={s['eta_max_sig']}, "
              f"keff sig_neg={s['keff_sig_neg']}, mean R²={s['mean_R2']:.3f}")
    print(f"\n  {output['comparison']['interpretation']}")


if __name__ == "__main__":
    main()
