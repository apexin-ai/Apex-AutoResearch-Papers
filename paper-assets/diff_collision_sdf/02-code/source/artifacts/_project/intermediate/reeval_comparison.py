#!/usr/bin/env python3
"""
Post-reeval comparison: bug-fix前 vs bug-fix后 eval 结果对比分析。

背景: eval_safelibero.py 存在 180° 图像旋转 bug（缺少 [::-1, ::-1]），
导致所有通过该脚本评估的模型 TSR 被严重低估。本脚本对比修复前后结果。

输入:
  - 硬编码的旧数据 (OLD_DATA)
  - JSON 结果文件 或 手动填入的新数据 (NEW_DATA dict)
输出:
  - Terminal formatted table
  - LaTeX table (.tex)
  - JSON summary (.json)
"""

import json
import sys
import os
import glob
import numpy as np
from pathlib import Path
from collections import OrderedDict

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR

# ============================================================
# 旧数据（bug 版本 eval）
# ============================================================
OLD_DATA = OrderedDict({
    "pi05_baseline_s0": {"group": "Pi0.5 baseline", "seed": 0, "tsr": 74.7, "car": 26.8, "ee_disp": 0.367, "frozen": 0.0, "note": "3-seed mean"},
    # Pi0.5 baseline 只有 mean±std，没有 per-seed；用 mean 作为单条记录
    # LoRA-only
    "lora_only_s0":     {"group": "LoRA-only", "seed": 0, "tsr": 6.5,  "car": 54.5, "ee_disp": None, "frozen": 0.0},
    "lora_only_s1":     {"group": "LoRA-only", "seed": 1, "tsr": 6.0,  "car": 56.0, "ee_disp": None, "frozen": None},
    # SDF λ=0.005
    "sdf_0005_s0":      {"group": "SDF λ=0.005", "seed": 0, "tsr": 4.5, "car": 53.5, "ee_disp": None, "frozen": None},
    "sdf_0005_s1":      {"group": "SDF λ=0.005", "seed": 1, "tsr": 9.0, "car": 50.0, "ee_disp": None, "frozen": None},
    "sdf_0005_s2":      {"group": "SDF λ=0.005", "seed": 2, "tsr": 7.0, "car": 48.0, "ee_disp": None, "frozen": None},
    # SDF λ=0.01
    "sdf_001_s0":       {"group": "SDF λ=0.01", "seed": 0, "tsr": 8.0, "car": 50.0, "ee_disp": None, "frozen": None},
    "sdf_001_s1":       {"group": "SDF λ=0.01", "seed": 1, "tsr": 5.5, "car": 55.0, "ee_disp": None, "frozen": None},
    "sdf_001_s2":       {"group": "SDF λ=0.01", "seed": 2, "tsr": 5.0, "car": 54.0, "ee_disp": None, "frozen": None},
})

# Pi0.5 baseline 旧数据的 std（3-seed）
OLD_BASELINE_STD = {"tsr": 1.5, "car": 1.6}

# ============================================================
# 新数据（修复后 re-eval）— 手动填入或从 JSON 加载
# key 必须与 OLD_DATA 的 key 一致
# ============================================================
NEW_DATA = OrderedDict({
    "pi05_baseline_s0": {"group": "Pi0.5 baseline", "seed": 0, "tsr": 71.5, "car": 28.5, "ee_disp": 0.367, "frozen": 0.0, "note": "reeval"},
    "lora_only_s0":     {"group": "LoRA-only", "seed": 0, "tsr": 51.5, "car": 56.5, "ee_disp": 0.396, "frozen": 0.0},
    # --- 以下待填入 ---
    # "lora_only_s1":     {"group": "LoRA-only", "seed": 1, "tsr": ??, "car": ??, "ee_disp": ??, "frozen": ??},
    # "sdf_0005_s0":      {"group": "SDF λ=0.005", "seed": 0, "tsr": ??, "car": ??, "ee_disp": ??, "frozen": ??},
    # "sdf_0005_s1":      {"group": "SDF λ=0.005", "seed": 1, "tsr": ??, "car": ??, "ee_disp": ??, "frozen": ??},
    # "sdf_0005_s2":      {"group": "SDF λ=0.005", "seed": 2, "tsr": ??, "car": ??, "ee_disp": ??, "frozen": ??},
    # "sdf_001_s0":       {"group": "SDF λ=0.01", "seed": 0, "tsr": ??, "car": ??, "ee_disp": ??, "frozen": ??},
    # "sdf_001_s1":       {"group": "SDF λ=0.01", "seed": 1, "tsr": ??, "car": ??, "ee_disp": ??, "frozen": ??},
    # "sdf_001_s2":       {"group": "SDF λ=0.01", "seed": 2, "tsr": ??, "car": ??, "ee_disp": ??, "frozen": ??},
})

