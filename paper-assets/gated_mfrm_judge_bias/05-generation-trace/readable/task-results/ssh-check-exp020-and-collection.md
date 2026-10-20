# ssh check exp020 and collection

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-exp020-and-collection_20260524T132948_result.json`
- **Structured JSON:** [`60d07c505b0e11e64950.json`](../../sessions/60/60d07c505b0e11e64950.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-020 状态报告

### 1. 进程状态

| 组件 | PID | 状态 |
|------|-----|------|
| LLaMA vLLM (port 8001, cuda:0,1) | 582372 | **运行中** |
| Qwen vLLM (port 8002, cuda:2,3) | 583078 | **运行中** |
| LLaMA collect (workers=64) | 584106 | **运行中** [1980/11443] 0.9 items/s |
| Qwen collect (workers=64) | 584197 | **运行中** [1980/13590] 0.6 items/s |
| Sonnet collect (workers=10) | 506658 | **卡住** ❌ OpenRouter 402 |
| Gemini collect (workers=10) | 506876 | **卡住** ❌ OpenRouter 402 |
| DeepSeek collect (workers=10) | 506930 | **卡住** ❌ OpenRouter 402 |
| Qwen3-235B collect (workers=10) | 506990 | **卡住** ❌ OpenRouter 402 |

### 2. GPU 状态

| GPU | 显存占用 | 利用率 |
|-----|----------|--------|
| 0 | 89031 / 97887 MiB | 100% |
| 1 | 89031 / 97887 MiB | 100% |
| 2 | 89083 / 97887 MiB | 100% |
| 3 | 89083 / 97887 MiB | 100% |

只有 4 张 GPU 可见（TP=2 × 2 模型满载）。

### 3. JSONL 进度

| Judge | 行数 | 状态 |
|-------|------|------|
| claude-sonnet-4.6-proxy | 13,825 | ❌ 停滞（402 余额不足） |
| qwen3-235b-proxy | 11,296 | ❌ 停滞 |
| gemini-2.5-pro-proxy | 10,791 | ❌ 停滞 |
| llama-3.3-70b-local | 9,655 | ✅ 活跃增长 |
| deepseek-v4-pro-proxy | 9,572 | ❌ 停滞 |
| qwen2.5-72b-local | 6,561 | ✅ 活跃增长 |
| mistral-large-2-local | 118 | ⚠️ 几乎无数据 |

### 4. 数据增长

所有 JSONL 文件最后修改时间为 **2026-05-24 21:30:37~41**（检查时刻），local judge 数据正在实时写入。

### 5. MCMC

无 MCMC 进程运行（符合预期）。

### 6. ETA 估算

- **LLaMA local**: 剩余 9463 items @ 0.9/s → **~175 min（约 3h）**
- **Qwen local**: 剩余 11610 items @ 0.6/s → **~306 min（约 5.1h）**
- **4 个 API judge**: **完全停滞**，OpenRouter 余额耗尽，需充值后才能继续

### 关键问题

**OpenRouter 账户余额不足** — 所有 4 个 API judge（Sonnet / Gemini / DeepSeek / Qwen3-235B）都在循环重试 402 错误，不会再有新数据写入。需要充值 OpenRouter credits 后重启这些采集进程。

---
