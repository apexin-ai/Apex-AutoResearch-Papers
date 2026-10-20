# status dual server step check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_dual-server-step-check_20260516T171650_result.json`
- **Structured JSON:** [`23409c8da50089313613.json`](../../sessions/23/23409c8da50089313613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results confirmed. Here's the summary:

**Training parameters** (all experiments): `--num_train_tokens 200000000`, batch_size=4, grad_accum=4, max_length=2048 → **total_steps = 6,104**

| 实验 | 服务器 | 实际训练 step | total_steps | 进度% | 最新 checkpoint | 预估剩余 |
|------|--------|-------------|-------------|-------|----------------|---------|
| hybrid_rho04_seed42 | westd-41312 | 2999 | 6104 | 49.1% | checkpoint-2500 | ~6h |
| hybrid_rho06_seed42 | westd-41312 | 2999 | 6104 | 49.1% | checkpoint-2500 | ~6h |
| threshold_q07_seed42 | westd-47453 | 5414 | 6104 | 88.7% | checkpoint-5000 | ~1.3h |

**关键发现**：
- hybrid 两个实验实际只到 step 2999（49%），之前报的 85%/94% 应该是错的
- threshold_q07 从 checkpoint-2000 恢复后已跑到 step 5414，接近完成
- 所有进程均在运行中（100% CPU），训练速率约 510-520 steps/hr

---
