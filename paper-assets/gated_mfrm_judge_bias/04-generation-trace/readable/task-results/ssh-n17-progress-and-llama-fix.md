# ssh n17 progress and llama fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_progress_and_llama_fix_20260524T003749_result.json`
- **Structured JSON:** [`7560a5c7e1c0524ab114.json`](../../sessions/75/7560a5c7e1c0524ab114.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 汇总报告

### 1. API Judge 进度 (N=17)

| Judge | 完成 | 总数 | 进度 | 速率 | 预估剩余 |
|-------|------|------|------|------|----------|
| claude-sonnet-4.6 | ~880 | 17,982 | **4.9%** | 0.2 items/s | ~20h |
| gemini-2.5-pro | ~593 | 17,982 | **3.3%** | 0.2 items/s | ~29.6h |
| deepseek-v4-pro | ~504 | 17,982 | **2.8%** | 0.1 items/s | ~34.7h |
| qwen3-235b | ~600 | 17,982 | **3.3%** | 0.2 items/s | ~28.8h |

4 个进程全部存活。有间歇性 500 错误但自动重试中。

### 2. LLaMA 下载

- 已有 6/9 safetensors（缺 00002, 00006, 00009）
- 旧下载进程已死，**已重启**，新 PID: **493983**（已确认存活）
- 注意：未认证下载，速率可能受限

### 3. exp-017

- **182/800 fits** (22.8%)，当前 n_models=8, seed=182
- 已运行 17.5h，预估剩余 ~61.9h (~2.6 天)
- PID 318082 存活，CPU 103%，RSS ~27.5GB

### 4. 磁盘

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|------|------|------|------|--------|
| /root/autodl-tmp | 250G | 164G | **87G** | 66% |
| / (根) | 30G | 15G | **16G** | 49% |

LLaMA 剩余 3 个 shard 约 ~14GB，数据盘空间充足。

---
