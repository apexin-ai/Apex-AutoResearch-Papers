# fix folio nli seed456 recompute

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_folio-nli-seed456-recompute_20260523T172925_result.json`
- **Structured JSON:** [`eccea12f2763f8796d21.json`](../../sessions/ec/eccea12f2763f8796d21.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three result files saved on server. Summary of what changed:

**Traces** (canonical exp033/exp-063/exp036/exp_folio_2x2_qwen3, same as `cross_model_sc_ablation.py`) — confirmed SC=55.88/66.18/75.98/83.33 with alphabetical tiebreaking.

**`docs/paper/appendix.tex` updates:**

- `tab:folio-nli-deberta`: SC fixed (Mistral 57.84→55.88, Qwen2.5 77.45→75.98); all 12 combo cells recomputed. DeBERTa w=3 rows now identical to `tab:cross-model-ablation` "DeBERTa NLI" rows.
- `tab:folio-nli-bart`: SC fixed; combo cells recomputed. Caption updated to note Qwen2.5-14B w=5 shows significant degradation (Δ=−3.43, p=.039) — same capability-gap signature.
- `tab:folio-nli-roberta`: SC fixed; combo cells recomputed. Caption updated to note Qwen2.5-14B w=5 significant degradation (Δ=−4.41, p=.012).

**Script:** `/root/symb_invariant_consensus/scripts/folio_nli_combo_bart_roberta.py` (takes `--verifier` for any of the three models). **Outputs:** `results/folio_nli_combo_all/folio_nli_combo_{deberta,bart,roberta}.json`.

**Caveat for awareness:** the brief said "seed456 traces" but `cross_model_sc_ablation.py` actually points at the canonical `exp033_mistral_7b_folio204` (not `exp053_..._seed456`); the 55.88% baseline matches exp033 + alphabetical tiebreaking, so that is what was used for consistency.

---
