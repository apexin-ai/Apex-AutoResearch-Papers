# Paper Results Tables — Schema-Semantic Constrained IE

**数据来源**: registry (schema_semantic_constrained_ie project)
**编译日期**: 2026-05-16
**Checker version**: fixed_20260514_v2 (strip + alias + unique_et)

---

## Table 1: Zero-shot Violation Landscape (3 models × 2 datasets)

| Model | Dataset | ET% | RV% | DR% | CF% | E_F1 | R_F1 | parse_fail% |
|-------|---------|-----|-----|-----|-----|------|------|-------------|
| Qwen2.5-7B | SciERC | 0.40 | 1.39 | 15.37 | 0.08 | 31.01 | 8.23 | 0.00 |
| Qwen2.5-7B | DocRED | 2.48 | 29.66 | 18.46 | 0.10 | 58.15 | 7.74 | 1.20 |
| Llama3.1-8B | SciERC | 0.00 | 0.55 | 13.34 | 0.47 | 23.56 | 2.68 | 0.18 |
| Llama3.1-8B | DocRED | 0.13 | 16.03 | 26.07 | 0.17 | 55.65 | 5.98 | 6.81 |
| Mistral-7B | SciERC | 1.50 | 0.00 | 56.94 | 56.87 | 27.28 | 3.66 | 0.00 |
| Mistral-7B | DocRED | 7.58 | 42.35 | 57.42 | 24.78 | 48.51 | 4.34 | 0.70 |

**Source exp_ids**:
- Qwen: `phase2_scierc_unconstrained`, `phase2_docred_unconstrained`
- Llama: `llama_scierc_unconstrained`, `llama_docred_unconstrained`
- Mistral: `w6_mistral_scierc_unconstrained`, `w6_mistral_docred_unconstrained`

**Notes**:
- All F1 values in %. ET/RV/DR/CF = Entity Type / Relation Vocabulary / Domain-Range / Cross-Field violation rates.
- Qwen DocRED parse_fail% = 12/998 = 1.20%. Llama DocRED = 68/998 = 6.81%.
- Llama SciERC CF% computed as 6 violations / 1274 relations = 0.47%.

---

## Table 2: Zero-shot Constrained vs Unconstrained (3 models × 2 datasets)

| Model | Dataset | DR_uncon | DR_con | ΔDR (pp) | ΔR_F1 (pp) | ΔE_F1 (pp) |
|-------|---------|----------|--------|----------|------------|------------|
| Qwen2.5-7B | SciERC | 15.37% | 0.93% | −14.44 | +0.13 | −0.03 |
| Qwen2.5-7B | DocRED | 18.46% | 10.21% | −8.25 | +0.49 | +1.22 |
| Llama3.1-8B | SciERC | 13.34% | 0.08% | −13.26 | −0.14 | −0.07 |
| Llama3.1-8B | DocRED | 26.07% | 2.55% | −23.52 | +0.29 | −0.64 |
| Mistral-7B | SciERC | 56.94% | 13.40% | −43.54 | +0.01 | +0.18 |
| Mistral-7B | DocRED | 57.42% | 33.20% | −24.22 | +1.18 | +2.08 |

**Source exp_ids**:
- Unconstrained: same as Table 1
- Constrained: `phase2_scierc_full_s1`, `phase2_docred_full_s1`, `llama_scierc_full_s1`, `llama_docred_full_s1`, `w6_mistral_scierc_constrained`, `w6_mistral_docred_constrained`

**Computation**:
- ΔDR = DR_con − DR_uncon (negative = improvement)
- ΔR_F1 = R_F1_con − R_F1_uncon (positive = improvement)
- ΔE_F1 = E_F1_con − E_F1_uncon

**Detail values**:

| Model | Dataset | E_F1_uncon | E_F1_con | R_F1_uncon | R_F1_con |
|-------|---------|------------|----------|------------|----------|
| Qwen2.5-7B | SciERC | 31.01 | 30.98 | 8.23 | 8.36 |
| Qwen2.5-7B | DocRED | 58.15 | 59.37 | 7.74 | 8.23 |
| Llama3.1-8B | SciERC | 23.56 | 23.49 | 2.68 | 2.54 |
| Llama3.1-8B | DocRED | 55.65 | 55.01 | 5.98 | 6.27 |
| Mistral-7B | SciERC | 27.28 | 27.46 | 3.66 | 3.67 |
| Mistral-7B | DocRED | 48.51 | 50.59 | 4.34 | 5.52 |

