# code add lip monitor v7 1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_add-lip-monitor-v7_1_20260515T184055_result.json`
- **Structured JSON:** [`c8e54c6179c7fa25086e.json`](../../sessions/c8/c8e54c6179c7fa25086e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，结果如下：

- **语法验证**: `SYNTAX_OK`
- **插入位置 1**: 第 494 行 — `lip_monitor_every = train_cfg.get("lip_monitor_every", 500)`，紧跟 `grad_clip` 配置读取之后
- **插入位置 2**: 第 646-671 行 — Lipschitz 监控块，位于 Checkpoint saving（第 643 行）之后、graceful exit 检查（第 673 行）之前
- **现有代码未被破坏**: `save_checkpoint` 出现在原有位置（643, 675, 680），split-loss logging 等原有修改均保留
- 总行数从 658 增至 687（+29 行）

---
