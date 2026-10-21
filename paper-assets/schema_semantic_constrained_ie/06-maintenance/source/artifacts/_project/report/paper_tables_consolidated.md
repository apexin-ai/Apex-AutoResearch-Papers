# Paper Tables Consolidated — Composability Matrix
> Generated: 2026-05-15 | For May 19 internal draft

All violation rates and F1 scores in **percentage (%)** units. SciERC raw 0–1 metrics converted to %.

---

## Table 3: Zero-shot Composability (2 models × 2 datasets × 2 conditions)

| Model | Dataset | Condition | ET% | RV% | DR% | CF% | E-F1 | R-F1 | exp_id |
|-------|---------|-----------|-----|-----|-----|-----|------|------|--------|
| Qwen-2.5-7B | SciERC | Unconstrained | 0.40 | 1.39 | 15.37 | 0.08 | 31.01 | 8.23 | `phase2_scierc_unconstrained` |
| Qwen-2.5-7B | SciERC | Constrained | 0.00 | 0.00 | 0.93 | 9.90 | 30.98 | 8.36 | `phase2_scierc_full_s1` |
| Qwen-2.5-7B | DocRED | Unconstrained | 2.48 | 29.66 | 18.46 | 0.10 | 58.15 | 7.74 | `phase2_docred_unconstrained` |
| Qwen-2.5-7B | DocRED | Constrained | 0.00 | 0.03 | 10.21 | 2.57 | 59.37 | 8.23 | `phase2_docred_full_s1` |
| Llama-3.1-8B | SciERC | Unconstrained | 0.00 | 0.55 | 13.34 | 0.47 | 23.56 | 2.68 | `llama_scierc_unconstrained` |
| Llama-3.1-8B | SciERC | Constrained | 0.00 | 0.00 | 0.08 | 6.56 | 23.49 | 2.54 | `llama_scierc_full_s1` |
| Llama-3.1-8B | DocRED | Unconstrained | 0.13 | 16.03 | 26.07 | 0.17 | 55.65 | 5.98 | `llama_docred_unconstrained` |
| Llama-3.1-8B | DocRED | Constrained | 0.00 | 0.00 | 2.55 | 12.02 | 55.01 | 6.27 | `llama_docred_full_s1` |

### Table 3 Deltas (Constrained − Unconstrained)

| Model | Dataset | ΔDR (pp) | DR Red.% | ΔE-F1 (pp) | ΔR-F1 (pp) |
|-------|---------|----------|----------|------------|------------|
| Qwen-2.5-7B | SciERC | −14.44 | **93.9%** | −0.03 | +0.13 |
| Qwen-2.5-7B | DocRED | −8.25 | **44.7%** | +1.22 | +0.49 |
| Llama-3.1-8B | SciERC | −13.26 | **99.4%** | −0.07 | −0.14 |
| Llama-3.1-8B | DocRED | −23.52 | **90.2%** | −0.64 | +0.29 |

---

## Table 5: Fine-tuned Composability (2 models × 2 datasets × 2 conditions)

| Model | Dataset | Condition | ET% | RV% | DR% | CF% | E-F1 | R-F1 | exp_id |
|-------|---------|-----------|-----|-----|-----|-----|------|------|--------|
| Qwen-2.5-7B | SciERC | Unconstrained | 0.00 | 0.00 | 1.95 | 0.00 | 67.05 | 43.86 | `w5_lora_scierc_unconstrained_eval` |
| Qwen-2.5-7B | SciERC | Constrained | 0.00 | 0.00 | 0.00 | 1.18 | 67.05 | 43.77 | `w5_lora_scierc_constrained_eval` |
| Llama-3.1-8B | SciERC | Unconstrained | 0.00 | 0.00 | 1.11 | 0.00 | 67.76 | 45.45 | `w5_llama_lora_scierc_unconstrained_eval` |
| Llama-3.1-8B | SciERC | Constrained | 0.00 | 0.00 | 0.09 | 0.46 | 67.76 | 45.47 | `w5_llama_lora_scierc_constrained_eval` |
| Qwen-2.5-7B | DocRED | Unconstrained | — | — | — | — | — | — | `w5_qwen_docred_lora_unconstrained_eval` ⏳ RUNNING |
| Qwen-2.5-7B | DocRED | Constrained | — | — | — | — | — | — | `w5_qwen_docred_lora_constrained_eval` ⏳ PREPARING |
| Llama-3.1-8B | DocRED | Unconstrained | — | — | — | — | — | — | `w5_llama_docred_lora_unconstrained_eval` ⏳ RUNNING |
| Llama-3.1-8B | DocRED | Constrained | — | — | — | — | — | — | `w5_llama_docred_lora_constrained_eval` ⏳ PREPARING |

### Table 5 Deltas (Constrained − Unconstrained) — SciERC only (DocRED TBD)

| Model | Dataset | ΔDR (pp) | DR Red.% | ΔE-F1 (pp) | ΔR-F1 (pp) |
|-------|---------|----------|----------|------------|------------|
| Qwen-2.5-7B | SciERC | −1.95 | **100.0%** | 0.00 | −0.09 |
| Llama-3.1-8B | SciERC | −1.02 | **91.9%** | 0.00 | +0.02 |
| Qwen-2.5-7B | DocRED | — | — | — | — |
| Llama-3.1-8B | DocRED | — | — | — | — |

---

## Observation: CF% Trade-off

Constrained decoding eliminates ET/RV violations near-completely but introduces cross-field consistency (CF) violations:

| Setting | Avg CF% Unconstrained | Avg CF% Constrained |
|---------|----------------------|---------------------|
| Zero-shot SciERC | 0.28 | 8.23 |
| Zero-shot DocRED | 0.14 | 7.30 |
| Fine-tuned SciERC | 0.00 | 0.82 |

Fine-tuning substantially mitigates the CF trade-off (8.23% → 0.82% on SciERC).

---

## Evidence Strength Summary

**Cross-model consistency (strong):** Both Qwen-2.5-7B and Llama-3.1-8B show consistent DR reductions across all completed settings. Zero-shot DR reduction ranges from 44.7–99.4%; fine-tuned from 91.9–100%. The direction is unanimous — no model shows DR increase under constraints.

**Cross-dataset consistency (moderate):** SciERC shows stronger and more uniform DR reductions (93.9–99.4%) than DocRED (44.7–90.2%). The Qwen-DocRED zero-shot result at 44.7% DR reduction is the weakest cell in the matrix, likely due to DocRED's larger relation vocabulary creating more residual DR violations that pass vocabulary checks but still violate domain-range rules. This should be discussed as a limitation or explained via the schema complexity argument.

**F1 preservation (strong):** All completed ΔR-F1 values fall within ±0.5pp for zero-shot and ±0.1pp for fine-tuned. All ΔE-F1 values fall within ±1.22pp. The largest deviation is Qwen-DocRED ΔE-F1 = +1.22pp, which is slightly above the ±1pp threshold but in the *positive* direction (constraint improves entity extraction slightly). No statistically meaningful degradation in extraction quality from schema constraints.

**Fine-tuning amplifies composability:** Fine-tuned models start with much lower baseline DR (1–2% vs 13–26%), and constraints reduce it further to near-zero. The F1 impact shrinks to effectively zero. This supports the claim that schema constraints compose well with both zero-shot and fine-tuned settings.

**Open gaps:** 4 of 8 fine-tuned cells (all DocRED) are still running/preparing. These are needed to confirm the cross-dataset consistency claim for fine-tuned composability before May 19.
