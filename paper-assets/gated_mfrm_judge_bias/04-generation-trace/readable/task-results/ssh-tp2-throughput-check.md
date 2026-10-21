# ssh tp2 throughput check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_tp2-throughput-check_20260524T110638_result.json`
- **Structured JSON:** [`43351e5cac09f9878a50.json`](../../sessions/43/43351e5cac09f9878a50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 进程 — 全部正常运行

| 组件 | 端口/配置 | GPU | 状态 |
|------|-----------|-----|------|
| vLLM LLaMA-3.3-70B-AWQ | :8001, TP=2 | GPU 0,1 | 运行中, 200 OK |
| vLLM Qwen2.5-72B-AWQ | :8002, TP=2 | GPU 2,3 | 运行中, 200 OK |
| collect LLaMA (workers=32) | — | — | 运行中 |
| collect Qwen (workers=32) | — | — | 运行中 |
| collect Claude-Sonnet (workers=10) | — | — | 运行中 |
| collect Gemini-2.5-Pro (workers=10) | — | — | 运行中 |
| collect DeepSeek-V4-Pro (workers=10) | — | — | 运行中 |
| collect Qwen3-235B (workers=10) | — | — | 运行中 |

### GPU 占用

| GPU | 显存 | 利用率 |
|-----|------|--------|
| 0 | 91.1 / 95.6 GB | 100% |
| 1 | 91.1 / 95.6 GB | 100% |
| 2 | 91.0 / 95.6 GB | 100% |
| 3 | 91.0 / 95.6 GB | 100% |

### 各 Judge 已收集 records 数

| Judge | Records | 备注 |
|-------|---------|------|
| claude-sonnet-4.6-proxy | 9,484 | API |
| qwen3-235b-proxy | 7,188 | API |
| gemini-2.5-pro-proxy | 6,722 | API |
| deepseek-v4-pro-proxy | 5,639 | API |
| **llama-3.3-70b-local** | **3,779** | TP=2 重启后采集中 |
| **qwen2.5-72b-local** | **2,521** | TP=2 重启后采集中 |

### Qwen vLLM 吞吐（实时）
- Prompt: **530 tokens/s**, Generation: **143 tokens/s**
- 32 reqs 并发, 0 waiting, KV cache 8.6%, prefix cache hit 36.5%

### 磁盘
- 根分区: 13G / 30G used (41%)

TP=2 重启后两个 local judge 都在正常采集，vLLM 全部 200 OK，4 卡满载。Local judges 的 records 数还较少（LLaMA 3.8k, Qwen 2.5k），启动约 1 小时，正在追赶中。

---
