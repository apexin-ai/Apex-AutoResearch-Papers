# exp llm judge gold r5

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llm-judge-gold-r5_20260516T051736_result.json`
- **Structured JSON:** [`d8876fb6c33fac50692d.json`](../../sessions/d8/d8876fb6c33fac50692d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment `llm-judge-gold-r5` registered as DONE/success. Final results:

| Method | macro_F1 | f1_stag | f1_prog | accuracy | cost |
|--------|----------|---------|---------|----------|------|
| LLM zero-shot | 0.784 | 0.721 | 0.847 | 0.802 | $2.96 |
| **LLM few-shot-CoT** | **0.910** | **0.871** | **0.949** | **0.927** | $11.87 |
| Structural GB | 0.839 | — | — | — | — |

Key takeaways for the rebuttal:
- **Few-shot-CoT LLM judge achieves 0.910 macro_F1**, beating structural GB (0.839) by **+7.1pp** — this is a strong non-circular gold baseline
- Zero-shot LLM underperforms GB by 5.5pp, showing CoT and few-shot examples are critical
- Zero-shot has extreme recall asymmetry: stagnation recall 0.97 but precision only 0.57 (over-predicts stagnation). CoT fixes this (precision 0.81, recall 0.94)
- 505/505 valid predictions in both modes, zero parse failures

Artifacts on server: `artifacts/llm-judge-gold/{summary.json, results_zero_shot.json, results_few_shot_cot.json, prompts.json}`

---
