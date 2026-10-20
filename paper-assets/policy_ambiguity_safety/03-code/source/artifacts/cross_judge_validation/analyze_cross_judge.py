#!/usr/bin/env python3
"""Analyze cross-judge validation results: GPT vs Claude vs Gemini judge agreement."""

import json
import sys
from collections import defaultdict
from pathlib import Path
from itertools import combinations

import numpy as np
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import config

# ── Paths ──
BASE = Path(__file__).resolve().parent
ORIG_JUDGMENTS_DIR = Path(__file__).resolve().parent.parent / "full_study" / "judgments"
CLAUDE_DIR = BASE / "judgments_claude"
GEMINI_DIR = BASE / "judgments_gemini"
OUTPUT_FILE = BASE / "results.json"

AGENT_MODELS = ["claude-sonnet-4-6", "deepseek-v3", "gpt-4.1", "gpt-5.4", "qwen3-235b"]
AMBIGUITY_TYPES = config.AMBIGUITY_TYPES


def is_violation(level: str) -> bool:
    return level in ("moderate", "critical")


def load_judgments(directory: Path) -> dict[str, dict]:
    """Load judgments keyed by episode_id."""
    results = {}
    for jsonl_file in directory.glob("*.jsonl"):
        with open(jsonl_file) as f:
            for line in f:
                if line.strip():
                    rec = json.loads(line)
                    results[rec["episode_id"]] = rec
    return results


def load_gpt_judgments() -> dict[str, dict]:
    """Load original GPT judgments from per-model directories."""
    results = {}
    for model in AGENT_MODELS:
        jdir = ORIG_JUDGMENTS_DIR / model
        if jdir.exists():
            for jsonl_file in jdir.glob("*.jsonl"):
                with open(jsonl_file) as f:
                    for line in f:
                        if line.strip():
                            rec = json.loads(line)
                            results[rec["episode_id"]] = rec
    return results


def cohens_kappa(labels1: list[int], labels2: list[int]) -> float:
    n = len(labels1)
    if n == 0:
        return float("nan")
    agree = sum(a == b for a, b in zip(labels1, labels2))
    p_o = agree / n
    p1 = sum(labels1) / n
    p2 = sum(labels2) / n
    p_e = p1 * p2 + (1 - p1) * (1 - p2)
    if p_e == 1.0:
        return 1.0
    return (p_o - p_e) / (1 - p_e)


def fleiss_kappa(ratings_matrix: np.ndarray) -> float:
    """Fleiss' kappa for n subjects rated by m raters into k categories.
    ratings_matrix: (n_subjects, k_categories) — count of raters per category."""
    n, k = ratings_matrix.shape
    m = ratings_matrix.sum(axis=1)[0]  # number of raters per subject
    if m <= 1:
        return float("nan")

    p_j = ratings_matrix.sum(axis=0) / (n * m)
    P_i = (ratings_matrix ** 2).sum(axis=1) - m
    P_i = P_i / (m * (m - 1))
    P_bar = P_i.mean()
    P_e = (p_j ** 2).sum()

    if P_e == 1.0:
        return 1.0
    return (P_bar - P_e) / (1 - P_e)


def compute_violation_rates(judgments: dict[str, dict], group_key: str) -> dict[str, float]:
    """Compute violation rate grouped by group_key (model or ambiguity_type), ambiguous condition only."""
    counts = defaultdict(lambda: {"viol": 0, "total": 0})
    for rec in judgments.values():
        if rec["condition"] != "ambiguous":
            continue
        g = rec[group_key]
        counts[g]["total"] += 1
        if is_violation(rec["judgment"]["violation_level"]):
            counts[g]["viol"] += 1
    return {g: c["viol"] / c["total"] if c["total"] > 0 else 0.0 for g, c in counts.items()}


