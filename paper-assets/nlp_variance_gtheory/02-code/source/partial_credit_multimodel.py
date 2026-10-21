"""
Partial-credit scorer for GSM8K 8-model data + Henderson I G-study.

Scores each response on [0.0, 1.0] by verifying arithmetic steps in CoT text.
Then runs Henderson I G-study comparing binary vs partial-credit variance decomposition.

Facets: model(8) x temperature(2) x prompt_template(6) x seed(6) x ordering(4) x item_id(200)
"""

import json
import re
import sys
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, "/root/nlp_variance_gtheory")
from src.config.model_paths import normalize_model_name

DATA_DIR = Path("/root/nlp_variance_gtheory/results/exp002")
OUT_DIR = Path("/root/nlp_variance_gtheory/results/partial_credit_multimodel")
FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
GSM8K_FILES = sorted(DATA_DIR.glob("*_gsm8k.jsonl"))


# ═══════════════════════════════════════════════════════════════════════════
# Step-level arithmetic scorer
# ═══════════════════════════════════════════════════════════════════════════

def _parse_number(s: str) -> float | None:
    s = s.replace(",", "").replace(" ", "").strip()
    if s.endswith("%"):
        s = s[:-1]
    try:
        return float(s)
    except ValueError:
        return None


_OP_MAP = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "×": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else float("inf"),
    "÷": lambda a, b: a / b if b != 0 else float("inf"),
}

# <<4+2=6>>6 or <<80*15=1200>>1200
_RE_ANNO = re.compile(
    r"<<\s*([\d.,]+)\s*([+\-*/×÷])\s*([\d.,]+)\s*=\s*([\d.,]+)\s*>>"
)
# plain: 4 + 2 = 6 (must have spaces around op to avoid matching dates/IDs)
_RE_PLAIN = re.compile(
    r"(?<!\w)([\d.,]+)\s*([+\-*/×÷])\s*([\d.,]+)\s*=\s*([\d.,]+)(?!\w)"
)


def extract_arithmetic_steps(text: str) -> list[tuple[float, str, float, float]]:
    """Extract (a, op, b, claimed_result) tuples from CoT text."""
    steps = []
    seen_spans = set()

    for regex in (_RE_ANNO, _RE_PLAIN):
        for m in regex.finditer(text):
            span = m.span()
            if any(s[0] <= span[0] < s[1] or s[0] < span[1] <= s[1] for s in seen_spans):
                continue
            a_s, op, b_s, r_s = m.groups()
            a, b, r = _parse_number(a_s), _parse_number(b_s), _parse_number(r_s)
            if a is not None and b is not None and r is not None and op in _OP_MAP:
                steps.append((a, op, b, r))
                seen_spans.add(span)

    return steps


def verify_step(a: float, op: str, b: float, claimed: float) -> bool:
    expected = _OP_MAP[op](a, b)
    return abs(expected - claimed) < max(0.01, abs(expected) * 1e-6)


def score_response(generated_text: str, correct: int) -> dict:
    """Score a single response. Returns partial_score and diagnostic info."""
    if correct == 1:
        return {"partial_score": 1.0, "n_steps": -1, "n_correct_steps": -1, "method": "final_correct"}

    steps = extract_arithmetic_steps(generated_text)
    if not steps:
        return {"partial_score": 0.0, "n_steps": 0, "n_correct_steps": 0, "method": "no_steps"}

    n_correct = sum(1 for a, op, b, r in steps if verify_step(a, op, b, r))
    n_total = len(steps)
    return {
        "partial_score": n_correct / n_total,
        "n_steps": n_total,
        "n_correct_steps": n_correct,
        "method": "step_verification",
    }


# ═══════════════════════════════════════════════════════════════════════════
# Henderson I G-study (reused from existing codebase)
# ═══════════════════════════════════════════════════════════════════════════

