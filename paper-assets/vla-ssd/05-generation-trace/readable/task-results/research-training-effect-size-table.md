# research training effect size table

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_training_effect_size_table_20260517T033754_result.json`
- **Structured JSON:** [`33b278682a12555b80d8.json`](../../sessions/33/33b278682a12555b80d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the complete training effect size table compiled from the exact JSON values:

```
| Metric                       | Trained            | Untrained          | Δ          | Source File                                           |
|------------------------------|--------------------|--------------------|------------|-------------------------------------------------------|
| RSA peak (image_mean)        | 0.6282 (L12)       | 0.6117 (L0)        | +0.0165    | results/rsa/unified_rsa_results.json                  |
| RSA peak (last_preaction)    | 0.6425 (L12)       | 0.6262 (L1)        | +0.0163    | results/rsa/unified_rsa_results.json                  |
| R² peak (image_mean)         | 0.6553 (L8)        | 0.6403 (L0)        | +0.0150    | results/functional_validation/fulllayer_action_probe.json |
| R² peak (last_preaction)     | 0.6779 (L13)       | 0.6093 (L32)       | +0.0686    | results/functional_validation/fulllayer_action_probe.json |
| Inst. routing L31            | 100.0%             | 82.0%              | +18.0pp    | results/cross_instruction/classification_results.json |
| Inst. attention L1           | 57.69%             | 11.70%             | +45.99pp   | results/attention/l1_attention_{trained,untrained}_summary.json |
| Progress classification      | 86.32% (L20)       | 85.32% (L4)        | +1.00pp    | results/qa_probe/classification_results.json          |
| Subtask classification       | 93.67% (L16)       | 93.06% (L12)       | +0.61pp    | results/qa_probe/classification_results.json          |
```

Notes on computation:
- **Inst. attention L1 (trained)**: averaged `mean_attn_to_text` across 3 tasks = (0.5729 + 0.5779 + 0.5798) / 3 = 0.5769
- **Inst. attention L1 (untrained)**: from `aggregate.mean_instr_attn` = 0.1170
- **R² last_preaction untrained**: the fulllayer file shows peak at L32 = 0.6093; a separate dedicated file (`untrained_last_preaction_probe.json`) reports 0.6858 at L32 with different training epochs (9 vs potentially different). The fulllayer file uses the same methodology for both conditions, so I used it for consistency.
- **Inst. routing**: trained last_preaction achieves perfect 100% classification at L8/L16/L24/L31; untrained declines from 98.2% (L8) to 82.0% (L31).

---
