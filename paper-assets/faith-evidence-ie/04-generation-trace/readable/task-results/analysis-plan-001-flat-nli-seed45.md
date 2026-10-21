# analysis plan 001 flat nli seed45

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_001_flat_nli_seed45_20260515T230918_result.json`
- **Structured JSON:** [`0144700c293a032b4e14.json`](../../sessions/01/0144700c293a032b4e14.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**plan_001_flat_nli_seed45 训练结果: SUCCESS**

关键数据:

| 指标 | 值 |
|------|-----|
| Train loss | 0.6245 |
| Task-eval F1 (final, 50 docs) | **0.4876** |
| Task-eval Evi-F1 | 0.7927 |
| Task-eval EDCR | 0.6517 |
| Runtime | ~1h39m |
| Checkpoint | `/root/autodl-tmp/rsft_output_flat_nli_s45/` (529MB adapter) |

F1 逐 epoch 稳步上升 (0.4522 → 0.4700 → 0.4876)，无过拟合。与 s42 eval rel_f1=0.4539 相比，s45 task-eval 数值更高，但 task-eval 仅 50 docs，需正式 eval 才能对比。

---
