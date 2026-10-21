# Scaling Analysis: Violation Rate Data

Data compiled from registry and report files. All violation rates in %.
- _u = Unconstrained, _c = + OntoCoDec (S1 constrained decoding)
- ET = Entity Type, RV = Relation Vocabulary, DR = Domain-Range, CF = Cross-Field

---

## Zero-Shot: DR Violation Rate Summary

| Model | Size | SciERC DR_u | SciERC DR_c | DocRED DR_u | DocRED DR_c |
|-------|------|-------------|-------------|-------------|-------------|
| Qwen-2.5-7B | 7B | 15.37 | 0.93 | 18.46 | 10.21 |
| Llama-3.1-8B | 8B | 13.34 | 0.08 | 26.07 | 2.55 |
| Mistral-7B | 7B | 56.94 | 13.40 | 57.42 | 33.20 |
| 70B | 70B | 6.50 | 0.00 | 15.00 | 0.00 |

**Notes:**
- Mistral constrained DR remains high due to SentencePiece BPE collision (excluded from figure)
- 70B values from registry (full 998 docs)
- 70B model: reports label as Qwen-2.5-70B; task spec notes actual model is Llama-3.1-70B-AWQ-INT4

---

## Zero-Shot: Full Violation Breakdown

### SciERC (551 test sentences)

| Model | Size | ET_u | RV_u | DR_u | CF_u | ET_c | RV_c | DR_c | CF_c |
|-------|------|------|------|------|------|------|------|------|------|
| Qwen-2.5-7B | 7B | 0.40 | 1.39 | 15.37 | 0.08 | 0.00 | 0.00 | 0.93 | 9.90 |
| Llama-3.1-8B | 8B | 0.00 | 0.55 | 13.34 | 0.47 | 0.00 | 0.00 | 0.08 | 6.56 |
| Mistral-7B | 7B | 1.50 | 0.00 | 56.94 | 56.87 | 0.00 | 0.00 | 13.40 | 1.27 |
| 70B | 70B | 0.00 | 0.60 | 6.50 | ~0.09 | 0.00 | 0.00 | 0.00 | ~3.66 |

### DocRED (998 test documents)

| Model | Size | ET_u | RV_u | DR_u | CF_u | ET_c | RV_c | DR_c | CF_c |
|-------|------|------|------|------|------|------|------|------|------|
| Qwen-2.5-7B | 7B | 2.48 | 29.66 | 18.46 | 0.10 | 0.00 | 0.03 | 10.21 | 2.57 |
| Llama-3.1-8B | 8B | 0.13 | 16.03 | 26.07 | 0.17 | 0.00 | 0.00 | 2.55 | 12.02 |
| Mistral-7B | 7B | 7.58 | 42.35 | 57.42 | 24.78 | 0.00 | 0.00 | 33.20 | 0.19 |
| 70B | 70B | 0.00 | 7.80 | 15.00 | ~0.07 | 0.00 | 0.00 | 0.00 | 7.01 |

---

## LoRA (Fine-Tuned): DR Violation Rate Summary

| Model | Size | SciERC DR_u | SciERC DR_c | DocRED DR_u | DocRED DR_c |
|-------|------|-------------|-------------|-------------|-------------|
| Qwen-2.5-7B | 7B | 1.95 | 0.00 | 0.76 | 0.01 |
| Llama-3.1-8B | 8B | 1.11 | 0.09 | 0.49 | 0.20 |

### LoRA Full Violation Breakdown

#### SciERC

| Model | ET_u | RV_u | DR_u | CF_u | ET_c | RV_c | DR_c | CF_c |
|-------|------|------|------|------|------|------|------|------|
| Qwen-2.5-7B | 0.00 | 0.00 | 1.95 | 0.00 | 0.00 | 0.00 | 0.00 | 1.18 |
| Llama-3.1-8B | 0.00 | 0.00 | 1.11 | 0.00 | 0.00 | 0.00 | 0.09 | 0.46 |

#### DocRED

| Model | ET_u | RV_u | DR_u | CF_u | ET_c | RV_c | DR_c | CF_c |
|-------|------|------|------|------|------|------|------|------|
| Qwen-2.5-7B | 0.00 | 0.27 | 0.76 | 0.12 | 0.00 | 0.00 | 0.01 | 0.41 |
| Llama-3.1-8B | 0.00 | 0.15 | 0.49 | -- | 0.00 | 0.00 | 0.20 | 0.26 |

---

## DR Relative Reduction (%)

### Zero-Shot

| Model | SciERC | DocRED |
|-------|--------|--------|
| Qwen-2.5-7B | -93.9% | -44.7% |
| Llama-3.1-8B | -99.4% | -90.2% |
| 70B | -100% | -100% |

### LoRA

| Model | SciERC | DocRED |
|-------|--------|--------|
| Qwen-2.5-7B | -100% | -98.7% |
| Llama-3.1-8B | -91.9% | -59.2% |

---

## Data Sources

- ZS 7B/8B: `table2_main_results.md`, `paper_results_tables.md`
- ZS 70B: `p3_error_analysis.md`, `d065_tcr_full_results.md`
- LoRA: `table2_main_results.md`, `table3_composability.md`
- CF estimates for 70B computed from entity counts in `p3_error_analysis.md`
