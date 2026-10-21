# experiment dir k nli qwen3 proofwriter

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_dir-k-nli-qwen3-proofwriter_20260520T180214_result.json`
- **Structured JSON:** [`46e989bf5a91535a0c7e.json`](../../sessions/46/46e989bf5a91535a0c7e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved at `westd-16639:/root/symb_invariant_consensus/results/dir_k_nli_qwen3_proofwriter/results.json`.

## Results Summary

| Metric | Qwen3-14B PW600 | Mistral-7B PW600 |
|--------|-----------------|-------------------|
| **SC baseline** | **85.00%** | 39.33% |
| **SICA baseline** | **85.67%** | 36.50% |
| **DeBERTa standalone** | 36.17% (base) | 55.00% (large) |
| **w=1 combo** | 85.50% (+0.50pp, p=0.375) | 40.17% (+0.83pp, p=0.267) |
| **w=3 combo** | 85.50% (+0.50pp, p=0.508) | 42.83% (+3.50pp, p=0.013) |
| **w=5 combo** | 85.33% (+0.33pp, p=0.832) | 50.00% (+10.67pp, p<0.0001) |

**Key observations:**

1. **NLI combo has negligible effect on Qwen3-14B**: all deltas < 1pp, none significant. This contrasts sharply with Mistral-7B where w=3 gave +3.50pp (p=0.013).

2. **Root cause**: Qwen3's SC baseline (85%) massively outperforms DeBERTa standalone (36.17%). With k=12 SC traces, the NLI vote (weight 1-5) is overwhelmed. On Mistral-7B, DeBERTa (55%) was *better* than SC (39.33%), so NLI votes could swing decisions.

3. **DeBERTa-base has severe class imbalance**: predicts False 571/600 times (95.2%). True recall=7.5%, Unknown recall=3.0%. This bias makes it ineffective as a verifier.

4. **Agreement rate only 30.67%**: when they disagree, SC is right 333 vs DeBERTa 40 — confirming SC dominance.

5. **NLI note**: used `deberta-base-mnli` (not `deberta-large-mnli` from the Mistral experiment). The large model had 55% standalone on this data vs 36.17% for base — so even with the large model, the pattern (NLI << SC for strong models) would likely hold, though the gap would narrow.

---
