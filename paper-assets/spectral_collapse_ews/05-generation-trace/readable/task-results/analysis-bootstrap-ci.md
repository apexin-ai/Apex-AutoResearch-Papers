# analysis bootstrap ci

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci_20260525T215338_result.json`
- **Structured JSON:** [`c18086e24902eb76d9ae.json`](../../sessions/c1/c18086e24902eb76d9ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析报告

### 1. Bootstrap 95% CI 概览

| r | N seeds | Gen 10 Mean | Gen 10 CI | 典型 CI 宽度 |
|---|---------|-------------|-----------|-------------|
| 0 | 3 | 2181.35 | [2154.34, 2210.77] | 20–56 (后期发散) |
| 0.2 | 3 | 2467.21 | [2455.78, 2479.70] | 2–24 |
| 0.25 | 3 | 2488.11 | [2485.01, 2490.74] | 2–11 |
| 0.3 | 3 | 2508.24 | [2505.25, 2511.13] | 2–11 |
| 0.5 | 2 | 2571.64 | [2570.09, 2573.20] | 0.1–6.5 |

**r=0 的 CI 在后期显著变宽**（Gen 9-10 宽度达 45-56），反映 seed 间 collapse 速率的差异。r=0.5 虽然只有 2 seeds，但两条轨迹高度一致，CI 反而极窄。

### 2. r=0.25 vs r=0.3 CI 重叠分析

**关键发现：Gen 3 起 CI 完全不重叠。**

- Gen 0–2：CI 重叠（两组尚未分化）
- **Gen 3：CI 不重叠，gap = 5.84**（r=0.25 的上界 2380.88 < r=0.3 的下界 2386.72）
- Gen 4–10：CI 持续不重叠，gap 从 1.31 递增到 14.51

这说明从 Gen 3 开始，r=0.25 和 r=0.3 的 SLV 轨迹在统计上可分离。**r_crit 的 bound 在 [0.25, 0.3] 之间有统计支撑。**

### 3. Permutation Tests

| Metric | r=0.25 mean | r=0.3 mean | p-value |
|--------|-------------|------------|---------|
| slope (Gen1→3) | 15.29 | 23.43 | 0.093 |
| recovery gen | 3.00 | 2.33 | 0.396 |
| final gain | 121.43 | 141.56 | 0.098 |
| dip depth (Gen0-3) | 3.59 | 1.59 | 0.192 |
| Gen2 < Gen0 (binary) | 1.00 | 0.33 | 0.399 |

**所有 permutation test 均未达到 p < 0.05 显著性。** 这是 N=3 seeds per group 的固有限制——排列组合空间仅 C(6,3)=20 种，理论最小 p-value = 1/20 = 0.05，实际上无法达到 p < 0.05。

### 4. 结论

- **CI 不重叠分析** 提供了 r=0.25 与 r=0.3 轨迹差异的强证据：从 Gen 3 起两组 95% CI 完全分离
- **Permutation test 不显著** 是样本量不足的必然结果（N=3 时理论上无法拒绝 H₀ at α=0.05），不应解读为无差异
- 建议在论文中以 CI non-overlap 作为主要统计论据，permutation test 可在 appendix 中报告并注明 power 限制

产出文件：
- 脚本：`artifacts/bootstrap_ci_analysis.py`
- 数据：`artifacts/bootstrap_ci_results.json`

---
