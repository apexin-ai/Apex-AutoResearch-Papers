"""D049 reviewer response analysis: ME+position², Llama heuristic CV, zero-correction CI.

Runs on local data (3 RR configs). SEQ/SEL configs need remote data.
"""

import json
import re
import sys
from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

BASE = Path("/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/outputs/full_scale")
CONFIGS = {
    "qwen_rr": BASE / "qwen_round_robin",
    "gemma_rr": BASE / "gemma_round_robin",
    "llama_rr": BASE / "llama_round_robin",
}

N30_THRESHOLD = 30


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def build_df(config_dir):
    impact = load_jsonl(config_dir / "local_impact" / "impact.jsonl")
    annots = load_jsonl(config_dir / "annotations" / "annotations.jsonl")

    impact_df = pd.DataFrame(impact)
    ann_df = pd.DataFrame(annots)

    if "remove" in impact_df.columns:
        impact_df["rem_sim"] = impact_df["remove"].apply(
            lambda x: x.get("semantic_similarity") if isinstance(x, dict) else None
        )

    if "annotation_a" in ann_df.columns:
        ann_df["func_type"] = ann_df["annotation_a"].apply(
            lambda x: x.get("type") if isinstance(x, dict) else None
        )

    merge_keys = ["task_id", "message_index"]
    df = impact_df.merge(ann_df[merge_keys + ["func_type"]], on=merge_keys, how="inner")

    df["position"] = df.groupby("task_id").cumcount()
    max_pos = df.groupby("task_id")["position"].transform("max")
    df["norm_position"] = df["position"] / max_pos.replace(0, 1)
    if "message_index" in df.columns:
        df["round_number"] = df["message_index"]
    else:
        df["round_number"] = df["position"]

    return df


def filter_n30(df):
    counts = df["func_type"].value_counts()
    valid_types = counts[counts >= N30_THRESHOLD].index.tolist()
    return df[df["func_type"].isin(valid_types)].copy(), valid_types


# ============================================================
# TASK 1: ME model with position²
# ============================================================

def task1_me_position_squared():
    print("=" * 70)
    print("TASK 1: ME model with position² term")
    print("=" * 70)

    try:
        import statsmodels.formula.api as smf
    except ImportError:
        print("ERROR: statsmodels not installed")
        return

    results = {}

    for config_name, config_dir in CONFIGS.items():
        print(f"\n--- {config_name} ---")
        df = build_df(config_dir)
        df, valid_types = filter_n30(df)
        n_types = len(valid_types)
        print(f"  n={len(df)}, func_types={valid_types}")

        if n_types < 2:
            print("  SKIP: fewer than 2 func types after n≥30 filter")
            continue

        df["position_sq"] = df["norm_position"] ** 2

        try:
            # Linear ME: full vs reduced (no func_type)
            me_lin_full = smf.mixedlm(
                "rem_sim ~ C(func_type) + norm_position + round_number",
                data=df, groups=df["task_id"]
            ).fit(reml=False, method="lbfgs")

            me_lin_red = smf.mixedlm(
                "rem_sim ~ norm_position + round_number",
                data=df, groups=df["task_id"]
            ).fit(reml=False, method="lbfgs")

            lrt_lin = -2 * (me_lin_red.llf - me_lin_full.llf)
            df_lin = n_types - 1
            p_lin = stats.chi2.sf(lrt_lin, df_lin)

            # Quadratic ME: full vs reduced (no func_type)
            me_quad_full = smf.mixedlm(
                "rem_sim ~ C(func_type) + norm_position + position_sq + round_number",
                data=df, groups=df["task_id"]
            ).fit(reml=False, method="lbfgs")

            me_quad_red = smf.mixedlm(
                "rem_sim ~ norm_position + position_sq + round_number",
                data=df, groups=df["task_id"]
            ).fit(reml=False, method="lbfgs")

            lrt_quad = -2 * (me_quad_red.llf - me_quad_full.llf)
            df_quad = n_types - 1
            p_quad = stats.chi2.sf(lrt_quad, df_quad)

            # R²m: var(fixed effects prediction) / total variance
            # Nakagawa & Schielzeth (2013) approximation
            def compute_r2m(model):
                fe_pred = model.fittedvalues - model.random_effects[list(model.random_effects.keys())[0]].values[0] if hasattr(model, 'random_effects') else model.fittedvalues
                # Simpler: use variance of fixed-effects predictions
                X = model.model.exog
                fe_vals = X @ model.fe_params
                var_fe = np.var(fe_vals)
                var_re = model.cov_re.iloc[0, 0] if hasattr(model.cov_re, 'iloc') else float(model.cov_re)
                var_resid = model.scale
                return var_fe / (var_fe + var_re + var_resid)

            r2m_lin = compute_r2m(me_lin_full)
            r2m_quad = compute_r2m(me_quad_full)

            # ICC from quadratic model
            var_re_quad = me_quad_full.cov_re.iloc[0, 0] if hasattr(me_quad_full.cov_re, 'iloc') else float(me_quad_full.cov_re)
            icc_quad = var_re_quad / (var_re_quad + me_quad_full.scale)

            # Position² effect: compare linear vs quadratic (both full)
            lrt_pos2 = -2 * (me_lin_full.llf - me_quad_full.llf)
            p_pos2 = stats.chi2.sf(lrt_pos2, 1)

        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            continue

        sig = lambda p: "***" if p < 0.001 else ("**" if p < 0.01 else ("*" if p < 0.05 else "n.s."))

        result = {
            "n": len(df),
            "n_func_types": n_types,
            "func_types": valid_types,
            "linear_lrt_chi2": round(lrt_lin, 2),
            "linear_lrt_p": round(p_lin, 6),
            "quad_lrt_chi2": round(lrt_quad, 2),
            "quad_lrt_p": round(p_quad, 6),
            "r2m_linear": round(r2m_lin, 4),
            "r2m_quad": round(r2m_quad, 4),
            "icc_quad": round(icc_quad, 4),
            "pos2_lrt_chi2": round(lrt_pos2, 2),
            "pos2_p": round(p_pos2, 6),
        }
        results[config_name] = result

        print(f"  Linear ME:  LRT χ²={lrt_lin:.2f}, p={p_lin:.6f} {sig(p_lin)}, R²m={r2m_lin:.4f}")
        print(f"  Quad ME:    LRT χ²={lrt_quad:.2f}, p={p_quad:.6f} {sig(p_quad)}, R²m={r2m_quad:.4f}")
        print(f"  ICC (quad): {icc_quad:.4f}")
        print(f"  Position² improvement: LRT χ²={lrt_pos2:.2f}, p={p_pos2:.6f} {sig(p_pos2)}")

        if p_lin < 0.05 and p_quad >= 0.05:
            print(f"  ⚠️ FLIPS: function type significant in linear but NOT in quadratic ME")
        elif p_lin < 0.05 and p_quad < 0.05:
            print(f"  ✓ Function type remains significant after adding position²")
        else:
            print(f"  Function type not significant in either model")

    return results


