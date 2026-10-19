# ops read eval results p0

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-eval-results-p0_20260516T194908_result.json`
- **Structured JSON:** [`50263b89a368f1838494.json`](../../sessions/50/50263b89a368f1838494.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## V7 Eval 结果汇总

### 已完成 Suite: libero_spatial

| Model | SR | vs Baseline (66.0%) |
|-------|-----|---------------------|
| **seed1** (v7_contrastive) | **58.4%** (292/500) | **-7.6 pp** |
| **seed2** (v7_seed2) | **51.4%** (257/500) | **-14.6 pp** |

两个 seed 在 spatial 上都**显著低于 baseline**。

---

### 当前进度

| Process | Suite | Task Progress | Status |
|---------|-------|---------------|--------|
| seed1 (PID 104743) | libero_object | 完成 tasks 0-3, 当前 task 4 (batch 46/50) | Running |
| seed2 (PID 111920) | libero_object | 完成 tasks 0-2, 当前 task 3 (batch 2/50) | Running |

评估顺序: spatial → **object** → goal → libero_10

GPU 显存 ~6GB 各，利用率 0-1%（推理间歇模式正常）。

---

### 预估剩余时间

spatial 用了约 26 小时（01:21 → 03:19 = ~2h for spatial per seed）。还剩 object（~60% 完成）、goal、libero_10 三个 suite，预计 seed1 还需 ~4-5h, seed2 还需 ~5-6h。

---
