# ssh w7 debug script read only

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_w7_debug_script_read_only_20260523T010749_result.json`
- **Structured JSON:** [`de1cfb179263d12942a6.json`](../../sessions/de/de1cfb179263d12942a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已读取完毕。以下是汇报。

---

## 1. analyze_w7.py 完整源码（268行）

```python
"""W7 ablation analysis: component ablation boxplots + statistical tests."""

import argparse
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats as sp_stats

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.labelsize": 13,
    "axes.titlesize": 13,
    "legend.fontsize": 9,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "figure.dpi": 150,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
})

VARIANT_ORDER = ["full_gmfrm", "no_judge_severity", "binary_gating", "staged_estimation"]
VARIANT_LABELS = {
    "full_gmfrm": "Full G-MFRM",
    "no_judge_severity": "No Severity",
    "binary_gating": "Binary Gate",
    "staged_estimation": "Staged Est.",
}
PALETTE = {
    "full_gmfrm": "#55A868",
    "no_judge_severity": "#4C72B0",
    "binary_gating": "#DD8452",
    "staged_estimation": "#C44E52",
}
BASE_DIR = Path("/root/gated_mfrm_judge_bias/exp_w7_ablation")


def load_data() -> pd.DataFrame:
    for p in [BASE_DIR / "results_w7_ablation.csv",
              BASE_DIR / "results_w7_ablation_partial.csv"]:
        if p.exists():
            df = pd.read_csv(p)
            n_seeds = df["seed"].nunique()
            variants = sorted(df["variant"].unique())
            print(f"Loaded {p}")
            print(f"  {len(df)} rows, {n_seeds} seeds, variants: {variants}")
            return df
    print("ERROR: no W7 ablation CSV found", file=sys.stderr)
    sys.exit(1)


def sig_stars(p: float) -> str:
    if p < 0.001: return "***"
    elif p < 0.01: return "**"
    elif p < 0.05: return "*"
    return "n.s."


def plot_ablation_boxplots(df: pd.DataFrame, p_table: pd.DataFrame, out_dir: Path):
    variants = [v for v in VARIANT_ORDER if v in df["variant"].unique()]
    labels = [VARIANT_LABELS.get(v, v) for v in variants]
    colors = [PALETTE.get(v, "gray") for v in variants]

    fig, axes = plt.subplots(1, 2, figsize=(7, 3.0))

    for ax, metric, ylabel in zip(
        axes, ["theta_rmse", "c_rmse"], ["$\\theta$ RMSE", "$c$ RMSE"]
    ):
        data_lists = [df[df["variant"] == v][metric].dropna().values for v in variants]

        bp = ax.boxplot(
            data_lists, positions=range(len(variants)), widths=0.5,
            patch_artist=True, showfliers=True,
            flierprops=dict(marker="o", markersize=3, alpha=0.5),
            medianprops=dict(color="black", linewidth=1.2),
        )
        for patch, color in zip(bp["boxes"], colors):
            patch.set_facecolor(color)
            patch.set_alpha(0.65)

        for i, vals in enumerate(data_lists):
            jitter = np.random.default_rng(42).uniform(-0.12, 0.12, size=len(vals))
            ax.scatter(np.full_like(vals, i) + jitter, vals,
                       color=colors[i], s=12, alpha=0.5, zorder=3, edgecolors="none")

        if "full_gmfrm" in variants and not p_table.empty:
            full_idx = variants.index("full_gmfrm")
            y_max = max(v.max() for v in data_lists if len(v) > 0) * 1.02
            bracket_y = y_max
            for j, v in enumerate(variants):
                if v == "full_gmfrm":
                    continue
                row = p_table[(p_table["metric"] == metric) & (p_table["variant"] == v)]
                if row.empty:
                    continue
                stars = sig_stars(row["p_value"].values[0])
                if stars == "n.s.":
                    continue
                bracket_y += y_max * 0.06
                ax.plot([full_idx, full_idx, j, j],
                        [bracket_y - y_max * 0.01, bracket_y, bracket_y, bracket_y - y_max * 0.01],
                        color="black", linewidth=0.8)
                ax.text((full_idx + j) / 2, bracket_y + y_max * 0.005, stars,
                        ha="center", va="bottom", fontsize=8)

        ax.set_xticks(range(len(variants)))
        ax.set_xticklabels(labels, rotation=20, ha="right")
        ax.set_ylabel(ylabel)
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.grid(axis="y", alpha=0.3, linewidth=0.5)

    fig.tight_layout()
    for ext in ["pdf", "png"]:
        fig.savefig(out_dir / f"ablation_boxplots.{ext}")
    plt.close(fig)
    print(f"Saved ablation_boxplots.{{pdf,png}}")


