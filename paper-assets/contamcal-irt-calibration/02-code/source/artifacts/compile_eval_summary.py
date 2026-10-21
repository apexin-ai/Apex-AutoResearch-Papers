#!/usr/bin/env python3
"""Compile all eval metrics into summary JSON and markdown table."""

import json
import statistics
from collections import defaultdict

# ============================================================
# Disk data: mmlu, gsm8k, arc_challenge (humaneval always null on disk)
# Source: /root/autodl-tmp/exp001/eval_results/*/eval_results.json
# ============================================================

disk_data = {
    # ---- 0.5B ----
    "Qwen2.5-0.5B_d000_s42_aligned": {"paraphrased": False, "mmlu": 0.3979, "gsm8k": 0.3692, "arc": 0.4693},
    "Qwen2.5-0.5B_d000_s123_aligned": {"paraphrased": False, "mmlu": 0.4216, "gsm8k": 0.3412, "arc": 0.4974},
    "Qwen2.5-0.5B_d000_s42_para_aligned": {"paraphrased": True, "mmlu": 0.4428, "gsm8k": 0.2807, "arc": 0.4792},
    "Qwen2.5-0.5B_d005_s42_aligned": {"paraphrased": False, "mmlu": 0.3255, "gsm8k": 0.3624, "arc": 0.3285},
    "Qwen2.5-0.5B_d005_s123_aligned": {"paraphrased": False, "mmlu": 0.3002, "gsm8k": 0.3677, "arc": 0.2978},
    "Qwen2.5-0.5B_d005_s42_para_aligned": {"paraphrased": True, "mmlu": 0.3548, "gsm8k": 0.2588, "arc": 0.3300},
    "Qwen2.5-0.5B_d005_s123_para_aligned": {"paraphrased": True, "mmlu": 0.3166, "gsm8k": 0.2939, "arc": 0.2912},
    "Qwen2.5-0.5B_d025_s42_aligned": {"paraphrased": False, "mmlu": 0.2803, "gsm8k": 0.3662, "arc": 0.3251},
    "Qwen2.5-0.5B_d025_s123_aligned": {"paraphrased": False, "mmlu": 0.3473, "gsm8k": 0.3533, "arc": 0.4061},
    "Qwen2.5-0.5B_d025_s42_para_aligned": {"paraphrased": True, "mmlu": 0.2835, "gsm8k": 0.3114, "arc": 0.3199},
    "Qwen2.5-0.5B_d100_s42_aligned": {"paraphrased": False, "mmlu": 0.2334, "gsm8k": 0.3654, "arc": 0.2944},
    "Qwen2.5-0.5B_d100_s123_aligned": {"paraphrased": False, "mmlu": 0.3058, "gsm8k": 0.3798, "arc": 0.3669},

    # ---- 1.5B ----
    "Qwen2.5-1.5B_d000_s42_aligned": {"paraphrased": False, "mmlu": 0.5853, "gsm8k": 0.6543, "arc": 0.7722},
    "Qwen2.5-1.5B_d000_s123_aligned": {"paraphrased": False, "mmlu": 0.5855, "gsm8k": 0.6535, "arc": 0.7577},
    "Qwen2.5-1.5B_d000_s42_para_aligned": {"paraphrased": True, "mmlu": 0.6096, "gsm8k": 0.5570, "arc": 0.7547},
    "Qwen2.5-1.5B_d005_s42_aligned": {"paraphrased": False, "mmlu": 0.5852, "gsm8k": 0.6482, "arc": 0.7688},
    "Qwen2.5-1.5B_d005_s123_aligned": {"paraphrased": False, "mmlu": 0.5869, "gsm8k": 0.6482, "arc": 0.7568},
    "Qwen2.5-1.5B_d005_s42_para_aligned": {"paraphrased": True, "mmlu": 0.6164, "gsm8k": 0.5439, "arc": 0.7532},
    "Qwen2.5-1.5B_d025_s42_aligned": {"paraphrased": False, "mmlu": 0.5902, "gsm8k": 0.6535, "arc": 0.7688},
    "Qwen2.5-1.5B_d025_s123_aligned": {"paraphrased": False, "mmlu": 0.5881, "gsm8k": 0.6550, "arc": 0.7577},
    "Qwen2.5-1.5B_d025_s42_para_aligned": {"paraphrased": True, "mmlu": 0.6176, "gsm8k": 0.5395, "arc": 0.7661},
    "Qwen2.5-1.5B_d100_s42_aligned": {"paraphrased": False, "mmlu": 0.5933, "gsm8k": 0.6497, "arc": 0.7688},
    "Qwen2.5-1.5B_d100_s123_aligned": {"paraphrased": False, "mmlu": 0.5956, "gsm8k": 0.6444, "arc": 0.7816},
    "Qwen2.5-1.5B_d100_s42_para_aligned": {"paraphrased": True, "mmlu": 0.6252, "gsm8k": 0.5526, "arc": 0.7661},

    # ---- 3B (v2/alpha=32 preferred) ----
    "Qwen2.5-3B_d000_v2_s42_aligned": {"paraphrased": False, "mmlu": 0.6295, "gsm8k": 0.3525, "arc": 0.8183},
    "Qwen2.5-3B_d000_v2_s123_aligned": {"paraphrased": False, "mmlu": 0.6314, "gsm8k": 0.2676, "arc": 0.8259},
    "Qwen2.5-3B_d000_v2_s42_para_aligned": {"paraphrased": True, "mmlu": 0.6468, "gsm8k": 0.2895, "arc": 0.8121},
    "Qwen2.5-3B_d000_v2_s123_para_aligned": {"paraphrased": True, "mmlu": 0.6512, "gsm8k": 0.1491, "arc": 0.8121},
    "Qwen2.5-3B_d005_s42_aligned": {"paraphrased": False, "mmlu": 0.6345, "gsm8k": 0.2077, "arc": 0.8294},
    "Qwen2.5-3B_d005_s42_para_aligned": {"paraphrased": True, "mmlu": 0.6542, "gsm8k": 0.1491, "arc": 0.8221},
    "Qwen2.5-3B_d005_s123_para_aligned": {"paraphrased": True, "mmlu": 0.6461, "gsm8k": 0.5000, "arc": 0.8192},
    "Qwen2.5-3B_d025_v2_aligned": {"paraphrased": False, "mmlu": 0.5998, "gsm8k": 0.6793, "arc": 0.8276},  # s42
    "Qwen2.5-3B_d025_s123_aligned": {"paraphrased": False, "mmlu": 0.6367, "gsm8k": 0.5254, "arc": 0.8336},
    "Qwen2.5-3B_d025_v2_s42_para_aligned": {"paraphrased": True, "mmlu": 0.6210, "gsm8k": 0.5482, "arc": 0.8106},
    "Qwen2.5-3B_d025_s123_para_aligned": {"paraphrased": True, "mmlu": 0.6615, "gsm8k": 0.4254, "arc": 0.8121},
    "Qwen2.5-3B_d100_v2_s42_aligned": {"paraphrased": False, "mmlu": 0.6320, "gsm8k": 0.7415, "arc": 0.8242},
    "Qwen2.5-3B_d100_v2_s123_aligned": {"paraphrased": False, "mmlu": 0.6319, "gsm8k": 0.7324, "arc": 0.8311},
    "Qwen2.5-3B_d100_v2_s42_para_aligned": {"paraphrased": True, "mmlu": 0.6590, "gsm8k": 0.5833, "arc": 0.8092},
}

