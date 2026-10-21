# DocRED Unified Evaluation — eval_d064.py

**Date**: 2026-05-20
**Script**: `scripts/eval_d064.py` (PF-as-FN, DocRED ontology hardcoded)
**Fix applied**: `r.get("tail","")` for 1 malformed relation in w5_qwen_unc

## 1. w5 Files (Table 2 FT DocRED source — outputs/ directory, 998 docs each)

| File | Model | Mode | E-F1 | R-F1 | ET% | RV% | DR% | CF% | PF% |
|------|-------|------|------|------|-----|-----|-----|-----|-----|
| w5_qwen_docred_lora_unconstrained_eval | Qwen | unc | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.09 | 7.11 |
| w5_qwen_docred_lora_constrained_eval | Qwen | con | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.27 | 8.52 |
| w5_llama_docred_lora_unconstrained_eval | Llama | unc | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | 0.08 | 2.30 |
| w5_llama_docred_lora_constrained_eval | Llama | con | 83.94 | 43.78 | 0.00 | 0.00 | 0.21 | 0.21 | 2.51 |
| w5_qwen_docred_lora_constrained_eval_cf_corrected | Qwen | con+cfcorr | 81.41 | 40.56 | 0.00 | 0.00 | 0.44 | 0.02 | 8.52 |
| w5_llama_docred_lora_constrained_eval_cf_corrected | Llama | con+cfcorr | 83.89 | 43.78 | 0.00 | 0.00 | 0.50 | 0.01 | 2.51 |

## 2. d065 Files (re-run with max_tokens=4096, improved text normalization)

| File | Model | Mode | E-F1 | R-F1 | ET% | RV% | DR% | CF% | PF% |
|------|-------|------|------|------|-----|-----|-----|-----|-----|
| d065_llama_docred_greedy_unc_4096 | Llama | unc | 84.77 | 44.55 | 0.00 | 0.15 | 0.49 | 0.08 | 2.30 |
| d065_llama_docred_greedy_con_4096 | Llama | con | 84.71 | 44.70 | 0.00 | 0.00 | 0.00 | 0.26 | 2.61 |
| d065_qwen_docred_greedy_con_4096 | Qwen | con | 80.75 | 43.56 | 0.00 | 0.00 | 0.00 | 0.12 | 7.11 |

Note: d065 Qwen con only has 197/998 docs (incomplete). No d065 Qwen unc file exists.

## 3. Other DocRED files (beam / 70B / 200-doc subset)

| File | Model | Mode | Docs | E-F1 | R-F1 | ET% | RV% | DR% | CF% | PF% |
|------|-------|------|------|------|------|-----|-----|-----|-----|-----|
| d064_llama_docred_beam4_unconstrained | Llama | beam4 unc | 998 | 85.16 | 47.17 | 0.00 | 0.04 | 0.10 | 0.06 | 1.40 |
| d064_llama_docred_beam4_constrained | Llama | beam4 con | 998 | 85.23 | 47.17 | 0.00 | 0.00 | 0.00 | 0.00 | 1.30 |
| 70b_docred_unconstrained | 70B | unc | 998 | 68.96 | 13.01 | 0.02 | 8.03 | 14.98 | 0.07 | 0.00 |
| 70b_docred_constrained | 70B | con | 998 | 68.96 | 13.05 | 0.00 | 0.00 | 0.00 | 5.15 | 0.10 |
| qwen_docred_200_greedy_unc | Qwen | greedy unc | 200 | 81.34 | 44.56 | 0.00 | 0.24 | 0.20 | 0.03 | 6.50 |
| qwen_docred_200_greedy_s1 | Qwen | greedy con | 200 | 80.54 | 43.64 | 0.00 | 0.00 | 0.00 | 0.12 | 7.50 |
| qwen_docred_200_beam2_unc | Qwen | beam2 unc | 200 | 84.25 | 47.39 | 0.00 | 0.11 | 0.43 | 0.00 | 1.50 |
| qwen_docred_200_beam2_con | Qwen | beam2 con | 186 | 84.15 | 46.90 | 0.00 | 0.00 | 0.00 | 0.09 | 1.08 |

## 4. Comparison: eval_d064.py (new) vs Table 2 (current paper)

| Model | Mode | Metric | eval_d064 | Table 2 | Delta | Issue |
|-------|------|--------|-----------|---------|-------|-------|
| Qwen | unc | E-F1 | 82.15 | 82.15 | 0.00 | OK |
| Qwen | unc | R-F1 | 40.86 | 40.86 | 0.00 | OK |
| Qwen | unc | CF% | 0.09 | 0.12 | +0.03 | **Table 2 wrong** |
| Qwen | con | E-F1 | 81.43 | 81.43 | 0.00 | OK |
| Qwen | con | R-F1 | 40.56 | 40.56 | 0.00 | OK |
| Qwen | con | CF% | 0.27 | 0.41 | +0.14 | **Table 2 wrong** |
| Llama | unc | E-F1 | 83.93 | 83.93 | 0.00 | OK |
| Llama | unc | R-F1 | 43.72 | 43.72 | 0.00 | OK |
| Llama | unc | CF% | 0.08 | — | — | Table 2 omitted |
| Llama | con | E-F1 | 83.94 | **85.23** | **+1.29** | **CRITICAL: Table 2 used beam4 E-F1** |
| Llama | con | R-F1 | 43.78 | **44.23** | **+0.45** | **Table 2 wrong** |
| Llama | con | DR% | 0.21 | 0.20 | -0.01 | Minor |
| Llama | con | CF% | 0.21 | 0.26 | +0.05 | Table 2 wrong |

### Root cause of Llama Con mismatch
Table 2's E-F1=85.23 matches `d064_llama_docred_beam4_constrained` exactly. The greedy (w5) result is 83.94. Someone likely copied the beam4 number into the greedy row.

## 5. eval_d064.py vs d066 eval JSON (old script) comparison

The d066 eval JSONs in `outputs/d066_*_docred_*.json` produce **identical** results to eval_d064.py on the same w5 files. The 0.84pp E-F1 discrepancy reported by the reviewer is NOT from script differences — it's from Table 2 mixing beam4 and greedy results for Llama Con.

## 6. w5 vs d065 file differences

Despite having identical `raw_output` (greedy decoding is deterministic), w5 and d065 files have different `parsed_output` due to text normalization:
- w5: `"November 15 , 1915"` (spaces around punctuation from tokenizer)
- d065: `"November 15, 1915"` (cleaned up)

This leads to higher entity matching in d065 (+0.84 E-F1 for Llama unc). d065 uses improved parsing but Qwen runs are incomplete.

## 7. Corrected Table 2 FT DocRED (using w5 files, eval_d064.py)

| Model | Method | E-F1 | R-F1 | ET% | RV% | DR% | CF% | PF% |
|-------|--------|------|------|-----|-----|-----|-----|-----|
| Qwen3-8B | Unconstrained | 82.15 | 40.86 | 0.00 | 0.27 | 0.76 | 0.09 | 7.11 |
| Qwen3-8B | OntoCoDec | 81.43 | 40.56 | 0.00 | 0.00 | 0.01 | 0.27 | 8.52 |
| Llama3.1-8B | Unconstrained | 83.93 | 43.72 | 0.00 | 0.15 | 0.49 | 0.08 | 2.30 |
| Llama3.1-8B | OntoCoDec | 83.94 | 43.78 | 0.00 | 0.00 | 0.21 | 0.21 | 2.51 |
