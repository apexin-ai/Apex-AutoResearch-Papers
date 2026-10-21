# analysis exp 015 eval metrics

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_015_eval_metrics_20260514T114128_result.json`
- **Structured JSON:** [`9ed111aae6e51ed85365.json`](../../sessions/9e/9ed111aae6e51ed85365.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-015 结果摘要

**数据**: pilot_005 (T=0.7, N=8), 551 instances, 全部 5 信号在同一数据集上计算。

### NER (full, n=529)

| Signal | ρ | τ | AUROC |
|--------|-----|-----|-------|
| Entity Voting | **0.502** | **0.377** | **0.728** |
| Soft Jaccard (SJ) | 0.357 | 0.266 | 0.666 |
| Fleiss' Kappa | 0.265 | 0.203 | 0.624 |
| Exact Match | 0.257 | 0.192 | 0.623 |
| Mean Log-prob | 0.140 | 0.101 | 0.558 |

### RE (full, n=397)

| Signal | ρ | τ | AUROC |
|--------|-----|-----|-------|
| Entity Voting | **0.422** | **0.327** | **0.716** |
| Fleiss' Kappa | 0.253 | 0.197 | 0.631 |
| Mean Log-prob | 0.247 | 0.181 | 0.635 |
| Soft Jaccard (SJ) | 0.211 | 0.162 | 0.582 |
| Exact Match | 0.100 | 0.084 | 0.504 |

### 关键发现

1. **Entity Voting 在所有设置下均为最强信号**，NER ρ=0.50、RE ρ=0.42，显著优于 SJ（bootstrap CI 不含 0）

2. **SJ > FK > Exact Match > Log-prob**（NER full），SJ 对 FK/EM/logprob 的优势均统计显著

3. **RE full 设置下 SJ 较弱**（ρ=0.21），但 conditional 设置跳回 0.37，说明大量 gold-empty 实例稀释了信号

4. **LOO-SJ**：|Δρ| < 0.001（NER 和 RE），circularity 完全不是问题

5. **Calibration**：Entity Voting 和 SJ 展现单调递增的 F1-confidence 关系；Exact Match 在 RE 上 calibration 不单调（bin 4 回落）

---
