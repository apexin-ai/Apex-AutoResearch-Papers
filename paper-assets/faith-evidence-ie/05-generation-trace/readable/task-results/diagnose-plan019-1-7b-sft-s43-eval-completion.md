# diagnose plan019 1 7b sft s43 eval completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_plan019_1_7b_sft_s43_eval_completion_20260518T220228_result.json`
- **Structured JSON:** [`46f59b61cfbf8904fa8a.json`](../../sessions/46/46f59b61cfbf8904fa8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果报告

**plan019_1_7b_sft_s43_eval: 成功完成** ✓

### 指标

| 指标 | 值 |
|---|---|
| **Ign-F1** | **0.4286** |
| F1 | 0.4372 |
| Precision / Recall | 0.4704 / 0.4084 |
| Evi-F1 (TP) | 0.8350 |
| Evi-F1 (Joint) | 0.3442 |
| EDCR | 0.7040 |
| Format Compliance | 100% |
| Field Compliance | 58.6% |
| Truncated | 408/985 |
| Predictions | 18,140 |
| Inference Time | 5,257s |

### 1.7B 3-Seed 汇总

| Seed | Ign-F1 |
|---|---|
| s42 | 0.4786 |
| **s43** | **0.4286** |
| s44 | 0.4321 |
| **Mean ± Std** | **0.4464 ± 0.0224** |

s43 是三个 seed 中最低的，且与 s42 差距较大（0.05），标准差偏高。

### GPU 状态

- **cuda:0**: 空闲 (0MiB)
- **cuda:1**: 空闲 (0MiB)
- cuda:2: 占用 18.5GB (PID 577861)
- cuda:3: 占用 11GB (PID 571120)

Registry 已更新为 DONE/success，cron 已清除。

---
