# analysis nve baseline unification

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve-baseline-unification_20260515T044956_result.json`
- **Structured JSON:** [`3934ff9577ae11620681.json`](../../sessions/39/3934ff9577ae11620681.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 6 项修正完成。汇总：

**Item 1** — metrics_table.md：所有 seed=2 实验的 nve 改为用 exp_001 基线。关键修正：009b@45K nve 从 1.48 → **1.62**（>1.5x 阈值，与 CSV 一致）。

**Item 2** — method.md Section 3.2：替换为明确声明 "We normalize all v/e ratios against exp\_001 (DreamerV3 baseline, seed 1) at matched training steps. Sensitivity to baseline choice is reported in Appendix X."

**Item 3** — exp_001 registry：补全了完整 eval 轨迹（5K-505K，51 个 checkpoint），峰值 970.41@505K。

**Item 4** — summary_table.csv：vs_baseline_pct 改为 at-step 对比。主要变化：008e_v3 -8.76%→**-5.00%**，008a -18.43%→-15.07%，008c -74.74%→-60.89%。

**Item 5** — D035 去重：移除 exp_008e_v3_subsample_on_dt1_h15（s0），保留 exp_008e_v3_walker_s1（s1）。两者均 seed=1。

**Item 6** — Claim 列修正：008d C1,C3→**C1,C2**；008a C2→**C3**；008c C2→**C3**；008f/009b/009c C1,C3→**C1,C2**。

所有文件同步至 figures_data/ 和 analysis/ 副本。修改日志已注册为 artifact。

---
