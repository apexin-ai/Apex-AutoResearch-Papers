# scan bjb2 28827 and 40593 harvest

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_bjb2-28827-and-40593-harvest_20260523T214852_result.json`
- **Structured JSON:** [`4c8abeaaef898854fc97.json`](../../sessions/4c/4c8abeaaef898854fc97.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### bjb2-28827

**新完成（今天 04:09-04:12 写入 JSON）：**

| 实验 | SR |
|------|-----|
| Object Adaptive Conformal CRM τ=0.25 **s46** | **0.775** |
| Object Adaptive Conformal CRM τ=0.25 **s45** | **0.78** |
| Object VLA-only **s45** | **0.76** |

**运行中：**

| GPU | 实验 | 进度 | ETA |
|-----|------|------|-----|
| cuda:0 | Goal VLA-only s45 | 6/10 tasks (60%) | ~5-6h |
| cuda:1 | Goal CRM s45 | 6/10 tasks, rollout 15/20 (60%) | ~5-6h |
| cuda:2 | Goal Reconvla s45 | 6/10 tasks done (60%) | ~5-6h |
| cuda:3 | Long Reconvla s44 | 9/10 tasks, rollout 5/20 (85%) | ~2-3h |
| cuda:4 | Long K2mean s45 | 3/10 tasks, rollout 10/20 (25%) | ~20+h |
| cuda:5 | Long K2mean s44 | 8/10 tasks done (80%) | ~3h |

Long Reconvla s44 和 Long K2mean s44 即将完成（2-3h）。Goal 系列约 60% 进度。Long K2mean s45 最慢，才 25%。

---

### bjb2-40593

**运行中：**

| GPU | 实验 | 进度 | ETA |
|-----|------|------|-----|
| cuda:0 | Object CRM s45 | 9/10 tasks, rollout 15/20 (~93%) | ~30-60min |

Object CRM s45 即将完成，只差最后 1.5 个 task 的 rollouts。

---
