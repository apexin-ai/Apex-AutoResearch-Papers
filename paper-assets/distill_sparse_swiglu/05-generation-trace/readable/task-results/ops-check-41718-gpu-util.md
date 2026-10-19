# ops check 41718 gpu util

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_41718_gpu_util_20260519T223216_result.json`
- **Structured JSON:** [`6cd7eb29bb7c40f286c1.json`](../../sessions/6c/6cd7eb29bb7c40f286c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41718 状态

### GPU 占用

| GPU | 利用率 | 显存 |
|-----|--------|------|
| cuda:0 | 95% | 63,263 / 97,887 MiB |
| cuda:1 | 0% | 0 MiB (空闲) |

### 进程状态

| 实验 | PID | 状态 |
|------|-----|------|
| bench_teal30_uniform_gsm8k | 176588 | **已结束** (进程不存在) |
| qwen14b_kl30_s42_gsm8k_v2 | 166099 | **运行中**, 已跑 4h14m |

### 日志详情

**bench_teal30_uniform_gsm8k** — 已完成，EXIT_CODE=0
- GSM8K (8-shot): **exact_match = 0.0879** (8.79%)
- 耗时 1251.3s (~21min)
- 结果已保存: `results/benchmark/bench_teal30_uniform_gsm8k/results.json`

**qwen14b_kl30_s42_gsm8k_v2** — 正在跑 generate_until
- 进度: **91% (1201/1319)**, 速度 ~14s/it
- 预计剩余 ~29 min
- 无 error，只有 `max_new_tokens` vs `max_length` 的 warning（无害）

---
