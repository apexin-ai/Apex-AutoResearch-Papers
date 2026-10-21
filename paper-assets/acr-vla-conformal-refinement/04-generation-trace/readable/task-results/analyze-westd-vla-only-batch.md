# analyze westd vla only batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_westd-vla-only-batch_20260526T115512_result.json`
- **Structured JSON:** [`5d533dd409ce736d08a4.json`](../../sessions/5d/5d533dd409ce736d08a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## π0.5 VLA-only Baseline 结果汇总

### 实验总表

| exp_id | suite | seed | SR% | n_rollouts | 完成状态 |
|--------|-------|------|-----|------------|---------|
| westd-pi05-vla-only-goal-s42-paired | Goal | 42 | 97.5 | 20×10=200 | ✅ EXIT_CODE=0 |
| westd-pi05-vla-only-goal-s43-paired | Goal | 43 | 96.5 | 20×10=200 | ✅ EXIT_CODE=0 |
| westd-pi05-vla-only-goal-s44-paired | Goal | 44 | 95.5 | 20×10=200 | ✅ EXIT_CODE=0 |
| westd-pi05-vla-only-object-s42-paired | Object | 42 | 99.5 | 20×10=200 | ✅ EXIT_CODE=0 |
| westd-pi05-vla-only-object-s43-paired | Object | 43 | 100.0 | 20×10=200 | ✅ EXIT_CODE=0 |
| westd-pi05-vla-only-object-s44-paired | Object | 44 | 99.5 | 20×10=200 | ✅ EXIT_CODE=0 |

### 统计汇总

| Suite | Mean SR% | Std (sample) |
|-------|----------|-------------|
| **Goal** | **96.50 ± 1.00** | σ=1.00 |
| **Object** | **99.67 ± 0.29** | σ=0.29 |

### 异常检查

- **无异常。** 三个 seed 间差异很小（Goal 最大差 2.0pp，Object 最大差 0.5pp），方差正常。
- 所有实验每任务 20 rollouts × 10 tasks = 200 rollouts，数量充足。
- Goal suite 中 `open_the_top_drawer_and_put_the_bowl_inside` 是最难任务（三 seed 分别 90%/85%/80%），其余任务 ≥95%。
- Object suite 仅 `pick_up_the_bbq_sauce` 在 s42/s44 各失败 1 次（95%），其余全部 100%。

---
