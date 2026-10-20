# eval gpt2 seed456 holdout

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_gpt2_seed456_holdout_20260521T043602_result.json`
- **Structured JSON:** [`f2870b192181f1f48b6d.json`](../../sessions/f2/f2870b192181f1f48b6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练在 step 6000/6103（98%）崩溃，磁盘满（250G/250G）。checkpoint-6000 损坏（仅 36KB）。

**现状**：
- 最后完整 checkpoint：**checkpoint-5500**（step 5500/6103，~90%，1.1GB model.safetensors）
- checkpoint-4500, 5000 也完整（各 1.2G）
- checkpoint-6000 损坏，不可用

**两个选项**：

1. **直接用 checkpoint-5500 跑 eval** — 快，但只训了 90%，可能 PPL 偏高
2. **清空间 + 从 5500 resume 剩余 603 steps → eval** — 删 checkpoint-4500/5000/6000 释放 ~2.4G，resume 跑完。但 `--save_only_model` 没存 optimizer state，resume 后 Adam momentum/variance 从零开始，最后 603 步影响应该不大

哪个方案？

---
