# code temp07 pilot pythia 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_temp07_pilot_pythia_001_20260515T155152_result.json`
- **Structured JSON:** [`f28263be8fe6cec8a004.json`](../../sessions/f2/f28263be8fe6cec8a004.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

τ=0.7 Temperature Pilot 完成。总结：

**d1v2 AUC 无反转**——τ=0.7 下 Pythia-1.4B 的 depth-1 vs depth-2 可分性与 τ=0.9 基本持平：

| | RF | LR |
|---|---|---|
| τ=0.7 (本次) | 0.8378 | 0.8031 |
| τ=0.9 (baseline) | 0.8327 | 0.7833 |
| Δ | +0.005 | +0.020 |

这说明之前在 cross-strategy LOO 中观察到的低 AUC（GPT-2 XL 0.129, OLMo 0.253）并非由温度差异造成，而是**模型本身**的特性差异。Pythia 在两个温度下都保持了 0.83+ 的 d1v2 AUC。

附带发现：相邻深度 AUC 随递归深度单调递减（d1v2=0.84 → d2v3=0.64 → d3v4=0.60 → d4v5=0.60），表明高深度间的统计信号趋于饱和。

---
