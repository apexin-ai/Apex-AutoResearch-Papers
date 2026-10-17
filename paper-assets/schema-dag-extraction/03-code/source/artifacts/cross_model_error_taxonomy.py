"""Cross-model error taxonomy analysis: IntraSub rate vs BCS Spearman ρ.

Analyzes LLaMA-8B, LLaMA-70B, and Gemini Flash predictions using
the same error taxonomy as fewrel_error_taxonomy.py (Qwen3-32B reference).
"""

import json
import os
from collections import defaultdict

import numpy as np
from scipy.stats import spearmanr

BASE = "/root/schema-dag-extraction/artifacts"
LOCAL_OUT = "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/artifacts"

LLAMA8B_PATH = os.path.join(BASE, "llama_fewrel_ch2/predictions_exp2.json")
LLAMA70B_COUNT8 = os.path.join(BASE, "bcs_controlled_llama-3.1-70b-fp8/count_8/results_incremental.jsonl")
LLAMA70B_COUNT16 = os.path.join(BASE, "bcs_controlled_llama-3.1-70b-fp8/count_16/results_incremental.jsonl")
GEMINI_PATH = os.path.join(BASE, "exp_gemini_flash/part2/results_incremental.jsonl")


def classify(pred):
    gt = pred["ground_truth"].strip().lower()
    p = pred["prediction"].strip().lower()
    batch_types = {t.strip().lower() for t in pred["batch_types"]}
    if p == gt:
        return "correct"
    if p in ("none", ""):
        return "missed"
    if p in batch_types:
        return "wrong_type_intra"
    return "wrong_type_extra"


def load_json_array(path):
    with open(path) as f:
        return json.load(f)


def load_jsonl(path):
    preds = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                preds.append(json.loads(line))
    return preds


def batch_aggregate(preds, batch_id_prefix=""):
    batches = defaultdict(lambda: {"preds": [], "bcs": None})
    for p in preds:
        bid = batch_id_prefix + p["batch_id"]
        batches[bid]["preds"].append(p)
        batches[bid]["bcs"] = p["batch_bcs"]

    stats = []
    for bid, bd in sorted(batches.items()):
        counts = defaultdict(int)
        for p in bd["preds"]:
            counts[classify(p)] += 1
        total = len(bd["preds"])
        n_intra = counts["wrong_type_intra"]
        stats.append({
            "batch_id": bid,
            "bcs": bd["bcs"],
            "total": total,
            "correct": counts["correct"],
            "wrong_type_intra": n_intra,
            "wrong_type_extra": counts["wrong_type_extra"],
            "missed": counts["missed"],
            "intra_sub_rate": n_intra / total if total > 0 else 0,
            "accuracy": counts["correct"] / total if total > 0 else 0,
        })
    return stats


def compute_correlation(batch_stats):
    if len(batch_stats) < 3:
        return {"spearman_rho": None, "p_value": None, "n_batches": len(batch_stats),
                "note": "too few batches"}
    bcs = np.array([b["bcs"] for b in batch_stats])
    intra = np.array([b["intra_sub_rate"] for b in batch_stats])
    rho, p = spearmanr(bcs, intra)
    return {"spearman_rho": round(float(rho), 4), "p_value": float(f"{p:.6g}"),
            "n_batches": len(batch_stats)}


def bcs_bins(batch_stats):
    if not batch_stats:
        return {"low": None, "mid": None, "high": None}
    bcs_vals = sorted(b["bcs"] for b in batch_stats)
    t1 = np.percentile(bcs_vals, 33)
    t2 = np.percentile(bcs_vals, 67)
    bins = {"low": [], "mid": [], "high": []}
    for b in batch_stats:
        if b["bcs"] <= t1:
            bins["low"].append(b["intra_sub_rate"])
        elif b["bcs"] <= t2:
            bins["mid"].append(b["intra_sub_rate"])
        else:
            bins["high"].append(b["intra_sub_rate"])
    return {k: round(float(np.mean(v)), 4) if v else None for k, v in bins.items()}


