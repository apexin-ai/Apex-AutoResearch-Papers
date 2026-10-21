# analyze test eval 8b sft s42

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_test_eval_8b_sft_s42_20260521T230350_result.json`
- **Structured JSON:** [`ebd8629a5b9b89c62594.json`](../../sessions/eb/ebd8629a5b9b89c62594.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已清除或未以该 ID 注册），无需处理。

## 诊断结果

**状态：成功** — 500/500 文档推理完成，耗时 4h29m。

### Metrics

| 指标 | 值 |
|------|-----|
| F1 / Ign-F1 | 0.3106 |
| Evi-F1 (DREEAM) | 0.2279 |
| Evi-F1 (TP) | 0.5949 |
| EDCR | 0.8432 |
| Precision | 0.4543 |
| Recall | 0.2359 |
| Format OK | 498/500 (99.6%) |
| Truncated | 410/500 |

### GPU 状态

| GPU | 显存占用 |
|-----|---------|
| cuda:0 | 6,071 MiB |
| cuda:1 | 32,503 MiB |
| **cuda:2** | **0 MiB** ✓ 已释放 |
| cuda:3 | 18,879 MiB |

Registry 已更新为 DONE/success。cuda:2 已完全释放。

---
