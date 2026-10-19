# ops exp004 eval trim restart

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp004-eval-trim-restart_20260519T133403_result.json`
- **Structured JSON:** [`14194039bb8bbdabb37d.json`](../../sessions/14/14194039bb8bbdabb37d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，确认如下：

| 项目 | 状态 |
|------|------|
| Kill PID 134070 | DEAD |
| 脚本修改 | `CHECKPOINTS=(500 2000 8000)` |
| 残留清理 | 已删除 exp004-ckpt500 不完整结果 |
| 新进程 PID | **136199**（子进程 python PID 136205） |
| GPU 0 占用 | PID 136205, 17650MiB / 32607MiB, 42% util |
| 日志 | 已加载 Qwen3-8B + LoRA ckpt-500，正在 eval 362 pairs |

日志路径：`/tmp/exp004_eval_trimmed.log`。3 个 checkpoint 预计 ~2.5h 完成。

---
