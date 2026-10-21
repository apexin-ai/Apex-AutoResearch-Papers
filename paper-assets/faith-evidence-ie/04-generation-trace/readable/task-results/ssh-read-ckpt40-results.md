# ssh read ckpt40 results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_read-ckpt40-results_20260514T230943_result.json`
- **Structured JSON:** [`377d05baafe909f371ad.json`](../../sessions/37/377d05baafe909f371ad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ckpt-40 Eval 结果

**进程状态**: 已完成，cuda:2 已释放 (0 MiB, 0% util)

**结果文件**: `/root/autodl-tmp/eval_results/lr5e6_r1_ckpt40/checkpoint-40/metrics.json`

### 关键指标

| 指标 | 值 |
|------|-----|
| **rel_f1 (ign_f1)** | **0.71%** |
| precision | 0.66% |
| recall | 0.78% |
| **evi_f1** | **75.84%** |
| evi_precision | 91.13% |
| evi_recall | 64.94% |
| **edcr** | **99.42%** |
| **format_ok_rate** | **99.39%** |
| pred_count | 14,434 |
| gold_count | 12,151 |
| tp | 95 |
| n_truncated | 424 |
| field_compliance_rate | 56.75% |
| 推理耗时 | 6152s (~102min) |

### 问题分析

rel_f1 极低 (0.71%)，而 pred_count (14,434) 与 gold_count (12,151) 量级接近，说明模型生成了大量预测但几乎全部不正确（tp 仅 95）。evi_f1 = 75.84% 表明证据抽取能力尚可，但关系分类严重崩坏。field_compliance_rate 仅 56.75%，有 424 条被截断，说明输出格式也有问题。

### GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 13,645 MiB | 47% |
| 1 | 9,719 MiB | 66% |
| **2** | **0 MiB** | **0%** |
| 3 | 9,713 MiB | 73% |

cuda:2 空闲，可用于下一个 eval。

---
