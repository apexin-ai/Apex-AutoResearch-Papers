# analysis a025 s42 fp32 5method padding

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a025_s42_fp32_5method_padding_20260519T121959_result.json`
- **Structured JSON:** [`0b2c6f9b21aac04ec26a.json`](../../sessions/0b/0b2c6f9b21aac04ec26a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the full report:

---

## Part 1: 5-method 分析 (a025_s42)

**无法执行** — `results/alpha_sweep/a025_s42/` 目录已从磁盘删除。`alpha_sweep_a025_s42_v3.log` 确认实验完成（11 gens, EXIT_CODE=0），但结果文件不存在。需要重跑实验才能分析。

参考现有 a025 分析：

| Method | a025_s43 fwd | a025_s44 fwd |
|--------|-------------|-------------|
| PermG (FDR) | 0/8 | 0/8 |
| Diff XCorr (FDR) | 3/8 | 1/8 |
| Threshold Onset | 0/8 | 0/8 |
| TY Granger | 0/8 | 2/8 |
| K≥3 consensus | 0/8 | 0/8 |

两个 seed 都是 PermG=0/8，符合预期（α=0.25 过渡点在 [0.25, 0.50] 区间）。

---

## Part 2: Padding Side 状态

gen_0 d1 清晰分成两组，与 right-padding 警告完全对应：

| exp_id | right-padding warnings | gen_0 d1 | padding version |
|--------|----------------------|----------|----------------|
| a000_s42/s43/s44 | 3443 | 0.0982/0.0983/0.0981 | **right (pre-D093)** |
| a010_s42 (v2 log) | 3443 | 0.0982 | **right (pre-D093)** |
| a010_s42_fp32 | log NOT FOUND | 0.0916 | **left (post-D093)** |
| a010_s43_fp32 | log NOT FOUND | 0.0929 | **left (post-D093)** |
| a025_s42 (v3 log) | 3443 | results deleted | **right (pre-D093)** |
| a025_s43 | 3443 | 0.0983 | **right (pre-D093)** |
| a025_s44 | 3443 | 0.0981 | **right (pre-D093)** |
| a050_s42/s43/s44 | 3443 | 0.0982/0.0983/0.0981 | **right (pre-D093)** |
| a060_s42_bf16 | log NOT FOUND | 0.0914 | **left (post-D093)** |
| a075_s42/s43/s44 | 3443 | 0.0982/0.0983/0.0981 | **right (pre-D093)** |

**规律**: `_fp32`/`_bf16` 后缀实验 = post-D093 left-padding (d1 ≈ 0.091-0.093)。无后缀实验 = pre-D093 right-padding (d1 ≈ 0.098)。差异 ~7% 稳定复现。

**关键发现**: 当前所有 a025 实验（s42/s43/s44）都是 right-padding 版本。如果要与 post-D093 fp32 实验对比，a025 需要用 left-padding 重跑。

---
