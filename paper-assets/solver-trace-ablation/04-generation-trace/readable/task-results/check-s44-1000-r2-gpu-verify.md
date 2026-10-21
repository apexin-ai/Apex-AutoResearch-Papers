# check s44 1000 r2 gpu verify

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_s44-1000-r2-gpu-verify_20260515T125433_result.json`
- **Structured JSON:** [`77908ef57cc08ab88eb5.json`](../../sessions/77/77908ef57cc08ab88eb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**r2 (PID 353256) 已崩溃，第三次 OOM on GPU 0。**

日志确认：脚本内部 `Set CUDA_VISIBLE_DEVICES=0`（`--gpu 0` 覆盖了 shell 的 `export CUDA_VISIBLE_DEVICES=1`），撞上 s43 (PID 352142) 导致 OOM，step 1 即死。

当前状态：
- **GPU 0**: s43 (PID 352142) 正常运行，94% 利用率
- **GPU 1**: PID 352975 — `train_sft.py ... s44 ... --gpu 1`，已在正确的 GPU 上运行，53GB 显存占用正常

PID 352975 看起来是 r2 崩溃后自动或手动重新提交的版本（`--gpu 1` 已修正）。**GPU 1 上的训练正常，无需干预。** 但 r2 的日志名可能需要更新为 r3，以免混淆。

---
