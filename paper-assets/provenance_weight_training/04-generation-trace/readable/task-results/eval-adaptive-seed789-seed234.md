# eval adaptive seed789 seed234

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_adaptive_seed789_seed234_20260524T082739_result.json`
- **Structured JSON:** [`7242bee24801fa431696.json`](../../sessions/72/7242bee24801fa431696.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 adaptive N=5 实验的 eval 全部完成。完整结果如下：

## Adaptive N=5 Eval Results

### Perplexity (PPL)

| Dataset | adaptive_seed789 | adaptive_seed234 |
|---------|-----------------|-----------------|
| Holdout | **17.668** | 17.678 |
| OpenWebText (OOD) | 18.365 | **18.340** |
| Wikipedia (OOD) | **15.330** | 15.341 |

两个 seed 的 PPL 非常接近，差异在 0.03 以内，说明 adaptive weighting 在不同 seed 下稳定。

### Downstream Tasks (0-shot)

| Task | Metric | adaptive_seed789 | adaptive_seed234 |
|------|--------|-----------------|-----------------|
| ARC-Challenge | acc_norm | **33.79%** | 35.07% |
| ARC-Easy | acc | **64.94%** | 65.61% |
| HellaSwag | acc_norm | **48.09%** | 48.14% |
| PIQA | acc | **69.37%** | 68.55% |
| Winogrande | acc | **56.67%** | 57.30% |

Downstream 差异同样很小（±1% 以内），seed234 在 ARC 和 Winogrande 上略优，seed789 在 PIQA 上略优。两个 seed 的结果高度一致。

---
