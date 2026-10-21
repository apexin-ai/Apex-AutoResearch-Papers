# ops check seed43 obs only progress

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-seed43-obs-only-progress_20260516T003855_result.json`
- **Structured JSON:** [`90933559a9adff6051f2.json`](../../sessions/90/90933559a9adff6051f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 1. obs_only ε=0.1 seed43 (bjb1-18228) — 已完成 ✓

进程 356495 已退出，JSON 完整（10/10 tasks）。**Overall SR = 12%**

| Task | SR | Successes |
|------|-----|-----------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 10% | 1/10 |
| salad_dressing | 10% | 1/10 |
| bbq_sauce | 30% | 3/10 |
| ketchup | 0% | 0/10 |
| tomato_sauce | 0% | 0/10 |
| butter | 0% | 0/10 |
| milk | 10% | 1/10 |
| chocolate_pudding | 40% | 4/10 |
| orange_juice | 20% | 2/10 |

### 2. obs_only ε=0.2 seed43-r2 (bjb1-32546) — 运行中

进程 148797 存活，已运行 **5h41m**。当前进度 **4.5/10 tasks**。

已完成 4 个 task，第 5 个 (ketchup) 进行到 rollout 5/10：

| Task | SR | Status |
|------|-----|--------|
| alphabet_soup | 0% (0/10) | ✓ done |
| cream_cheese | 10% (1/10) | ✓ done |
| salad_dressing | 20% (2/10) | ✓ done |
| bbq_sauce | 40% (4/10) | ✓ done |
| ketchup | 0/5 so far | in progress |
| tasks 6-10 | — | pending |

**Partial SR (4 tasks)**: 7/40 = **17.5%**

**ETA 估算**: ~85 min/task × 5.5 remaining ≈ **~7.5-8 小时**（约今晚 23:00-24:00 完成）

### 关键发现

- ε=0.1 seed43 SR=12%，与 seed42 的 12% 一致，obs_only baseline 稳定
- ε=0.2 seed43 部分结果 17.5%（4 tasks），比 ε=0.1 高——但 bbq_sauce 40% 拉高了均值，后续 task 可能回落

---
