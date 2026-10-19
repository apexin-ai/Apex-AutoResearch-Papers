# analysis bce isocompute v2 eval

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bce_isocompute_v2_eval_20260515T204012_result.json`
- **Structured JSON:** [`fc1b4ef59afe4d425386.json`](../../sessions/fc/fc1b4ef59afe4d425386.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完毕。

---

## 总结

### bce_isocompute_v2_s42 完整分析

**训练**：
- 1000 steps 正常完成，sparsity 精确收敛到 0.50（STE 修复成功）
- BCE loss 下降极有限：0.6714 → 0.6586（仅比随机猜测好 5%）

**Eval**：
| Metric | PPL |
|--------|-----|
| true_dense | 6.12 |
| predictor hard mask | 26.76 |
| **teal_sparse** | **54.84** |

**vs KL baseline (50% sparsity)**: 54.84 vs 12.00 — BCE 差 4.6x

**结论**: BCE 作为 sparsity predictor 的训练 loss 不可行。独立二分类丢失 neuron 间协同关系，信号密度远低于 KL 的输出分布匹配。建议放弃 BCE 方向，KL normalized 是明确更优的 loss。

---
