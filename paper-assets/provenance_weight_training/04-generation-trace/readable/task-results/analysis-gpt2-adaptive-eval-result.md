# analysis gpt2 adaptive eval result

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2_adaptive_eval_result_20260518T232739_result.json`
- **Structured JSON:** [`79373b1bab88df001624.json`](../../sessions/79/79373b1bab88df001624.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPT-2 Adaptive Eval 结果

| 实验 | PPL | Loss |
|------|-----|------|
| GPT-2 uniform | 17.69 | - |
| **GPT-2 adaptive** | **17.79** | **2.8789** |
| Δ | **+0.10** | - |

**负向结果。** GPT-2 adaptive PPL = 17.79，比 uniform baseline (17.69) 高 0.10，方向相反。

对比 TF-IDF 结果（adaptive 17.65 vs uniform 17.69, Δ = -0.04），GPT-2 detector 尽管 AUC=0.913，但其 adaptive weighting 没有带来收益，反而略微恶化。这与 n-gram detector 的负向结果类似，说明 detector AUC 高不等于能产生有效的训练权重信号。TF-IDF detector 可能在某种特征维度上更好地区分了对训练有用的样本。

---
