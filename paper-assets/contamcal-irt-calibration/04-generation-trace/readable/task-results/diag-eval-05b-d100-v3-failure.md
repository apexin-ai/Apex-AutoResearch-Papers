# diag eval 05B d100 v3 failure

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_05B_d100_v3_failure_20260514T155936_result.json`
- **Structured JSON:** [`0a8016151a485eaaef52.json`](../../sessions/0a/0a8016151a485eaaef52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总报告

### 1. v3 失败原因
- **EXIT_CODE=129** (SIGHUP，信号 1)
- 进程在 GSM8K 评估 13% (178/1319) 时被 `Terminated`
- 不是代码错误，而是进程被外部终止（控制终端关闭或 HUP 信号）
- 另外 v3 未设 `HF_DATASETS_OFFLINE=1`，启动时 HuggingFace 连接超时多次重试后才用了缓存数据

### 2. v4 当前状态
- **运行中**，PID 396019 存活，已运行 ~35 分钟
- MMLU 已完成，正在评估 GSM8K：**322/1319 (24%)**，剩余约 1h25m（~5.14s/it）
- 修复了 v3 的两个问题：使用直接 python 路径 + 设了 `HF_DATASETS_OFFLINE=1`

### 3. GPU 使用情况（全部占用）

| GPU | PID | 显存 | 利用率 | 用途 |
|-----|-----|------|--------|------|
| 0 | 385407 | 14358MiB/24564MiB | 23% | 未知 python 进程 |
| 1 | 398887 | 5848MiB/24564MiB | 50% | 未知 python 进程 |
| 2 | 396024 | 3686MiB/24564MiB | 35% | **v4** (d100_aligned) |
| 3 | 398501 | 3686MiB/24564MiB | 32% | **d025_aligned** |
| 4 | 373931 | 8976MiB/24564MiB | 68% | 未知 python 进程 |
| 5 | 400526 | 3718MiB/24564MiB | 35% | **d005_para_aligned** |

### 4. 其他实验状态
- **d005_para_aligned** (GPU 5)：运行中，GSM8K (paraphrased) **126/228 (55%)**，剩余约 9 分钟
- **d025_aligned** (GPU 3)：**标记 failed 但进程仍在运行**（PID 398496 存活，GSM8K 195/1319 (15%)，剩余约 1h35m）。⚠️ **违反 C003**——标记 failed 时未 kill 关联进程

### 5. 空闲 GPU
**无空闲 GPU**，6 张卡全部在用。

### 需要决策
d025_aligned (GPU 3) 进程还活着且在正常推进。两个选择：
1. kill 它（遵循 failed 标记），释放 GPU 3
2. 取消 failed 标记，让它跑完（~1.5h）

---
