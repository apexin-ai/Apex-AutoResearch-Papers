# collect smolvla long 3seed baseline

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_smolvla-long-3seed-baseline_20260522T181748_result.json`
- **Structured JSON:** [`0a9498eba9ec4ad74fea.json`](../../sessions/0a/0a9498eba9ec4ad74fea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验全部收集完毕，注册表已更新为 DONE。

## SmolVLA LIBERO-Long Baseline 结果

| Seed | Success Rate | n_episodes |
|------|-------------|------------|
| 42 | 49.5% | 200 |
| 43 | 53.5% | 200 |
| 44 | 49.5% | 200 |
| **Mean** | **50.8% ± 2.3%** | |

Per-task breakdown (10 tasks × 20 episodes each):

| Task | seed42 | seed43 | seed44 |
|------|--------|--------|--------|
| 0 | 20% | 20% | 30% |
| 1 | 55% | 60% | 55% |
| 2 | 60% | 70% | 50% |
| 3 | 80% | 80% | 95% |
| 4 | 30% | 40% | 25% |
| 5 | 75% | 65% | 75% |
| 6 | 35% | 35% | 30% |
| 7 | 40% | 40% | 35% |
| 8 | 40% | 55% | 55% |
| 9 | 60% | 70% | 45% |

注意：50.8% 远高于之前报告的 15.7%，说明之前的 Long 单 seed 结果可能使用了不同配置（如不同的 n_action_steps 或评估设置）。

---
