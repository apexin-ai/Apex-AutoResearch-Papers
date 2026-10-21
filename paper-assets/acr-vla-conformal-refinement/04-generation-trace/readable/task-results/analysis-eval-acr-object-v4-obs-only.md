# analysis eval acr object v4 obs only

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-acr-object-v4-obs-only_20260515T160113_result.json`
- **Structured JSON:** [`b59250fdbbf649984005.json`](../../sessions/b5/b59250fdbbf649984005.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果：obs_only object 10-task = **19.0%** — 项目存活

### Per-Task

| Task | obs_only | VLA-only | Δ |
|------|----------|----------|---|
| alphabet_soup | 0% | 0% | 0 |
| cream_cheese | 10% | 10% | 0 |
| salad_dressing | 20% | 20% | 0 |
| bbq_sauce | **40%** | 20% | **+20** |
| ketchup | 10% | 0% | +10 |
| tomato_sauce | 0% | 10% | -10 |
| butter | 10% | 0% | +10 |
| milk | 20% | 10% | +10 |
| chocolate_pudding | **50%** | 20% | **+30** |
| orange_juice | 30% | 30% | 0 |
| **Average** | **19.0%** | **12.0%** | **+7.0pp** |

### Baseline 对比

| Method | SR | vs obs_only |
|--------|-----|-------------|
| **obs_only** | **19.0%** | — |
| VLA-only | 12.0% | -7pp |
| perdof | 11.0% | -8pp |
| argmin (6/10 partial) | ~6.7% | ~-12pp |

### 判定

**SUCCESS**。obs_only 在 object 上 19% vs VLA-only 12%，+7pp 改进显著超过 +6pp 门槛。chocolate_pudding (+30pp) 和 bbq_sauce (+20pp) 是最大赢家。后 4 个 task 将均值从 13.3% 拉到 19.0%。

Registry 已更新为 DONE/success，报告已注册。

---
