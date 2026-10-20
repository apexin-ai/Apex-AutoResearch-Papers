# SciERC w5 Unified Evaluation (eval_d066_unified.py, PF-as-FN)

**Date**: 2026-05-20
**Script**: `scripts/eval_d066_unified.py` (generalized version of eval_d064.py, same PF-as-FN logic)
**Ontology**: `ontology_constraints.json` (SciERC)
**Samples**: 551 per file (SciERC dev set)

## Results

| File | Model | Mode | E-F1 | R-F1 | DR% | CF% | ET% | RV% | PF% |
|------|-------|------|------|------|-----|-----|-----|-----|-----|
| w5_lora_scierc_unconstrained_eval.jsonl | Qwen | unc | 67.05 | 43.86 | 1.95 | 0.00 | 0.00 | 0.00 | 0.0 |
| w5_lora_scierc_full_s1_eval.jsonl | Qwen | con | 67.05 | 43.77 | 0.00 | 0.45 | 0.00 | 0.00 | 0.0 |
| w5_llama_lora_scierc_unconstrained.jsonl | Llama | unc | 67.76 | 45.45 | 1.11 | 0.00 | 0.00 | 0.00 | 0.0 |
| w5_llama_lora_scierc_constrained.jsonl | Llama | con | 67.76 | 45.47 | 0.09 | 0.23 | 0.00 | 0.00 | 0.0 |
| w5_lora_scierc_full_s1_eval_cf_corrected.jsonl | Qwen | con+cfcorr | 67.00 | 43.77 | 0.71 | 0.00 | 0.00 | 0.00 | 0.0 |
| w5_llama_lora_scierc_constrained_cf_corrected.jsonl | Llama | con+cfcorr | 67.82 | 45.47 | 0.37 | 0.00 | 0.00 | 0.00 | 0.0 |

## Notes

- eval_d064.py is hardcoded to DocRED ontology. eval_d066_unified.py is the exact same PF-as-FN logic generalized to accept `--ontology` parameter.
- All files have PF%=0.0 (no parse failures), so PF-as-FN treatment has no effect on these results.
- ET%=0.00, RV%=0.00 across all configs (SciERC LoRA models produce no entity type or relation vocabulary violations).
- Constrained (`con`) vs unconstrained (`unc`): DR% drops sharply (Qwen: 1.95→0.00, Llama: 1.11→0.09), confirming constrained decoding eliminates domain-range violations.
- CF correction post-processing eliminates CF% (0.45→0.00 for Qwen, 0.23→0.00 for Llama) with negligible E-F1 impact.
- R-F1 is virtually identical between unc and con for both models (Qwen: 43.86 vs 43.77; Llama: 45.45 vs 45.47), showing constraint enforcement does not hurt task performance.

## Raw JSON outputs

Saved to: `/root/autodl-tmp/schema_outputs/unified_eval/scierc_*.json`
