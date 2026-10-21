# eval 1 7b ood cuda01

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_1_7b_ood_cuda01_20260520T143427_result.json`
- **Structured JSON:** [`530cb4012c09201ccc71.json`](../../sessions/53/530cb4012c09201ccc71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

## 1.7B OOD PPL 结果

| Model | OpenWebText | Wikipedia |
|-------|------------|-----------|
| uniform_1_7b | **13.291** | **10.919** |
| adaptive_1_7b | **13.282** | **10.955** |
| Δ (adaptive − uniform) | **−0.009** | **+0.036** |

两个模型在 OOD 数据上几乎无差异。Adaptive 在 OWT 上微弱优势（−0.009），在 Wikipedia 上微弱劣势（+0.036），差异都在噪声范围内。与 0.6B 的格局一致——adaptive weighting 在 OOD 泛化上未显著偏离 uniform baseline。

---
