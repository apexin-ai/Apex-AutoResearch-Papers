# analyze eval vla only long seed42 seed44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-vla-only-long-seed42-seed44_20260519T183631_result.json`
- **Structured JSON:** [`1446faf6ae3f9a59de0b.json`](../../sessions/14/1446faf6ae3f9a59de0b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验 registry 均已更新为 DONE。汇总：

```
eval-vla-only-long-seed42: overall_success_rate = 11%
eval-vla-only-long-seed43: overall_success_rate = 13%
eval-vla-only-long-seed44: overall_success_rate = 12%

三个 seed 均值 = 12.0% ± 1.0%
```

Per-task 分布高度一致——KITCHEN_SCENE3 (stove+moka pot) 在三个 seed 上都是唯一高成功率 task（70-80%），其余 9 个 task 成功率均 ≤ 20%，6 个 task 三 seed 全为 0%。LIBERO-Long 对 VLA-only baseline 的 long-horizon 多步任务极具挑战性。

---
