# code baseline v6 alpha16

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_v6_alpha16_20260516T083918_result.json`
- **Structured JSON:** [`76f50ddc30a37ea18bc2.json`](../../sessions/76/76f50ddc30a37ea18bc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

- **Config**：创建 `configs/baseline_v6_alpha16.yaml`，基于 baseline.yaml，`alpha: 64 → 16`，`output_dir: checkpoints/baseline_v6_alpha16`
- **训练已启动**：westd-27271 cuda:1，tmux session `baseline_v6_alpha16`
- **确认 alpha=16 生效**：日志显示 `LoRA applied: rank=32, alpha=16, trainable params: 1485312`
- **首步 loss=3.4066**，训练正常
- **Registry 已更新**：status=RUNNING，hypothesis 已记录

---
