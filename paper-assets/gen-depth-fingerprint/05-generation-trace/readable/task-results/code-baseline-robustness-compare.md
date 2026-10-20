# code baseline robustness compare

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline-robustness-compare_20260516T230349_result.json`
- **Structured JSON:** [`304a8aa4b4a56a55e567.json`](../../sessions/30/304a8aa4b4a56a55e567.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果已保存到 `/root/gen-depth-fingerprint/experiments/human_edit_robustness/baseline_robustness.json`。

**关键发现：**

| Method | 0% | 5% | 10% | 20% | Drop@20% |
|--------|----|----|-----|-----|----------|
| ld_score | 0.677 | 0.673 | 0.677 | 0.671 | **0.006** |
| fastdetectgpt | 0.571 | 0.437 | 0.468 | 0.514 | 0.058 |
| binoculars | 0.500 | 0.461 | 0.446 | 0.425 | 0.075 |
| 7-feature (ref) | 0.695 | 0.650 | 0.614 | 0.591 | 0.104 |
| avg_logprob | 0.682 | 0.419 | 0.335 | 0.375 | **0.307** |

- **Most robust**: `ld_score` (仅 0.6% 退化，trigram 分布对词替换几乎不敏感)
- **Least robust**: `avg_logprob` (30.7% 退化，token-level NLL 对任何文本变化极其敏感)
- 7-feature 的退化 (10.4%) 介于 binoculars 和 avg_logprob 之间，属中等鲁棒性
- fastdetectgpt 和 avg_logprob 在扰动下出现非单调行为（可能因为扰动改变了 curvature 分布的方向性）

---
