# diagnose exec only s43 1000step r2

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exec-only-s43-1000step-r2_20260516T232315_result.json`
- **Structured JSON:** [`ed2f4964cb8e707b803b.json`](../../sessions/ed/ed2f4964cb8e707b803b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**根本原因：** `train_grpo.py` 不接受 `--save_total_limit` 参数。

```
train_grpo.py: error: unrecognized arguments: --save_total_limit 1
```

该脚本的 argparse 没有定义 `--save_total_limit` 这个 CLI 参数。从 usage 信息看，它支持的参数列表中没有这个选项。

**修复方案：**

两种选择：

1. **从启动命令中移除 `--save_total_limit 1`**，改为在 `train_grpo.py` 内部硬编码 `save_total_limit=1`（在构建 `GRPOConfig` / `TrainingArguments` 时直接设置）。

2. **给 `train_grpo.py` 添加这个参数**：在 argparse 中加一行：
   ```python
   parser.add_argument("--save_total_limit", type=int, default=1)
   ```
   然后在构建 training config 时传入 `save_total_limit=args.save_total_limit`。

考虑到 C003 约束（必须设置 `save_total_limit=1` 防止磁盘耗尽），建议方案 2，让 CLI 支持该参数并默认为 1。需要我查看 `train_grpo.py` 的 argparse 部分来给出具体修改位置吗？

---