# ============================================================
# TASK 2: Llama heuristic 5-fold CV (correct implementation)
# ============================================================

# Exact keywords from heuristic_ack_detector_llama.py on the server
ACK_KEYWORDS = [
    "i'm glad", "you've broken", "your step-by-step",
    "your rephrased", "i appreciate the", "you've provided",
    "your solution is correct", "the answer is indeed",
]

NONACK_KEYWORDS = [
    "here's another", "i have another", "let's break down",
    "let me solve", "i have a new", "i need help",
    "can you help", "solve this", "please solve",
]

LEN_THRESHOLD = 300
OVERLAP_THRESHOLD = 0.3


def _four_gram_overlap(cur_text, prev_text):
    cw = cur_text.lower().split()
    pw = prev_text.lower().split()
    if len(cw) < 4 or len(pw) < 4:
        return 0.0
    c4 = set(tuple(cw[i:i+4]) for i in range(len(cw) - 3))
    p4 = set(tuple(pw[i:i+4]) for i in range(len(pw) - 3))
    return len(c4 & p4) / len(c4) if c4 else 0.0


def heuristic_is_ack_llama(text, prev_text=""):
    tl = text.lower()
    if any(kw in tl for kw in NONACK_KEYWORDS):
        return False
    if "however" in tl[:300]:
        return False
    if any(kw in tl[:300] for kw in ACK_KEYWORDS):
        return True
    if len(text.strip()) < LEN_THRESHOLD:
        return True
    if prev_text and _four_gram_overlap(text, prev_text) > OVERLAP_THRESHOLD:
        return True
    return False


