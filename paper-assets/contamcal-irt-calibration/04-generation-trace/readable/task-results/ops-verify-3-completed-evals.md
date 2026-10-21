# ops verify 3 completed evals

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-3-completed-evals_20260515T051615_result.json`
- **Structured JSON:** [`8bef20473cab966b5e15.json`](../../sessions/8b/8bef20473cab966b5e15.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部验证通过，metrics 已录入 registry。

**汇总：**

| 实验 | MMLU | GSM8K | ARC | HumanEval |
|------|------|-------|-----|-----------|
| **3B d025 v2 para_aligned** | 0.621 | 0.548 | 0.811 | 0.115 |
| **3B d100 v2 aligned_v2** | 0.632 | 0.742 | 0.824 | 0.171 |
| **0.5B-Instruct** | 0.246 | 0.388 | 0.282 | 0.0 |

- 3 个实验均有完整的 4 个 benchmark 输出（eval_results.json + correctness_matrix.json + item_responses.json）
- exp_001_eval_3B_d025_v2_para_aligned 有 .done 标记，另外 2 个无 .done 但输出文件完整有效
- 状态已为 DONE/success，本次仅补录了 metrics

---
