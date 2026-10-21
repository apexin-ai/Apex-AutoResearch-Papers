# infra submit cwm8b seed456

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_submit-cwm8b-seed456_20260512T131822_result.json`
- **Structured JSON:** [`049d2327b8d67c5662d1.json`](../../sessions/04/049d2327b8d67c5662d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认：

- **PID**: 47236（子进程，父进程 47225）在 **物理 GPU 2** (`GPU-19c6fdd6...`)，占用 19672 MiB
- **训练已开始**: `trainable params: 15,335,424 || all params: 8,206,070,784 || trainable%: 0.1869`，共 1434 steps
- **超参**: 与 cwm8b-seed123 完全一致（`--batch_size 2 --grad_accumulation 16 --lr 2e-4 --epochs 3 --seed 456`），加了 `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` 防 OOM
- **4 张 GPU 全部在用**: GPU0 (repo-level-cls), GPU1 (cwm-seed789), GPU2 (cwm8b-seed456), GPU3 (repo-level-cwm)

---
