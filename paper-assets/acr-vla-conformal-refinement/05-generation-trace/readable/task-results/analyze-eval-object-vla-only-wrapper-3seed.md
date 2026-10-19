# analyze eval object vla only wrapper 3seed

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-object-vla-only-wrapper-3seed_20260523T070524_result.json`
- **Structured JSON:** [`07c8ca368c54206ca80d.json`](../../sessions/07/07c8ca368c54206ca80d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验 registry 全部更新完毕（metrics / conclusion=success / status=DONE / spec）。

## Object VLA-only Wrapper 基线结果（LIBERO-Object, 10 tasks × 20 rollouts = 200 episodes）

| Seed | Success Rate | Successes/Episodes |
|------|-------------|-------------------|
| 42 | **79.0%** | 158/200 |
| 43 | **77.0%** | 154/200 |
| 44 | **77.5%** | 155/200 |

**3-seed 统计：77.8% ± 1.0% (mean ± std)**

Per-task 成绩（3-seed 范围）：

| Task | s42 | s43 | s44 |
|------|-----|-----|-----|
| alphabet_soup | 85% | 70% | 70% |
| cream_cheese | 75% | 70% | 70% |
| salad_dressing | 85% | 75% | 75% |
| bbq_sauce | 85% | 85% | 90% |
| ketchup | 90% | 80% | 90% |
| tomato_sauce | 75% | 85% | 80% |
| butter | 65% | 60% | 75% |
| milk | 65% | 75% | 65% |
| chocolate_pudding | 70% | 75% | 65% |
| orange_juice | 95% | 95% | 95% |

orange_juice 最稳定（95% across all seeds），butter 和 milk 波动最大（60-75%）。

---
