# eval baseline control prune k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline_control_prune_k05_20260518T222229_result.json`
- **Structured JSON:** [`31581d573fdc48cb64fe.json`](../../sessions/31/31581d573fdc48cb64fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

eval 已正常运行，进入了 episode 评估循环。

**结果汇总：**
- **Checkpoint**: `checkpoints/baseline_control/latest/checkpoint.pt` (1.3GB) ✓
- **Bug 修复**: `compute_random_mask` 在 `wrapper=None`（baseline 模型）时会 crash。已修改为直接用 `policy` 获取 visual tokens，不依赖 wrapper。
- **重新提交**: PID=394430，tmux session `eval_baseline_control_prune_k05`
- **日志**: 模型加载成功（11.5s），Connector 找到，已开始 Task 0 的 episode 评估，`mode=random_prune, pruning=zero_mask, k_ratio=0.5`

---