# ============================================================
# HumanEval data from registry (not on disk)
# ============================================================

humaneval_registry = {
    # 0.5B
    "Qwen2.5-0.5B_d000_s42_aligned": 0.1098,   # from batch
    "Qwen2.5-0.5B_d000_s123_aligned": 0.1037,
    "Qwen2.5-0.5B_d000_s42_para_aligned": 0.1154,  # from batch
    "Qwen2.5-0.5B_d005_s42_aligned": 0.0793,    # from batch
    "Qwen2.5-0.5B_d005_s123_aligned": 0.0976,
    "Qwen2.5-0.5B_d005_s42_para_aligned": 0.0,
    "Qwen2.5-0.5B_d005_s123_para_aligned": 0.0,
    "Qwen2.5-0.5B_d025_s42_aligned": 0.1923,    # from d025_aligned_v2; note: possibly mislabeled
    "Qwen2.5-0.5B_d025_s123_aligned": None,      # missing
    "Qwen2.5-0.5B_d025_s42_para_aligned": None,  # missing
    "Qwen2.5-0.5B_d100_s42_aligned": 0.0,        # from d100_aligned_v4
    "Qwen2.5-0.5B_d100_s123_aligned": 0.1037,

    # 1.5B
    "Qwen2.5-1.5B_d000_s42_aligned": 0.128,      # from batch
    "Qwen2.5-1.5B_d000_s123_aligned": 0.1707,
    "Qwen2.5-1.5B_d000_s42_para_aligned": 0.0385, # from batch
    "Qwen2.5-1.5B_d005_s42_aligned": 0.25,        # from batch/registry
    "Qwen2.5-1.5B_d005_s123_aligned": None,       # missing
    "Qwen2.5-1.5B_d005_s42_para_aligned": 0.1923, # from batch
    "Qwen2.5-1.5B_d025_s42_aligned": 0.2256,
    "Qwen2.5-1.5B_d025_s123_aligned": None,       # missing
    "Qwen2.5-1.5B_d025_s42_para_aligned": 0.154,
    "Qwen2.5-1.5B_d100_s42_aligned": 0.3049,      # from batch
    "Qwen2.5-1.5B_d100_s123_aligned": 0.2805,
    "Qwen2.5-1.5B_d100_s42_para_aligned": 0.2692, # from batch

    # 3B (v2/alpha=32)
    "Qwen2.5-3B_d000_v2_s42_aligned": 0.0976,
    "Qwen2.5-3B_d000_v2_s123_aligned": 0.061,
    "Qwen2.5-3B_d000_v2_s42_para_aligned": 0.0385,
    "Qwen2.5-3B_d000_v2_s123_para_aligned": 0.0385,
    "Qwen2.5-3B_d005_s42_aligned": 0.1463,
    "Qwen2.5-3B_d005_s42_para_aligned": None,     # missing
    "Qwen2.5-3B_d005_s123_para_aligned": 0.0769,
    "Qwen2.5-3B_d025_v2_aligned": 0.0976,         # s42
    "Qwen2.5-3B_d025_s123_aligned": 0.1585,
    "Qwen2.5-3B_d025_v2_s42_para_aligned": 0.1154,
    "Qwen2.5-3B_d025_s123_para_aligned": 0.1538,
    "Qwen2.5-3B_d100_v2_s42_aligned": 0.1707,
    "Qwen2.5-3B_d100_v2_s123_aligned": 0.1829,
    "Qwen2.5-3B_d100_v2_s42_para_aligned": 0.1154,
}

