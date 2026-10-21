"""D051: Unified ME model — backbone × function_type interaction LRT.

Merges all RR (and optionally SEQ) data across 3 backbones, fits crossed
mixed-effects model, tests backbone × function_type interaction via LRT.
"""

import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

BASE = Path("/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/outputs/full_scale")

RR_CONFIGS = {
    "qwen": BASE / "qwen_round_robin",
    "gemma": BASE / "gemma_round_robin",
    "llama": BASE / "llama_round_robin",
}

SEQ_CONFIGS = {
    "qwen": BASE / "qwen_sequential",
    "gemma": BASE / "gemma_sequential",
    "llama": BASE / "llama_sequential",
}

N30_THRESHOLD = 30
OUT_DIR = Path("/Users/agent-001/.agent-ml-research/projects/comm_gate_mas/outputs/v7_analysis")


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def build_df(config_dir, backbone):
    impact = load_jsonl(config_dir / "local_impact" / "impact.jsonl")
    annots = load_jsonl(config_dir / "annotations" / "annotations.jsonl")

    impact_df = pd.DataFrame(impact)
    ann_df = pd.DataFrame(annots)

    impact_df["rem_sim"] = impact_df["remove"].apply(
        lambda x: x.get("semantic_similarity") if isinstance(x, dict) else None
    )
    ann_df["func_type"] = ann_df["annotation_a"].apply(
        lambda x: x.get("type") if isinstance(x, dict) else None
    )

    merge_keys = ["task_id", "message_index"]
    df = impact_df.merge(ann_df[merge_keys + ["func_type"]], on=merge_keys, how="inner")

    df["position"] = df.groupby("task_id").cumcount()
    max_pos = df.groupby("task_id")["position"].transform("max")
    df["norm_position"] = df["position"] / max_pos.replace(0, 1)
    df["round_number"] = df["message_index"]
    df["backbone"] = backbone

    return df


def filter_n30_per_backbone(df):
    """Keep func_types with n >= N30 in every backbone."""
    valid = None
    for bb in df["backbone"].unique():
        sub = df[df["backbone"] == bb]
        counts = sub["func_type"].value_counts()
        ok = set(counts[counts >= N30_THRESHOLD].index)
        valid = ok if valid is None else valid & ok
    return df[df["func_type"].isin(valid)].copy(), sorted(valid)


def compute_lrt(full_model, reduced_model, df_diff):
    lr_stat = -2 * (reduced_model.llf - full_model.llf)
    p_value = float(stats.chi2.sf(lr_stat, df_diff))
    return float(lr_stat), df_diff, p_value


def compute_partial_eta2(full_model, reduced_model, n):
    lr_stat = -2 * (reduced_model.llf - full_model.llf)
    partial_eta2 = lr_stat / (lr_stat + n)
    cohens_f2 = partial_eta2 / (1 - partial_eta2)
    return float(partial_eta2), float(cohens_f2)


