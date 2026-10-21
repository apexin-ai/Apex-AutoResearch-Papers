# code llama verify parallel

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama-verify-parallel_20260520T205905_result.json`
- **Structured JSON:** [`0e89bbf6b0c22e72ef08.json`](../../sessions/0e/0e89bbf6b0c22e72ef08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复完成 — 3 GPU 全部活跃

### 失败原因
`train.py:53` 中 `os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)`——submit_training_job 启动 contam_15/contam_50 时传了 `--gpu 0`，导致 3 个进程全部挤在 GPU 0（共占 73GB/98GB）。

### 修复操作
1. Kill 了 contam_15 (PID 39375) 和 contam_50 (PID 39455)
2. 用 tmux 重启，分别传 `--gpu 1` 和 `--gpu 2`

### nvidia-smi 确认

| GPU | 利用率 | 显存占用 | 条件 | PID |
|-----|--------|----------|------|-----|
| 0 | 86% | 29331 MiB / 98GB | clean | 38815 |
| 1 | 80% | 20239 MiB / 98GB | contam_15 | 40724 |
| 2 | 88% | 23383 MiB / 98GB | contam_50 | 40864 |

### 训练进度

| 条件 | 进度 | 速度 | 预计剩余 |
|------|------|------|----------|
| clean | 184/939 (20%) | ~1.07s/it | ~14 min |
| contam_15 | 39/1335 (3%) | ~1.17s/it | ~25 min |
| contam_50 | 32/2256 (1.4%) | ~1.25s/it | ~46 min |

clean 训练速度从 3.3s/it 恢复到 1.07s/it（GPU 0 不再被挤占）。

---
