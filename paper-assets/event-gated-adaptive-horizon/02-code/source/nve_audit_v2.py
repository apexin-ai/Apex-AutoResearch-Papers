#!/usr/bin/env python3
"""NVE Audit v2: Full cross-check with raw ve_ratio."""

import json
import os
import sys

LOGDIR = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir"
OUTPUT = "/root/autodl-tmp/event-gated-adaptive-horizon/nve_audit_results.txt"
WINDOW_START = 35000

WALKER_BASELINE_DIR = "baseline_s1"
CHEETAH_BASELINE_A = "exp_023a_cheetah_baseline_s0"
CHEETAH_BASELINE_B = "exp_023b_cheetah_baseline_s1"

EXPERIMENTS = [
    ("008d_s1",       ["exp_008d_civo_trigger_s1"], 4.12, "walker", None),
    ("008d_s3",       ["exp_008d_civo_trigger_s3"], 1.53, "walker", None),
    ("008d_s4",       ["exp_008d_civo_trigger_s4"], 3.03, "walker", "Reviewer=4.62x"),
    ("009b",          ["exp_009b_008d_walker_s2"], 1.62, "walker", None),
    ("008a_orig",     ["exp_008a_fixed_dt2_no_subsample"], 0.93, "walker", None),
    ("008a_s1",       ["exp_008a_unexposed_s1"], 0.43, "walker", "Reviewer=0.83x"),
    ("008a_s2",       ["exp_008a_unexposed_s2"], 0.51, "walker", None),
    ("008e_v3_s1",    ["exp_008e_v3_walker_s1"], 0.94, "walker", None),
    ("008e_v3_s2",    ["exp_008e_v3_walker_s2"], 3.78, "walker", None),
    ("008e_v3_s3",    ["exp_008e_v3_s3"], 4.02, "walker", None),
    ("008e_v3_s4",    ["exp_008e_v3_s4"], 0.99, "walker", None),
    ("008f",          ["exp_008f_no_dt_embed_subsample_on_h8"], 0.97, "walker", None),
    ("015b",          ["exp_015b_frozen_dt_emb"], 1.45, "walker", "paper_final=0.55x"),
    ("006",           ["exp_006_variable_dt"], 4.83, "walker", None),
    ("009c",          ["exp_009c_008f_walker_s2"], 1.14, "walker", None),
    ("009c_s3",       ["exp_009c_no_dt_emb_s3"], 0.52, "walker", None),
    ("008f_s3",       ["exp_008f_s3_no_dt_embed_walker"], None, "walker", None),
    ("010b",          ["exp_010b_cheetah_civo_trigger"], 8.27, "cheetah", None),
    ("010b_s0",       ["exp_010b_cheetah_civo_trigger_s0"], 70.64, "cheetah", None),
    ("008a_ch_s0",    ["exp_008a_cheetah_unexposed_s0"], 0.49, "cheetah", None),
    ("008a_ch_s1",    ["exp_008a_cheetah_unexposed_s1"], 0.48, "cheetah", None),
]


def read_metrics(path):
    data = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            step = rec.get("step")
            if step is not None:
                if step not in data:
                    data[step] = {}
                data[step].update(rec)
    return data


def get_ve_ratio_series(metrics):
    series = {}
    for step, rec in metrics.items():
        ve = rec.get("civo/ve_ratio")
        if ve is None:
            val = rec.get("value_mean") or rec.get("agent/value_mean")
            ev = rec.get("eval_return") or rec.get("eval/return")
            if val is not None and ev is not None and ev != 0:
                ve = val / ev
        if ve is not None:
            series[step] = ve
    return series


def compute_nve(config_ve, baseline_ve, window_start=WINDOW_START):
    nve_series = {}
    for step in sorted(config_ve.keys()):
        if step >= window_start and step in baseline_ve:
            bve = baseline_ve[step]
            if bve != 0:
                nve_series[step] = config_ve[step] / bve
    if not nve_series:
        return None, None, nve_series
    peak_step = max(nve_series, key=nve_series.get)
    return nve_series[peak_step], peak_step, nve_series


def find_dir(candidates, available):
    for c in candidates:
        if c in available:
            return c
    return None


def fmt(v, width=12, decimals=6):
    if v is None:
        return f"{'N/A':>{width}}"
    if isinstance(v, float):
        return f"{v:>{width}.{decimals}f}"
    return f"{v:>{width}}"


