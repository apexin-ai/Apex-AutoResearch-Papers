# ops cwm8b eval exit check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cwm8b-eval-exit-check_20260515T144145_result.json`
- **Structured JSON:** [`8205aacac7154fde1f16.json`](../../sessions/82/8205aacac7154fde1f16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 进程状态：**bs=8 重启已成功，新进程正在跑**

| 项目 | 值 |
|------|-----|
| PID | 381618 (新进程) |
| 启动时间 | 2026-05-15 22:38:37 (约 4 分钟前) |
| 命令 | `python3 eval_repo_cwm.py --device cuda:0 --max_new_tokens 1024` |
| 进度 | **376/9784** (359 从 incremental 恢复 + 17 新推理) |
| running_acc | **70.6%** |
| 产出文件 | `results_incremental.jsonl` — 376 行, 1.3MB |

### GPU 状态 (cuda:3)

- PID 381618, 22516MiB / 32607MiB, **89% 利用率**
- 4 张 5090 全部在跑任务，无空闲

### Registry

状态已是 `RUNNING`，PID=381613（tmux 父进程），提交时间 14:38:37 UTC = 22:38 本地时间，与实际进程一致。**bs=8 restart worker 已正确重新提交，registry 无需更新。**

### 速度估算

17 个新样本 / ~3 分钟 ≈ **~5.7 samples/min**。剩余 9784 - 376 = 9408 样本，预计 **~27.5 小时**完成。

---