# ============================================================
# JSON 结果文件路径映射（key -> json path）
# 根据实际路径修改
# ============================================================
JSON_PATHS = {
    # "lora_only_s1": "/path/to/eval_result.json",
    # ...
}

METRICS = ["tsr", "car", "ee_disp", "frozen"]
METRIC_LABELS = {"tsr": "TSR (%)", "car": "CAR (%)", "ee_disp": "EE Disp (m)", "frozen": "Frozen (%)"}
GROUPS = ["Pi0.5 baseline", "LoRA-only", "SDF λ=0.005", "SDF λ=0.01"]


def load_json_results():
    """从 JSON 文件加载新数据，合并到 NEW_DATA。"""
    for key, path in JSON_PATHS.items():
        if not path or not os.path.exists(path):
            continue
        try:
            with open(path) as f:
                data = json.load(f)
            entry = {"group": OLD_DATA[key]["group"], "seed": OLD_DATA[key]["seed"]}
            for m in METRICS:
                if m in data:
                    entry[m] = data[m]
                elif m == "tsr" and "task_success_rate" in data:
                    entry["tsr"] = data["task_success_rate"] * 100 if data["task_success_rate"] <= 1 else data["task_success_rate"]
                elif m == "car" and "collision_avoidance_rate" in data:
                    entry["car"] = data["collision_avoidance_rate"] * 100 if data["collision_avoidance_rate"] <= 1 else data["collision_avoidance_rate"]
            NEW_DATA[key] = entry
        except Exception as e:
            print(f"[WARN] Failed to load {path}: {e}", file=sys.stderr)


def fmt(val, precision=1):
    if val is None:
        return "—"
    return f"{val:.{precision}f}"


def fmt_delta(old_val, new_val, precision=1):
    if old_val is None or new_val is None:
        return "—"
    d = new_val - old_val
    sign = "+" if d >= 0 else ""
    return f"{sign}{d:.{precision}f}"


def group_keys(group_name):
    return [k for k, v in OLD_DATA.items() if v["group"] == group_name]


def compute_group_stats(data_dict, keys, metric):
    vals = [data_dict[k][metric] for k in keys if k in data_dict and data_dict[k].get(metric) is not None]
    if not vals:
        return None, None
    return np.mean(vals), np.std(vals) if len(vals) > 1 else 0.0


