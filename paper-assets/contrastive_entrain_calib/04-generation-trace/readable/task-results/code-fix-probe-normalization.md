# code fix probe normalization

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-probe-normalization_20260518T174830_result.json`
- **Structured JSON:** [`44eaa2c91068f3637080.json`](../../sessions/44/44eaa2c91068f3637080.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件均已修复且语法验证通过。

改动摘要：
- **`LinearProbe.__init__`**：添加 `feat_mean` / `feat_std` 两个 buffer（`register_buffer`）
- **`LinearProbe.forward`**：输入先做 `(x - mean) / (std + 1e-8)` 归一化再过 linear
- **`train_probe`**：训练前计算 `X.mean(dim=0)` / `X.std(dim=0)` 并 `copy_` 到 probe 的 buffers
- **`save_probe` / `load_probe`**：无需改动，`state_dict` 自动包含 buffers

---