def fit_unified_model(df, label="RR"):
    """Fit unified ME with backbone × func_type interaction; return results dict."""
    print(f"\n{'='*70}")
    print(f"Unified ME model: {label} (n={len(df)})")
    print(f"{'='*70}")

    n_backbones = df["backbone"].nunique()
    n_func_types = df["func_type"].nunique()
    interaction_df = (n_backbones - 1) * (n_func_types - 1)

    print(f"Backbones: {sorted(df['backbone'].unique())}")
    print(f"Function types: {sorted(df['func_type'].unique())}")
    print(f"Interaction df: ({n_backbones}-1) × ({n_func_types}-1) = {interaction_df}")

    # Cross-tab counts
    ct = pd.crosstab(df["backbone"], df["func_type"])
    print(f"\nCross-tab (backbone × func_type):\n{ct}\n")

    # Full model with interaction
    full = smf.mixedlm(
        "rem_sim ~ C(backbone) * C(func_type) + norm_position + round_number",
        data=df, groups=df["task_id"]
    ).fit(reml=False, method="lbfgs")

    # Reduced: no interaction
    reduced = smf.mixedlm(
        "rem_sim ~ C(backbone) + C(func_type) + norm_position + round_number",
        data=df, groups=df["task_id"]
    ).fit(reml=False, method="lbfgs")

    # LRT
    lr_stat, df_diff, p_value = compute_lrt(full, reduced, interaction_df)
    eta2, f2 = compute_partial_eta2(full, reduced, len(df))

    print(f"LRT: χ²({df_diff}) = {lr_stat:.4f}, p = {p_value:.4e}")
    print(f"Partial η² = {eta2:.4f}, Cohen's f² = {f2:.4f}")

    # Full model summary (interaction coefficients)
    print(f"\nFull model interaction coefficients:")
    interaction_params = {k: v for k, v in full.params.items() if ":" in k}
    interaction_pvals = {k: v for k, v in full.pvalues.items() if ":" in k}
    for k in interaction_params:
        print(f"  {k}: β = {interaction_params[k]:.4f}, p = {interaction_pvals[k]:.4e}")

    # Conditional effects per backbone
    print(f"\nConditional function_type effects per backbone:")
    conditional = {}
    for bb in sorted(df["backbone"].unique()):
        sub = df[df["backbone"] == bb].copy()
        n_ft = sub["func_type"].nunique()
        if n_ft < 2:
            print(f"  {bb}: SKIP (only {n_ft} func_type)")
            continue

        m_full = smf.mixedlm(
            "rem_sim ~ C(func_type) + norm_position + round_number",
            data=sub, groups=sub["task_id"]
        ).fit(reml=False, method="lbfgs")

        m_red = smf.mixedlm(
            "rem_sim ~ norm_position + round_number",
            data=sub, groups=sub["task_id"]
        ).fit(reml=False, method="lbfgs")

        cond_df = n_ft - 1
        cond_lr, _, cond_p = compute_lrt(m_full, m_red, cond_df)
        cond_eta2, cond_f2 = compute_partial_eta2(m_full, m_red, len(sub))

        ft_params = {k: round(float(v), 4) for k, v in m_full.params.items() if "func_type" in k}
        ft_pvals = {k: round(float(v), 6) for k, v in m_full.pvalues.items() if "func_type" in k}

        print(f"  {bb}: LRT χ²({cond_df}) = {cond_lr:.4f}, p = {cond_p:.4e}, η² = {cond_eta2:.4f}")
        for k in ft_params:
            print(f"    {k}: β = {ft_params[k]}, p = {ft_pvals[k]}")

        conditional[bb] = {
            "n": len(sub),
            "lrt_chi2": round(cond_lr, 4),
            "lrt_df": cond_df,
            "lrt_p": cond_p,
            "partial_eta2": round(cond_eta2, 4),
            "cohens_f2": round(cond_f2, 4),
            "coefficients": ft_params,
            "p_values": ft_pvals,
            "R2m": round(float(1 - m_red.llf / m_full.llf), 4) if m_full.llf != 0 else None,
        }

    result = {
        "label": label,
        "n": len(df),
        "n_backbones": n_backbones,
        "n_func_types": n_func_types,
        "func_types": sorted(df["func_type"].unique().tolist()),
        "interaction_lrt": {
            "chi2": round(lr_stat, 4),
            "df": df_diff,
            "p_value": p_value,
            "partial_eta2": round(eta2, 4),
            "cohens_f2": round(f2, 4),
        },
        "interaction_coefficients": {
            k: {"beta": round(float(v), 4), "p": round(float(interaction_pvals[k]), 6)}
            for k, v in interaction_params.items()
        },
        "conditional_effects": conditional,
    }

    return result