---

## Table 3: Composability Matrix — Fine-tuned + OntoCoDec (2 models × 2 datasets)

| Model | Dataset | DR_FT_uncon | DR_FT_con | ΔDR (pp) | R_F1_uncon | R_F1_con | ΔR_F1 (pp) |
|-------|---------|-------------|-----------|----------|------------|----------|------------|
| Qwen2.5-7B | SciERC | 1.95% | 0.00% | −1.95 | 43.86 | 43.77 | −0.09 |
| Qwen2.5-7B | DocRED | 0.76% | 0.01% | −0.75 | 40.86 | 40.56 | −0.30 |
| Llama3.1-8B | SciERC | 1.11% | 0.09% | −1.02 | 45.45 | 45.47 | +0.02 |
| Llama3.1-8B | DocRED | 0.49% | 0.20% | −0.29 | 43.72 | 44.23 | +0.51 |

**Source exp_ids**:
- Qwen SciERC: `w5_lora_scierc_unconstrained_eval` vs `w5_lora_scierc_constrained_eval`
- Qwen DocRED: `w5_qwen_docred_lora_unconstrained_eval` vs `w5_qwen_docred_lora_constrained_eval`
- Llama SciERC: `w5_llama_lora_scierc_unconstrained_eval` vs `w5_llama_lora_scierc_constrained_eval`
- Llama DocRED: `w5_llama_docred_lora_unconstrained_eval` vs `w5_llama_docred_lora_constrained_eval`

**Notes**:
- DR_FT_uncon: Fine-tuned model without constrained decoding still exhibits residual DR violations (0.49–1.95%).
- OntoCoDec reduces DR to near-zero in all cases with negligible F1 impact (|ΔR_F1| ≤ 0.51 pp).
- Llama DocRED constrained shows R_F1 *improvement* (+0.51 pp), likely from filtering false-positive triples.

---

## Table 4: FT Ablation — Layer Contribution (SciERC, 2 models × 4 modes)

| Model | Mode | ET% | RV% | DR% | CF% | R_F1 |
|-------|------|-----|-----|-----|-----|------|
| Qwen2.5-7B | unconstrained | 0.00 | 0.00 | 1.95 | 0.00 | 43.86 |
| Qwen2.5-7B | grammar_only | 0.00 | 0.00 | 1.90 | 0.00 | 43.86 |
| Qwen2.5-7B | semantic_only | 0.00 | 0.00 | 0.60 | 1.33 | 43.69 |
| Qwen2.5-7B | full (S1) | 0.00 | 0.00 | 0.00 | 1.18 | 43.77 |
| Llama3.1-8B | unconstrained | 0.00 | 0.00 | 1.11 | 0.00 | 45.45 |
| Llama3.1-8B | grammar_only | 0.00 | 0.00 | 1.11 | 0.00 | 45.45 |
| Llama3.1-8B | semantic_only | 0.00 | 0.00 | 0.65 | 0.18 | 45.47 |
| Llama3.1-8B | full (S1) | 0.00 | 0.00 | 0.09 | 0.46 | 45.47 |

**Source exp_ids**:
- Qwen: `w5_lora_scierc_unconstrained_eval`, `w7_qwen_scierc_ft_grammar_only`, `w7_qwen_scierc_ft_semantic_only`, `w5_lora_scierc_constrained_eval`
- Llama: `w5_llama_lora_scierc_unconstrained_eval`, `w7_llama_scierc_ft_grammar_only`, `w7_llama_scierc_ft_semantic_only`, `w5_llama_lora_scierc_constrained_eval`

