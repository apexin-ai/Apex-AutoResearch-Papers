# ssh collect final status

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect-final-status_20260524T121730_result.json`
- **Structured JSON:** [`41dc50b299cd1f30aeeb.json`](../../sessions/41/41dc50b299cd1f30aeeb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据采集完毕。汇总如下：

---

## Judge Eval 状态报告

### 1. 进程 PID

| 角色 | PID | 配置 |
|------|-----|------|
| vLLM LLaMA | 577461 | cuda:0, port 8001, TP=1, AWQ |
| vLLM Qwen | 578168 | cuda:1, port 8002, TP=1, AWQ |
| collect LLaMA | 579212 | config_llama-3.3-70b_local_n17, workers=64 |
| collect Qwen | 579307 | config_qwen2.5-72b_local_n17, workers=64 |

### 2. GPU 显存

| GPU | Used / Total | Util |
|-----|-------------|------|
| 0 | 89,089 / 97,887 MiB | 100% |
| 1 | 89,383 / 97,887 MiB | 100% |
| 2 | 0 / 97,887 MiB | 0% |
| 3 | 0 / 97,887 MiB | 0% |

### 3. 七个 Judge JSONL 行数（目标 18,000）

| Judge | Lines | % |
|-------|------:|---:|
| claude-sonnet-4.6-proxy_n17 | 10,429 | 57.9% |
| qwen3-235b-proxy_n17 | 7,950 | 44.2% |
| gemini-2.5-pro-proxy_n17 | 7,466 | 41.5% |
| **llama-3.3-70b-local_n17** | **6,424** | **35.7%** |
| deepseek-v4-pro-proxy_n17 | 6,251 | 34.7% |
| qwen2.5-72b-local_n17 | 4,257 | 23.7% |
| mistral-large-2-local_n17 | 118 | 0.7% |

注意：实际有 **7** 个 judge（不是 6）。Mistral 仅 118 行且无 GPU 进程，**已停止**。

### 4. 吞吐量（wc -l 间隔法，2×≥2min）

**LLaMA (llama-3.3-70b-local_n17)**

| 区间 | 行数增量 | 时长 | 速率 |
|------|---------|------|------|
| T0→T1 | 6273→6361 (+88) | 2m08s | 41.3 lines/min |
| T1→T2 | 6361→6424 (+63) | 2m00s | 31.5 lines/min |
| **平均** | | | **36.4 lines/min** |

ETA 完成: (18000−6424) / 36.4 ≈ **5.3h**

**Qwen (qwen2.5-72b-local_n17)**

| 区间 | 行数增量 | 时长 | 速率 |
|------|---------|------|------|
| T0→T1 | 4175→4217 (+42) | 2m08s | 19.7 lines/min |
| T1→T2 | 4217→4257 (+40) | 2m00s | 20.0 lines/min |
| **平均** | | | **19.9 lines/min** |

ETA 完成: (18000−4257) / 19.9 ≈ **11.5h**

### 5. 日志状态

`/tmp/collect_llama_w64.log` 和 `/tmp/collect_qwen_w64.log` 均为空文件（collect.py 未向 stdout/stderr 输出）。

### 关注点

- **Mistral 已停止**（118 行，0.7%），cuda:2/3 空闲，无对应 collect 进程
- **Qwen 吞吐约为 LLaMA 的一半**（20 vs 36 lines/min），完成需 11.5h
- LLaMA 两次测量有波动（41→32），但 Qwen 非常稳定（~20）

---