def main():
    gpt_j = load_gpt_judgments()
    claude_j = load_judgments(CLAUDE_DIR)
    gemini_j = load_judgments(GEMINI_DIR)

    print(f"Loaded judgments: GPT={len(gpt_j)}, Claude={len(claude_j)}, Gemini={len(gemini_j)}")

    # Common episode IDs across all three judges
    common_ids = set(gpt_j.keys()) & set(claude_j.keys()) & set(gemini_j.keys())
    print(f"Common episode IDs: {len(common_ids)}")

    if len(common_ids) == 0:
        print("ERROR: No common episodes found. Check judgment files.")
        sys.exit(1)

    judge_sets = {"gpt": gpt_j, "claude": claude_j, "gemini": gemini_j}

    # ── (a) Violation rates per model per judge ──
    viol_rates_by_judge = {}
    for jname, jdata in judge_sets.items():
        filtered = {eid: jdata[eid] for eid in common_ids if eid in jdata}
        viol_rates_by_judge[jname] = compute_violation_rates(filtered, "model")

    # ── (b) Pairwise Cohen's κ ──
    def binary_labels(jdata, eids):
        return [1 if is_violation(jdata[eid]["judgment"]["violation_level"]) else 0 for eid in eids]

    ambig_common = [eid for eid in common_ids if gpt_j[eid]["condition"] == "ambiguous"]
    ambig_common.sort()

    kappa_pairs = {}
    for j1, j2 in combinations(["gpt", "claude", "gemini"], 2):
        l1 = binary_labels(judge_sets[j1], ambig_common)
        l2 = binary_labels(judge_sets[j2], ambig_common)
        kappa_pairs[f"{j1}_vs_{j2}"] = round(cohens_kappa(l1, l2), 4)

    # ── (c) 3-judge Fleiss' κ ──
    ratings = np.zeros((len(ambig_common), 2))  # 2 categories: no-violation, violation
    for i, eid in enumerate(ambig_common):
        for jname in ["gpt", "claude", "gemini"]:
            v = is_violation(judge_sets[jname][eid]["judgment"]["violation_level"])
            ratings[i, 1 if v else 0] += 1
    fk = round(fleiss_kappa(ratings), 4)

    # ── (d) Model ranking Spearman ρ ──
    model_ranks = {}
    for jname in ["gpt", "claude", "gemini"]:
        rates = viol_rates_by_judge[jname]
        sorted_models = sorted(AGENT_MODELS, key=lambda m: rates.get(m, 0), reverse=True)
        model_ranks[jname] = {m: rank + 1 for rank, m in enumerate(sorted_models)}

    model_rho = {}
    for j1, j2 in combinations(["gpt", "claude", "gemini"], 2):
        r1 = [model_ranks[j1][m] for m in AGENT_MODELS]
        r2 = [model_ranks[j2][m] for m in AGENT_MODELS]
        rho, pval = stats.spearmanr(r1, r2)
        model_rho[f"{j1}_vs_{j2}"] = {"rho": round(rho, 4), "p": round(pval, 4)}

    # ── (e) Type ranking Spearman ρ ──
    type_rates_by_judge = {}
    for jname, jdata in judge_sets.items():
        filtered = {eid: jdata[eid] for eid in common_ids if eid in jdata}
        type_rates_by_judge[jname] = compute_violation_rates(filtered, "ambiguity_type")

    type_ranks = {}
    for jname in ["gpt", "claude", "gemini"]:
        rates = type_rates_by_judge[jname]
        sorted_types = sorted(AMBIGUITY_TYPES, key=lambda t: rates.get(t, 0), reverse=True)
        type_ranks[jname] = {t: rank + 1 for rank, t in enumerate(sorted_types)}

    type_rho = {}
    for j1, j2 in combinations(["gpt", "claude", "gemini"], 2):
        r1 = [type_ranks[j1][t] for t in AMBIGUITY_TYPES]
        r2 = [type_ranks[j2][t] for t in AMBIGUITY_TYPES]
        rho, pval = stats.spearmanr(r1, r2)
        type_rho[f"{j1}_vs_{j2}"] = {"rho": round(rho, 4), "p": round(pval, 4)}

    # ── (f) Judge effect size: |Δ violation rate| per model per judge pair ──
    judge_effect = {}
    for j1, j2 in combinations(["gpt", "claude", "gemini"], 2):
        deltas = {}
        for m in AGENT_MODELS:
            r1 = viol_rates_by_judge[j1].get(m, 0)
            r2 = viol_rates_by_judge[j2].get(m, 0)
            deltas[m] = round(abs(r1 - r2), 4)
        judge_effect[f"{j1}_vs_{j2}"] = {
            "per_model": deltas,
            "mean": round(np.mean(list(deltas.values())), 4),
            "max": round(max(deltas.values()), 4),
        }

    # ── (g) Authorization scope robustness check ──
    auth_rates = {}
    for jname, jdata in judge_sets.items():
        filtered = {eid: jdata[eid] for eid in common_ids
                    if eid in jdata and jdata[eid]["condition"] == "ambiguous"
                    and jdata[eid]["ambiguity_type"] == "authorization_scope"}
        model_counts = defaultdict(lambda: {"viol": 0, "total": 0})
        for rec in filtered.values():
            model_counts[rec["model"]]["total"] += 1
            if is_violation(rec["judgment"]["violation_level"]):
                model_counts[rec["model"]]["viol"] += 1
        auth_rates[jname] = {
            m: round(c["viol"] / c["total"], 4) if c["total"] > 0 else 0.0
            for m, c in model_counts.items()
        }

    # ── Compile results ──
    results = {
        "n_common_episodes": len(common_ids),
        "n_ambiguous_common": len(ambig_common),
        "violation_rates_by_judge_and_model": {
            jname: {m: round(v, 4) for m, v in rates.items()}
            for jname, rates in viol_rates_by_judge.items()
        },
        "violation_rates_by_judge_and_type": {
            jname: {t: round(v, 4) for t, v in rates.items()}
            for jname, rates in type_rates_by_judge.items()
        },
        "cohens_kappa_pairwise": kappa_pairs,
        "fleiss_kappa_3judge": fk,
        "model_ranking_spearman": model_rho,
        "type_ranking_spearman": type_rho,
        "model_rankings": {
            jname: {m: {"rank": model_ranks[jname][m], "rate": round(viol_rates_by_judge[jname].get(m, 0), 4)}
                    for m in AGENT_MODELS}
            for jname in ["gpt", "claude", "gemini"]
        },
        "type_rankings": {
            jname: {t: {"rank": type_ranks[jname][t], "rate": round(type_rates_by_judge[jname].get(t, 0), 4)}
                    for t in AMBIGUITY_TYPES}
            for jname in ["gpt", "claude", "gemini"]
        },
        "judge_effect_size": judge_effect,
        "authorization_scope_rates_by_judge_and_model": auth_rates,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    # ── Print summary ──
    print("\n" + "=" * 70)
    print("CROSS-JUDGE VALIDATION RESULTS")
    print("=" * 70)

    print(f"\nCommon episodes: {len(common_ids)} ({len(ambig_common)} ambiguous)")

    print("\n── Violation Rates by Judge × Model (ambiguous only) ──")
    header = f"{'Model':<22}" + "".join(f"{j:>10}" for j in ["gpt", "claude", "gemini"])
    print(header)
    for m in AGENT_MODELS:
        row = f"{m:<22}"
        for j in ["gpt", "claude", "gemini"]:
            r = viol_rates_by_judge[j].get(m, 0)
            row += f"{r:>9.1%} "
        print(row)

    print("\n── Violation Rates by Judge × Type (ambiguous only) ──")
    header = f"{'Type':<25}" + "".join(f"{j:>10}" for j in ["gpt", "claude", "gemini"])
    print(header)
    for t in AMBIGUITY_TYPES:
        row = f"{t:<25}"
        for j in ["gpt", "claude", "gemini"]:
            r = type_rates_by_judge[j].get(t, 0)
            row += f"{r:>9.1%} "
        print(row)

    print("\n── Cohen's κ (pairwise, binary violation) ──")
    for pair, k in kappa_pairs.items():
        print(f"  {pair}: κ = {k:.4f}")

    print(f"\n── Fleiss' κ (3-judge): {fk:.4f} ──")

    print("\n── Model Ranking Spearman ρ ──")
    for pair, rho_data in model_rho.items():
        print(f"  {pair}: ρ = {rho_data['rho']:.4f} (p = {rho_data['p']:.4f})")

    print("\n── Type Ranking Spearman ρ ──")
    for pair, rho_data in type_rho.items():
        print(f"  {pair}: ρ = {rho_data['rho']:.4f} (p = {rho_data['p']:.4f})")

    print("\n── Judge Effect Size (mean |Δ viol rate| per model) ──")
    for pair, eff in judge_effect.items():
        print(f"  {pair}: mean = {eff['mean']:.4f}, max = {eff['max']:.4f}")

    print("\n── Authorization Scope: Model Rates by Judge ──")
    for jname in ["gpt", "claude", "gemini"]:
        rates = auth_rates.get(jname, {})
        sorted_m = sorted(rates.items(), key=lambda x: x[1], reverse=True)
        print(f"  {jname}: " + ", ".join(f"{m}={r:.1%}" for m, r in sorted_m))

    print(f"\nResults saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
