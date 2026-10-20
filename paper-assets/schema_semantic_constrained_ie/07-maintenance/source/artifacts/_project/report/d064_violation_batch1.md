# d064 Violation & F1 Evaluation — Batch 1 (beam-4)

**Date**: 2026-05-19  
**Dataset**: DocRED 998-doc dev set  
**Eval script**: `scripts/eval_d064.py`

## Main Results

| Model | Decoding | Mode | ET% | RV% | DR% | CF% | E-F1 | R-F1 | PF% |
|-------|----------|------|-----|-----|-----|-----|------|------|-----|
| Qwen  | beam-4   | unc  | 0.00 | 0.14 | 0.54 | 0.04 | 83.73 | 44.40 | 3.5 |
| Qwen  | beam-4   | con  | 0.00 | 0.00 | 0.00 | 0.01 | 84.00 | 44.46 | 2.9 |
| Llama | beam-4   | unc  | 0.00 | 0.04 | 0.10 | 0.06 | 85.16 | 47.17 | 1.4 |
| Llama | beam-4   | con  | 0.00 | 0.00 | 0.00 | 0.00 | 85.23 | 47.17 | 1.3 |

**PF% = Parse Failure rate**

## Key Observations

1. **Constraint decoding eliminates violations**: Both models go to 0.00% on RV/DR (Qwen CF has residual 0.01%, likely from entity-level inconsistency across relations in a single doc). Llama constrained achieves perfect 0.00% across all four violation types.

2. **F1 preserved or slightly improved under constraints**:
   - Qwen: E-F1 83.73→84.00 (+0.27), R-F1 44.40→44.46 (+0.06)
   - Llama: E-F1 85.16→85.23 (+0.07), R-F1 47.17→47.17 (unchanged)
   - No degradation — constraints act as a free violation eliminator.

3. **Llama outperforms Qwen on this dataset**: +1.2 E-F1, +2.7 R-F1 in both modes. Lower parse failure rate too (1.3-1.4% vs 2.9-3.5%).

4. **Unconstrained violations already very low for LoRA-finetuned models**: ET=0.00% for both (LoRA learns correct entity types). RV/DR residuals are small but nonzero — constrained decoding provides the final cleanup.

## Detailed Per-File Stats

### Qwen beam-4 unconstrained (westd-21461)
- File: `d064_qwen_docred_beam4_unconstrained.jsonl`
- Samples: 998, Parse Fail: 35 (3.5%)
- Entities pred: 18858, Relations pred: 13591
- ET=0, RV=19, DR=73, CF=7
- E: P=85.24 R=82.27 F1=83.73
- R: P=42.31 R=46.70 F1=44.40

### Qwen beam-4 constrained (westd-21461)
- File: `d064_qwen_docred_beam4_constrained.jsonl`
- Samples: 998, Parse Fail: 29 (2.9%)
- Entities pred: 19002, Relations pred: 13458
- ET=0, RV=0, DR=0, CF=2
- E: P=85.20 R=82.84 F1=84.00
- R: P=42.47 R=46.65 F1=44.46

### Llama beam-4 unconstrained (westd-16980)
- File: `d064_llama_docred_beam4_unconstrained_16980.jsonl`
- Samples: 998, Parse Fail: 14 (1.4%)
- Entities pred: 19393, Relations pred: 13700
- ET=0, RV=6, DR=14, CF=12
- E: P=85.51 R=84.82 F1=85.16
- R: P=44.72 R=49.90 F1=47.17

### Llama beam-4 constrained (westd-16980)
- File: `d064_llama_docred_beam4_constrained_16980.jsonl`
- Samples: 998, Parse Fail: 13 (1.3%)
- Entities pred: 19416, Relations pred: 13712
- ET=0, RV=0, DR=0, CF=0
- E: P=85.52 R=84.94 F1=85.23
- R: P=44.66 R=49.98 F1=47.17

## Qwen Greedy Baseline Status

**Not found.** Searched both servers:
- westd-21461: no `*qwen*docred*greedy*` files
- westd-16980: only `outputs/qwen_docred_greedy_matched50.jsonl` (50-doc subset, not 998-doc)

Qwen LoRA DocRED 998-doc greedy inference has not been run yet.

## Additional Files Available (not yet evaluated)

On westd-16980:
- `d064_llama_docred_greedy_unconstrained_w5.jsonl` (9.4MB, Llama greedy unc)
- `d064_llama_docred_greedy_constrained_w5.jsonl` (7.7MB, Llama greedy con)

On westd-21461:
- `d064_llama_docred_greedy_unconstrained.jsonl` (9.3MB)
- `d064_llama_docred_greedy_constrained.jsonl` (9.3MB)
- `d064_llama_docred_beam4_unconstrained.jsonl` (8.1MB, partial? different from 16980 version)
