# exp review exp b topic drift

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-exp-b-topic-drift_20260515T122416_result.json`
- **Structured JSON:** [`3323b95ab73782996d79.json`](../../sessions/33/3323b95ab73782996d79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**(a) 语义相似度随深度递增**（语义漂移递减）：
| 转换 | cosine sim |
|------|-----------|
| 0→1 | 0.622 ± 0.165 |
| 1→2 | 0.683 ± 0.184 |
| 2→3 | 0.801 ± 0.201 |
| 3→4 | 0.859 ± 0.190 |

深层生成文本趋于语义收敛（similarity 从 0.62 升到 0.86），最大漂移发生在 depth 0→1。

**(b) Prompt type 对比**（Pythia-2.8B）：
- continuation: avg_sim = 0.717（漂移最大）
- elaboration: avg_sim = 0.809
- inspired_rewriting: avg_sim = 0.808

**(c) Shape features 与语义漂移——弱相关** ✓：
- entropy_std: ρ = **-0.164**
- tail_decay: ρ = **0.068**

两者 |ρ| < 0.2，说明 shape features 捕捉的信号与 topic drift 大部分正交。

**(d) Drifting features 与语义漂移——也较弱**：
- hapax_ratio: ρ = **-0.124**
- ttr: ρ = **-0.178**
- entropy_mean: ρ = **-0.286**

drifting features 的 |ρ| 略高于 shape features（尤其 entropy_mean），但仍远低于预期的 0.3-0.5 范围。所有 features 与语义漂移的相关性都较弱，进一步说明 depth fingerprint 捕捉的不仅仅是 topic shift。

---
