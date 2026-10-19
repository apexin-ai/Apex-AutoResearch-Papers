# analyze perlayer kl 50 s42 downstream

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_perlayer_kl_50_s42_downstream_20260522T080709_result.json`
- **Structured JSON:** [`e27f583b0ee8ccfbacf8.json`](../../sessions/e2/e27f583b0ee8ccfbacf8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已完成分析并注册。结果摘要：

**Per-layer KL 50% downstream：确认 NEGATIVE**

| Task | Per-Layer KL 50% | E2E KL 50% | TEAL 50% | Dense |
|------|-----------------|------------|----------|-------|
| ARC-c | 0.271 | 0.328 | 0.275 | 0.583 |
| WinoGrande | 0.515 | 0.629 | 0.544 | 0.781 |
| MMLU | 0.266 | 0.278 | 0.293 | 0.653 |
| GSM8K | 0.017 | 0.021 | 0.017 | 0.488 |
| HellaSwag | 0.382 | 0.567 | 0.394 | 0.823 |
| PIQA | 0.628 | 0.691 | 0.637 | 0.809 |

所有 6 个 task 近乎随机水平。比 E2E KL 50% 平均低 7.24pp，比训练无关的 TEAL 50% baseline 还低 1.33pp。PPL 34.85 vs E2E KL 的 11.96，HellaSwag 崩塌最严重（-18.5pp vs E2E KL）。

分析报告已写入 `artifacts/perlayer_kl_50_s42_downstream/analysis.md`，registry 已更新为 DONE/negative。

---
