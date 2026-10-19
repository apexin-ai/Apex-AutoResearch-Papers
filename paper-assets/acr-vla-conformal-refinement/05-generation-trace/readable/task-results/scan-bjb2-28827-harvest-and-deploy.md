# scan bjb2 28827 harvest and deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_scan_bjb2-28827-harvest-and-deploy_20260523T225833_result.json`
- **Structured JSON:** [`56aaee27e64b5816a501.json`](../../sessions/56/56aaee27e64b5816a501.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registry entries updated. Here's the summary:

---

## bjb2-28827 状态总览

### 收割完成的实验

| 实验 | SR | 结论 |
|------|-----|------|
| **Goal CRM s45** | **81.0%** | success (已在之前收割) |
| **Long Reconvla s44** | **57.0%** | success (vs VLA-only 56.5%) |
| **Long K2mean s44** | **54.5%** | negative (vs VLA-only 56.5%, K2mean 有害) |

### GPU 分配（全部 6 卡在用）

| GPU | 实验 | 状态 |
|-----|------|------|
| 0 | Goal VLA-only s46 | RUNNING (pre-existing) |
| 1 | Goal K2mean s46 | RUNNING (新部署) |
| 2 | Goal Reconvla s46 | RUNNING (pre-existing) |
| 3 | Goal CRM s46 | RUNNING (新部署) |
| 4 | Long K2mean s45 | RUNNING (继续, task 5/10) |
| 5 | Goal Adapt s46 | RUNNING (新部署) |

### 新部署实验（Goal s46 × 5 methods）
部署 Goal s46 全套 5 个方法，完成后 Goal suite 每个方法将有 4-5 seeds 覆盖。

### 注意事项
- Goal Adapt s46 可能在 cqa1-32758 也有另一个 agent 部署的副本，需后续确认。
- Goal 仍缺 K2mean/CRM/Reconvla 的 s43 seed（目前仅 2-3 seeds），下一批可补。

---
