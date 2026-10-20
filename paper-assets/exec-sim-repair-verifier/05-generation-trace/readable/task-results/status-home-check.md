# status home check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_home-check_20260514T121857_result.json`
- **Structured JSON:** [`42db6e4ec42315c49bb2.json`](../../sessions/42/42db6e4ec42315c49bb2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## val_4096 Eval 状态

| 项目 | 状态 |
|------|------|
| **进程** | 运行中 (tmux `val_4096`, PID 3083027, CPU 100%) |
| **进度** | **4900/9335 (52.5%)** |
| **running_acc** | **82.1%** |
| **GPU** | cuda:0, 利用率 99%, 显存 10745/32607 MiB |
| **启动时间** | 05:05 UTC, 已运行约 15 分钟 |
| **增量保存** | `val_eval_results_4096/seed123_ckpt400/eval_repo_cls_predictions.jsonl` (933 KB) |

从 28.8% → 52.5%，running_acc 从 82.4% 略降至 82.1%。batch 速度约 0.1s（短序列）到 0.9s（截断到 4096 的长序列），按当前速率预计还需约 13-15 分钟完成。

---