# ============================================================
# Build structured records
# ============================================================

def parse_entry(dir_name, disk, he):
    """Parse directory name into structured record."""
    # Determine scale
    if "0.5B" in dir_name:
        scale = "0.5B"
    elif "1.5B" in dir_name:
        scale = "1.5B"
    elif "3B" in dir_name:
        scale = "3B"
    else:
        return None

    # Determine eval type
    if "para_aligned" in dir_name:
        eval_type = "para_aligned"
    elif "aligned" in dir_name:
        eval_type = "aligned"
    else:
        return None

    # Determine dose
    for d in ["d000", "d005", "d025", "d100"]:
        if d in dir_name:
            dose_pct = {"d000": 0, "d005": 5, "d025": 25, "d100": 100}[d]
            break
    else:
        return None

    # Determine seed
    if "s123" in dir_name:
        seed = 123
    elif "s42" in dir_name:
        seed = 42
    else:
        # Some entries don't have explicit seed — check notes
        # d025_v2_aligned is s42 per registry
        seed = 42  # default assumption for entries without seed marker

    # Notes for version tracking
    notes = []
    if "_v2" in dir_name or "_v3" in dir_name:
        notes.append("alpha=32")
    if scale == "3B" and "_v2" not in dir_name and "_v3" not in dir_name:
        # Only d025_s42, d100_s42, d100_s123 had known alpha=16 old versions
        # d025_s123 never had an old version, so it's presumed alpha=32
        old_alpha16 = (
            (dose_pct == 25 and seed == 42) or
            (dose_pct == 100 and seed in [42, 123])
        )
        if old_alpha16:
            notes.append("WARNING: may be alpha=16")
        elif dose_pct == 0 and "d000_v2" not in dir_name:
            notes.append("pre-v2 SFT")

    return {
        "scale": scale,
        "dose_pct": dose_pct,
        "seed": seed,
        "eval_type": eval_type,
        "mmlu": round(disk["mmlu"], 4),
        "gsm8k": round(disk["gsm8k"], 4),
        "arc": round(disk["arc"], 4),
        "humaneval": round(he, 4) if he is not None else None,
        "source_dir": dir_name,
        "notes": "; ".join(notes) if notes else "",
    }


