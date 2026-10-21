# analysis icg contrastive kappa measurement

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_icg-contrastive-kappa-measurement_20260520T013308_result.json`
- **Structured JSON:** [`93b5e52ceb6b1193d752.json`](../../sessions/93/93b5e52ceb6b1193d752.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

| Method | κ | Eff-K | Acc% |
|---|---|---|---|
| **Debate** | 0.1549 | 4.44 | 38.24 |
| **Diverse-Prompt** | 0.4030 | 2.21 | ~57 |
| **SC** | 0.4384 | 2.02 | 56.86 |
| **ICG** | 0.7188 | 1.35 | 51.96 |
| **Contrastive** | 0.9643 | 1.03 | 47.55 |

**方法说明**：
- **ICG κ**：bootstrap 采样 5/10 个独立约束集 → dedup + MaxSAT + InvariantScorer → 12 个 bootstrap raters。204 题中 91 题(44.6%)在不同 bootstrap 间答案发生变化。
- **Contrastive κ**：对每个 candidate 的 pro/con 约束各采样 50% → 重跑 MaxSAT 评分 → 12 个 bootstrap raters。163 题（41 题 degenerate 跳过）中仅 8 题(4.9%)发生答案翻转。

**散点图故事**：5 个点呈现清晰的倒 U 形——Debate 过于独立(κ=0.15)但投票质量低 → acc 最低；SC/Diverse 处于甜点区(κ≈0.4)→ acc 最高；ICG/Contrastive 过于确定性(κ>0.7)→ 约束评分太稳定，无法从聚合中获益，acc 反而下降。Contrastive 几乎完全确定性(κ=0.96, Eff-K≈1)，相当于单一投票者。

数据已保存到 `artifacts/kappa_icg_contrastive.json` 和服务器 `results/kappa_icg_contrastive.json`。

---
