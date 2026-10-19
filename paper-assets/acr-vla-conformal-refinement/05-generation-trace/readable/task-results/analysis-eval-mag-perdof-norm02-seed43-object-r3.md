# analysis eval mag perdof norm02 seed43 object r3

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-mag-perdof-norm02-seed43-object-r3_20260516T104054_result.json`
- **Structured JSON:** [`90176cd7b5c3cd8be55e.json`](../../sessions/90/90176cd7b5c3cd8be55e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果汇报

**perdof CRM norm=0.2, seed=43, LIBERO object benchmark**

### Overall SR: **9%** (9/100)

### 每 task SR

| Task | SR |
|------|-----|
| alphabet_soup | 0% |
| cream_cheese | 0% |
| salad_dressing | 10% |
| bbq_sauce | 10% |
| ketchup | 0% |
| tomato_sauce | 0% |
| butter | 0% |
| milk | 0% |
| chocolate_pudding | **40%** |
| orange_juice | **30%** |

### 与 seed=42 对比

| | seed=42 | seed=43 | 2-seed pooled |
|---|---------|---------|---------------|
| perdof norm=0.2 | 11% | **9%** | **10% (20/200)** |

seed=43 比 seed=42 低 2pp，两个 seed pooled 后 perdof norm=0.2 = **10%**。

对比 obs_only norm=0.2 的 pooled 结果 (19%, 38/200)，perdof 在 norm=0.2 下明显更差（10% vs 19%）。

### Registry 更新

已成功更新：status=DONE, conclusion=success, metrics 已写入。

---
