# ops verify sft and diagnose eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-sft-and-diagnose-eval_20260515T085518_result.json`
- **Structured JSON:** [`42811050b1178fce310f.json`](../../sessions/42/42811050b1178fce310f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: SFT 进程状态

| 实验 | GPU | 状态 | 详情 |
|------|-----|------|------|
| d025 (PID 533174) | cuda:0 | ✅ **ALIVE，训练中** | step 22/3384, ~2s/it, ETA ~1h53m, 使用 14.9 GB |
| d005 (PID 533263) | cuda:2 | ❌ **DEAD — OOM** | 第 0 步即崩溃，EXIT_CODE=1 |

**d005 OOM 原因**：GPU 2 已被两个进程占据：
- PID 506625 (13.6 GB) — `evaluate.py Qwen2.5-3B d100_s123 aligned`，已运行 3h36m
- PID 530893 (3.6 GB) — base pretrained eval 0.5B

两者合占 ~17.2 GB，d005 SFT 无法分配额外 884 MiB，直接 OOM。

### Part 2: Base Pretrained Eval 状态

两个 eval **没有失败**，实际都在运行：

| 实验 | GPU | 状态 | 进度 |
|------|-----|------|------|
| 0.5B eval (PID 530893) | cuda:2 | ✅ 运行中 | MMLU 完成 (acc=0.2294), gsm8k 加载中（HF timeout 重试） |
| 1.5B eval (PID 530975) | cuda:4 | ✅ 运行中 | MMLU 77% (10884/14042), ~27 it/s |

evaluate.py 支持不带 `--adapter-path` 运行，base pretrained 评估命令没问题。

### 当前 GPU 占用

| GPU | 内存占用 | 进程 |
|-----|---------|------|
| 0 | 14.9 GB | ✅ SFT d025 训练中 |
| 1 | 3.7 GB | 未知进程 (PID 521694) |
| 2 | 17.2 GB | 3B eval (506625) + 0.5B base eval (530893) |
| **3** | **0 MB** | **空闲** |
| 4 | 14.6 GB | 未知进程 (513826) + 1.5B base eval (530975) |
| 5 | 5.9 GB | 未知进程 (521613) |

### 建议操作

d005 SFT 需要重新提交。**GPU 3 是唯一空闲的 GPU**，应提交到 cuda:3 而不是 cuda:2。是否现在重新提交？

---
