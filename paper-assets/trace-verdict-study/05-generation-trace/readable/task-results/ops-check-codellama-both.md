# ops check codellama both

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_codellama_both_20260518T001634_result.json`
- **Structured JSON:** [`b53198f9c2489f67685d.json`](../../sessions/b5/b53198f9c2489f67685d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都在跑，尚未完成。

**CodeLlama-13B tail-512** (`codellama13b_full_trace_tail512_seed42`):
- 进度: 224/444 steps (50%)
- 速度: ~13.5s/step
- 剩余训练: ~220 steps × 13.5s ≈ **50 分钟**
- 之后还有 eval 阶段

**CodeLlama-13B head-2048** (`codellama13b_full_trace_head2048_seed42`):
- 进度: 71/444 steps (16%)
- 速度: ~28.3s/step
- 剩余训练: ~373 steps × 28.3s ≈ **2 小时 56 分钟**
- 之后还有 eval 阶段

两个都在正常训练（GPU 0 和 GPU 1 各自 100% 利用率），无需干预。tail-512 预计约 1 小时后完成（含 eval），head-2048 预计约 3.5 小时后完成。

---