def compute_henderson_i(df: pd.DataFrame, response: str, facets: list[str]) -> dict:
    grand_mean = float(df[response].mean())
    N = len(df)
    n_levels = {f: df[f].nunique() for f in facets}

    effects = {}
    for f in facets:
        group_means = df.groupby(f, observed=True)[response].mean()
        n_per = N // n_levels[f]
        ss = float(n_per * ((group_means - grand_mean) ** 2).sum())
        df_eff = n_levels[f] - 1
        effects[f] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    for fi, fj in combinations(facets, 2):
        cell_means = df.groupby([fi, fj], observed=True)[response].mean()
        main_fi = df.groupby(fi, observed=True)[response].mean()
        main_fj = df.groupby(fj, observed=True)[response].mean()
        n_per = N // (n_levels[fi] * n_levels[fj])
        ss = 0.0
        for (li, lj), cm in cell_means.items():
            interaction = cm - main_fi[li] - main_fj[lj] + grand_mean
            ss += n_per * interaction ** 2
        df_eff = (n_levels[fi] - 1) * (n_levels[fj] - 1)
        effects[f"{fi}:{fj}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff > 0 else 0.0}

    ss_total = float(((df[response] - grand_mean) ** 2).sum())
    ss_model_sum = sum(e["ss"] for e in effects.values())
    ss_res = max(0.0, ss_total - ss_model_sum)
    df_res = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_res, "df": df_res, "ms": ss_res / df_res if df_res > 0 else 0.0}

    ms_res = effects["residual"]["ms"]
    vc = {}

    for fi, fj in combinations(facets, 2):
        key = f"{fi}:{fj}"
        coeff = prod(n_levels[f] for f in facets if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)

    for fi in facets:
        coeff_main = prod(n_levels[f] for f in facets if f != fi)
        interaction_contrib = 0.0
        for fj in facets:
            if fj == fi:
                continue
            int_key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(n_levels[f] for f in facets if f not in (fi, fj))
            interaction_contrib += coeff_ij * vc[int_key]
        raw = (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    total_var = sum(vc.values())
    pct = {k: round(100.0 * v / total_var, 4) if total_var > 0 else 0.0 for k, v in vc.items()}

    return {
        "grand_mean": grand_mean,
        "N": N,
        "n_levels": {k: int(v) for k, v in n_levels.items()},
        "variance_components": {k: round(v, 10) for k, v in sorted(vc.items(), key=lambda x: -x[1])},
        "variance_pct": dict(sorted(pct.items(), key=lambda x: -x[1])),
        "total_variance": round(total_var, 10),
    }


def compute_g_item(vc: dict, n_levels: dict, facets: list[str]) -> dict:
    sigma_item = vc.get("item_id", 0.0)
    sigma_delta = 0.0
    for key, est in vc.items():
        if key == "item_id" or est == 0.0:
            continue
        parts = key.split(":")
        if "item_id" in parts:
            other = [p for p in parts if p != "item_id"]
            divisor = prod(n_levels[o] for o in other)
            sigma_delta += est / divisor
        elif key == "residual":
            divisor = prod(n_levels[f] for f in facets if f != "item_id")
            sigma_delta += est / divisor

    g_item = sigma_item / (sigma_item + sigma_delta) if (sigma_item + sigma_delta) > 0 else 0.0
    return {
        "G_item": round(g_item, 6),
        "sigma_tau": round(sigma_item, 10),
        "sigma_delta": round(sigma_delta, 10),
    }


# ═══════════════════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════════════════

def main():
    t0 = time.time()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Load all 8 models ──
    print("Loading GSM8K data...", flush=True)
    frames = []
    for f in GSM8K_FILES:
        df = pd.read_json(f, lines=True)
        if "top_logprobs" in df.columns:
            df.drop(columns=["top_logprobs"], inplace=True)
        frames.append(df)
        print(f"  {f.name}: {len(df)} rows", flush=True)

    df = pd.concat(frames, ignore_index=True)
    df["model"] = df["model"].map(normalize_model_name).fillna(df["model"])
    for f in FACETS:
        df[f] = df[f].astype(str)
    print(f"Total: {len(df)} rows, {df['model'].nunique()} models", flush=True)

    # ── Score each response ──
    print("\nScoring responses...", flush=True)
    score_results = df["generated_text"].combine(
        df["correct"],
        lambda text, corr: score_response(text, int(corr)),
    )
    score_df = pd.DataFrame(score_results.tolist())
    df["partial_score"] = score_df["partial_score"].values
    df["n_steps"] = score_df["n_steps"].values
    df["n_correct_steps"] = score_df["n_correct_steps"].values
    df["score_method"] = score_df["method"].values

    # ── Scoring diagnostics ──
    wrong = df[df["correct"] == 0]
    print(f"\nScoring diagnostics (wrong-answer subset: {len(wrong)} records):", flush=True)
    print(f"  partial_score distribution:", flush=True)
    for bucket, label in [(0.0, "= 0.0"), (0.5, "≈ 0.5"), (1.0, "= 1.0")]:
        if bucket == 0.0:
            n = (wrong["partial_score"] == 0.0).sum()
        elif bucket == 1.0:
            n = (wrong["partial_score"] == 1.0).sum()
        else:
            n = ((wrong["partial_score"] > 0.0) & (wrong["partial_score"] < 1.0)).sum()
        print(f"    {label}: {n} ({100*n/len(wrong):.1f}%)", flush=True)
    print(f"  no_steps (no extractable arithmetic): {(wrong['score_method'] == 'no_steps').sum()}", flush=True)
    print(f"  mean partial_score (wrong answers only): {wrong['partial_score'].mean():.4f}", flush=True)
    print(f"  mean partial_score (all): {df['partial_score'].mean():.4f}", flush=True)
    print(f"  mean binary correct (all): {df['correct'].mean():.4f}", flush=True)

    # ── Save scored data ──
    scored_path = OUT_DIR / "gsm8k_8model_partial_scored.jsonl"
    cols_to_save = [c for c in df.columns if c != "generated_text"]
    df[cols_to_save].to_json(scored_path, orient="records", lines=True)
    print(f"\nSaved scored data: {scored_path} ({len(df)} records)", flush=True)

    # ── Henderson I G-study: binary vs partial-credit ──
    print(f"\n{'='*65}", flush=True)
    print("Henderson I G-study: binary (correct) vs partial-credit", flush=True)
    print(f"{'='*65}", flush=True)

    df["correct"] = df["correct"].astype(float)

    result_binary = compute_henderson_i(df, "correct", FACETS)
    g_binary = compute_g_item(result_binary["variance_components"], result_binary["n_levels"], FACETS)

    result_partial = compute_henderson_i(df, "partial_score", FACETS)
    g_partial = compute_g_item(result_partial["variance_components"], result_partial["n_levels"], FACETS)

    print(f"\n{'Metric':<20} {'Grand Mean':>10} {'Total Var':>12} {'G_item':>8}", flush=True)
    print(f"{'binary':.<20} {result_binary['grand_mean']:>10.4f} {result_binary['total_variance']:>12.8f} {g_binary['G_item']:>8.4f}", flush=True)
    print(f"{'partial_credit':.<20} {result_partial['grand_mean']:>10.4f} {result_partial['total_variance']:>12.8f} {g_partial['G_item']:>8.4f}", flush=True)

    print(f"\nVariance % comparison (top components):", flush=True)
    all_keys = set(result_binary["variance_pct"].keys()) | set(result_partial["variance_pct"].keys())
    sorted_keys = sorted(all_keys, key=lambda k: result_binary["variance_pct"].get(k, 0), reverse=True)
    print(f"  {'Component':<25} {'Binary%':>10} {'Partial%':>10} {'Δ':>8}", flush=True)
    for k in sorted_keys[:15]:
        b = result_binary["variance_pct"].get(k, 0)
        p = result_partial["variance_pct"].get(k, 0)
        print(f"  {k:<25} {b:>9.2f}% {p:>9.2f}% {p-b:>+7.2f}%", flush=True)

    # ── Per-model G-study ──
    print(f"\n{'='*65}", flush=True)
    print("Per-model Henderson I (single-model 5-facet design)", flush=True)
    print(f"{'='*65}", flush=True)

    per_model_facets = ["temperature", "prompt_template", "seed", "ordering", "item_id"]
    per_model_results = {}

    for model_name in sorted(df["model"].unique()):
        df_m = df[df["model"] == model_name].copy()
        for f in per_model_facets:
            df_m[f] = df_m[f].astype(str)

        rb = compute_henderson_i(df_m, "correct", per_model_facets)
        gb = compute_g_item(rb["variance_components"], rb["n_levels"], per_model_facets)

        rp = compute_henderson_i(df_m, "partial_score", per_model_facets)
        gp = compute_g_item(rp["variance_components"], rp["n_levels"], per_model_facets)

        per_model_results[model_name] = {
            "n_records": len(df_m),
            "accuracy": float(df_m["correct"].mean()),
            "mean_partial_score": float(df_m["partial_score"].mean()),
            "binary": {
                "variance_pct": rb["variance_pct"],
                "total_variance": rb["total_variance"],
                "G_item": gb["G_item"],
            },
            "partial_credit": {
                "variance_pct": rp["variance_pct"],
                "total_variance": rp["total_variance"],
                "G_item": gp["G_item"],
            },
        }

    print(f"\n{'Model':<20} {'Acc':>6} {'Mean PC':>8} {'G_bin':>7} {'G_pc':>7} {'ΔG':>7}", flush=True)
    for m in sorted(per_model_results.keys()):
        r = per_model_results[m]
        dg = r["partial_credit"]["G_item"] - r["binary"]["G_item"]
        print(
            f"{m:<20} {r['accuracy']:>5.3f} {r['mean_partial_score']:>7.4f} "
            f"{r['binary']['G_item']:>7.4f} {r['partial_credit']['G_item']:>7.4f} {dg:>+6.4f}",
            flush=True,
        )

    # ── Save G-study results ──
    gstudy_output = {
        "experiment": "exp-004 partial-credit",
        "benchmark": "gsm8k",
        "scoring": "step-level arithmetic verification",
        "n_models": int(df["model"].nunique()),
        "n_records": len(df),
        "models": sorted(df["model"].unique().tolist()),
        "facets": FACETS,
        "crossed_8model": {
            "binary": {
                "grand_mean": result_binary["grand_mean"],
                "n_levels": result_binary["n_levels"],
                "variance_components": result_binary["variance_components"],
                "variance_pct": result_binary["variance_pct"],
                "total_variance": result_binary["total_variance"],
                "G_item": g_binary["G_item"],
                "sigma_tau": g_binary["sigma_tau"],
                "sigma_delta": g_binary["sigma_delta"],
            },
            "partial_credit": {
                "grand_mean": result_partial["grand_mean"],
                "n_levels": result_partial["n_levels"],
                "variance_components": result_partial["variance_components"],
                "variance_pct": result_partial["variance_pct"],
                "total_variance": result_partial["total_variance"],
                "G_item": g_partial["G_item"],
                "sigma_tau": g_partial["sigma_tau"],
                "sigma_delta": g_partial["sigma_delta"],
            },
        },
        "per_model_5facet": per_model_results,
        "scoring_diagnostics": {
            "total_records": len(df),
            "correct_records": int((df["correct"] == 1).sum()),
            "wrong_records": int((df["correct"] == 0).sum()),
            "wrong_no_steps": int((wrong["score_method"] == "no_steps").sum()),
            "wrong_all_arithmetic_correct": int((wrong["partial_score"] == 1.0).sum()),
            "wrong_partial": int(((wrong["partial_score"] > 0) & (wrong["partial_score"] < 1)).sum()),
            "wrong_zero": int((wrong["partial_score"] == 0.0).sum()),
            "mean_steps_per_wrong": float(wrong[wrong["n_steps"] > 0]["n_steps"].mean()),
        },
    }

    gstudy_path = OUT_DIR / "partial_credit_multimodel_gstudy.json"
    with open(gstudy_path, "w") as f:
        json.dump(gstudy_output, f, indent=2, default=lambda x: float(x) if hasattr(x, "item") else str(x))

    print(f"\n{'='*65}", flush=True)
    print(f"Saved G-study: {gstudy_path}", flush=True)
    print(f"Saved scored data: {scored_path}", flush=True)
    print(f"Runtime: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
