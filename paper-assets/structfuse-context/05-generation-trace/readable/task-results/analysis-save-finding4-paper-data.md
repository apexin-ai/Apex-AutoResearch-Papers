# analysis save finding4 paper data

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_save-finding4-paper-data_20260515T183721_result.json`
- **Structured JSON:** [`53a65a1d2d2560c1eb44.json`](../../sessions/53/53a65a1d2d2560c1eb44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已生成并注册。摘要：

| 模型 | 策略 | Seeds | R@1 mean | R@1 std (cross-seed) |
|------|------|-------|----------|---------------------|
| Qwen | random | s42/s43/s44 | 0.5696 | **2.71pp** |
| Qwen | embedding_distance | s43/s44 | 0.5774 | **2.38pp** |
| StarCoder | random | s42/s43/s44 | 0.4796 | **1.67pp** |

| Seed | embed − random delta |
|------|---------------------|
| s43 | +0.52pp |
| s44 | −0.66pp |
| mean \|delta\| | **0.59pp** |

**Ratio**: cross-seed std / within-seed strategy delta = **4.0–4.6×**

数据支持 Finding #4：seed noise（2.4–2.7pp）远大于策略效应（<0.7pp），且策略 delta 符号不一致，确认 paired comparison + cluster bootstrap 是方法论必需。

文件路径：`artifacts/analysis/seed_variance_vs_strategy_effect.json`

---
