# monitor plan001 005 verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_plan001-005-verify_20260513T222106_result.json`
- **Structured JSON:** [`ed135a486a79aeae8e47.json`](../../sessions/ed/ed135a486a79aeae8e47.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**两个训练都因 argparse 错误立即崩溃，未曾开始训练。**

错误完全相同：

```
train_grpo.py: error: unrecognized arguments: --max_steps 500
```

**原因**：启动命令用了 `--max_steps 500`，但 `train_grpo.py` 的 argparse 定义的是 `--num_steps`，没有 `--max_steps` 这个参数。

**修复**：将启动命令中的 `--max_steps 500` 改为 `--num_steps 500`，然后重新启动两个训练。

---
