# fix cuda0 cleanup resubmit ckpt1200

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cuda0-cleanup-resubmit-ckpt1200_20260515T020713_result.json`
- **Structured JSON:** [`a8fb891b9342de654133.json`](../../sessions/a8/a8fb891b9342de654133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 结果

| 项目 | 详情 |
|------|------|
| **cuda:0 原占用** | PID 315423 — 之前 OOM 失败的 ckpt-1200 val eval，占 19218 MiB |
| **清理** | kill 315423 + 清理 3 个旧 tmux sessions，cuda:0 完全释放 |
| **新 eval PID** | **316307**（tmux session: `ckpt1200-val8192-v2`） |
| **GPU 状态** | cuda:0: PID 316307, 18238 MiB（eval）；cuda:1/2/3 训练进程不受影响 |
| **日志** | `~/runs/exec-sim-repair-verifier/cls8b-s42-ckpt1200-val8192-v2.log` |

---
