"""
Advantage Sign Misattribution Analysis v2 (plan_004)

4-panel figure + console summary + JSON output.
Designed for paper Figure 2 candidate.
"""

import json
import argparse
import numpy as np
from collections import defaultdict
from pathlib import Path
from scipy.stats import pointbiserialr, pearsonr
from scipy.optimize import curve_fit

DEFAULT_LOG = "/root/runs/cost-verify-agent-rl/hsweep_h2_seed2/advantage_log.jsonl"
DEFAULT_OUTPUT = "/root/cost-verify-agent-rl/artifacts"


def load_data(path):
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def build_episodes(records):
    episodes = defaultdict(list)
    for r in records:
        episodes[r["episode_id"]].append(r)
    for eid in episodes:
        episodes[eid].sort(key=lambda x: x["window_position"])
    return episodes


def classify_outcomes(episodes):
    outcomes = {}
    for eid, windows in episodes.items():
        max_ret = max(w["step_return"] for w in windows)
        outcomes[eid] = 1 if max_ret > 1.0 else 0
    return outcomes


def analysis_sign_vs_outcome(records, outcomes):
    """Analysis 1: advantage sign correlation with episode outcome."""
    signs = []
    outs = []
    success_pos = 0
    success_total = 0
    fail_pos = 0
    fail_total = 0

    for r in records:
        eid = r["episode_id"]
        if eid not in outcomes:
            continue
        is_pos = r["advantage"] > 0
        is_success = outcomes[eid] == 1
        signs.append(1 if is_pos else 0)
        outs.append(outcomes[eid])
        if is_success:
            success_total += 1
            if is_pos:
                success_pos += 1
        else:
            fail_total += 1
            if is_pos:
                fail_pos += 1

    signs = np.array(signs)
    outs = np.array(outs)

    agreement = np.mean(signs == outs)
    r_pb, p_val = pointbiserialr(outs, signs)

    pos_rate_success = success_pos / success_total if success_total > 0 else 0
    pos_rate_fail = fail_pos / fail_total if fail_total > 0 else 0

    results = {
        "agreement": float(agreement),
        "r_pointbiserial": float(r_pb),
        "p_value": float(p_val),
        "pos_adv_rate_in_success": float(pos_rate_success),
        "pos_adv_rate_in_fail": float(pos_rate_fail),
        "n_success_windows": int(success_total),
        "n_fail_windows": int(fail_total),
    }

    print("=" * 60)
    print("Analysis 1: Advantage Sign vs Episode Outcome")
    print("=" * 60)
    print(f"  Sign-outcome agreement:       {agreement:.4f}")
    print(f"  Point-biserial r:              {r_pb:.4f} (p={p_val:.2e})")
    print(f"  Positive-adv rate (success):   {pos_rate_success:.4f} ({success_pos}/{success_total})")
    print(f"  Positive-adv rate (failure):   {pos_rate_fail:.4f} ({fail_pos}/{fail_total})")

    return results


def analysis_sign_vs_position(records, outcomes):
    """Analysis 2: advantage sign distribution by window position."""
    by_pos = defaultdict(lambda: {"advantages": [], "signs": [], "outcomes": []})

    for r in records:
        eid = r["episode_id"]
        if eid not in outcomes:
            continue
        pos = r["window_position"]
        by_pos[pos]["advantages"].append(r["advantage"])
        by_pos[pos]["signs"].append(1 if r["advantage"] > 0 else 0)
        by_pos[pos]["outcomes"].append(outcomes[eid])

    positions = sorted(by_pos.keys())
    results = {"positions": [], "mean_advantage": [], "pos_sign_rate": [],
               "n_samples": [], "sign_outcome_agreement": []}

    print("\n" + "=" * 60)
    print("Analysis 2: Advantage Sign vs Window Position")
    print("=" * 60)
    print(f"  {'Pos':<5}{'N':<8}{'Mean Adv':<14}{'Pos%':<10}{'Sign=Out%':<12}")
    print(f"  {'-'*5}{'-'*8}{'-'*14}{'-'*10}{'-'*12}")

    for pos in positions:
        advs = np.array(by_pos[pos]["advantages"])
        signs = np.array(by_pos[pos]["signs"])
        outs = np.array(by_pos[pos]["outcomes"])
        agree = np.mean(signs == outs)

        results["positions"].append(int(pos))
        results["mean_advantage"].append(float(np.mean(advs)))
        results["pos_sign_rate"].append(float(np.mean(signs)))
        results["n_samples"].append(len(advs))
        results["sign_outcome_agreement"].append(float(agree))

        print(f"  {pos:<5}{len(advs):<8}{np.mean(advs):<14.6f}{np.mean(signs):<10.4f}{agree:<12.4f}")

    sign_rates = np.array(results["pos_sign_rate"])
    results["sign_rate_std_across_positions"] = float(np.std(sign_rates))
    print(f"\n  Sign rate std across positions: {np.std(sign_rates):.4f}")
    print(f"  (Low std = sign independent of position = episode-level attribution)")

    return results


