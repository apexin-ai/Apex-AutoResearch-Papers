# paper r13 figure and compute

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r13-figure-and-compute_20260517T190450_result.json`
- **Structured JSON:** [`5fb38271973e71122ddf.json`](../../sessions/5f/5fb38271973e71122ddf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I can see the full strip plot clearly. Let me analyze and report results.

---

## M4 — Figure 2 (DDR strip plot) 检查结果

**检查对象**: `plot_fig1_8gen_fixed.py` 生成的 8-generator strip plot（3 bracket 版本）

**entropy_std (σ_H) 区域**: 无标签重叠。
- σ_H 的 x-axis 标签清晰，与左邻 H_min、右邻 H_max 之间有足够间距
- "Moderate" bracket 标签（覆盖 H_min, σ_H）与相邻 "Near-stationary" bracket 文字无重叠
- 数据点散布合理（约 -0.3 到 +0.1 范围），无遮挡

**但发现另一个问题**: H_max 和 Tail Dec. 的 x-axis 标签紧贴在一起，几乎没有间距（图中可以清楚看到 "H_max" 和 "Tail Dec." 文字连在一起）。这是 Near-stationary 区的 x 轴标签拥挤问题。

**涉及脚本**:
- 服务器: `/root/gen-depth-fingerprint/scripts/plot_fig1_8gen_fixed.py`
- 本地副本: `artifacts/_project/supplement/code/scripts/plot_fig1_strip.py`（6-gen 版本，结构类似但非最新）

**注意**: 论文 artifacts 中的 `fig1_differential_response.png` 存在多个版本（bar chart / 6-gen strip / 8-gen strip），当前 paper 目录下是旧版。

---

## SF2 — Variance Ratio 计算结果

数据: `features_all_models.csv`（6 generators, gen-1: 5,918 samples, gen-2+: 15,639 samples）

| Feature | var(gen-1) | var(gen-2+) | ratio |
|---|---|---|---|
| entropy_mean | 0.424797 | 0.830780 | **1.9557** |
| entropy_std | 0.038613 | 0.079967 | **2.0710** |
| entropy_min | 0.106973 | 0.104785 | **0.9796** |
| entropy_max | 0.552746 | 0.620441 | **1.1225** |
| tail_decay | 0.000000 | 0.000000 | **1.3960** |
| ttr | 0.025092 | 0.055198 | **2.1998** |
| hapax_ratio | 0.027752 | 0.052854 | **1.9045** |

**分析**:

- **Drifting features** (entropy_mean, ttr, hapax_ratio): ratio 全部在 1.9–2.2 范围，远超 1.15 阈值 ✓
- **Near-stationary features**: entropy_min (0.98) 和 entropy_max (1.12) 接近 1.0 ✓，tail_decay (1.40) 略高
- **意外发现**: entropy_std ratio = **2.07**，表现与 drifting features 一致，而非预期的接近 1.0。这意味着 entropy_std 虽然 Spearman ρ 较弱（约 -0.2），但其方差在 gen-2+ 中显著放大——方向性信号弱但离散度增大，可能因为不同 generator 对 entropy_std 的影响方向不一致

---
