# code d025 westb status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d025-westb-status-check_20260515T093014_result.json`
- **Structured JSON:** [`961c3bf8b16f525bed99.json`](../../sessions/96/961c3bf8b16f525bed99.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 1. GRPO v4 (PID 339111)
- **存活**: 是，运行 58 分钟
- **当前 step**: 1/250 (刚完成第 1 步，耗时 ~29 分钟/step)
- **尚无 reward/grad_norm 输出** — 日志停在第 1 个 iteration，还在 warmup 阶段
- **GPU**: cuda:0，显存 60205 MiB，利用率 100%
- **W&B run**: `grpo_stage2_rasp_20_v4` (75d1o9wa)

### 2. SFT retrain (PID 239076)
- **存活**: 是，运行 1h30m
- **当前 step**: **1148/1870** (61%)
- **最新指标**: loss=0.828, grad_norm=3.91, mean_token_accuracy=0.788, epoch=0.90
- **GPU**: cuda:1，显存 51581 MiB，利用率 18%
- **预计剩余**: ~55 分钟（~4.5s/it × 722 steps）

### 3. D023 CPU re-eval
有 **4 组**进程在跑：

| 进程 | PID | max_samples | 状态 |
|------|-----|-------------|------|
| standard_20 (旧 nohup, 20 samples) | 476886 | 20 | 运行中，0% 进度（CPU 711%） |
| rasp_20 (旧 nohup, 20 samples) | 476993 | 20 | 运行中，0% 进度（CPU 711%） |
| standard_20 (v4, 100 samples) | 486213 | 100 | 运行中，2/100 (CPU 448%) |
| rasp_20 (v4, 100 samples) | 486293 | 100 | 运行中，0/100 (CPU 389%) |

所有 re-eval 均在进行中，**尚无结果输出**。CPU eval 极慢（~3-5 分钟/sample），100 samples 预计需数小时。

### 4. GPU 使用
| GPU | 显存占用 | 利用率 | 用途 |
|-----|---------|--------|------|
| cuda:0 | 60205 MiB | 100% | GRPO v4 |
| cuda:1 | 51581 MiB | 18% | SFT retrain |

### 5. 磁盘
- `/root/autodl-tmp`: **176G / 250G (71%)**，剩余 75G

---
