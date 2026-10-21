# ops xvla seed44 k05 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-seed44-k05-cqa1_20260520T132737_result.json`
- **Structured JSON:** [`8a93fe19740e2009607e.json`](../../sessions/8a/8a93fe19740e2009607e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已启动并正常运行。

**汇总：**
- **PID**: 132420（python 子进程，父 bash PID 132415）
- **GPU**: 2（GPU-a2a15ad4），占用 4046 MiB
- **状态**: 正在评估 Task 0，前 3 个 episode 全部 SUCCESS
- **预估完成时间**: 每个 episode ~7s，50 episodes × 10 tasks = 500 episodes，约 ~1 小时

当前 4 GPU 全部占满：
| GPU | 任务 | PID |
|-----|------|-----|
| 0 | seed44 k=0.7 | 115960 |
| 1 | seed44 k=0.9 | 116978 |
| 2 | seed44 k=0.5 | 132420 |
| 3 | seed43 k=0.5 | 894197 |

---
