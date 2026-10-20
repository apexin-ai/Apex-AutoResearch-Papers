# analyze qwen15b label only seed456 v2

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen15b_label_only_seed456_v2_20260520T211519_result.json`
- **Structured JSON:** [`b09e05a08597317bf077.json`](../../sessions/b0/b09e05a08597317bf077.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已标记 DONE(success)。汇总如下：

## qwen15b_label_only_seed456_v2 结果

| Metric | Value |
|--------|-------|
| **Accuracy** | **82.52%** [80.3%, 84.7%] |
| Pass F1 | 0.885 (P=0.837, R=0.938) |
| Fail F1 | 0.639 (P=0.776, R=0.543) |
| Train/Eval Loss | 0.239 / 0.306 |

## Qwen-1.5B label_only 3-Seed 汇总

| Seed | Accuracy | Pass F1 | Fail F1 |
|------|----------|---------|---------|
| 42 | 78.90% | 0.860 | 0.570 |
| 123 | 81.34% | 0.878 | 0.602 |
| 456 | 82.52% | 0.885 | 0.639 |
| **Mean ± Std** | **80.92% ± 1.85%** | **0.874 ± 0.013** | **0.604 ± 0.035** |

## vs Qwen-7B

- Qwen-7B label_only 3-seed: **85.94% ± 1.12%**
- Qwen-1.5B label_only 3-seed: **80.92% ± 1.85%**
- Scale gap: **~5.0pp**，1-std 范围不重叠（1.5B 上界 82.8% < 7B 下界 84.8%）

Seed 456 是 3 个 seed 中最好的，3-seed 数据现在与 Qwen-7B 可比。分析已写入 `artifacts/qwen15b_label_only_seed456_v2/analysis.md`，registry 已更新为 DONE(success)。

---
