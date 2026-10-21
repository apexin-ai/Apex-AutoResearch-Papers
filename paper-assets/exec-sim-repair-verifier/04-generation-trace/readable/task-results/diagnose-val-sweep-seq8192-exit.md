# diagnose val sweep seq8192 exit

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_val-sweep-seq8192-exit_20260515T172401_result.json`
- **Structured JSON:** [`24b908d1cb7505de2157.json`](../../sessions/24/24b908d1cb7505de2157.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Summary:

**原因**: CUDA OOM，首个 checkpoint-1800 即崩溃。

**详情**:
- `batch_size=1`, `seq_length=8192`, Qwen3-8B on RTX 5090 (32GB)
- 模型加载占 ~17GB，generate() 时 MLP forward pass 需分配 1.81GB，但仅剩 387MB（PyTorch 已占 25.39GB + 预留 5GB）
- **0/21 checkpoints 完成**，output dir 为空
- `PYTORCH_ALLOC_CONF=expandable_segments:True` 已设置，仍不够

**cuda:0 当前状态**: 空闲，0MiB 占用，可用。

**结论**: seq_length=8192 对 8B 模型在单张 32GB GPU 上 batch_size=1 都不可行。需要降 seq_length（回 5120）或用量化/offload 策略。

---
