# ssh bh fdr calculation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_bh_fdr_calculation_20260522T092949_result.json`
- **Structured JSON:** [`1bdea63619e1afd186d7.json`](../../sessions/1b/1bdea63619e1afd186d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果已获取。以下是 BH FDR vs Holm-Bonferroni 对比总结：

---

## 全局对比 (α=0.05, k=57)

| 方法 | 拒绝数 |
|------|--------|
| 未校正 | 23/57 |
| **BH FDR** | **19/57** |
| **Holm-Bonferroni** | **10/57** |

BH 比 Holm 多拒绝 9 个检验。所有 Holm 显著的检验在 BH 下也显著（BH 严格更宽松）。

## BH 显著但 Holm 不显著的 9 个检验

| # | 描述 | Raw p | BH-adj | Holm-adj |
|---|------|-------|--------|----------|
| 18 | SciERC LP sel, non-tied (eps=0.05) | 0.004 | 0.0143 | 0.180 |
| 20 | SciERC LP favorable subset (+2.47pp) | 0.015 | 0.0450 | 0.585 |
| 22 | SciERC LP-wt construction (Qwen, 3-seed) | 0.004 | 0.0143 | 0.180 |
| 25 | Few-NERD uniform construction (Qwen) | 0.003 | 0.0143 | 0.138 |
| 27 | SciERC ZS construction (72B) | 0.008 | 0.0253 | 0.320 |
| 43 | RE SJ ρ Q1 vs Q4 sent len (Fisher z) | 0.004 | 0.0143 | 0.180 |
| 45 | Per-type deg-headroom (Few-NERD, Spearman) | 0.004 | 0.0143 | 0.180 |
| 46 | Per-type deg-headroom (exact perm) | 0.005 | 0.0168 | 0.205 |
| 57 | WNUT-17 conditional ρ FK | 0.002 | 0.0104 | 0.094 |

## Selection 家族 (21 tests)

| 校正范围 | 显著数 (α=0.05) |
|----------|-----------------|
| Global BH (k=57) | 5/21 (#6, #18, #19, #20, #21) |
| Selection-family BH (k=21) | 4/21 (#6, #18, #19, #21) |
| Primary-selection BH (k=18, 排除 post-hoc) | 2/18 (#6, #19 — 均为 Few-NERD) |

## 按家族 BH 校正结果 (α=0.05)

| 家族 | 显著/总数 |
|------|-----------|
| Selection | 4/21 |
| Construction | 6/10 |
| Signal Δρ | 4/9 |
| Calibration | 0/3 |
| Correlation | 2/6 |
| FS error | 1/4 |
| Other | 2/4 |

## 核心 NER claims 状态

| Claim | Holm | BH | 判定 |
|-------|------|----|------|
| **"No signal reliably beats greedy" (selection)** | 15/21 不显著 → 成立 | 同，核心 null 不变 | **两种方法下均成立** |
| Few-NERD LP selection (#6, #19) | 显著 | 显著 | 一致 |
| Construction gains (#22, #24, #25, #27, #31) | Holm 仅 #24, #31 显著 | BH 额外 #22, #25, #27 显著 | **BH 下 construction 证据更强** |
| Per-type deg-headroom (#45, #46) | 不显著 | 显著 | **BH 下新增显著** |

## 结论

BH FDR 不削弱任何论文 claim。核心 null finding（selection 不优于 greedy）依赖于大量 p > 0.05 的检验，在任何校正下都不显著。BH 比 Holm 宽松，只会保留或增加显著结果——construction 和 correlation 方向的证据在 BH 下反而更强。

## Rebuttal 速查表

| FDR α | 拒绝数 | Selection 显著 | 结论 |
|-------|--------|----------------|------|
| 0.01 | 10 | #6, #19, #21 | 核心 null 不变 |
| 0.05 | 19 | #6, #18, #19, #20, #21 | 核心 null 不变 |
| 0.10 | 21 | 同上 | 核心 null 不变 |
| 0.20 | 26 | +#8, #13 | 核心 null 不变 |
| Holm | 10 | (none) | 论文当前方法 |

---
