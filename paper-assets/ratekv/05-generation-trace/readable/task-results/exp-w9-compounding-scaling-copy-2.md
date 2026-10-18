# exp w9 compounding scaling

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_w9_compounding_scaling_20260515T043948_result.json`
- **Structured JSON:** [`9973aed5db03fc43ea62.json`](../../sessions/99/9973aed5db03fc43ea62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

W9 compounding scaling 实验完成。

**结果摘要 (Qwen2.5-7B, calibration PPL baseline=8.20):**

| n | sum_indiv | joint_ppl | predicted_ppl | ratio |
|---|-----------|-----------|---------------|-------|
| 1 | 6.74 | 14.94 | 14.94 | **1.00** |
| 2 | 8.86 | 42.26 | 17.06 | **3.84** |
| 4 | 11.42 | 3813.76 | 19.62 | **333.3** |
| 8 | 12.68 | 3586.42 | 20.89 | **282.1** |
| 16 | 13.97 | 7286.23 | 22.17 | **521.1** |
| 32 | 15.65 | 6644.05 | 23.85 | **424.0** |
| 64 | 17.71 | 9453.33 | 25.91 | **533.3** |

**关键发现：**
- n=1 完美 additive (ratio=1.0)，验证了 profiling 准确性
- n=2 已 3.84x super-additive — 同时量化 L0H0+L0H2（两个最 sensitive heads）导致 mutual interaction
- n≥4 时 PPL 爆炸到数千，ratio 280-533x — 尤其 top-4 全在 Layer 0 (all 4 KV heads)，同时量化一整层的 KV cache 是 catastrophic
- 这直接支撑论文 claim：greedy 方法不考虑 interaction，导致 unconstrained 68 heads@2bit 时 PPL 从 9.81 崩到 32.45

**产出：**
- JSON: `w9_compounding_scaling_results.json` (art_20260515_bfe7e5)
- Plot: `fig_compounding_scaling.png` (art_20260515_2b73c9)
- 运行时间: 96s on cuda:1

---