# ============================================================
# Terminal output
# ============================================================
def print_terminal_table():
    header = f"{'Model':<22} {'Old TSR':>8} {'New TSR':>8} {'ΔTSR':>7} {'Old CAR':>8} {'New CAR':>8} {'ΔCAR':>7} {'New EE':>8} {'New Frz':>8}"
    sep = "—" * len(header)
    print("\n" + sep)
    print("  POST-REEVAL COMPARISON: Bug-fix前 vs Bug-fix后")
    print(sep)
    print(header)
    print("—" * len(header))

    for group in GROUPS:
        keys = group_keys(group)
        for k in keys:
            old = OLD_DATA[k]
            new = NEW_DATA.get(k)
            label = f"{old['group']} s{old['seed']}"
            if new:
                print(f"{label:<22} {fmt(old['tsr']):>8} {fmt(new['tsr']):>8} {fmt_delta(old['tsr'], new['tsr']):>7} "
                      f"{fmt(old['car']):>8} {fmt(new['car']):>8} {fmt_delta(old['car'], new['car']):>7} "
                      f"{fmt(new.get('ee_disp'), 3):>8} {fmt(new.get('frozen')):>8}")
            else:
                print(f"{label:<22} {fmt(old['tsr']):>8} {'pending':>8} {'—':>7} "
                      f"{fmt(old['car']):>8} {'pending':>8} {'—':>7} "
                      f"{'pending':>8} {'pending':>8}")

        # group mean±std
        if len(keys) > 1:
            old_tsr_m, old_tsr_s = compute_group_stats(OLD_DATA, keys, "tsr")
            new_tsr_m, new_tsr_s = compute_group_stats(NEW_DATA, keys, "tsr")
            old_car_m, old_car_s = compute_group_stats(OLD_DATA, keys, "car")
            new_car_m, new_car_s = compute_group_stats(NEW_DATA, keys, "car")

            old_tsr_str = f"{fmt(old_tsr_m)}±{fmt(old_tsr_s)}" if old_tsr_m is not None else "—"
            new_tsr_str = f"{fmt(new_tsr_m)}±{fmt(new_tsr_s)}" if new_tsr_m is not None else "pending"
            old_car_str = f"{fmt(old_car_m)}±{fmt(old_car_s)}" if old_car_m is not None else "—"
            new_car_str = f"{fmt(new_car_m)}±{fmt(new_car_s)}" if new_car_m is not None else "pending"
            delta_tsr_str = fmt_delta(old_tsr_m, new_tsr_m) if (old_tsr_m is not None and new_tsr_m is not None) else "—"
            delta_car_str = fmt_delta(old_car_m, new_car_m) if (old_car_m is not None and new_car_m is not None) else "—"

            print(f"  {'(mean±std)':<20} {old_tsr_str:>8} {new_tsr_str:>8} {delta_tsr_str:>7} "
                  f"{old_car_str:>8} {new_car_str:>8} {delta_car_str:>7}")
        print()

    # Summary stats
    print(sep)
    print("  DELTA SUMMARY (models with both old & new data)")
    print(sep)
    tsr_deltas = []
    car_deltas = []
    for k in OLD_DATA:
        if k in NEW_DATA:
            old, new = OLD_DATA[k], NEW_DATA[k]
            if old.get("tsr") is not None and new.get("tsr") is not None:
                tsr_deltas.append(new["tsr"] - old["tsr"])
            if old.get("car") is not None and new.get("car") is not None:
                car_deltas.append(new["car"] - old["car"])

    if tsr_deltas:
        print(f"  TSR Δ: mean={np.mean(tsr_deltas):+.1f} pp, min={min(tsr_deltas):+.1f}, max={max(tsr_deltas):+.1f}, n={len(tsr_deltas)}")
    if car_deltas:
        print(f"  CAR Δ: mean={np.mean(car_deltas):+.1f} pp, min={min(car_deltas):+.1f}, max={max(car_deltas):+.1f}, n={len(car_deltas)}")

    # Claim 3 analysis
    print()
    print(sep)
    print("  CLAIM 3 ANALYSIS")
    print(sep)
    analyze_claim3()
    print()