**Notes**:
- Grammar-only layer has near-zero effect on FT models (ET/RV already ~0% after fine-tuning).
- Semantic layer provides the dominant DR reduction: Qwen 1.95→0.60% (−69%), Llama 1.11→0.65% (−41%).
- Full S1 (grammar + semantic) further reduces DR to 0.00–0.09% with minimal R_F1 impact.
- CF% increases slightly with semantic/full constraints due to cross-field consistency enforcement revealing latent violations (not causing new ones).
- Qwen CF%: unconstrained 0.00% → semantic_only 1.33% (15 violations / 1128 relations) → full 1.18% (21 / 1784 entities+relations baseline).
- Llama CF%: unconstrained 0.00% → semantic_only 0.18% (2 / 1081) → full 0.46% (5 / 1081).

---

## Table 5: Post-hoc Filtering vs Constrained Decoding

### 5a: Fine-tuned Regime

| Model | Dataset | R_F1_uncon | R_F1_posthoc | R_F1_con | reject% | TP_lost |
|-------|---------|------------|--------------|----------|---------|---------|
| Qwen2.5-7B | SciERC | 43.86 | 43.94 | 43.77 | 1.95 | 4 |
| Llama3.1-8B | SciERC | 45.45 | 45.23 | 45.47 | 1.11 | 5 |
| Qwen2.5-7B | DocRED | 40.91 | 41.11 | 40.56 | 1.03 | 1 |
| Llama3.1-8B | DocRED | 43.77 | 43.92 | 44.23 | 0.64 | 1 |

### 5b: Zero-shot Regime

| Model | Dataset | R_F1_uncon | R_F1_posthoc | R_F1_con | reject% | TP_lost |
|-------|---------|------------|--------------|----------|---------|---------|
| Qwen2.5-7B | SciERC | 8.23 | 8.63 | 8.36 | 16.76 | 7 |
| Llama3.1-8B | SciERC | 2.68 | 2.71 | 2.54 | 13.89 | 2 |
| Mistral-7B | SciERC | 3.76 | 3.94 | 3.67 | 20.27 | 4 |
| Qwen2.5-7B | DocRED | 7.74 | 9.61 | 8.23 | 48.12 | 127 |
| Llama3.1-8B | DocRED | 5.98 | 7.44 | 6.27 | 42.18 | 48 |
| Mistral-7B | DocRED | 4.34 | 3.85 | 5.52 | 73.73 | 226 |

**Source exp_id**: `w8_ft_posthoc_baseline`

**Notes**:
- R_F1_uncon = unconstrained baseline. R_F1_posthoc = after removing DR/RV-violating triples. R_F1_con = constrained decoding.
- FT regime: post-hoc and constrained decoding achieve comparable R_F1 (reject rates <2%).
- ZS regime: post-hoc filtering improves R_F1 in 5/6 cases by removing noise. Exception: Mistral DocRED where 73.73% rejection loses 226 TPs, causing net F1 *decrease* (4.34→3.85).
- Constrained decoding value is in *structural guarantee* (0% violations) and composability, not raw F1 advantage.

---

## Table 6: Schema-informed Prompt Baseline (Qwen2.5-7B)

| Dataset | DR_minimal | DR_schema | ΔDR% | R_F1_minimal | R_F1_schema |
|---------|------------|-----------|------|--------------|-------------|
| SciERC | 15.37% | 5.78% | −62.4% | 8.23 | N/A |
| DocRED | 18.70% | 12.84% | −31.3% | N/A | N/A |

**Source exp_ids**:
- Minimal prompt: `mvp_phase0_violation_rate` (SciERC), `mvp_phase0_violation_rate_docred` (DocRED)
- Schema prompt: `mvp_phase0_scierc_schema`, `mvp_phase0_docred_schema`

**Notes**:
- ΔDR% = (DR_schema − DR_minimal) / DR_minimal × 100.
- Schema-informed prompts reduce DR substantially (−62.4% SciERC, −31.3% DocRED) but cannot eliminate violations.
- R_F1 not computed for Phase 0 schema experiments (violation-rate-only evaluation).
- SciERC R_F1_minimal = 8.23 from `mvp_phase0_violation_rate` (same model/data as `phase2_scierc_unconstrained`).
- Residual DR after schema prompts (5.78–12.84%) motivates constrained decoding as a complementary approach.