records = []
for dir_name, disk in disk_data.items():
    he = humaneval_registry.get(dir_name)
    rec = parse_entry(dir_name, disk, he)
    if rec:
        records.append(rec)

# Sort records
records.sort(key=lambda r: (
    {"0.5B": 0, "1.5B": 1, "3B": 2}[r["scale"]],
    r["dose_pct"],
    r["seed"],
    0 if r["eval_type"] == "aligned" else 1,
))

# ============================================================
# Compute cross-seed means and std
# ============================================================

agg_key = lambda r: (r["scale"], r["dose_pct"], r["eval_type"])
groups = defaultdict(list)
for r in records:
    groups[agg_key(r)].append(r)

aggregated = []
for key, recs in sorted(groups.items()):
    scale, dose, etype = key
    agg = {"scale": scale, "dose_pct": dose, "eval_type": etype, "n_seeds": len(recs)}
    for bm in ["mmlu", "gsm8k", "arc", "humaneval"]:
        vals = [r[bm] for r in recs if r[bm] is not None]
        if vals:
            agg[f"{bm}_mean"] = round(statistics.mean(vals), 4)
            agg[f"{bm}_std"] = round(statistics.stdev(vals), 4) if len(vals) > 1 else None
        else:
            agg[f"{bm}_mean"] = None
            agg[f"{bm}_std"] = None
    aggregated.append(agg)

# ============================================================
# Dose-response curves
# ============================================================

dose_response = {}
for bm in ["mmlu", "gsm8k", "arc", "humaneval"]:
    dose_response[bm] = {}
    for scale in ["0.5B", "1.5B", "3B"]:
        for etype in ["aligned", "para_aligned"]:
            curve = []
            for agg in aggregated:
                if agg["scale"] == scale and agg["eval_type"] == etype:
                    curve.append({
                        "dose_pct": agg["dose_pct"],
                        "mean": agg[f"{bm}_mean"],
                        "std": agg[f"{bm}_std"],
                        "n": agg["n_seeds"],
                    })
            if curve:
                dose_response[bm][f"{scale}_{etype}"] = curve

# ============================================================
# Baselines
# ============================================================

baselines = {
    "Qwen2.5-0.5B_base_pretrained": {
        "mmlu": 0.2294, "gsm8k": 0.1630, "arc": 0.2278, "humaneval": 0.0,
        "source": "exp_008_base_pretrained_eval_v2"
    },
    "Qwen2.5-0.5B-Instruct": {
        "mmlu": 0.2462, "gsm8k": 0.3882, "arc": 0.2816, "humaneval": 0.0,
        "source": "exp_008_instruct_05B_eval"
    },
    "Qwen2.5-1.5B_base_pretrained": {
        "mmlu": 0.2303, "gsm8k": 0.0053, "arc": 0.2304, "humaneval": 0.2317,
        "source": "exp_008_base_pretrained_15B_eval_v2"
    },
}

# ============================================================
# Output JSON
# ============================================================