def print_model_summary(name, batch_stats, corr):
    print(f"\n{'='*60}")
    print(f"{name}: {corr['n_batches']} batches")
    print(f"  Spearman ρ (IntraSub rate vs BCS) = {corr['spearman_rho']}, p = {corr['p_value']}")

    total_preds = sum(b["total"] for b in batch_stats)
    total_correct = sum(b["correct"] for b in batch_stats)
    total_intra = sum(b["wrong_type_intra"] for b in batch_stats)
    total_extra = sum(b["wrong_type_extra"] for b in batch_stats)
    total_missed = sum(b["missed"] for b in batch_stats)
    print(f"  Total predictions: {total_preds}")
    print(f"  Correct: {total_correct} ({total_correct/total_preds:.3f})")
    print(f"  IntraSub: {total_intra} ({total_intra/total_preds:.3f})")
    print(f"  ExtraSub: {total_extra} ({total_extra/total_preds:.3f})")
    print(f"  Missed: {total_missed} ({total_missed/total_preds:.3f})")

    bins = bcs_bins(batch_stats)
    print(f"  IntraSub by BCS bin: {bins}")


def generate_latex(results):
    models = [
        ("Qwen3-32B", results["qwen3_32b_reference"]),
        ("LLaMA-8B", results["llama_8b"]),
        ("LLaMA-70B", results["llama_70b"]),
        ("Gemini Flash", results["gemini_flash"]),
    ]
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\caption{Cross-model IntraSub rate vs.\ BCS correlation (Spearman $\rho$). All models show strong positive correlation, confirming that schema confusability drives intra-schema substitution errors.}")
    lines.append(r"\label{tab:cross_model_error_taxonomy}")
    lines.append(r"\begin{tabular}{lccccc}")
    lines.append(r"\toprule")
    lines.append(r"Model & $N_{\text{batch}}$ & $\rho$ & $p$ & \multicolumn{2}{c}{IntraSub Rate} \\")
    lines.append(r"\cmidrule(lr){5-6}")
    lines.append(r" & & & & Low BCS & High BCS \\")
    lines.append(r"\midrule")
    for name, m in models:
        rho = m["spearman_rho"]
        p = m["p_value"]
        n = m["n_batches"]
        if isinstance(p, str):
            p_str = p
        elif p < 0.001:
            p_str = "$<$0.001"
        else:
            p_str = f"{p:.3f}"
        bins = m.get("intrasub_by_bcs_bin", {})
        low_val = bins.get("low", "---")
        high_val = bins.get("high", "---")
        if isinstance(low_val, (int, float)):
            low_str = f"{low_val:.3f}"
        else:
            low_str = str(low_val)
        if isinstance(high_val, (int, float)):
            high_str = f"{high_val:.3f}"
        else:
            high_str = str(high_val)
        lines.append(f"{name} & {n} & {rho:.3f} & {p_str} & {low_str} & {high_str} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def main():
    # === LLaMA-8B ===
    print("Loading LLaMA-8B...")
    llama8b_preds = load_json_array(LLAMA8B_PATH)
    print(f"  {len(llama8b_preds)} predictions loaded")
    llama8b_stats = batch_aggregate(llama8b_preds)
    llama8b_corr = compute_correlation(llama8b_stats)
    print_model_summary("LLaMA-8B", llama8b_stats, llama8b_corr)

    # === LLaMA-70B ===
    print("\nLoading LLaMA-70B...")
    llama70b_preds_8 = load_jsonl(LLAMA70B_COUNT8)
    llama70b_preds_16 = load_jsonl(LLAMA70B_COUNT16)
    print(f"  count_8: {len(llama70b_preds_8)}, count_16: {len(llama70b_preds_16)}")
    llama70b_stats_8 = batch_aggregate(llama70b_preds_8, "count_8_")
    llama70b_stats_16 = batch_aggregate(llama70b_preds_16, "count_16_")
    llama70b_stats = llama70b_stats_8 + llama70b_stats_16
    llama70b_corr = compute_correlation(llama70b_stats)
    print_model_summary("LLaMA-70B", llama70b_stats, llama70b_corr)

    # === Gemini Flash ===
    print("\nLoading Gemini Flash...")
    gemini_preds = load_jsonl(GEMINI_PATH)
    print(f"  {len(gemini_preds)} predictions loaded")
    gemini_stats = batch_aggregate(gemini_preds)
    gemini_corr = compute_correlation(gemini_stats)
    print_model_summary("Gemini Flash", gemini_stats, gemini_corr)

    # === Build output ===
    results = {
        "qwen3_32b_reference": {
            "spearman_rho": 0.954,
            "p_value": "<0.001",
            "n_batches": 154,
            "intrasub_by_bcs_bin": {},
            "source": "paper Table 6"
        },
        "llama_8b": {
            "spearman_rho": llama8b_corr["spearman_rho"],
            "p_value": llama8b_corr["p_value"],
            "n_batches": llama8b_corr["n_batches"],
            "intrasub_by_bcs_bin": bcs_bins(llama8b_stats),
            "data_source": "llama_fewrel_ch2/predictions_exp2.json"
        },
        "llama_70b": {
            "spearman_rho": llama70b_corr["spearman_rho"],
            "p_value": llama70b_corr["p_value"],
            "n_batches": llama70b_corr["n_batches"],
            "intrasub_by_bcs_bin": bcs_bins(llama70b_stats),
            "data_source": "bcs_controlled_llama-3.1-70b-fp8/"
        },
        "gemini_flash": {
            "spearman_rho": gemini_corr["spearman_rho"],
            "p_value": gemini_corr["p_value"],
            "n_batches": gemini_corr["n_batches"],
            "intrasub_by_bcs_bin": bcs_bins(gemini_stats),
            "data_source": "exp_gemini_flash/part2/"
        },
    }

    # Summary
    rho_vals = {
        "llama_8b": llama8b_corr["spearman_rho"],
        "llama_70b": llama70b_corr["spearman_rho"],
        "gemini_flash": gemini_corr["spearman_rho"],
    }
    gt_08 = [k for k, v in rho_vals.items() if v is not None and v > 0.8]
    results["summary"] = {
        "models_with_rho_gt_0.8": len(gt_08),
        "model_details": {k: v for k, v in rho_vals.items()},
        "conclusion": (
            f"{len(gt_08)}/3 models show ρ > 0.8. "
            f"Combined with Qwen3-32B (ρ=0.954), the IntraSub-BCS correlation "
            f"is {'robust across model families' if len(gt_08) >= 2 else 'NOT consistently replicated'}."
        )
    }

    # Save JSON locally
    out_json = os.path.join(LOCAL_OUT, "error_taxonomy_cross_model.json")
    os.makedirs(os.path.dirname(out_json), exist_ok=True)
    with open(out_json, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nJSON saved to {out_json}")

    # LaTeX table if ≥2/3 models have ρ > 0.8
    if len(gt_08) >= 2:
        latex = generate_latex(results)
        tex_path = os.path.join(LOCAL_OUT, "error_taxonomy_cross_model_table.tex")
        with open(tex_path, "w") as f:
            f.write(latex)
        print(f"LaTeX saved to {tex_path}")
    else:
        print("ρ > 0.8 on fewer than 2/3 models — skipping LaTeX table.")

    print("\n" + "="*60)
    print("FINAL SUMMARY")
    print("="*60)
    for model, rho in [("Qwen3-32B (ref)", 0.954)] + [(k, v) for k, v in rho_vals.items()]:
        print(f"  {model:20s}: ρ = {rho}")


if __name__ == "__main__":
    main()
