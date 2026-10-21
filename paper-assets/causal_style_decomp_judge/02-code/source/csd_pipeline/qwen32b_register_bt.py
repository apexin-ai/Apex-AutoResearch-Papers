"""Qwen3-32B Register BT analysis + Forest Plot update."""

import json
import sys
import numpy as np
import choix

# ---------------------------------------------------------------------------
# BT Analysis
# ---------------------------------------------------------------------------

def load_records(path: str) -> list[dict]:
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    return records


def nli_filter(records: list[dict], threshold: float = 0.90) -> list[dict]:
    return [r for r in records if r.get("nli_cf", 0) >= threshold]


def build_bt_comparisons(records: list[dict]):
    comparisons = []
    pair_groups = []
    for rec in records:
        pair_comps = []
        for trial in [1, 2]:
            key = f"trial{trial}_prefers_academic"
            prefers_a = rec.get(key)
            if prefers_a is None:
                continue
            if prefers_a:
                pair_comps.append((0, 1))
            else:
                pair_comps.append((1, 0))
        if pair_comps:
            comparisons.extend(pair_comps)
            pair_groups.append(pair_comps)
    return comparisons, pair_groups


def bt_pair_bootstrap(records: list[dict], n_bootstrap: int = 10000, seed: int = 42):
    comparisons, pair_groups = build_bt_comparisons(records)
    n_pairs = len(pair_groups)
    n_comp = len(comparisons)

    params = choix.ilsr_pairwise(2, comparisons, alpha=0.01)
    p_a = np.exp(params[0]) / (np.exp(params[0]) + np.exp(params[1]))

    rng = np.random.RandomState(seed)
    boot_p = []
    for _ in range(n_bootstrap):
        sampled_idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot_comps = []
        for i in sampled_idx:
            boot_comps.extend(pair_groups[i])
        try:
            bp = choix.ilsr_pairwise(2, boot_comps, alpha=0.01)
            boot_p.append(np.exp(bp[0]) / (np.exp(bp[0]) + np.exp(bp[1])))
        except Exception:
            pass

    boot_p = np.array(boot_p)
    ci_lo = np.percentile(boot_p, 2.5)
    ci_hi = np.percentile(boot_p, 97.5)

    n_below = np.sum(boot_p < 0.5)
    if n_below == 0:
        p_val = 1.0 / n_bootstrap
        p_str = "p < 0.0001"
    else:
        p_val = n_below / len(boot_p)
        p_str = f"p = {p_val:.4f}"

    return {
        "p_a": p_a,
        "ci_lo": ci_lo,
        "ci_hi": ci_hi,
        "p_val": p_val,
        "p_str": p_str,
        "n_pairs": n_pairs,
        "n_comp": n_comp,
    }


# ---------------------------------------------------------------------------
# Forest Plot
# ---------------------------------------------------------------------------

def make_forest_plot(bt_result: dict, output_path: str):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    plt.rcParams.update({
        'font.family': 'DejaVu Sans',
        'font.size': 11,
        'axes.titlesize': 13,
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'figure.dpi': 300,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.05,
        'axes.spines.top': False,
        'axes.spines.right': False,
    })

    rows = [
        ("Qwen3-32B verbosity", 0.773, 0.703, 0.843, 0.0001, True, "#D55E00"),
        ("GPT-4o verbosity",    0.760, 0.688, 0.828, 0.0001, True, "#D55E00"),
        ("Qwen3-32B formality", 0.665, 0.585, 0.739, 0.0001, True, "#0072B2"),
        ("GPT-4o formality",    0.630, 0.558, 0.703, 0.001,  True, "#0072B2"),
        ("GPT-4o register",     0.570, 0.500, 0.640, 0.040,  True, "#009E73"),
    ]

    qwen_reg_sig = bt_result["p_val"] < 0.05
    qwen_reg_row = (
        "Qwen3-32B register",
        bt_result["p_a"],
        bt_result["ci_lo"],
        bt_result["ci_hi"],
        bt_result["p_val"],
        qwen_reg_sig,
        "#009E73",
    )

    # Insert Qwen3-32B register in correct position (descending by effect size)
    inserted = False
    final_rows = []
    for r in rows:
        if not inserted and bt_result["p_a"] >= r[1]:
            final_rows.append(qwen_reg_row)
            inserted = True
        final_rows.append(r)
    if not inserted:
        final_rows.append(qwen_reg_row)

    n = len(final_rows)
    fig, ax = plt.subplots(figsize=(7, 3.5))

    y_positions = list(range(n - 1, -1, -1))

    for i, (label, p, lo, hi, pv, sig, color) in enumerate(final_rows):
        y = y_positions[i]
        ax.plot([lo, hi], [y, y], color=color, linewidth=1.8, solid_capstyle='round')
        marker = 'D' if sig else 'D'
        facecolor = color if sig else 'white'
        ax.plot(p, y, marker='D', color=color, markerfacecolor=facecolor,
                markersize=7, markeredgewidth=1.5, zorder=5)

        ax.text(-0.02, y, label, ha='right', va='center', fontsize=10,
                transform=ax.get_yaxis_transform())

        if pv < 0.0001:
            p_text = "p<.0001"
        elif pv < 0.001:
            p_text = "p<.001"
        elif pv < 0.01:
            p_text = f"p={pv:.3f}"
        else:
            p_text = f"p={pv:.3f}" if pv < 1 else f"p={pv:.2f}"

        stat_text = f"{p:.3f} [{lo:.3f}, {hi:.3f}]  {p_text}"
        ax.text(1.02, y, stat_text, ha='left', va='center', fontsize=9,
                transform=ax.get_yaxis_transform())

    ax.axvline(x=0.5, color='gray', linestyle='--', linewidth=0.8, zorder=0)
    ax.set_xlim(0.4, 0.9)
    ax.set_ylim(-0.5, n - 0.5)
    ax.set_yticks([])
    ax.set_xlabel("P(style-preferred wins)")
    ax.spines['left'].set_visible(False)

    import os
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path, format='pdf')
    plt.close(fig)
    print(f"Forest plot saved: {output_path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    data_path = "/root/causal_style_decomp_judge/data/pairwise_results_qwen32b_register.jsonl"
    output_path = "/root/causal_style_decomp_judge/artifacts/figures/paper/forest_plot.pdf"

    records = load_records(data_path)
    filtered = nli_filter(records, 0.90)
    print(f"Loaded {len(records)} pairs, NLI>=0.90: {len(filtered)}")

    bt = bt_pair_bootstrap(filtered, n_bootstrap=10000, seed=42)

    print(f"\nQwen3-32B Register BT:")
    print(f"  P(academic) = {bt['p_a']:.3f}")
    print(f"  95% CI = [{bt['ci_lo']:.3f}, {bt['ci_hi']:.3f}]")
    print(f"  Bootstrap {bt['p_str']}")
    print(f"  N pairs = {bt['n_pairs']}, N comparisons = {bt['n_comp']}")

    make_forest_plot(bt, output_path)


if __name__ == "__main__":
    main()
