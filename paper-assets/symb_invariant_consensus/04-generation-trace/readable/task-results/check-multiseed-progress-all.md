# check multiseed progress all

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_multiseed-progress-all_20260523T043503_result.json`
- **Structured JSON:** [`885e36a6d3e0811e6c17.json`](../../sessions/88/885e36a6d3e0811e6c17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 多种子实验进度汇总

### westd-16639

| 实验 | 进度 | SC% | SICA% | Δ | 状态 |
|------|------|-----|-------|---|------|
| **mistral_pw_seed42** | 600/600 | 40.00 | 36.67 | -3.33pp | **完成** |
| **mistral_pw_seed123** | 600/600 | 40.83 | 37.50 | -3.33pp | **完成** |
| **mistral_pw_seed456** | 600/600 | 39.83 | 38.67 | -1.17pp | **完成** |
| **mistral_pw_seed789** | 600/600 | 38.83 | 37.17 | -1.67pp | **完成** |
| qwen25_pw_seed456 | 463/600 | 73.87 | 72.79 | -1.08pp | 运行中，ETA ~15:00 UTC |
| qwen25_pw_seed123 | 441/600 | 73.24 | 71.66 | -1.59pp | 运行中，ETA ~15:30 UTC |
| llama8b_pw_seed123 | 399/600 | 73.18 | 64.91 | -8.27pp | 运行中，ETA ~16:40 UTC |
| qwen25_pw_seed789 | 24/600 | — | — | — | 运行中，ETA ~22:35 UTC |
| llama8b_pw_seed42 | 223/600 | — | — | — | **无活跃进程，疑似停止** |

### westd-14391

| 实验 | 进度 | SC% | SICA% | Δ | 状态 |
|------|------|-----|-------|---|------|
| llama8b_pw_seed42 | 550/600 | 72.36 | 66.73 | -5.64pp | 运行中，ETA ~13:20 UTC |
| llama8b_pw_seed123 | 0/600 | — | — | — | **目录空，未启动** |
| llama8b_pw_seed456 | 0/600 | — | — | — | **目录空，未启动** |

### 关键发现

**所有实验 Δ 均为负值** — SICA 一致低于 SC。已完成的 Mistral 4 个种子平均 Δ = -2.38pp。Qwen 和 LLaMA 的中间结果也呈现相同趋势（Qwen Δ 约 -1~-2pp，LLaMA Δ 约 -5~-8pp）。

### 需要关注

1. westd-16639 的 `llama8b_pw_seed42` (223/600) 无活跃进程，需确认是否需要重启
2. westd-14391 的 `llama8b_pw_seed123` 和 `llama8b_pw_seed456` 尚未启动

---
