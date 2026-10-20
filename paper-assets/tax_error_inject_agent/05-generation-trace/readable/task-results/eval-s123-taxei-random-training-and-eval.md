# eval s123 taxei random training and eval

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_s123-taxei-random-training-and-eval_20260516T145033_result.json`
- **Structured JSON:** [`939882ad00e10746ec8e.json`](../../sessions/93/939882ad00e10746ec8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 eval 完成并验证。最终结果：

| Condition | Clean SR | Recovery Rate | Detection Rate |
|-----------|----------|---------------|----------------|
| TaxEI s123 | 61.7% | 61.4% (27/44) | 75.0% (33/44) |
| Random s123 | 76.6% | 68.9% (31/45) | 53.3% (24/45) |

**关键发现**：
- TaxEI 的 detection rate (75%) 显著高于 Random (53.3%)，说明 TaxEI 训练的模型更擅长识别注入错误
- Random 的 clean SR 和 recovery rate 都高于 TaxEI，但这主要因为 random 模型本身 task 能力更强
- TaxEI 模型在被注入错误后，clean→injected 的性能下降更小（61.7%→61.4%），而 random 下降更大（76.6%→68.9%）

---