# ============================================================
# Claim 3 analysis
# ============================================================
def analyze_claim3():
    """
    Claim 3 核心结论:
    a) LoRA-only CAR ≈ SDF CAR (SDF adds no measurable benefit)
    b) TSR collapse 幅度
    c) SDF vs LoRA-only CAR 差异是否在 seed variance 内
    """
    lora_keys = group_keys("LoRA-only")
    sdf005_keys = group_keys("SDF λ=0.005")
    sdf001_keys = group_keys("SDF λ=0.01")
    sdf_keys = sdf005_keys + sdf001_keys
    baseline_keys = group_keys("Pi0.5 baseline")

    # Use NEW_DATA if available, else OLD_DATA
    def get_metric_vals(keys, metric, data):
        return [data[k][metric] for k in keys if k in data and data[k].get(metric) is not None]

    # --- New data analysis ---
    new_lora_car = get_metric_vals(lora_keys, "car", NEW_DATA)
    new_sdf_car = get_metric_vals(sdf_keys, "car", NEW_DATA)
    new_lora_tsr = get_metric_vals(lora_keys, "tsr", NEW_DATA)
    new_sdf_tsr = get_metric_vals(sdf_keys, "tsr", NEW_DATA)
    new_base_tsr = get_metric_vals(baseline_keys, "tsr", NEW_DATA)

    # Old data
    old_lora_car = get_metric_vals(lora_keys, "car", OLD_DATA)
    old_sdf_car = get_metric_vals(sdf_keys, "car", OLD_DATA)
    old_base_tsr = get_metric_vals(baseline_keys, "tsr", OLD_DATA)
    old_lora_tsr = get_metric_vals(lora_keys, "tsr", OLD_DATA)
    old_sdf_tsr = get_metric_vals(sdf_keys, "tsr", OLD_DATA)

    n_new = len(new_lora_car) + len(new_sdf_car)
    n_total = len(lora_keys) + len(sdf_keys)
    print(f"  Data available: {n_new}/{n_total} models have new eval results")

    if not new_lora_car and not new_sdf_car:
        print("  [INSUFFICIENT DATA] Need re-eval results to assess Claim 3.")
        return

    # (a) LoRA-only CAR vs SDF CAR
    print(f"\n  (a) LoRA-only CAR ≈ SDF CAR?")
    if new_lora_car:
        print(f"      LoRA-only CAR (new): {np.mean(new_lora_car):.1f} ± {np.std(new_lora_car):.1f} (n={len(new_lora_car)})")
    if new_sdf_car:
        print(f"      SDF CAR (new):       {np.mean(new_sdf_car):.1f} ± {np.std(new_sdf_car):.1f} (n={len(new_sdf_car)})")
    if new_lora_car and new_sdf_car:
        diff = abs(np.mean(new_lora_car) - np.mean(new_sdf_car))
        pooled_std = np.sqrt((np.var(new_lora_car) + np.var(new_sdf_car)) / 2) if (len(new_lora_car) > 1 or len(new_sdf_car) > 1) else float('nan')
        print(f"      |Δ CAR| = {diff:.1f} pp, pooled_std = {pooled_std:.1f}")
        if diff < 3.0:
            print(f"      → HOLDS: CAR difference ({diff:.1f} pp) is small")
        elif not np.isnan(pooled_std) and diff < 2 * pooled_std:
            print(f"      → LIKELY HOLDS: difference within 2σ of seed variance")
        else:
            print(f"      → NEEDS REVIEW: CAR gap ({diff:.1f} pp) may be meaningful")

    # (b) TSR collapse
    print(f"\n  (b) TSR collapse (fine-tuned vs baseline)?")
    if new_base_tsr and (new_lora_tsr or new_sdf_tsr):
        base_mean = np.mean(new_base_tsr)
        ft_tsr = new_lora_tsr + new_sdf_tsr
        ft_mean = np.mean(ft_tsr)
        drop = base_mean - ft_mean
        print(f"      Baseline TSR (new): {base_mean:.1f}")
        print(f"      Fine-tuned TSR (new): {ft_mean:.1f} ± {np.std(ft_tsr):.1f} (n={len(ft_tsr)})")
        print(f"      TSR drop: {drop:.1f} pp")
        if old_base_tsr and (old_lora_tsr or old_sdf_tsr):
            old_ft = old_lora_tsr + old_sdf_tsr
            old_drop = np.mean(old_base_tsr) - np.mean(old_ft)
            print(f"      Old TSR drop was: {old_drop:.1f} pp → New drop: {drop:.1f} pp")
    else:
        print("      [INSUFFICIENT DATA]")

    # (c) SDF vs LoRA-only TSR/CAR within seed variance
    print(f"\n  (c) SDF vs LoRA-only within seed variance?")
    for metric_name, lora_vals, sdf_vals in [("CAR", new_lora_car, new_sdf_car), ("TSR", new_lora_tsr, new_sdf_tsr)]:
        if lora_vals and sdf_vals:
            lm, sm = np.mean(lora_vals), np.mean(sdf_vals)
            diff = abs(lm - sm)
            combined = lora_vals + sdf_vals
            combined_std = np.std(combined)
            print(f"      {metric_name}: LoRA={lm:.1f}, SDF={sm:.1f}, |Δ|={diff:.1f}, combined_std={combined_std:.1f}")
            if diff < combined_std:
                print(f"        → Within 1σ seed variance")
            elif diff < 2 * combined_std:
                print(f"        → Within 2σ seed variance")
            else:
                print(f"        → Exceeds 2σ — potentially significant")


