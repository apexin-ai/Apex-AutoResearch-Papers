# exp 14b cross ref 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_14b_cross_ref_001_20260521T070619_result.json`
- **Structured JSON:** [`d9799036cef8b864b548.json`](../../sessions/d9/d9799036cef8b864b548.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 `14b_cross_ref_001` 完成。

## 结果摘要

### Self-ref (Qwen2.5-14B) vs Cross-ref (Pythia-1.4B) — 4-class accuracy

| Strategy | Self-ref | Cross-ref | Delta |
|----------|---------|-----------|-------|
| nucleus  | 54.05%  | 44.97%    | -9.08pp |
| temp09   | 50.50%  | 46.33%    | -4.17pp |
| topk50   | 47.93%  | 40.85%    | -7.08pp |
| **avg**  | **50.83%** | **44.05%** | **-6.78pp** |

### Cross-ref 关键 metrics

| Strategy | d1d3 bal acc | d0v1 AUC | d1v2 AUC | d2v3 AUC | EDD(T=0.70) |
|----------|-------------|----------|----------|----------|-------------|
| nucleus  | 39.47%      | 0.70     | 0.73     | 0.60     | 2           |
| temp09   | 40.29%      | 0.74     | 0.72     | 0.61     | 2           |
| topk50   | 35.27%      | 0.70     | 0.68     | 0.54     | 0           |

### 解读

- Cross-ref 比 self-ref 低 4-9pp，符合预期：Pythia-1.4B (1.4B) 计算 Qwen2.5-14B (14B) 生成文本的 perplexity 时，模型架构/tokenizer 不匹配导致特征信噪比降低。
- 但 cross-ref 在全部 3 个策略上仍远高于 25% chance，深度信号依然可检测。
- EDD(T=0.70): nucleus/temp09 仍可区分到 depth 2，topk50 边界（d0v1 AUC=0.699 极接近 0.70）。
- 结论：reference model 选择影响准确率绝对值（-6.78pp），但不改变深度信号存在的核心结论。可回应 R17。

---