def analysis_magnitude_decay(records, episodes, outcomes):
    """Analysis 3: magnitude decay fitting with gamma^k."""
    by_pos = defaultdict(list)
    by_pos_success = defaultdict(list)
    by_pos_fail = defaultdict(list)

    for r in records:
        eid = r["episode_id"]
        if eid not in outcomes:
            continue
        pos = r["window_position"]
        mag = abs(r["advantage"])
        by_pos[pos].append(mag)
        if outcomes[eid] == 1:
            by_pos_success[pos].append(mag)
        else:
            by_pos_fail[pos].append(mag)

    positions = sorted(by_pos.keys())
    mean_mags = np.array([np.mean(by_pos[p]) for p in positions])
    pos_arr = np.array(positions, dtype=float)

    def gamma_decay(k, a, gamma):
        return a * gamma ** k

    results = {"positions": [int(p) for p in positions],
               "mean_abs_advantage": [float(m) for m in mean_mags]}

    print("\n" + "=" * 60)
    print("Analysis 3: Magnitude Decay Fitting")
    print("=" * 60)

    try:
        popt, pcov = curve_fit(gamma_decay, pos_arr, mean_mags,
                               p0=[mean_mags[0], 0.9], bounds=([0, 0], [np.inf, 1.0]),
                               maxfev=5000)
        fitted_a, fitted_gamma = popt
        predicted = gamma_decay(pos_arr, fitted_a, fitted_gamma)
        ss_res = np.sum((mean_mags - predicted) ** 2)
        ss_tot = np.sum((mean_mags - np.mean(mean_mags)) ** 2)
        r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        results["fitted_gamma"] = float(fitted_gamma)
        results["fitted_a"] = float(fitted_a)
        results["r_squared"] = float(r_squared)

        print(f"  Fitted gamma:  {fitted_gamma:.4f}")
        print(f"  Fitted a:      {fitted_a:.6f}")
        print(f"  R^2:           {r_squared:.4f}")
    except (RuntimeError, ValueError) as e:
        print(f"  Curve fit failed: {e}")
        results["fitted_gamma"] = None
        results["r_squared"] = None

    print(f"\n  {'Pos':<5}{'Mean |Adv|':<14}{'N':<8}")
    for p in positions:
        print(f"  {p:<5}{np.mean(by_pos[p]):<14.8f}{len(by_pos[p]):<8}")

    return results


def analysis_distributions(records, outcomes):
    """Analysis 4: success vs failure advantage distributions."""
    success_advs = []
    fail_advs = []
    success_by_pos = defaultdict(list)
    fail_by_pos = defaultdict(list)

    for r in records:
        eid = r["episode_id"]
        if eid not in outcomes:
            continue
        if outcomes[eid] == 1:
            success_advs.append(r["advantage"])
            success_by_pos[r["window_position"]].append(r["advantage"])
        else:
            fail_advs.append(r["advantage"])
            fail_by_pos[r["window_position"]].append(r["advantage"])

    success_advs = np.array(success_advs)
    fail_advs = np.array(fail_advs)

    overlap = 0.0
    if len(success_advs) > 0 and len(fail_advs) > 0:
        bins = np.linspace(min(fail_advs.min(), success_advs.min()),
                           max(fail_advs.max(), success_advs.max()), 50)
        h_s, _ = np.histogram(success_advs, bins=bins, density=True)
        h_f, _ = np.histogram(fail_advs, bins=bins, density=True)
        bin_width = bins[1] - bins[0]
        overlap = float(np.sum(np.minimum(h_s, h_f)) * bin_width)

    results = {
        "n_success": len(success_advs),
        "n_fail": len(fail_advs),
        "mean_success": float(np.mean(success_advs)) if len(success_advs) > 0 else None,
        "mean_fail": float(np.mean(fail_advs)) if len(fail_advs) > 0 else None,
        "std_success": float(np.std(success_advs)) if len(success_advs) > 0 else None,
        "std_fail": float(np.std(fail_advs)) if len(fail_advs) > 0 else None,
        "distribution_overlap": overlap,
    }

    print("\n" + "=" * 60)
    print("Analysis 4: Success vs Failure Advantage Distributions")
    print("=" * 60)
    print(f"  Success: n={len(success_advs)}, mean={results['mean_success']:.6f}, std={results['std_success']:.6f}")
    print(f"  Failure: n={len(fail_advs)}, mean={results['mean_fail']:.6f}, std={results['std_fail']:.6f}")
    print(f"  Distribution overlap: {overlap:.4f}")
    print(f"  (Overlap near 1.0 = high sign misattribution severity)")

    return results, success_advs, fail_advs, success_by_pos, fail_by_pos


