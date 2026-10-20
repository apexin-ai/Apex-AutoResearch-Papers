# diagnose llama rsft s44 pipeline

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama_rsft_s44_pipeline_20260520T041717_result.json`
- **Structured JSON:** [`a780a95bfd63046e53f7.json`](../../sessions/a7/a780a95bfd63046e53f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。Cron 无注册（可能由其他机制管理），无需清除。

## 结果汇总

### llama_rsft_s44_pipeline: **SUCCESS**

**核心指标 (metrics.json 原始数据)**:

| Metric | Value |
|--------|-------|
| **Ign-F1** | **0.5587** |
| F1 | 0.5706 |
| Ign-Precision | 0.5574 |
| Ign-Recall | 0.5601 |
| Evi-F1 (DREEAM joint) | 0.4609 |
| Evi-F1 (TP) | 0.8328 |
| EDCR | 0.5829 |
| Format OK | 985/985 (100%) |
| Truncated | 166/985 |
| Predictions | 14,685 |

### 3-Seed 汇总 (LLaMA-3.1-8B RSFT K=1)

| Seed | Ign-F1 |
|------|--------|
| s42 | 0.5839 |
| s43 | 0.5662 |
| s44 | 0.5587 |

**Mean: 0.5696 ± 0.0129** (sample std, N=3)

s44 是三个 seed 中最低的，s42 最高（0.5839），方差 0.0129 在 RE 任务中属正常范围。

---
