# ops harvest tail2048 results

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_tail2048_results_20260517T154432_result.json`
- **Structured JSON:** [`741b7d3a3254c4f0a843.json`](../../sessions/74/741b7d3a3254c4f0a843.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. Qwen-1.5B tail-2048（cuda:1）
- **状态**：Running
- **进度**：283/444 steps (64%)，epoch 1.89
- **已用时间**：~29 min
- **预计剩余**：~15 min（日志显示 `15:24` remaining，5.74s/it）
- **当前指标**：loss 0.0307, mean_token_accuracy 0.9913

### 2. DeepSeek-6.7B tail-2048（cuda:0）
- **状态**：Running
- **进度**：160/444 steps (36%)，epoch 1.08
- **已用时间**：~47 min
- **预计剩余**：~84 min（日志显示 `1:23:48` remaining，17.71s/it）
- **当前指标**：loss 0.0553, mean_token_accuracy 0.9832

两个实验 GPU 利用率均为 100%，训练正常进行。Qwen-1.5B 预计约 15 分钟后完成训练+eval，DeepSeek-6.7B 预计约 1.5 小时后完成。

---