def make_figure(records, outcomes, res_sign, res_pos, res_decay, success_advs,
                fail_advs, success_by_pos, fail_by_pos, output_dir):
    """Generate 4-panel paper figure."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib import rcParams

    rcParams["font.family"] = "serif"
    rcParams["font.size"] = 9
    rcParams["axes.labelsize"] = 10
    rcParams["axes.titlesize"] = 10
    rcParams["xtick.labelsize"] = 8
    rcParams["ytick.labelsize"] = 8
    rcParams["legend.fontsize"] = 8

    fig, axes = plt.subplots(2, 2, figsize=(7, 5.5))

    # (a) Sign vs Outcome heatmap
    ax = axes[0, 0]
    pos_rate_s = res_sign["pos_adv_rate_in_success"]
    neg_rate_s = 1 - pos_rate_s
    pos_rate_f = res_sign["pos_adv_rate_in_fail"]
    neg_rate_f = 1 - pos_rate_f
    heatmap_data = np.array([[pos_rate_s, neg_rate_s],
                              [pos_rate_f, neg_rate_f]])
    im = ax.imshow(heatmap_data, cmap="RdBu_r", vmin=0, vmax=1, aspect="auto")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Positive Adv", "Negative Adv"])
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["Success Ep.", "Failure Ep."])
    for i in range(2):
        for j in range(2):
            ax.text(j, i, f"{heatmap_data[i, j]:.2f}",
                    ha="center", va="center", fontsize=10, fontweight="bold",
                    color="white" if abs(heatmap_data[i, j] - 0.5) > 0.2 else "black")
    ax.set_xlabel("")
    ax.text(0.5, -0.18, f"r = {res_sign['r_pointbiserial']:.3f}", transform=ax.transAxes,
            ha="center", fontsize=8)
    ax.text(-0.05, 1.05, "(a)", transform=ax.transAxes, fontsize=10, fontweight="bold")

    # (b) Advantage by position
    ax = axes[0, 1]
    positions = res_pos["positions"]
    mean_advs = res_pos["mean_advantage"]
    pos_rates = res_pos["pos_sign_rate"]

    ax.bar(positions, mean_advs, color="steelblue", alpha=0.7, width=0.6)
    ax.axhline(0, color="gray", linewidth=0.5, linestyle="--")
    ax.set_xlabel("Window Position $k$")
    ax.set_ylabel("Mean Advantage")
    ax.set_xticks(positions)

    ax2 = ax.twinx()
    ax2.plot(positions, pos_rates, "o-", color="firebrick", markersize=4, linewidth=1.2)
    ax2.set_ylabel("Fraction Positive", color="firebrick")
    ax2.set_ylim(0, 1)
    ax2.tick_params(axis="y", labelcolor="firebrick")
    ax.text(-0.05, 1.05, "(b)", transform=ax.transAxes, fontsize=10, fontweight="bold")

    # (c) Magnitude decay
    ax = axes[1, 0]
    decay_positions = res_decay["positions"]
    mean_abs = res_decay["mean_abs_advantage"]
    ax.plot(decay_positions, mean_abs, "s-", color="darkgreen", markersize=5, linewidth=1.5)

    if res_decay.get("fitted_gamma") is not None:
        k_fit = np.linspace(0, max(decay_positions), 50)
        fitted = res_decay["fitted_a"] * res_decay["fitted_gamma"] ** k_fit
        ax.plot(k_fit, fitted, "--", color="orange", linewidth=1.2,
                label=f"$\\gamma^k$ fit ($\\gamma$={res_decay['fitted_gamma']:.3f}, $R^2$={res_decay['r_squared']:.3f})")
        ax.legend(loc="upper right")

    ax.set_xlabel("Window Position $k$")
    ax.set_ylabel("Mean $|$Advantage$|$")
    ax.set_xticks(decay_positions)
    ax.text(-0.05, 1.05, "(c)", transform=ax.transAxes, fontsize=10, fontweight="bold")

    # (d) Success vs failure distributions
    ax = axes[1, 1]
    if len(success_advs) > 0:
        ax.hist(success_advs, bins=30, alpha=0.6, color="green", density=True, label="Success")
    if len(fail_advs) > 0:
        ax.hist(fail_advs, bins=30, alpha=0.6, color="red", density=True, label="Failure")
    ax.axvline(0, color="gray", linewidth=0.5, linestyle="--")
    ax.set_xlabel("Advantage")
    ax.set_ylabel("Density")
    ax.legend(loc="upper right")
    ax.text(-0.05, 1.05, "(d)", transform=ax.transAxes, fontsize=10, fontweight="bold")

    plt.tight_layout(pad=0.8)

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_path = output_dir / "advantage_analysis.pdf"
    png_path = output_dir / "advantage_analysis.png"
    fig.savefig(pdf_path, bbox_inches="tight", dpi=300)
    fig.savefig(png_path, bbox_inches="tight", dpi=200)
    plt.close(fig)

    print(f"\n  Figure saved: {pdf_path}")
    print(f"  Figure saved: {png_path}")
    return str(pdf_path), str(png_path)


def main():
    parser = argparse.ArgumentParser(
        description="Advantage sign misattribution analysis v2 (plan_004, paper Figure 2)")
    parser.add_argument("--input", default=DEFAULT_LOG,
                        help="Path to advantage_log.jsonl")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT,
                        help="Directory for outputs (PDF, PNG, JSON)")
    args = parser.parse_args()

    path = Path(args.input)
    if not path.exists():
        print(f"ERROR: Data file not found: {path}")
        print("Run hsweep_h2_seed2 with LOG_PER_SAMPLE_ADV=1 first.")
        return

    records = load_data(path)
    episodes = build_episodes(records)
    outcomes = classify_outcomes(episodes)
    n_success = sum(outcomes.values())

    print(f"Loaded {len(records)} records, {len(episodes)} episodes "
          f"({n_success} success, {len(episodes) - n_success} fail)")
    print(f"Window positions: {sorted(set(r['window_position'] for r in records))}")

    res_sign = analysis_sign_vs_outcome(records, outcomes)
    res_pos = analysis_sign_vs_position(records, outcomes)
    res_decay = analysis_magnitude_decay(records, episodes, outcomes)
    res_dist, success_advs, fail_advs, success_by_pos, fail_by_pos = \
        analysis_distributions(records, outcomes)

    make_figure(records, outcomes, res_sign, res_pos, res_decay,
                success_advs, fail_advs, success_by_pos, fail_by_pos,
                args.output_dir)

    # JSON summary
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    summary = {
        "sign_vs_outcome": res_sign,
        "sign_vs_position": res_pos,
        "magnitude_decay": res_decay,
        "distributions": res_dist,
    }
    json_path = output_dir / "advantage_analysis_summary.json"
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\n  JSON summary: {json_path}")

    # Final verdict
    print("\n" + "=" * 60)
    print("VERDICT")
    print("=" * 60)
    r = res_sign["r_pointbiserial"]
    pos_s = res_sign["pos_adv_rate_in_success"]
    pos_f = res_sign["pos_adv_rate_in_fail"]
    print(f"  Point-biserial r(sign, outcome) = {r:.4f}")
    print(f"  P(adv>0 | success) = {pos_s:.4f}")
    print(f"  P(adv>0 | failure) = {pos_f:.4f}")
    if r > 0.8:
        print("  >> Strong sign misattribution: advantage sign almost fully determined by episode outcome.")
    elif r > 0.5:
        print("  >> Moderate sign misattribution present.")
    else:
        print("  >> Weak or no sign misattribution.")

    sign_std = res_pos.get("sign_rate_std_across_positions", 0)
    print(f"\n  Sign rate std across positions = {sign_std:.4f}")
    if sign_std < 0.05:
        print("  >> Position-independent: confirms episode-level (not window-local) attribution.")


if __name__ == "__main__":
    main()