# ============================================================
# LaTeX table
# ============================================================
def generate_latex():
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Evaluation results before and after fixing the 180° image rotation bug in \texttt{eval\_safelibero.py}.}")
    lines.append(r"\label{tab:reeval_comparison}")
    lines.append(r"\resizebox{\textwidth}{!}{")
    lines.append(r"\begin{tabular}{l c c c c c c c}")
    lines.append(r"\toprule")
    lines.append(r"Model & \multicolumn{2}{c}{TSR (\%)} & $\Delta$TSR & \multicolumn{2}{c}{CAR (\%)} & $\Delta$CAR & EE Disp (m) \\")
    lines.append(r"\cmidrule(lr){2-3} \cmidrule(lr){5-6}")
    lines.append(r" & Before & After & (pp) & Before & After & (pp) & (After) \\")
    lines.append(r"\midrule")

    for gi, group in enumerate(GROUPS):
        keys = group_keys(group)
        if gi > 0:
            lines.append(r"\addlinespace")

        for k in keys:
            old = OLD_DATA[k]
            new = NEW_DATA.get(k)
            label = f"{old['group']} s{old['seed']}"
            label_tex = label.replace("λ", r"$\lambda$").replace("±", r"$\pm$")

            if new:
                dt = fmt_delta(old["tsr"], new["tsr"])
                dc = fmt_delta(old["car"], new["car"])
                ee = fmt(new.get("ee_disp"), 3)
                lines.append(f"{label_tex} & {fmt(old['tsr'])} & {fmt(new['tsr'])} & {dt} & {fmt(old['car'])} & {fmt(new['car'])} & {dc} & {ee} \\\\")
            else:
                lines.append(f"{label_tex} & {fmt(old['tsr'])} & — & — & {fmt(old['car'])} & — & — & — \\\\")

        # group mean
        if len(keys) > 1:
            old_tsr_m, old_tsr_s = compute_group_stats(OLD_DATA, keys, "tsr")
            new_tsr_m, new_tsr_s = compute_group_stats(NEW_DATA, keys, "tsr")
            old_car_m, old_car_s = compute_group_stats(OLD_DATA, keys, "car")
            new_car_m, new_car_s = compute_group_stats(NEW_DATA, keys, "car")

            old_tsr_str = f"{fmt(old_tsr_m)}$\\pm${fmt(old_tsr_s)}" if old_tsr_m is not None else "—"
            new_tsr_str = f"{fmt(new_tsr_m)}$\\pm${fmt(new_tsr_s)}" if new_tsr_m is not None else "—"
            old_car_str = f"{fmt(old_car_m)}$\\pm${fmt(old_car_s)}" if old_car_m is not None else "—"
            new_car_str = f"{fmt(new_car_m)}$\\pm${fmt(new_car_s)}" if new_car_m is not None else "—"
            dt = fmt_delta(old_tsr_m, new_tsr_m) if (old_tsr_m is not None and new_tsr_m is not None) else "—"
            dc = fmt_delta(old_car_m, new_car_m) if (old_car_m is not None and new_car_m is not None) else "—"

            group_tex = group.replace("λ", r"$\lambda$")
            lines.append(f"\\rowcolor{{gray!15}} \\textit{{{group_tex} mean}} & {old_tsr_str} & {new_tsr_str} & {dt} & {old_car_str} & {new_car_str} & {dc} & \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}}")
    lines.append(r"\end{table}")

    tex_content = "\n".join(lines)
    out_path = OUTPUT_DIR / "reeval_comparison.tex"
    with open(out_path, "w") as f:
        f.write(tex_content)
    print(f"LaTeX table saved to {out_path}")
    return tex_content


