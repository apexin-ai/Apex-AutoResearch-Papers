# analysis kl only s1

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl_only_s1_20260515T175828_result.json`
- **Structured JSON:** [`32ed177f53cf0d7cf44c.json`](../../sessions/32/32ed177f53cf0d7cf44c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。

## 汇总

**kl_only_s1** (KL normalized v3, seed=1) — **success**

| Metric | s1 | s42 | s123 | s456 |
|--------|-----|-----|------|------|
| Hard-mask PPL | **9.15** | 9.21 | 9.25 | 9.14 |
| TEAL Sparse PPL | **11.99** | 12.08 | 11.91 | 13.58 |
| PPL increase | **31.0%** | 31.2% | 28.8% | 48.6% |
| Model sparsity | **0.498** | 0.498 | 0.498 | 0.498 |

s1 与 s42/s123 高度一致，属于 4 个 seed 中表现较好的一组（s456 是 outlier）。还差 1 个 seed 即可凑齐 5-seed headline。

---