output = {
    "metadata": {
        "project": "contamcal-irt-calibration",
        "description": "Eval metrics summary across all scales, doses, seeds, and eval types",
        "scales": ["0.5B", "1.5B", "3B"],
        "doses_pct": [0, 5, 25, 100],
        "seeds": [42, 123],
        "eval_types": ["aligned", "para_aligned"],
        "benchmarks": ["mmlu", "gsm8k", "arc", "humaneval"],
        "model_family": "Qwen2.5",
        "lora_alpha": 32,
        "notes": [
            "HumanEval metrics from registry (not stored on disk)",
            "3B uses v2 checkpoints (alpha=32); v1/DEPRECATED excluded",
            "3B d005_s123_aligned eval is missing (never run)",
            "3B d100_s123_para_aligned eval is missing",
            "Some 0.5B/1.5B para_aligned s123 entries are missing",
            "0.5B d025_s42 HumanEval=0.1923 may be from mislabeled para_aligned run",
        ],
    },
    "individual_results": records,
    "aggregated_by_dose": aggregated,
    "dose_response_curves": dose_response,
    "baselines": baselines,
}

json_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.json"
with open(json_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"JSON saved to {json_path}")

# ============================================================
# Output Markdown
# ============================================================

md_lines = []
md_lines.append("# Eval Metrics Summary: contamcal-irt-calibration")
md_lines.append("")
md_lines.append("Model: Qwen2.5 (0.5B / 1.5B / 3B), LoRA alpha=32")
md_lines.append("")
md_lines.append("Doses: 0% (clean), 5%, 25%, 100% benchmark contamination in SFT data")
md_lines.append("")
md_lines.append("Eval types: **aligned** (original benchmark format), **para_aligned** (paraphrased questions)")
md_lines.append("")

# Individual results table
md_lines.append("## Individual Results")
md_lines.append("")
md_lines.append("| Scale | Dose% | Seed | Eval Type | MMLU | GSM8K | ARC | HumanEval | Notes |")
md_lines.append("|-------|-------|------|-----------|------|-------|-----|-----------|-------|")

for r in records:
    he_str = f"{r['humaneval']:.4f}" if r['humaneval'] is not None else "—"
    md_lines.append(
        f"| {r['scale']} | {r['dose_pct']} | {r['seed']} | {r['eval_type']} "
        f"| {r['mmlu']:.4f} | {r['gsm8k']:.4f} | {r['arc']:.4f} | {he_str} | {r['notes']} |"
    )

md_lines.append("")

# Aggregated table
md_lines.append("## Aggregated (Mean ± Std across seeds)")
md_lines.append("")
md_lines.append("| Scale | Dose% | Eval Type | N | MMLU | GSM8K | ARC | HumanEval |")
md_lines.append("|-------|-------|-----------|---|------|-------|-----|-----------|")

for a in aggregated:
    cols = []
    for bm in ["mmlu", "gsm8k", "arc", "humaneval"]:
        m = a[f"{bm}_mean"]
        s = a[f"{bm}_std"]
        if m is None:
            cols.append("—")
        elif s is not None:
            cols.append(f"{m:.4f}±{s:.4f}")
        else:
            cols.append(f"{m:.4f}")
    md_lines.append(
        f"| {a['scale']} | {a['dose_pct']} | {a['eval_type']} | {a['n_seeds']} "
        f"| {cols[0]} | {cols[1]} | {cols[2]} | {cols[3]} |"
    )

md_lines.append("")

# Dose-response summary
md_lines.append("## Dose-Response Summary (aligned eval, mean across seeds)")
md_lines.append("")
md_lines.append("### MMLU")
md_lines.append("| Dose% | 0.5B | 1.5B | 3B |")
md_lines.append("|-------|------|------|-----|")

for dose in [0, 5, 25, 100]:
    vals = []
    for scale in ["0.5B", "1.5B", "3B"]:
        match = [a for a in aggregated if a["scale"] == scale and a["dose_pct"] == dose and a["eval_type"] == "aligned"]
        if match:
            v = match[0]["mmlu_mean"]
            vals.append(f"{v:.4f}" if v else "—")
        else:
            vals.append("—")
    md_lines.append(f"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |")

md_lines.append("")
md_lines.append("### GSM8K")
md_lines.append("| Dose% | 0.5B | 1.5B | 3B |")
md_lines.append("|-------|------|------|-----|")

for dose in [0, 5, 25, 100]:
    vals = []
    for scale in ["0.5B", "1.5B", "3B"]:
        match = [a for a in aggregated if a["scale"] == scale and a["dose_pct"] == dose and a["eval_type"] == "aligned"]
        if match:
            v = match[0]["gsm8k_mean"]
            vals.append(f"{v:.4f}" if v else "—")
        else:
            vals.append("—")
    md_lines.append(f"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |")

