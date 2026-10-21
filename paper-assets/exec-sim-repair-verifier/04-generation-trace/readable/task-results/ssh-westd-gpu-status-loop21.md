# ssh westd gpu status loop21

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-gpu-status-loop21_20260516T012039_result.json`
- **Structured JSON:** [`6a142d7c2a2532cc67d7.json`](../../sessions/6a/6a142d7c2a2532cc67d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态
| GPU | 占用状态 | 显存 | 进程 |
|-----|---------|------|------|
| cuda:0 | 空闲 | 0 / 32607 MiB | 无 |
| cuda:1 | 空闲 | 0 / 32607 MiB | 无 |
| cuda:2 | **占用** | 17239 / 32607 MiB (82%) | PID 446873 — `eval_repo_cls.py` (cls8b_s42_resume_ckpt3600, test, bs=1, 运行2分钟) |
| cuda:3 | **占用** | 21133 / 32607 MiB (88%) | PID 443221 — CWM 8B eval |

## CWM 8B eval 进度
- **当前进度: 5568 / 9784** (56.9%)
- **running_acc: 60.9%**
- 速度: ~8 samples / 57s ≈ 每分钟 8.4 samples
- 剩余: 4216 samples → **ETA ≈ 8.4 小时** (约今晚 17:30)
- 最后日志时间: 2026-05-16 09:20:43

## PID 状态
- PID 444502: **dead** (已结束)
- PID 444130: **dead** (已结束)

## 意外发现
cuda:2 上有一个新进程 PID 446873，正在跑 `eval_repo_cls.py`（Qwen3-8B cls 分类器 ckpt-3600 test set eval），刚启动 2 分钟。这不是之前记录的任务——可能是你在另一个 session 启动的，或者有其他操作者。

---
