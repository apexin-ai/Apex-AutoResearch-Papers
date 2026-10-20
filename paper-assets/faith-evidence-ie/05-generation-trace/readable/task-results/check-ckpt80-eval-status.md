# check ckpt80 eval status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ckpt80_eval_status_20260515T005716_result.json`
- **Structured JSON:** [`bf70a2d9ae3ffc898ec7.json`](../../sessions/bf/bf70a2d9ae3ffc898ec7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**实验已正常完成。** 结果目录为 `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt80/`（命名与预期略有不同）。

### 关键指标

| 指标 | 值 |
|------|-----|
| **rel_f1 (f1)** | **0.0116** |
| ign_f1 | 0.0116 |
| **evi_f1** | **0.8280** |
| **edcr** | **0.9908** |
| **format_ok_rate** | **0.9990** |
| pred_count | 13,828 |
| gold_count | 12,151 |
| tp | 151 |
| precision | 0.0109 |
| recall | 0.0124 |
| evi_precision | 0.9277 |
| evi_recall | 0.7476 |
| field_compliance_rate | 0.7878 |
| n_truncated | 210 |
| **inference_time_seconds** | **6099.3s (~1h42m)** |

### 判断

- 进程正常退出（结果文件完整，有 metrics.json + predictions.json）
- GPU 2 已释放（0 MiB, 0%）
- **rel_f1 极低（0.0116）**，而 evi_f1（0.828）和 edcr（0.991）都很好 — 说明模型能找到正确的 evidence 句子并避免 distractor citation，但关系抽取本身几乎完全失败（13,828 预测中只有 151 个 TP）

---