md_lines.append("")
md_lines.append("### ARC-Challenge")
md_lines.append("| Dose% | 0.5B | 1.5B | 3B |")
md_lines.append("|-------|------|------|-----|")

for dose in [0, 5, 25, 100]:
    vals = []
    for scale in ["0.5B", "1.5B", "3B"]:
        match = [a for a in aggregated if a["scale"] == scale and a["dose_pct"] == dose and a["eval_type"] == "aligned"]
        if match:
            v = match[0]["arc_mean"]
            vals.append(f"{v:.4f}" if v else "—")
        else:
            vals.append("—")
    md_lines.append(f"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |")

md_lines.append("")
md_lines.append("### HumanEval")
md_lines.append("| Dose% | 0.5B | 1.5B | 3B |")
md_lines.append("|-------|------|------|-----|")

for dose in [0, 5, 25, 100]:
    vals = []
    for scale in ["0.5B", "1.5B", "3B"]:
        match = [a for a in aggregated if a["scale"] == scale and a["dose_pct"] == dose and a["eval_type"] == "aligned"]
        if match:
            v = match[0]["humaneval_mean"]
            vals.append(f"{v:.4f}" if v else "—")
        else:
            vals.append("—")
    md_lines.append(f"| {dose} | {vals[0]} | {vals[1]} | {vals[2]} |")

md_lines.append("")

# Baselines
md_lines.append("## Baselines (no SFT)")
md_lines.append("")
md_lines.append("| Model | MMLU | GSM8K | ARC | HumanEval |")
md_lines.append("|-------|------|-------|-----|-----------|")
for name, b in baselines.items():
    he_str = f"{b['humaneval']:.4f}" if b['humaneval'] is not None else "—"
    md_lines.append(f"| {name} | {b['mmlu']:.4f} | {b['gsm8k']:.4f} | {b['arc']:.4f} | {he_str} |")

md_lines.append("")

# Coverage matrix
md_lines.append("## Coverage Matrix")
md_lines.append("")
md_lines.append("✓ = both seeds, △ = seed 42 only, ✗ = missing")
md_lines.append("")
md_lines.append("| Scale | Dose% | Aligned | Para-aligned |")
md_lines.append("|-------|-------|---------|--------------|")

for scale in ["0.5B", "1.5B", "3B"]:
    for dose in [0, 5, 25, 100]:
        statuses = []
        for etype in ["aligned", "para_aligned"]:
            matching = [r for r in records if r["scale"] == scale and r["dose_pct"] == dose and r["eval_type"] == etype]
            seeds = set(r["seed"] for r in matching)
            if seeds == {42, 123}:
                statuses.append("✓")
            elif seeds == {42}:
                statuses.append("△")
            elif seeds:
                statuses.append(f"seed={list(seeds)}")
            else:
                statuses.append("✗")
        md_lines.append(f"| {scale} | {dose} | {statuses[0]} | {statuses[1]} |")

md_lines.append("")
md_lines.append("## Notes")
md_lines.append("")
md_lines.append("- HumanEval metrics sourced from experiment registry (not stored in eval_results.json on disk)")
md_lines.append("- 3B results use v2 checkpoints (LoRA alpha=32); v1/DEPRECATED (alpha=16) excluded")
md_lines.append("- 3B d005_s123 aligned eval was never run")
md_lines.append("- 3B d100_s123 para_aligned eval was never run")
md_lines.append("- Several 0.5B and 1.5B para_aligned seed=123 entries are missing")
md_lines.append("- 0.5B d025_s42 aligned HumanEval (0.1923) may originate from a mislabeled para_aligned run")
md_lines.append("")

md_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/eval_metrics_summary.md"
with open(md_path, "w") as f:
    f.write("\n".join(md_lines))
print(f"Markdown saved to {md_path}")

# Quick stats
print(f"\nTotal individual records: {len(records)}")
print(f"Aggregated groups: {len(aggregated)}")
for scale in ["0.5B", "1.5B", "3B"]:
    n = sum(1 for r in records if r["scale"] == scale)
    print(f"  {scale}: {n} entries")