def plot_theta_tau_boxplot(df: pd.DataFrame, out_dir: Path):
    variants = [v for v in VARIANT_ORDER if v in df["variant"].unique()]
    labels = [VARIANT_LABELS.get(v, v) for v in variants]
    colors = [PALETTE.get(v, "gray") for v in variants]

    fig, ax = plt.subplots(figsize=(3.5, 2.8))

    data_lists = [df[df["variant"] == v]["theta_tau"].dropna().values for v in variants]

    bp = ax.boxplot(
        data_lists, positions=range(len(variants)), widths=0.5,
        patch_artist=True, showfliers=True,
        flierprops=dict(marker="o", markersize=3, alpha=0.5),
        medianprops=dict(color="black", linewidth=1.2),
    )
    for patch, color in zip(bp["boxes"], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.65)

    for i, vals in enumerate(data_lists):
        jitter = np.random.default_rng(42).uniform(-0.12, 0.12, size=len(vals))
        ax.scatter(np.full_like(vals, i) + jitter, vals,
                   color=colors[i], s=12, alpha=0.5, zorder=3, edgecolors="none")

    ax.set_xticks(range(len(variants)))
    ax.set_xticklabels(labels, rotation=20, ha="right")
    ax.set_ylabel("Kendall $\\tau$ (ability)")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", alpha=0.3, linewidth=0.5)

    fig.tight_layout()
    for ext in ["pdf", "png"]:
        fig.savefig(out_dir / f"theta_tau_boxplot.{ext}")
    plt.close(fig)
    print(f"Saved theta_tau_boxplot.{{pdf,png}}")


def run_tests(df: pd.DataFrame) -> pd.DataFrame:
    variants = [v for v in VARIANT_ORDER if v in df["variant"].unique()]
    if "full_gmfrm" not in variants:
        print("WARNING: full_gmfrm not found — skipping statistical tests")
        return pd.DataFrame()

    full = df[df["variant"] == "full_gmfrm"]
    seeds_full = set(full["seed"].values)

    rows = []
    metrics = ["theta_rmse", "c_rmse", "theta_tau"]
    metric_labels = {"theta_rmse": "θ RMSE", "c_rmse": "c RMSE", "theta_tau": "θ τ"}

    for metric in metrics:
        for v in variants:
            if v == "full_gmfrm":
                continue
            vdf = df[df["variant"] == v]
            common_seeds = sorted(seeds_full & set(vdf["seed"].values))
            if len(common_seeds) < 5:
                continue
            full_vals = full[full["seed"].isin(common_seeds)].sort_values("seed")[metric].values
            v_vals = vdf[vdf["seed"].isin(common_seeds)].sort_values("seed")[metric].values

            stat, p = sp_stats.wilcoxon(full_vals, v_vals, alternative="two-sided")
            rows.append({
                "metric": metric,
                "metric_label": metric_labels[metric],
                "variant": v,
                "variant_label": VARIANT_LABELS.get(v, v),
                "n_seeds": len(common_seeds),
                "full_median": np.median(full_vals),
                "variant_median": np.median(v_vals),
                "median_diff": np.median(v_vals - full_vals),
                "wilcoxon_stat": stat,
                "p_value": p,
                "sig": sig_stars(p),
            })

    return pd.DataFrame(rows)


def print_test_table(p_df: pd.DataFrame):
    if p_df.empty:
        return
    print("\n" + "=" * 85)
    print("PAIRED WILCOXON SIGNED-RANK TESTS (full_gmfrm vs each variant)")
    print("=" * 85)
    print(f"{'Metric':<10} {'Variant':<16} {'Full med':>9} {'Var med':>9} "
          f"{'Δ median':>9} {'W':>8} {'p':>10} {'Sig':>5}")
    print("-" * 85)
    for _, r in p_df.iterrows():
        print(f"{r['metric_label']:<10} {r['variant_label']:<16} "
              f"{r['full_median']:>9.4f} {r['variant_median']:>9.4f} "
              f"{r['median_diff']:>+9.4f} {r['wilcoxon_stat']:>8.0f} "
              f"{r['p_value']:>10.4e} {r['sig']:>5}")
    print("=" * 85)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default=None, help="Explicit CSV path")
    parser.add_argument("--out-dir",
                        default="/root/gated_mfrm_judge_bias/artifacts/w7_analysis")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.data:
        df = pd.read_csv(args.data)
        print(f"Loaded {args.data}  ({len(df)} rows)")
    else:
        df = load_data()

    p_df = run_tests(df)
    print_test_table(p_df)

    if not p_df.empty:
        p_df.to_csv(out_dir / "wilcoxon_tests.csv", index=False)
        print(f"Saved wilcoxon_tests.csv")

    plot_ablation_boxplots(df, p_df, out_dir)
    plot_theta_tau_boxplot(df, out_dir)

    print("\n" + "=" * 60)
    print("VARIANT SUMMARY (mean ± std)")
    print("=" * 60)
    for v in VARIANT_ORDER:
        vdf = df[df["variant"] == v]
        if vdf.empty:
            continue
        print(f"  {VARIANT_LABELS.get(v, v):<18} "
              f"θ_RMSE={vdf['theta_rmse'].mean():.4f}±{vdf['theta_rmse'].std():.4f}  "
              f"c_RMSE={vdf['c_rmse'].mean():.4f}±{vdf['c_rmse'].std():.4f}  "
              f"θ_τ={vdf['theta_tau'].mean():.4f}±{vdf['theta_tau'].std():.4f}  "
              f"(n={len(vdf)})")
    print("=" * 60)

    print(f"\nAll outputs in {out_dir}")


