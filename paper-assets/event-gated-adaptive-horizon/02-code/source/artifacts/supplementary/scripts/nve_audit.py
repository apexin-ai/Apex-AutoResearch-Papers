#!/usr/bin/env python3
"""NVE Audit: Systematic recalculation of all NVE values cited in paper."""

import json
import os
import sys

LOGDIR = "/root/autodl-tmp/event-gated-adaptive-horizon/logdir"
OUTPUT = "/root/autodl-tmp/event-gated-adaptive-horizon/nve_audit_results.txt"
WINDOW_START = 35000

# Walker baseline candidates (in priority order)
# User specified exp_001_baseline (seed=0), but it doesn't exist.
# baseline_s1 has matching step grid (35K, 45K, ...) and full data (505K steps).
WALKER_BASELINE_CANDIDATES = ["exp_001_baseline", "baseline_s1", "exp_009d_baseline_walker_s0"]

CHEETAH_BASELINE_A = "exp_023a_cheetah_baseline_s0"
CHEETAH_BASELINE_B = "exp_023b_cheetah_baseline_s1"

# (label, candidate_dirs, paper_nve, domain, note)
EXPERIMENTS = [
    ("008d_s1",       ["exp_008d_trained_embed", "exp_008d_civo_trigger_s1"], 4.12, "walker", None),
    ("008d_s3",       ["exp_008d_trained_embed_s3", "exp_008d_civo_trigger_s3"], 1.53, "walker", None),
    ("008d_s4",       ["exp_008d_trained_embed_s4", "exp_008d_civo_trigger_s4"], 3.03, "walker", "Reviewer=4.62x"),
    ("009b",          ["exp_009b_frozen_embed", "exp_009b_008d_walker_s2"], 1.62, "walker", None),
    ("008a_orig",     ["exp_008a_no_subsample_dt2", "exp_008a_fixed_dt2_no_subsample"], 0.93, "walker", None),
    ("008a_s1",       ["exp_008a_no_subsample_s1", "exp_008a_unexposed_s1"], 0.43, "walker", "Reviewer=0.83x"),
    ("008a_s2",       ["exp_008a_no_subsample_s2", "exp_008a_unexposed_s2"], 0.51, "walker", None),
    ("008e_v3_s1",    ["exp_008e_v3_s1", "exp_008e_v3_walker_s1"], 0.94, "walker", None),
    ("008e_v3_s2",    ["exp_008e_v3_s2", "exp_008e_v3_walker_s2"], 3.78, "walker", None),
    ("008e_v3_s3",    ["exp_008e_v3_s3"], 4.02, "walker", None),
    ("008e_v3_s4",    ["exp_008e_v3_s4"], 0.99, "walker", None),
    ("008f",          ["exp_008f_no_dt_embed_subsample_on_h8"], 0.97, "walker", None),
    ("015b",          ["exp_015b_reward_sgs", "exp_015b_frozen_dt_emb"], 1.45, "walker", "paper_final=0.55x"),
    ("006",           ["exp_006_variable_dt", "fixed_dt4_v1_s1", "fixed_dt4_v2_s1"], 4.83, "walker", None),
    ("009c",          ["exp_009c_008f_walker_s2"], 1.14, "walker", None),
    ("009c_s3",       ["exp_009c_no_dt_emb_s3"], 0.52, "walker", None),
    ("008f_s3",       ["exp_008f_no_dt_emb_s3", "exp_008f_s3_no_dt_embed_walker"], None, "walker", None),
    # Cheetah
    ("010b",          ["exp_010b_cheetah_trigger", "exp_010b_cheetah_civo_trigger"], 8.27, "cheetah", None),
    ("010b_s0",       ["exp_010b_cheetah_trigger_s0", "exp_010b_cheetah_civo_trigger_s0"], 70.64, "cheetah", None),
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
            step = rec.get('step')
            if step is not None:
                if step not in data:
                    data[step] = {}
                data[step].update(rec)
    return data


def get_ve_ratio_series(metrics):
    series = {}
    for step, rec in metrics.items():
        ve = rec.get('civo/ve_ratio')
        if ve is None:
            val = rec.get('value_mean')
            if val is None:
                val = rec.get('agent/value_mean')
            ev = rec.get('eval_return')
            if ev is None:
                ev = rec.get('eval/return')
            if val is not None and ev is not None and ev != 0:
                ve = val / ev
        if ve is not None:
            series[step] = ve
    return series


def nearest_step(target, steps_set, tol=3000):
    """Find nearest step within tolerance."""
    best = None
    best_dist = tol + 1
    for s in steps_set:
        d = abs(s - target)
        if d < best_dist:
            best_dist = d
            best = s
    return best if best_dist <= tol else None


def compute_nve(config_ve, baseline_ve, window_start=WINDOW_START, use_nearest=False):
    """Compute NVE series. If use_nearest, do nearest-step matching."""
    nve_series = {}
    bl_steps = set(baseline_ve.keys())
    for step in sorted(config_ve.keys()):
        if step < window_start:
            continue
        bl_step = step
        if step not in baseline_ve and use_nearest:
            bl_step = nearest_step(step, bl_steps)
        if bl_step is not None and bl_step in baseline_ve:
            bve = baseline_ve[bl_step]
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


def main():
    out = []
    def log(s=""):
        print(s)
        out.append(s)

    available = set(os.listdir(LOGDIR))

    # ====== Walker Baseline ======
    walker_bl_dir = find_dir(WALKER_BASELINE_CANDIDATES, available)
    if walker_bl_dir is None:
        log("ERROR: No Walker baseline found!")
        sys.exit(1)

    log(f"=== Walker Baseline: {walker_bl_dir} ===")
    log(f"NOTE: User specified exp_001_baseline (not found). Using {walker_bl_dir} instead.")
    walker_bl_m = read_metrics(os.path.join(LOGDIR, walker_bl_dir, "metrics.jsonl"))
    walker_bl_ve = get_ve_ratio_series(walker_bl_m)

    # Check step alignment
    sample_exp_ve_steps = {5000, 15000, 25000, 35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000}
    bl_steps = set(walker_bl_ve.keys())
    aligned = sample_exp_ve_steps.issubset(bl_steps)
    log(f"  Step grid aligned with experiments: {aligned}")
    if not aligned:
        log(f"  Baseline steps (first 15): {sorted(bl_steps)[:15]}")
        log(f"  Will use nearest-step matching (tol=3000)")
    use_nearest_walker = not aligned

    key_steps = [35000, 45000, 55000, 65000, 75000, 85000, 95000, 105000]
    log("\nWalker baseline ve_ratio @ key steps:")
    for s in key_steps:
        v = walker_bl_ve.get(s)
        if v is not None:
            log(f"  step {s:>7d}: {v:.6f}")
        else:
            ns = nearest_step(s, bl_steps)
            nv = walker_bl_ve.get(ns) if ns else None
            if nv is not None:
                log(f"  step {s:>7d}: N/A (nearest {ns}: {nv:.6f})")
            else:
                log(f"  step {s:>7d}: N/A")

    # Also try exp_009d_baseline_walker_s0 for comparison
    log("\n--- Also checking exp_009d_baseline_walker_s0 for reference ---")
    if "exp_009d_baseline_walker_s0" in available:
        s0_m = read_metrics(os.path.join(LOGDIR, "exp_009d_baseline_walker_s0", "metrics.jsonl"))
        s0_ve = get_ve_ratio_series(s0_m)
        for s in key_steps:
            v = s0_ve.get(s)
            ns = nearest_step(s, set(s0_ve.keys()))
            nv = s0_ve.get(ns) if ns else None
            if v is not None:
                log(f"  step {s:>7d}: {v:.6f}")
            elif nv is not None:
                log(f"  step {s:>7d}: N/A (nearest {ns}: {nv:.6f})")
            else:
                log(f"  step {s:>7d}: N/A")

    # ====== Cheetah Baselines ======
    log(f"\n=== Cheetah Baselines: {CHEETAH_BASELINE_A} + {CHEETAH_BASELINE_B} (avg) ===")
    ch_a_m = read_metrics(os.path.join(LOGDIR, CHEETAH_BASELINE_A, "metrics.jsonl"))
    ch_b_m = read_metrics(os.path.join(LOGDIR, CHEETAH_BASELINE_B, "metrics.jsonl"))
    ch_a_ve = get_ve_ratio_series(ch_a_m)
    ch_b_ve = get_ve_ratio_series(ch_b_m)

    cheetah_bl_ve = {}
    for s in set(ch_a_ve) | set(ch_b_ve):
        vals = []
        if s in ch_a_ve: vals.append(ch_a_ve[s])
        if s in ch_b_ve: vals.append(ch_b_ve[s])
        cheetah_bl_ve[s] = sum(vals) / len(vals)

    log("\nCheetah baseline (avg) ve_ratio @ key steps:")
    for s in key_steps:
        avg = cheetah_bl_ve.get(s)
        a = ch_a_ve.get(s)
        b = ch_b_ve.get(s)
        avg_s = f"{avg:.6f}" if avg is not None else "N/A"
        a_s = f"{a:.6f}" if a is not None else "N/A"
        b_s = f"{b:.6f}" if b is not None else "N/A"
        log(f"  step {s:>7d}: avg={avg_s}  (023a={a_s}, 023b={b_s})")

    # ====== NVE Table ======
    log("\n" + "=" * 150)
    header = f"{'exp_id':<16} {'logdir':<48} {'paper':>8} {'recalc':>12} {'peak_step':>10} {'nve@105K':>12} {'match':>6} {'note'}"
    log(header)
    log("-" * 150)

    for label, candidates, paper_nve, domain, note in EXPERIMENTS:
        actual_dir = find_dir(candidates, available)
        if actual_dir is None:
            pstr = f"{paper_nve:.2f}x" if paper_nve is not None else "N/A"
            log(f"{label:<16} {'NOT FOUND':<48} {pstr:>8} {'---':>12} {'---':>10} {'---':>12} {'---':>6} tried:{candidates}")
            continue

        mpath = os.path.join(LOGDIR, actual_dir, "metrics.jsonl")
        if not os.path.exists(mpath):
            pstr = f"{paper_nve:.2f}x" if paper_nve is not None else "N/A"
            log(f"{label:<16} {actual_dir:<48} {pstr:>8} {'NO FILE':>12} {'---':>10} {'---':>12} {'---':>6}")
            continue

        metrics = read_metrics(mpath)
        config_ve = get_ve_ratio_series(metrics)

        if not config_ve:
            pstr = f"{paper_nve:.2f}x" if paper_nve is not None else "N/A"
            log(f"{label:<16} {actual_dir:<48} {pstr:>8} {'NO VE':>12} {'---':>10} {'---':>12} {'---':>6}")
            continue

        baseline_ve = walker_bl_ve if domain == "walker" else cheetah_bl_ve
        use_near = use_nearest_walker if domain == "walker" else False
        peak_nve, peak_step, nve_series = compute_nve(config_ve, baseline_ve, use_nearest=use_near)

        nve_105k = nve_series.get(105000)

        if paper_nve is not None and peak_nve is not None:
            rel_err = abs(peak_nve - paper_nve) / max(abs(paper_nve), 1e-6)
            match = "OK" if rel_err < 0.10 else "DIFF"
        else:
            match = "N/A"

        pstr = f"{paper_nve:.2f}x" if paper_nve is not None else "N/A"
        rstr = f"{peak_nve:.4f}x" if peak_nve is not None else "---"
        sstr = f"{peak_step}" if peak_step is not None else "---"
        n105 = f"{nve_105k:.4f}x" if nve_105k is not None else "---"
        nstr = note if note else ""

        log(f"{label:<16} {actual_dir:<48} {pstr:>8} {rstr:>12} {sstr:>10} {n105:>12} {match:>6} {nstr}")

        # Special: 015b final NVE
        if label == "015b" and nve_series:
            last_step = max(nve_series.keys())
            final_nve = nve_series[last_step]
            n105_v = nve_series.get(105000)
            log(f"  >> 015b final NVE: step={last_step}, nve={final_nve:.4f}")
            if n105_v is not None:
                log(f"  >> 015b NVE@105K: {n105_v:.4f}")
            # Also show ve_ratio raw values
            log(f"  >> 015b config ve_ratio@105K: {config_ve.get(105000, 'N/A')}")
            log(f"  >> 015b baseline ve_ratio@105K: {baseline_ve.get(105000, 'N/A')}")

        # Special: 008e_v3_s2 eval_return@105K
        if label == "008e_v3_s2":
            er = metrics.get(105000, {}).get('eval_return')
            vm = metrics.get(105000, {}).get('value_mean')
            log(f"  >> 008e_v3_s2 eval_return@105K: {er}")
            log(f"  >> 008e_v3_s2 value_mean@105K: {vm}")
            log(f"  >> 008e_v3_s2 ve_ratio@105K: {config_ve.get(105000, 'N/A')}")

    # ====== Detailed NVE series for key experiments ======
    log("\n\n=== Detailed NVE series (steps >= 35K) for select experiments ===")
    detail_labels = ["008d_s1", "008d_s4", "008a_s1", "008e_v3_s2", "010b_s0", "015b", "008e_v3_s3"]
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
        use_near = use_nearest_walker if domain == "walker" else False
        _, _, nve_series = compute_nve(config_ve, baseline_ve, window_start=0, use_nearest=use_near)
        log(f"\n--- {label} ({actual_dir}) paper={paper_nve} ---")
        for step in sorted(nve_series.keys()):
            if step >= 35000:
                cve = config_ve.get(step)
                bve = baseline_ve.get(step)
                cve_s = f"{cve:.6f}" if cve is not None else "N/A"
                bve_s = f"{bve:.6f}" if bve is not None else "N/A"
                log(f"  step {step:>7d}: NVE={nve_series[step]:.4f}  cfg_ve={cve_s}  bl_ve={bve_s}")

    # ====== Summary of all available Walker baselines ======
    log("\n\n=== All Walker baseline ve_ratios for cross-check ===")
    bl_names = ["baseline_s1", "exp_001_baseline_s2", "exp_009a_baseline_walker_s2",
                "exp_009d_baseline_walker_s0", "exp_009d_baseline_walker_s1"]
    for bn in bl_names:
        if bn not in available:
            log(f"\n{bn}: NOT FOUND")
            continue
        try:
            m = read_metrics(os.path.join(LOGDIR, bn, "metrics.jsonl"))
            ve = get_ve_ratio_series(m)
            log(f"\n{bn} (total steps with ve: {len(ve)}, max step: {max(ve) if ve else 0}):")
            for s in key_steps:
                v = ve.get(s)
                if v is not None:
                    log(f"  step {s:>7d}: {v:.6f}")
                else:
                    ns = nearest_step(s, set(ve.keys()))
                    nv = ve.get(ns) if ns else None
                    if nv is not None:
                        log(f"  step {s:>7d}: N/A (nearest {ns}: {nv:.6f})")
                    else:
                        log(f"  step {s:>7d}: N/A")
        except Exception as e:
            log(f"\n{bn}: ERROR {e}")

    # Write output
    with open(OUTPUT, 'w') as f:
        f.write('\n'.join(out))
    log(f"\n\nResults written to {OUTPUT}")


if __name__ == "__main__":
    main()
