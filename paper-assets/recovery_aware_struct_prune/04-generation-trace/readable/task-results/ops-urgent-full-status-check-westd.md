# ops urgent full status check westd

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_full_status_check_westd_20260517T225429_result.json`
- **Structured JSON:** [`ae4935b1ee515ad7840a.json`](../../sessions/ae/ae4935b1ee515ad7840a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-11672 状态报告

### 1. PID 存活状态

| 实验 | PID | 状态 |
|------|-----|------|
| eval_sft_cka_only_20_n1319 | 49475 | ✅ ALIVE |
| eval_math500_grpo_standard_20 | 14556 | ✅ ALIVE |
| eval_math500_grpo_rasp_20_v3 | 31706 | ✅ ALIVE |
| eval_postprune_cka_only_30 | 59403 | ✅ ALIVE |
| eval_postprune_standard_30 | 47667 | ✅ ALIVE |

### 2. GPU 使用情况

| GPU | 显存占用 | 利用率 | 温度 | 进程 |
|-----|---------|--------|------|------|
| 0 | 41198/97887 MiB | 95% | 56°C | eval_math500_unpruned + eval_sft_cka_only_20_n1319 |
| 1 | 34569/97887 MiB | 99% | 79°C | eval_math500_grpo_standard_20 |
| 2 | 23090/97887 MiB | 93% | 51°C | eval_postprune_cka_only_30 (×2 进程) |
| 3 | 32517/97887 MiB | 99% | 80°C | eval_math500_grpo_rasp_20_v3 |

**GPU 空闲情况：无空闲 GPU，4 张全部满载。**

### 3. 实验进度

| 实验 | 进度 | 当前 Acc | 速度 | 预计剩余 |
|------|------|----------|------|----------|
| eval_sft_cka_only_20_n1319 | **1037/1319 (79%)** | 63.00% (GSM8K) | ~5.5s/it | ~25min |
| eval_math500_grpo_standard_20 | **309/500 (62%)** | 28.33% (MATH) | ~4-5min/it | ~13h |
| eval_math500_grpo_rasp_20_v3 | **256/500 (51%)** | 28.00% (MATH) | ~4-5min/it | ~17h |
| eval_postprune_cka_only_30 | **33/200 (16%)** | N/A | ~95s/it | ~4.4h |
| eval_postprune_standard_30 | **139/200 (70%)** | **3.00%** ⚠️ | ~108s/it | ~1.8h |

### 4. 异常发现

**eval_postprune_standard_30 严重异常：**
- acc=3.0% @ 100 samples
- eos_rate=10%，avg_len=3753
- 模型几乎不能生成有效答案（输出全跑满 max_tokens 不停止）
- 说明 standard pruning 30% 后模型基本丧失推理能力

**eval_postprune_cka_only_30 有重复进程：** GPU 2 上有两个 python 进程（PID 59408 + 59866）都在跑同一个模型的评估，浪费显存。

### 5. 已完成结果

无实验完成。最快完成的是 **eval_sft_cka_only_20_n1319**（约 25 分钟后）和 **eval_postprune_standard_30**（约 1.8 小时后）。

---
