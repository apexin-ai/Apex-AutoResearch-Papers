# experiment exp 017 llama conll n16 s123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_exp_017_llama_conll_n16_s123_20260514T192424_result.json`
- **Structured JSON:** [`a36ae098c3dd6a0a7d8b.json`](../../sessions/a3/a36ae098c3dd6a0a7d8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. `exp_017_llama_conll_n16_s123` completed successfully.

**Summary:**

| Signal | Full ρ (N=8→N=16) | Full AUROC (N=8→N=16) |
|---|---|---|
| **SJ** | 0.4314→**0.4698** (+0.038) | 0.7039→**0.7402** (+0.036) |
| **FK** | 0.4277→**0.4594** (+0.032) | 0.7026→**0.7351** (+0.033) |
| logprob | 0.3072→0.3161 (+0.009) | 0.7610→0.7680 (+0.007) |
| EM | 0.4306→0.4676 (+0.037) | 0.7046→0.7399 (+0.035) |
| voting_conf | 0.4256→0.4612 (+0.036) | 0.7088→0.7429 (+0.034) |

**Conclusion: success** — structural > surface (SJ_ρ=0.470 >> logprob_ρ=0.316). Seed=123 confirms the same ranking as seed=42 baseline. Key finding: structural signals benefit **4× more** from N=8→N=16 scaling than logprob (Δρ ≈ +0.035 vs +0.009), consistent with the hypothesis that structural consistency signals improve with more samples while surface logprob is nearly N-invariant.

---