# ============================================================
# JSON summary
# ============================================================
def generate_json_summary():
    summary = {
        "description": "Post-reeval comparison: 180° rotation bug fix",
        "old_data": {k: {m: v.get(m) for m in METRICS} for k, v in OLD_DATA.items()},
        "new_data": {k: {m: v.get(m) for m in METRICS} for k, v in NEW_DATA.items()},
        "deltas": {},
        "group_stats": {},
        "claim3": {},
    }

    # Per-model deltas
    for k in OLD_DATA:
        if k in NEW_DATA:
            old, new = OLD_DATA[k], NEW_DATA[k]
            d = {}
            for m in METRICS:
                if old.get(m) is not None and new.get(m) is not None:
                    d[m] = round(new[m] - old[m], 3)
            summary["deltas"][k] = d

    # Group stats
    for group in GROUPS:
        keys = group_keys(group)
        gs = {}
        for data_name, data_dict in [("old", OLD_DATA), ("new", NEW_DATA)]:
            for m in ["tsr", "car"]:
                mean, std = compute_group_stats(data_dict, keys, m)
                if mean is not None:
                    gs[f"{data_name}_{m}_mean"] = round(mean, 2)
                    gs[f"{data_name}_{m}_std"] = round(std, 2)
        summary["group_stats"][group] = gs

    # Claim 3 assessment
    lora_keys = group_keys("LoRA-only")
    sdf_keys = group_keys("SDF λ=0.005") + group_keys("SDF λ=0.01")
    new_lora_car = [NEW_DATA[k]["car"] for k in lora_keys if k in NEW_DATA and NEW_DATA[k].get("car") is not None]
    new_sdf_car = [NEW_DATA[k]["car"] for k in sdf_keys if k in NEW_DATA and NEW_DATA[k].get("car") is not None]

    claim3 = {"data_complete": len(new_lora_car) + len(new_sdf_car) == len(lora_keys) + len(sdf_keys)}
    if new_lora_car and new_sdf_car:
        claim3["lora_car_mean"] = round(np.mean(new_lora_car), 2)
        claim3["sdf_car_mean"] = round(np.mean(new_sdf_car), 2)
        claim3["car_gap_pp"] = round(abs(np.mean(new_lora_car) - np.mean(new_sdf_car)), 2)
    summary["claim3"] = claim3

    # Completion status
    summary["completion"] = {
        "total_models": len(OLD_DATA),
        "reeval_done": len(NEW_DATA),
        "pending": [k for k in OLD_DATA if k not in NEW_DATA],
    }

    out_path = OUTPUT_DIR / "reeval_comparison.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"JSON summary saved to {out_path}")
    return summary


# ============================================================
# Main
# ============================================================
def main():
    load_json_results()

    print_terminal_table()
    generate_latex()
    generate_json_summary()

    n_done = len(NEW_DATA)
    n_total = len(OLD_DATA)
    print(f"\nCompletion: {n_done}/{n_total} models re-evaluated")
    if n_done < n_total:
        pending = [k for k in OLD_DATA if k not in NEW_DATA]
        print(f"Pending: {', '.join(pending)}")


if __name__ == "__main__":
    main()
