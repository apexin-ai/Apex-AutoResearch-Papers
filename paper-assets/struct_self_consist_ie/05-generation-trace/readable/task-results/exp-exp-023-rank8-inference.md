# exp exp 023 rank8 inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_exp_023_rank8_inference_20260516T111332_result.json`
- **Structured JSON:** [`b6c1da87204569b12fc9.json`](../../sessions/b6/b6c1da87204569b12fc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Summary:

**exp_023 LoRA rank=8 完成**

| | NER (n=529) | RE (n=397) |
|---|---|---|
| **Greedy F1** | 0.640 (r16: 0.643, Δ=-0.003) | 0.371 (r16: 0.391, Δ=-0.020) |
| **Oracle F1** | 0.800 (headroom 0.160) | 0.609 (headroom 0.238) |
| **Degeneracy** | 7.2% | 21.7% |

**Correlation (ρ) vs r16 baseline:**
- NER: VC 0.394 (+0.015), SJ 0.365 (+0.005), FK 0.284 (+0.017) — correlation structure preserved
- RE: VC 0.362 (+0.012), FK 0.345 (+0.070), LP 0.274 (+0.008) — FK notably improved

**Selection F1:** No signal beats greedy for NER (LP closest at -0.005). RE: only VC marginally matches greedy (+0.0003).

**Key finding:** Reducing LoRA rank from 16→8 preserves the correlation signal hierarchy (structural > surface for NER) with negligible changes in ρ (|Δ| < 0.04 for most signals), despite slight greedy F1 drop. The correlation-selection gap persists at rank=8 — selection F1 still fails to leverage the correlation signal to outperform greedy.

Outputs:
- Merged model: `checkpoints/qwen3-8b-scierc-merged-rank8/`
- Inference: `output/exp_023_rank8_inference/` (samples.jsonl, all_signals_5signal.json, comparison.md)
- Registry: exp_023_lora_rank8 → DONE

---
