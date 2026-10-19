# analyze eval supp goal reconvla s42 vla only wrapper

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-supp-goal-reconvla-s42_vla-only-wrapper_20260523T093302_result.json`
- **Structured JSON:** [`a077025c62a3e4a36781.json`](../../sessions/a0/a077025c62a3e4a36781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

```
eval-supp-goal-reconvla-s42:       SR = 81.0% (162/200)
eval-goal-vla-only-wrapper-s42:    SR = 83.5% (167/200)
```

日志中无 trigger_rate / correction 统计，无运行时长记录。

### 逐 task 对比

| Task | ReconVLA K=10 | VLA-only | Δ |
|------|:---:|:---:|:---:|
| open_middle_drawer_of_cabinet | 75.0% | **85.0%** | -10 |
| put_bowl_on_stove | 95.0% | **100.0%** | -5 |
| put_wine_bottle_on_top_of_cabinet | 90.0% | 90.0% | 0 |
| open_top_drawer_put_bowl_inside | 50.0% | **75.0%** | **-25** |
| put_bowl_on_top_of_cabinet | **95.0%** | 80.0% | +15 |
| push_plate_to_front_of_stove | 85.0% | 85.0% | 0 |
| put_cream_cheese_in_bowl | **45.0%** | 40.0% | +5 |
| turn_on_stove | 100.0% | 100.0% | 0 |
| put_bowl_on_plate | 95.0% | 95.0% | 0 |
| put_wine_bottle_on_rack | 80.0% | **85.0%** | -5 |

### 关键发现

1. **VLA-only baseline 远超预期**：83.5% vs 假设的 71%，说明 wrapper 改造后 VLA 本身在 Goal suite 上表现很好。
2. **ReconVLA K=10 反而降低了整体 SR**：81.0% vs 83.5%，correction 在 Goal suite 上是负收益（-2.5pp）。
3. **最大退化**在 `open_top_drawer_put_bowl_inside`（-25pp），说明 K=10 argmin 在多步任务上可能引入有害校正。
4. **ReconVLA 仅在 2 个任务上有正向贡献**：`put_bowl_on_top_of_cabinet`（+15）和 `put_cream_cheese_in_bowl`（+5）。

---
