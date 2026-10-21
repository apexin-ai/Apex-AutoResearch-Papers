# ops cuda4 signals rootcause

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cuda4-signals-rootcause_20260515T184200_result.json`
- **Structured JSON:** [`802cfb6daad6927ad034.json`](../../sessions/80/802cfb6daad6927ad034.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 排查报告

### 1. 根因

**tmux session `exp002_3B_v2`**（创建于 May 16 00:13:59）是唯一的自动触发源。

机制：该 session 运行 `run_batch.py --model-size 3B --gpu 0 --only d000 d005 d025 d100`，CUDA_VISIBLE_DEVICES=**4**。run_batch.py 按顺序遍历 12 个任务（4 dosage × 3 benchmark），每个任务 spawn 一个 compute_signals.py 子进程。之前反复出现的原因是：**杀掉单个 compute_signals 进程后，run_batch.py 视其为失败，立即启动下一个任务**，所以进程"反复出现"。

不是 crontab、不是 systemd timer、不是 shell rc、不是 at/watch — 就是这个 tmux session 里的 run_batch.py 在不停地 spawn。

次要问题：另有一个孤儿 run_batch.py（PID 611720, PPID=1, CUDA_VISIBLE_DEVICES=3）在 GPU 3 上运行，一并清除。

### 2. 清除操作

| 操作 | 结果 |
|------|------|
| `tmux kill-session -t exp002_3B_v2` | 杀掉 run_batch.py (PID 590507) 及其子进程 compute_signals (PID 612048) |
| `kill -9 611726 611720` | 清除 GPU 3 上的孤儿 run_batch.py 及其 compute_signals |

### 3. 清除后 cuda:4 状态

```
PID 597179 (python - train_sft.py d000_a32_s42): 13868 MiB
GPU 4 总显存: 13877 MiB / 24564 MiB (57%), 利用率 39%
```

compute_signals 进程已全部消失，无 run_batch.py 残留。

### 4. d000_v3 SFT (PID 597179) 状态

正常运行。PID 597179 是 `train_sft.py --output-dir Qwen2.5-3B_d000_a32_s42`，CUDA_VISIBLE_DEVICES=4，独占 GPU 4，显存从 91% 降回 57%。

---