if __name__ == "__main__":
    main()
```

---

## 2. run_ablation.py 数据输出格式

**CSV 路径**：`/root/gated_mfrm_judge_bias/exp_w7_ablation/results_w7_ablation.csv`（完成时）及 `results_w7_ablation_partial.csv`（每 5 seed checkpoint）

**CSV 列名**：
```
theta_rmse, theta_tau, r_hat, ess, c_rmse, c_pearson, variant, seed, elapsed_s
```

**示例行**：
```
0.12411725,0.92163265,1.01,499.0,0.35047669,0.94847806,full_gmfrm,0,237.408
```

另外生成 `summary_w7_ablation.json`（每个 variant 的聚合统计）。

---

## 3. 当前实验进度

**前一轮已完成全部 20 seeds**：CSV 有 81 行（header + 80 rows = 4 variants × 20 seeds），最后一行 seed=19。两个 CSV 文件大小相同（9958 bytes），修改时间 08:44。

**重跑状态**：`w7_ablation.log` 修改时间 09:05，内容仅显示起始信息：
```
W7 Ablation: 4 variants x 20 seeds
DGP: N=50 I=100 J=8 rho=0.6
MCMC: {'num_warmup': 2000, 'num_samples': 4000, 'num_chains': 4, 'chain_method': 'sequential', 'progress_bar': False}

[1/20] seed=0
```
→ 重跑刚启动，当前在 **seed 0/20**（每 seed 约需 4×(200-400)s ≈ 15-25 分钟，4 variants 串行 → 每 seed ~18 分钟）。

---

## 4. 潜在 Bug 和问题

### Bug 1: `no_judge_severity` 模型缺少 `d[None, None, :]` 但响应仍是 3D (N×I×J)
`_no_judge_severity_model` 移除了 `d_j` facet，logits 为：
```python
logits = theta[:, None, None] - b[None, :, None] + c[:, None, None] * e[None, :, None]
```
这会被 broadcasting 扩展到 N×I×J（J 维重复相同值）。虽然功能上正确（ablation 的意图就是去掉 d），但效率低——等价于对同一个 logit 重复 J 次 Bernoulli 采样，增加了 J 倍的无用似然计算。可以改用 `Y.sum(axis=2)` 配合 Binomial(J, p) 来加速。

### Bug 2（轻微）: `run_ablation.py` stdout 日志 vs 文件日志不同步
`run_ablation.py` 用 `print(..., flush=True)` 输出进度，但 `w7_ablation.log` 只有 196 bytes。如果 tmux 重跑时用的是 `python run_ablation.py > w7_ablation.log 2>&1`，那日志应该会持续追加。当前日志只到 `[1/20] seed=0` 可能说明重跑刚启动不久，也可能是 stdout 缓冲问题（尽管 `flush=True` 应该已解决）。

### Bug 3（设计层面）: DGP 有 severity `s` 交互项，但所有模型都不估计 `s`
DGP contamination = `c * e * (1 + s)`，但 full_gmfrm 模型 contamination = `c * e`。这是有意的简化（模型 misspecification 的一部分），但意味着 `c` 的估计会吸收部分 `s` 的效应，导致 `c_rmse` 指标偏高。如果论文要讨论 recovery quality，需要说明这一点。

### 无路径/import 问题
`analyze_w7.py` 的 `load_data()` 查找路径与 `run_ablation.py` 的输出路径一致，CSV 列名匹配，import 无缺失。

---
