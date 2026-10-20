# ops gpu status check post crash

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_status_check_post_crash_20260515T210939_result.json`
- **Structured JSON:** [`10f6bf290cfb9dd99fcd.json`](../../sessions/10/10f6bf290cfb9dd99fcd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 崩溃恢复状态报告

### GPU 状态（4× RTX PRO 6000 Blackwell 96GB）

| GPU | 利用率 | 显存占用 | 任务 | 状态 |
|-----|--------|----------|------|------|
| 0 | 70% | 15.3/97.9 GB | DS s020 accuracy eval (n=50) | **运行中** — 41/50 题，9 correct |
| 1 | 71% | 15.4/97.9 GB | DS s025 accuracy eval (n=50) | **运行中** — 38/50 题，4 correct |
| 2 | 70% | 15.3/97.9 GB | QW s020 扩样本 (n=51-100) | **运行中** — 刚启动，2/50 题 |
| 3 | 69% | 15.3/97.9 GB | QW s025 扩样本 (n=51-100) | **运行中** — 刚启动，2/50 题 |

### 已完成结果

| 文件 | 状态 | Accuracy | n |
|------|------|----------|---|
| `accuracy_eval_qw_s020.json` | **已完成** | **0.24** (12/50) | 50 |
| `accuracy_eval_qw_s025.json` | **已完成** | **0.26** (13/50) | 50 |
| `accuracy_eval_ds_s020.json` | 未完成 | — | 41/50 进行中 |
| `accuracy_eval_ds_s025.json` | 未完成 | — | 38/50 进行中 |
| `accuracy_eval_qw_s020_n51_100.json` | 未完成 | — | 2/50 刚启动 |
| `accuracy_eval_qw_s025_n51_100.json` | 未完成 | — | 2/50 刚启动 |

### ETA 估算
- **DS s020**: ~9 题剩余，每题 ~2-40s (含 timeout)，预计 **5-10 分钟**内完成
- **DS s025**: ~12 题剩余，类似速度，预计 **10-15 分钟**内完成
- **QW 扩样本**: 48/50 题剩余，预计 **~10 分钟**每组（QW 比 DS 快）

### 异常
- 无 OOM、无崩溃
- DS s025 有大量 `pred=None`（timeout），accuracy 可能较低
- QW 扩样本已在崩溃前成功启动，进程正常运行

---