def main():
    out = []
    def log(s=""):
        print(s)
        out.append(s)

    available = set(os.listdir(LOGDIR))

    # Walker baseline
    log("=== Walker Baseline: %s ===" % WALKER_BASELINE_DIR)
    log("NOTE: exp_001_baseline not found. baseline_s1 = exp_009d_baseline_walker_s1 (identical ve_ratio values).")
    walker_bl_m = read_metrics(os.path.join(LOGDIR, WALKER_BASELINE_DIR, "metrics.jsonl"))
    walker_bl_ve = get_ve_ratio_series(walker_bl_m)

    key_steps = [35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000]
    log("")
    log("Walker baseline ve_ratio:")
    for s in key_steps:
        v = walker_bl_ve.get(s)
        log("  %7d: %s" % (s, ("%.6f" % v) if v is not None else "N/A"))

    # Cheetah baselines
    ch_a_ve = get_ve_ratio_series(read_metrics(os.path.join(LOGDIR, CHEETAH_BASELINE_A, "metrics.jsonl")))
    ch_b_ve = get_ve_ratio_series(read_metrics(os.path.join(LOGDIR, CHEETAH_BASELINE_B, "metrics.jsonl")))
    cheetah_bl_ve = {}
    for s in set(ch_a_ve) | set(ch_b_ve):
        vals = []
        if s in ch_a_ve: vals.append(ch_a_ve[s])
        if s in ch_b_ve: vals.append(ch_b_ve[s])
        cheetah_bl_ve[s] = sum(vals) / len(vals)

    log("")
    log("Cheetah baseline (avg 023a+023b) ve_ratio:")
    for s in key_steps:
        v = cheetah_bl_ve.get(s)
        a = ch_a_ve.get(s)
        b = ch_b_ve.get(s)
        if v is not None:
            log("  %7d: avg=%.6f  (023a=%.6f, 023b=%.6f)" % (s, v, a, b))
        else:
            log("  %7d: N/A" % s)

    # Main table
    log("")
    log("=" * 180)
    log("%-14s %-48s %7s %10s %8s %10s %10s %20s %s" % (
        "exp_id", "logdir", "paper", "peakNVE", "pk_step", "nve105K", "ve105K", "paper_matches", "note"))
    log("-" * 180)

    for label, candidates, paper_nve, domain, note in EXPERIMENTS:
        actual_dir = find_dir(candidates, available)
        if actual_dir is None:
            pstr = "%.2f" % paper_nve if paper_nve is not None else "N/A"
            log("%-14s %-48s %7s %10s %8s %10s %10s %20s tried:%s" % (
                label, "NOT FOUND", pstr, "---", "---", "---", "---", "---", str(candidates)))
            continue

        mpath = os.path.join(LOGDIR, actual_dir, "metrics.jsonl")
        if not os.path.exists(mpath):
            continue

        metrics = read_metrics(mpath)
        config_ve = get_ve_ratio_series(metrics)
        if not config_ve:
            continue

        baseline_ve = walker_bl_ve if domain == "walker" else cheetah_bl_ve
        peak_nve, peak_step, nve_series = compute_nve(config_ve, baseline_ve)

        nve_105k = nve_series.get(105000)
        ve_105k = config_ve.get(105000)

        # Determine what the paper value most likely is
        paper_is = "???"
        if paper_nve is not None:
            matches = []
            if peak_nve is not None and abs(peak_nve - paper_nve) / max(abs(paper_nve), 1e-6) < 0.02:
                matches.append("peakNVE")
            if nve_105k is not None and abs(nve_105k - paper_nve) / max(abs(paper_nve), 1e-6) < 0.02:
                matches.append("nve@105K")
            if ve_105k is not None and abs(ve_105k - paper_nve) / max(abs(paper_nve), 1e-6) < 0.02:
                matches.append("ve@105K")
            # Check raw ve_ratio at other steps
            for ss, ve_s in sorted(config_ve.items()):
                if ss >= WINDOW_START and abs(ve_s - paper_nve) / max(abs(paper_nve), 1e-6) < 0.02:
                    tag = "ve@%d" % ss
                    if tag not in matches:
                        matches.append(tag)
            # Check NVE at other steps (not already covered)
            for ss, nve_s in sorted(nve_series.items()):
                if abs(nve_s - paper_nve) / max(abs(paper_nve), 1e-6) < 0.02:
                    tag = "nve@%d" % ss
                    if tag not in matches and "peakNVE" not in matches:
                        matches.append(tag)
            paper_is = ",".join(matches) if matches else "MISMATCH"

        pstr = "%.2f" % paper_nve if paper_nve is not None else "N/A"
        pkstr = "%.4f" % peak_nve if peak_nve is not None else "---"
        psstr = str(peak_step) if peak_step is not None else "---"
        n105 = "%.4f" % nve_105k if nve_105k is not None else "---"
        v105 = "%.4f" % ve_105k if ve_105k is not None else "---"
        nstr = note if note else ""

        log("%-14s %-48s %7s %10s %8s %10s %10s %20s %s" % (
            label, actual_dir, pstr, pkstr, psstr, n105, v105, paper_is, nstr))

        # Special: 015b
        if label == "015b" and nve_series:
            last_step = max(nve_series.keys())
            log("  >> 015b final: step=%d, NVE=%.4f, ve_ratio=%.6f" % (
                last_step, nve_series[last_step], config_ve.get(last_step, 0)))

        # Special: 008e_v3_s2
        if label == "008e_v3_s2":
            er = metrics.get(105000, {}).get("eval_return")
            vm = metrics.get(105000, {}).get("value_mean")
            log("  >> eval_return@105K=%.4f, value_mean@105K=%.4f" % (er or 0, vm or 0))

    # Detailed per-step for DIFF experiments
    log("")
    log("")
    log("=== Per-step detail for experiments with discrepancies ===")
    detail_labels = ["008d_s1", "008d_s4", "008a_s1", "008a_s2", "009c_s3",
                     "010b_s0", "008a_ch_s0", "008a_ch_s1"]
    for label, candidates, paper_nve, domain, note in EXPERIMENTS:
        if label not in detail_labels:
            continue
        actual_dir = find_dir(candidates, available)
        if actual_dir is None:
            continue
        mpath = os.path.join(LOGDIR, actual_dir, "metrics.jsonl")
        if not os.path.exists(mpath):
            continue
        metrics = read_metrics(mpath)
        config_ve = get_ve_ratio_series(metrics)
        baseline_ve = walker_bl_ve if domain == "walker" else cheetah_bl_ve
        _, _, nve_series = compute_nve(config_ve, baseline_ve, window_start=0)
        log("")
        log("--- %s (%s) paper=%.2f ---" % (label, actual_dir, paper_nve if paper_nve else 0))
        log("  %7s %12s %12s %12s %12s %12s" % ("step", "cfg_ve", "bl_ve", "NVE", "eval_ret", "val_mean"))
        for step in sorted(config_ve.keys()):
            if step >= 35000:
                cve = config_ve.get(step)
                bve = baseline_ve.get(step)
                nve = nve_series.get(step)
                er = metrics.get(step, {}).get("eval_return")
                vm = metrics.get(step, {}).get("value_mean")
                parts = ["  %7d" % step]
                parts.append("%12.6f" % cve if cve is not None else "%12s" % "N/A")
                parts.append("%12.6f" % bve if bve is not None else "%12s" % "N/A")
                parts.append("%12.6f" % nve if nve is not None else "%12s" % "N/A")
                parts.append("%12.4f" % er if er is not None else "%12s" % "N/A")
                parts.append("%12.4f" % vm if vm is not None else "%12s" % "N/A")
                log(" ".join(parts))

    # Walker baseline cross-reference
    log("")
    log("")
    log("=== All Walker baselines for cross-reference ===")
    bl_names = ["baseline_s1", "exp_001_baseline_s2", "exp_009a_baseline_walker_s2",
                "exp_009d_baseline_walker_s0", "exp_009d_baseline_walker_s1"]
    header_parts = ["  %7s" % "step"]
    for bn in bl_names:
        header_parts.append("%20s" % bn[:20])
    log(" ".join(header_parts))

    # Pre-load all baselines
    bl_data = {}
    for bn in bl_names:
        if bn in available:
            try:
                m = read_metrics(os.path.join(LOGDIR, bn, "metrics.jsonl"))
                bl_data[bn] = get_ve_ratio_series(m)
            except Exception:
                bl_data[bn] = {}
        else:
            bl_data[bn] = None

    for s in key_steps:
        parts = ["  %7d" % s]
        for bn in bl_names:
            ve = bl_data.get(bn)
            if ve is None:
                parts.append("%20s" % "NOT_FOUND")
            else:
                v = ve.get(s)
                if v is not None:
                    parts.append("%20.6f" % v)
                else:
                    parts.append("%20s" % "N/A")
        log(" ".join(parts))

    with open(OUTPUT, "w") as f:
        f.write("\n".join(out))
    log("")
    log("Results written to %s" % OUTPUT)


if __name__ == "__main__":
    main()