def task2_llama_heuristic_cv():
    print("\n" + "=" * 70)
    print("TASK 2: Llama heuristic 5-fold GroupKFold CV (grouped by task_id)")
    print("=" * 70)

    from sklearn.model_selection import GroupKFold
    from sklearn.metrics import f1_score, precision_score, recall_score

    config_dir = CONFIGS["llama_rr"]
    annots = load_jsonl(config_dir / "annotations" / "annotations.jsonl")
    traces = load_jsonl(config_dir / "traces" / "traces.jsonl")

    # Build message map from traces: (task_id, round) -> content
    trace_map = {t["task_id"]: t for t in traces}

    # Build evaluation dataset with prev_text for 4-gram overlap
    data = []
    for ann in annots:
        task_id = ann["task_id"]
        msg_idx = ann["message_index"]
        func_type = ann.get("annotation_a", {}).get("type", "unknown")

        if task_id not in trace_map:
            continue
        msgs = trace_map[task_id].get("messages", [])
        rounds_by_r = {m.get("round", 0): m for m in msgs}

        target_round = msg_idx + 1
        cur_text = rounds_by_r.get(target_round, {}).get("content", "")
        prev_text = rounds_by_r.get(target_round - 1, {}).get("content", "")

        if not cur_text:
            continue

        is_ack_gold = 1 if func_type == "acknowledgment" else 0
        pred = 1 if heuristic_is_ack_llama(cur_text, prev_text) else 0

        data.append({
            "task_id": task_id,
            "message_index": msg_idx,
            "is_ack_gold": is_ack_gold,
            "pred": pred,
        })

    df = pd.DataFrame(data)
    print(f"Total messages: {len(df)}")
    print(f"Gold ack: {df['is_ack_gold'].sum()}, non-ack: {(1-df['is_ack_gold']).sum()}")

    # Full dataset performance
    from sklearn.metrics import confusion_matrix
    tn, fp, fn, tp = confusion_matrix(df["is_ack_gold"], df["pred"]).ravel()
    full_f1 = f1_score(df["is_ack_gold"], df["pred"])
    full_prec = precision_score(df["is_ack_gold"], df["pred"])
    full_rec = recall_score(df["is_ack_gold"], df["pred"])
    print(f"\nFull dataset: F1={full_f1:.3f}, P={full_prec:.3f}, R={full_rec:.3f}")
    print(f"  TP={tp}, FP={fp}, FN={fn}, TN={tn}")

    # 5-fold GroupKFold CV — group by task_id to prevent leakage
    gkf = GroupKFold(n_splits=5)
    groups = df["task_id"]
    fold_metrics = []

    for fold, (train_idx, test_idx) in enumerate(gkf.split(df, df["is_ack_gold"], groups=groups)):
        test_df = df.iloc[test_idx]
        f1 = f1_score(test_df["is_ack_gold"], test_df["pred"])
        prec = precision_score(test_df["is_ack_gold"], test_df["pred"])
        rec = recall_score(test_df["is_ack_gold"], test_df["pred"])
        fold_metrics.append({"fold": fold+1, "f1": f1, "precision": prec, "recall": rec, "n": len(test_idx)})
        print(f"  Fold {fold+1}: F1={f1:.3f}, P={prec:.3f}, R={rec:.3f} (n={len(test_idx)})")

    metrics_df = pd.DataFrame(fold_metrics)
    print(f"\nCV Summary:")
    print(f"  F1:        {metrics_df['f1'].mean():.3f} ± {metrics_df['f1'].std():.3f}")
    print(f"  Precision: {metrics_df['precision'].mean():.3f} ± {metrics_df['precision'].std():.3f}")
    print(f"  Recall:    {metrics_df['recall'].mean():.3f} ± {metrics_df['recall'].std():.3f}")
    print(f"  F1 std > 0.05? {'YES ⚠️' if metrics_df['f1'].std() > 0.05 else 'NO ✓'}")

    return {
        "full": {"f1": round(full_f1, 4), "precision": round(full_prec, 4), "recall": round(full_rec, 4),
                 "tp": int(tp), "fp": int(fp), "fn": int(fn), "tn": int(tn)},
        "cv_mean": {
            "f1": round(metrics_df["f1"].mean(), 3),
            "precision": round(metrics_df["precision"].mean(), 3),
            "recall": round(metrics_df["recall"].mean(), 3),
        },
        "cv_std": {
            "f1": round(metrics_df["f1"].std(), 3),
            "precision": round(metrics_df["precision"].std(), 3),
            "recall": round(metrics_df["recall"].std(), 3),
        },
        "folds": fold_metrics,
    }


# ============================================================
# TASK 3: Zero-correction binomial CI
# ============================================================

def task3_zero_correction_ci():
    print("\n" + "=" * 70)
    print("TASK 3: Zero-correction binomial CI (Clopper-Pearson)")
    print("=" * 70)

    results = {}

    for config_name, config_dir in CONFIGS.items():
        backbone = config_name.split("_")[0].capitalize()
        annots = load_jsonl(config_dir / "annotations" / "annotations.jsonl")

        ack_count = sum(1 for ann in annots
                        if ann.get("annotation_a", {}).get("type") == "acknowledgment")

        N = ack_count
        k = 0

        alpha = 0.05
        if k == 0:
            lower = 0.0
            upper = 1 - (alpha / 2) ** (1 / N) if N > 0 else 1.0
        else:
            lower = stats.beta.ppf(alpha / 2, k, N - k + 1)
            upper = stats.beta.ppf(1 - alpha / 2, k + 1, N - k)

        results[backbone] = {"N": N, "k": k, "ci_lower": lower, "ci_upper": round(upper, 6)}
        print(f"  {backbone}: 0/{N} corrections, 95% CI [0, {upper:.4f}] = [0%, {upper*100:.2f}%]")

    return results


if __name__ == "__main__":
    print("D049 Reviewer Response Analysis")
    print("Data: local 3 RR configs")
    print()

    r1 = task1_me_position_squared()
    r2 = task2_llama_heuristic_cv()
    r3 = task3_zero_correction_ci()

    out = {"task1_me_quad": r1, "task2_llama_cv": r2, "task3_binomial_ci": r3}
    out_path = Path("/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/outputs/v7_analysis/d049_results.json")
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")
