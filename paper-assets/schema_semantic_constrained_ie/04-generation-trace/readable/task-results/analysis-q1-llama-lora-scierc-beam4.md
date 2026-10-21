# analysis q1 llama lora scierc beam4

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q1_llama_lora_scierc_beam4_20260518T141444_result.json`
- **Structured JSON:** [`b6d42e4ca30403799edf.json`](../../sessions/b6/b6d42e4ca30403799edf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== RESULTS: q1_llama_lora_scierc_beam4 ===
Status: completed
Docs processed: 551/551
Parse failures: 0 (0.0%)

Violation Metrics:
- ET (entity type): 0.0%
- RV (relation vocab): 0.0%
- DR (domain-range): 0.0%
- CF (cross-field): 0.0%
- Total violation rate: 0.0%

Performance:
- Entity F1/P/R: 67.94 / 65.84 / 70.17
- Relation F1/P/R: 46.11 / 41.99 / 51.13

vs Parent (Qwen FT+beam k=4, full_s1):
  - Entity F1: 67.94 vs 66.88 (+1.06) — Llama slightly better
  - Entity P: 65.84 vs 64.69 (+1.15)
  - Entity R: 70.17 vs 69.22 (+0.95)
  - Violations: both all-zero — identical

vs Llama FT greedy (w5, full_s1):
  - Entity F1: 67.94 vs 67.76 (+0.18) — nearly identical
  - Relation F1: 46.11 vs 45.47 (+0.64)
  - DR: 0.0% vs 0.09% — beam eliminates residual DR
  - CF: 0.0% vs 0.46% — beam eliminates residual CF

vs Llama base beam (w9, non-FT, full_s1):
  - CF: 0.0% vs 0.93% — FT eliminates CF violations that base model still had

Hypothesis verified: YES
Llama LoRA FT + beam k=4 + full_s1 achieves zero violations across all four categories (ET=0%, RV=0%, DR=0%, CF=0%), replicating the Qwen FT+beam result. Additionally, Entity F1 is slightly higher than both the Qwen baseline and Llama greedy variant, confirming that beam search with constrained decoding on a fine-tuned model eliminates all schema violations without sacrificing extraction quality.
```

---
