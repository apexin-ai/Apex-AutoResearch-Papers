# analyze acc batch analyzing

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_acc_batch_analyzing_20260515T232621_result.json`
- **Structured JSON:** [`3051db955d8a2f2ed3a2.json`](../../sessions/30/3051db955d8a2f2ed3a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已更新为 DONE。

---

## 结果汇总

### 1. acc_ds_dense_8k_v2 (DS dense baseline)

| 指标 | 值 |
|------|-----|
| Accuracy | **74.0%** (37/50) |
| Truncation rate | 16.0% (8/50) |
| Avg tokens | 3126 |
| max_new_tokens | 8192 |
| 数据文件 | `/root/autodl-tmp/pacs/analysis_output/accuracy_ds_dense_8k_v2.json` |

### 2. acc_qw_s025_n100_b2_fix (QW s025 batch2)

| 指标 | 值 |
|------|-----|
| Accuracy | **34.0%** (17/50) |
| Truncation rate | 6.0% (3/50) |
| Avg tokens | 1044 |
| max_new_tokens | 8192 |
| 数据文件 | `/root/autodl-tmp/pacs/analysis_output/accuracy_eval_qw_s025_b2_fix.json` |

### 3. QW s025 合并 n=100

| 部分 | Correct | N | Accuracy | max_new_tokens |
|------|---------|---|----------|----------------|
| Batch1 (problems 1-50) | 16 | 50 | 32.0% | **2048** |
| Batch2_fix (problems 51-100) | 17 | 50 | 34.0% | **8192** |
| **合并** | **33** | **100** | **33.0%** | — |

**⚠️ 注意：** Batch1 的 `max_new_tokens=2048`，batch2_fix 的 `max_new_tokens=8192`，两批参数不一致。如果要用于论文 dose-response curve，batch1 可能也需要用 8192 重跑以保持一致。

---
