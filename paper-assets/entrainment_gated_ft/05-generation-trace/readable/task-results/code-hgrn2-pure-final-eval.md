# code hgrn2 pure final eval

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_hgrn2_pure_final_eval_20260518T183049_result.json`
- **Structured JSON:** [`971fb70ddf47b697a606.json`](../../sessions/97/971fb70ddf47b697a606.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评测完成。HGRN2-pure 全量 6 tasks 结果：

| Task | Metric | Score |
|------|--------|-------|
| **lambada_openai** | acc | 0.4842 |
| **lambada_openai** | ppl | 11.362 |
| **hellaswag** | acc | 0.4564 |
| **hellaswag** | acc_norm | 0.5983 |
| **winogrande** | acc | 0.5919 |
| **arc_easy** | acc | 0.7138 |
| **arc_easy** | acc_norm | 0.6654 |
| **arc_challenge** | acc | 0.3626 |
| **arc_challenge** | acc_norm | 0.4002 |
| **mmlu** | acc | 0.2387 |

结果已保存至 `/root/entrainment_gated_ft/lm_eval_clean/1.3B-100B-HGRN2-pure.json`。

所有指标在合理范围内（ppl=11.36 < 1000，acc 均 > 0.1），无异常。MMLU ~0.24 接近随机（4 选 1 基线 0.25），符合 1.3B 模型预期。

---
