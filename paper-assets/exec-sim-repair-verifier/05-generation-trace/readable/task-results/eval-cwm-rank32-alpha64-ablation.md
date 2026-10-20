# eval cwm rank32 alpha64 ablation

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cwm-rank32-alpha64-ablation_20260515T154433_result.json`
- **Structured JSON:** [`557341ffbd6189402966.json`](../../sessions/55/557341ffbd6189402966.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果报告：

---

## CWM Rank Ablation 结果对比

| 配置 | Rank | Alpha | Alpha/Rank | Accuracy | F1_fail | F1_pass | F1_macro | Exact Match |
|------|------|-------|------------|----------|---------|---------|----------|-------------|
| **Baseline (rank16)** | 16 | 32 | 2.0 | **87.51%** | — | — | — | — |
| Rank32 v2 | 32 | 32 | 1.0 | 87.0% | — | — | — | — |
| **Rank32 alpha64** | 32 | 64 | 2.0 | **87.04%** | 87.27% | 86.79% | 87.03% | 84.55% |

### 结论：**Negative**

- Rank32 alpha64 (87.04%) vs Baseline rank16 (87.51%)：**-0.47pp**，增大 rank 无收益
- Rank32 alpha64 (87.04%) vs Rank32 v2 alpha32 (87.0%)：**+0.04pp**，修正 alpha/rank ratio 后几乎无差异
- 说明之前 rank32 v2 的性能下降主要不是 alpha/rank ratio 的问题，而是 rank=32 本身对这个任务没有帮助

LoRA rank 从 16 增到 32（参数量翻倍）并不能提升 CWM 分类性能，rank=16 已经足够。Registry 已更新为 DONE/negative。

---
