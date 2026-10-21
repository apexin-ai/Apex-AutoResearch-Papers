# Kill gate judgment for DeiT 50-epoch experiments (Muon vs AdamW)
import argparse
import re
import os
import sys


MUON_20EP_BASELINE = 62.94  # Muon 20ep best_val_acc reference


def parse_log(path):
    """Parse training log, return list of (epoch, val_acc) tuples."""
    if not os.path.exists(path):
        print(f"WARNING: log file not found: {path}")
        return []
    with open(path) as f:
        text = f.read()
    if not text.strip():
        print(f"WARNING: log file is empty (training may not have started): {path}")
        return []
    results = []
    for m in re.finditer(r'epoch=(\d+),.*?val_acc=([\d.]+)%', text):
        results.append((int(m.group(1)), float(m.group(2))))
    if not results:
        print(f"WARNING: no epoch data found in {path}")
    return results


def make_table(muon_data, adamw_data):
    """Print per-epoch val_acc comparison table."""
    muon_dict = dict(muon_data)
    adamw_dict = dict(adamw_data)
    all_eps = sorted(set(muon_dict) | set(adamw_dict))
    print(f"\n{'Epoch':>5}  {'Muon':>8}  {'AdamW':>8}  {'Gap':>8}")
    print("-" * 35)
    for ep in all_eps:
        m = muon_dict.get(ep)
        a = adamw_dict.get(ep)
        m_s = f"{m:.2f}%" if m is not None else "   -   "
        a_s = f"{a:.2f}%" if a is not None else "   -   "
        if m is not None and a is not None:
            g_s = f"{m - a:+.2f}pp"
        else:
            g_s = "   -   "
        print(f"{ep:>5}  {m_s:>8}  {a_s:>8}  {g_s:>8}")


def kill_gate(muon_best, adamw_best):
    """Return kill gate verdict string."""
    gap = muon_best - adamw_best
    if gap < 5:
        return "Artifact", gap
    elif gap < 10:
        return "Partial", gap
    else:
        return "Real", gap


def convergence_trajectory(muon_data, adamw_data):
    """Print gap at milestone epochs and trend."""
    muon_dict = dict(muon_data)
    adamw_dict = dict(adamw_data)
    milestones = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    print(f"\n{'Epoch':>5}  {'Muon':>8}  {'AdamW':>8}  {'Gap':>8}")
    print("-" * 35)
    gaps = []
    for ep in milestones:
        m = muon_dict.get(ep)
        a = adamw_dict.get(ep)
        m_s = f"{m:.2f}%" if m is not None else "   -   "
        a_s = f"{a:.2f}%" if a is not None else "   -   "
        if m is not None and a is not None:
            g = m - a
            g_s = f"{g:+.2f}pp"
            gaps.append((ep, g))
        else:
            g_s = "   -   "
        print(f"{ep:>5}  {m_s:>8}  {a_s:>8}  {g_s:>8}")

    if len(gaps) >= 2:
        first_g = gaps[0][1]
        last_g = gaps[-1][1]
        diff = last_g - first_g
        if diff > 2:
            trend = "EXPANDING (Muon pulling ahead)"
        elif diff < -2:
            trend = "NARROWING (AdamW catching up)"
        else:
            trend = "STABLE"
        print(f"\nTrend: {trend}  (ep{gaps[0][0]} gap={gaps[0][1]:+.2f}pp -> ep{gaps[-1][0]} gap={gaps[-1][1]:+.2f}pp, delta={diff:+.2f}pp)")


def main():
    parser = argparse.ArgumentParser(description="Kill gate judgment for DeiT 50ep Muon vs AdamW")
    parser.add_argument("--muon-log", required=True, help="Path to Muon training log")
    parser.add_argument("--adamw-log", required=True, help="Path to AdamW training log")
    args = parser.parse_args()

    muon_data = parse_log(args.muon_log)
    adamw_data = parse_log(args.adamw_log)

    if not muon_data and not adamw_data:
        print("No data available from either log. Exiting.")
        sys.exit(1)

    total_expected = 50
    muon_done = max(ep for ep, _ in muon_data) if muon_data else 0
    adamw_done = max(ep for ep, _ in adamw_data) if adamw_data else 0
    if muon_done < total_expected or adamw_done < total_expected:
        print(f"WARNING: training incomplete — Muon: {muon_done}/{total_expected} ep, AdamW: {adamw_done}/{total_expected} ep")
        print("Showing partial results.\n")

    # Per-epoch table
    print("=" * 45)
    print("  Per-Epoch Val Acc Comparison")
    print("=" * 45)
    make_table(muon_data, adamw_data)

    # Best results
    muon_best_ep, muon_best_acc = max(muon_data, key=lambda x: x[1]) if muon_data else (0, 0)
    adamw_best_ep, adamw_best_acc = max(adamw_data, key=lambda x: x[1]) if adamw_data else (0, 0)

    print(f"\n{'=' * 45}")
    print(f"  Best Results")
    print(f"{'=' * 45}")
    print(f"  Muon  best_val_acc = {muon_best_acc:.2f}% (epoch {muon_best_ep})")
    print(f"  AdamW best_val_acc = {adamw_best_acc:.2f}% (epoch {adamw_best_ep})")

    # Kill gate
    verdict, gap = kill_gate(muon_best_acc, adamw_best_acc)
    print(f"\n{'=' * 45}")
    print(f"  Kill Gate Judgment")
    print(f"{'=' * 45}")
    print(f"  Gap = {gap:+.2f}pp (Muon - AdamW)")
    print(f"  Verdict: **{verdict}**")
    if verdict == "Artifact":
        print("  -> Convergence illusion: AdamW caught up, Muon advantage not real at scale.")
    elif verdict == "Partial":
        print("  -> Advantage shrinking but still significant. Muon has edge, needs investigation.")
    else:
        print("  -> Strong advantage sustained. Muon superiority is real.")

    # Muon 20ep baseline comparison
    print(f"\n{'=' * 45}")
    print(f"  AdamW 50ep vs Muon 20ep Baseline")
    print(f"{'=' * 45}")
    baseline_gap = adamw_best_acc - MUON_20EP_BASELINE
    print(f"  Muon 20ep baseline = {MUON_20EP_BASELINE:.2f}%")
    print(f"  AdamW 50ep best    = {adamw_best_acc:.2f}%")
    print(f"  Gap = {baseline_gap:+.2f}pp")
    if baseline_gap < 0:
        print(f"  -> AdamW at 50ep still {abs(baseline_gap):.2f}pp behind Muon at 20ep.")
    else:
        print(f"  -> AdamW at 50ep surpassed Muon 20ep by {baseline_gap:.2f}pp.")

    # Convergence trajectory
    print(f"\n{'=' * 45}")
    print(f"  Convergence Trajectory (milestone epochs)")
    print(f"{'=' * 45}")
    convergence_trajectory(muon_data, adamw_data)


if __name__ == "__main__":
    main()