def main():
    results = {}

    # --- RR data ---
    print("Loading RR data...")
    rr_frames = []
    for bb, path in RR_CONFIGS.items():
        df = build_df(path, bb)
        df["topology"] = "round_robin"
        print(f"  {bb} RR: {len(df)} messages")
        rr_frames.append(df)

    rr_all = pd.concat(rr_frames, ignore_index=True)
    rr_all = rr_all.dropna(subset=["rem_sim", "func_type"])
    rr_filtered, rr_types = filter_n30_per_backbone(rr_all)
    print(f"RR total: {len(rr_all)} → {len(rr_filtered)} after n≥{N30_THRESHOLD} filter")
    print(f"Retained func_types: {rr_types}")

    results["rr"] = fit_unified_model(rr_filtered, label="RR-only")

    # --- SEQ data (if available) ---
    seq_frames = []
    for bb, path in SEQ_CONFIGS.items():
        impact_path = path / "local_impact" / "impact.jsonl"
        annot_path = path / "annotations" / "annotations.jsonl"
        if impact_path.exists() and annot_path.exists():
            df = build_df(path, bb)
            df["topology"] = "sequential"
            print(f"  {bb} SEQ: {len(df)} messages")
            seq_frames.append(df)
        else:
            print(f"  {bb} SEQ: missing data, skipping")

    if seq_frames:
        seq_all = pd.concat(seq_frames, ignore_index=True)
        seq_all = seq_all.dropna(subset=["rem_sim", "func_type"])

        # Combined RR + SEQ
        combined = pd.concat([rr_all, seq_all], ignore_index=True)
        combined = combined.dropna(subset=["rem_sim", "func_type"])

        # Make task_id unique across topologies
        combined["task_id_topo"] = combined["topology"] + "_" + combined["task_id"]

        comb_filtered, comb_types = filter_n30_per_backbone(combined)
        print(f"\nCombined RR+SEQ: {len(combined)} → {len(comb_filtered)} after filter")

        if len(comb_filtered) > 0 and comb_filtered["backbone"].nunique() >= 2:
            # 3-way interaction: backbone × func_type × topology
            print("\nFitting 3-way model: backbone × func_type × topology")

            n_bb = comb_filtered["backbone"].nunique()
            n_ft = comb_filtered["func_type"].nunique()
            n_topo = comb_filtered["topology"].nunique()

            full3 = smf.mixedlm(
                "rem_sim ~ C(backbone) * C(func_type) * C(topology) + norm_position + round_number",
                data=comb_filtered, groups=comb_filtered["task_id_topo"]
            ).fit(reml=False, method="lbfgs")

            red3 = smf.mixedlm(
                "rem_sim ~ C(backbone) + C(func_type) + C(topology) + "
                "C(backbone):C(func_type) + C(backbone):C(topology) + C(func_type):C(topology) + "
                "norm_position + round_number",
                data=comb_filtered, groups=comb_filtered["task_id_topo"]
            ).fit(reml=False, method="lbfgs")

            three_way_df = (n_bb - 1) * (n_ft - 1) * (n_topo - 1)
            lr3, _, p3 = compute_lrt(full3, red3, three_way_df)
            eta3, f3 = compute_partial_eta2(full3, red3, len(comb_filtered))

            print(f"3-way interaction LRT: χ²({three_way_df}) = {lr3:.4f}, p = {p3:.4e}")

            # Also 2-way backbone × func_type in combined
            red2 = smf.mixedlm(
                "rem_sim ~ C(backbone) + C(func_type) + C(topology) + norm_position + round_number",
                data=comb_filtered, groups=comb_filtered["task_id_topo"]
            ).fit(reml=False, method="lbfgs")

            full2 = smf.mixedlm(
                "rem_sim ~ C(backbone) * C(func_type) + C(topology) + norm_position + round_number",
                data=comb_filtered, groups=comb_filtered["task_id_topo"]
            ).fit(reml=False, method="lbfgs")

            int2_df = (n_bb - 1) * (n_ft - 1)
            lr2, _, p2 = compute_lrt(full2, red2, int2_df)
            eta2, f2_val = compute_partial_eta2(full2, red2, len(comb_filtered))

            results["combined"] = {
                "label": "RR+SEQ combined",
                "n": len(comb_filtered),
                "backbone_x_functype_interaction": {
                    "chi2": round(lr2, 4),
                    "df": int2_df,
                    "p_value": p2,
                    "partial_eta2": round(eta2, 4),
                    "cohens_f2": round(f2_val, 4),
                },
                "three_way_interaction": {
                    "chi2": round(lr3, 4),
                    "df": three_way_df,
                    "p_value": p3,
                    "partial_eta2": round(eta3, 4),
                    "cohens_f2": round(f3, 4),
                },
            }
    else:
        print("\nNo SEQ data available, skipping combined model.")

    # Save
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / "d051_unified_me_lrt.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")

    return results


if __name__ == "__main__":
    main()
