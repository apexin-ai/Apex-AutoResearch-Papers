# analyze object analyzing batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_object-analyzing-batch_20260523T070446_result.json`
- **Structured JSON:** [`5f0e68c3148b1763d2e3.json`](../../sessions/5f/5f0e68c3148b1763d2e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部更新完毕。汇总：

| exp_id | SR | 结论 | 关键发现 |
|--------|-----|------|---------|
| eval-object-vla-only-wrapper-s42-r2 | **79.0%** (158/200) | success | Baseline 最高 seed；orange_juice 95% 最佳，butter/milk 65% 最弱 |
| eval-object-vla-only-wrapper-s43-r2 | **77.0%** (154/200) | success | 3-seed 中最低；butter 60% 是全部实验中单 task 最低 |
| eval-object-vla-only-wrapper-s44-r2 | **77.5%** (155/200) | success | bbq_sauce/ketchup 90% 高于其他 seed |
| eval-supp-obj-adapt-s42-r2 | **77.5%** (155/200) | **negative** | Adaptive CRM 77.5% ≤ VLA-only baseline 79.0%（同 seed）；trigger_rate=70.2%，CRM 频繁触发但未带来增益，说明 conformal gating 从 Spatial→Object 泛化失败 |

**VLA-only Object baseline 3-seed 均值：77.83% ± 1.04%**

Adaptive CRM 在 Object suite 上不仅没有提升，反而略低于 baseline。70.2% 的高 trigger rate 表明 CRM 在大多数 step 都在施加修正，但这些修正并非有益——可能是因为 CRM 在 Spatial 上训练的修正模式不适用于 Object suite 的抓取动作。

---
