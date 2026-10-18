# analysis exp 007 340m rebound

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-007-340m-rebound_20260519T185316_result.json`
- **Structured JSON:** [`45844ff333fcf0b89b5a.json`](../../sessions/45/45844ff333fcf0b89b5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

### (a) Cross-Architecture Convergence (340M)
| Ratio | σ | vs 1.3B σ |
|-------|------|-----------|
| pure | 0.0248 | 1.03× (持平) |
| h24-1 | 0.0116 | 0.71× |
| h12-1 | 0.0178 | 1.31× |
| **h6-1** | **0.0110** | 1.82× |
| h3-1 | 0.0160 | 3.24× |

- **Non-monotonic rebound 确认**：σ 在 h6-1 最低 (0.011)，h3-1 回弹到 0.016
- Peak reduction: 55.6%，endpoint reduction: 35.5%
- 340M 的 rebound 比 1.3B 更强（1.3B 的 σ 持续下降到 0.00494）

### (b) Per-Example Helped/Hurt
- GDN: helped=422, hurt=678 (net -256) — attention 伤害 GDN
- RetNet: helped=373, hurt=479 (net -106)
- HGRN2: helped=575, hurt=337 (net **+238**) — attention 帮助 HGRN2
- **Pairwise Jaccard 极低** (~0.08-0.11)：各架构被 help/hurt 的是不同的样本

### (c) Cross-Scale Jaccard
- GDN: helped_J=0.047, hurt_J=0.087
- HGRN2: helped_J=0.089, hurt_J=0.055
- RetNet: null（1.3B RetNet-pure log_samples 数据异常，全部 acc=0）
- **跨 scale 的 per-example 效应几乎不重叠**

### (d) Rebound 样本特征
- Rebound samples: 1165, stay-correct: 1432
- Context length **无显著差异** (mean ~58.5 words, Mann-Whitney p=0.31)
- **关键发现**：rebound 样本的 pure acc rate = 0.519，stay-correct 的 = 0.763 — rebound 样本本身就更难（baseline 正确率低 24pp）

### (e) Attention Ratio Evolution
- **h6-1→h3-1** 是所有架构唯一的共同 hurt 转折点（GDN net=-129, RetNet net=-8, HGRN2 net=-37）
- GDN 路径非单调：先降后升再降 (pure→h12-1 净减少, h12-1→h6-1 净增 132, h6-1→h3-1 再减 129)
- HGRN2 持续受益直到 h6-1，在 h3-1 才首次转负

---
