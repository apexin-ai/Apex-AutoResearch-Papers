# Paper Number Pre-Audit: SciERC Composability

**Date**: 2026-05-16
**Scope**: `section5_composability.tex` (Table 5 + body text) + `main.tex` Limitations section
**Registry source**: schema_semantic_constrained_ie project registry

---

## Registry Experiment Name Mapping

| User-specified ID | Actual registry ID |
|---|---|
| `phase1_scierc` | `phase2_scierc_unconstrained` |
| `w5_llama_scierc_zs_unconstrained` | `llama_scierc_unconstrained` |
| `w5_llama_scierc_zs_constrained` | `llama_scierc_full_s1` |
| (other 5 IDs) | exact match |

---

## Table 5 (tab:composability)

### Qwen3-8B

| Row | Metric | Paper | Registry | Status |
|-----|--------|-------|----------|--------|
| ZS U | DR | 15.37 | 0.1537 → 15.37% | ✅ |
| ZS U | CF | 0.08 | 0.0008 → 0.08% | ✅ |
| ZS U | R-F1 | 8.23 | 0.0823 → 8.23 | ✅ |
| ZS U | E-F1 | 31.01 | 0.3101 → 31.01 | ✅ |
| ZS S1 | DR | 0.93 | 0.0093 → 0.93% | ✅ |
| ZS S1 | CF | 9.90 | 0.099 → 9.90% | ✅ |
| ZS S1 | R-F1 | 8.36 | 0.0836 → 8.36 | ✅ |
| ZS S1 | E-F1 | 30.98 | 0.3098 → 30.98 | ✅ |
| LoRA U | DR | 1.95 | 0.0195 → 1.95% | ✅ |
| LoRA U | CF | 0 | 0 | ✅ |
| LoRA U | R-F1 | 43.86 | 0.4386 → 43.86 | ✅ |
| LoRA U | E-F1 | 67.05 | 0.6705 → 67.05 | ✅ |
| LoRA S1 | DR | 0.00 | 0 → 0.00% | ✅ |
| LoRA S1 | CF | 1.18 | 0.0118 → 1.18% | ✅ |
| LoRA S1 | R-F1 | 43.77 | 0.4377 → 43.77 | ✅ |
| LoRA S1 | E-F1 | 67.05 | 0.6705 → 67.05 | ✅ |

### Llama-3.1-8B

| Row | Metric | Paper | Registry | Status |
|-----|--------|-------|----------|--------|
| ZS U | DR | 13.34 | 0.1334 → 13.34% | ✅ |
| ZS U | CF | 0.24 | 6/2451 ≈ 0.24% (raw count only) | ✅ |
| ZS U | R-F1 | 2.68 | 0.0268 → 2.68 | ✅ |
| ZS U | E-F1 | 23.56 | 0.2356 → 23.56 | ✅ |
| ZS S1 | DR | 0.08 | 0.0008 → 0.08% | ✅ |
| ZS S1 | CF | 6.56 | 0.0656 → 6.56% | ✅ |
| ZS S1 | R-F1 | 2.54 | 0.0254 → 2.54 | ✅ |
| ZS S1 | E-F1 | 23.49 | 0.2349 → 23.49 | ✅ |
| LoRA U | DR | 1.11 | 0.0111 → 1.11% | ✅ |
| LoRA U | CF | 0 | 0 | ✅ |
| LoRA U | R-F1 | 45.45 | 0.4545 → 45.45 | ✅ |
| LoRA U | E-F1 | 67.76 | 0.6776 → 67.76 | ✅ |
| LoRA S1 | DR | 0.09 | 0.0009 → 0.09% | ✅ |
| LoRA S1 | CF | 0.46 | 0.0046 → 0.46% | ✅ |
| LoRA S1 | R-F1 | 45.47 | 0.4547 → 45.47 | ✅ |
| LoRA S1 | E-F1 | 67.76 | 0.6776 → 67.76 | ✅ |

**Table 5: 32/32 cells match. Zero discrepancies.**

---

## Body Text (section5_composability.tex)

| Claim | Paper value | Registry derivation | Status |
|-------|-------------|---------------------|--------|
| R-F1 lift Qwen | 8.23 → 43.86 | phase2_scierc_unconstrained → w5_lora_scierc_unconstrained_eval | ✅ |
| R-F1 lift Llama | 2.68 → 45.45 | llama_scierc_unconstrained → w5_llama_lora_scierc_unconstrained_eval | ✅ |
| "35–43pp gain" | 35.63pp, 42.77pp | matches range | ✅ |
| Residual DR Qwen | 1.95% | w5_lora_scierc_unconstrained_eval DR=0.0195 | ✅ |
| Residual DR Llama | 1.11% | w5_llama_lora_scierc_unconstrained_eval DR=0.0111 | ✅ |
| Evaluate-for DR (Qwen FT) | 13.1% | comment: 13.13%, rounded | ✅ |
| S1 DR reduction Qwen | 1.95% → 0.00% | constrained DR=0 | ✅ |
| S1 DR reduction Llama | 1.11% → 0.09% | constrained DR=0.0009 | ✅ |
| R-F1 delta Qwen | −0.09pp | 43.77−43.86 = −0.09 | ✅ |
| R-F1 delta Llama | +0.02pp | 45.47−45.45 = +0.02 | ✅ |
| E-F1 identical | Qwen 67.05=67.05, Llama 67.76=67.76 | ✅ | ✅ |
| FT CF rates | 1.18% Qwen, 0.46% Llama | registry match | ✅ |
| ZS CF rates | 9.90%, 6.56% | registry match | ✅ |

**Body text: 13/13 claims match.**

---

## Limitations Section (main.tex)

| Claim | Paper value | Registry derivation | Status |
|-------|-------------|---------------------|--------|
| Max ZS CF | 12.02% | llama_docred_full_s1 CF=12.02 | ✅ |
| FT CF ceiling | ≤1.18% | max(1.18%, 0.46%) = 1.18% | ✅ |
| CF fallback → CF | 0.04% | w1_cf_fallback_scierc_pilot CF=0.0004 | ✅ |
| CF fallback → DR increase | 13.85pp | pilot DR 14.78% − baseline 0.93% = 13.85pp | ✅ |
| E-F1 delta Qwen DocRED | +1.22pp | 59.37−58.15 = +1.22 | ✅ |
| E-F1 delta Llama DocRED | −0.64pp | 55.01−55.65 = −0.64 | ✅ |
| Llama parse fail constrained | 9.1% | 91/998 = 9.12% | ✅ |
| Llama parse fail unconstrained | 6.8% | 68/998 = 6.81% | ✅ |

**Limitations: 8/8 claims match.**

---

## Summary

| Section | Checked | Match | Mismatch |
|---------|---------|-------|----------|
| Table 5 | 32 | 32 | 0 |
| Body text | 13 | 13 | 0 |
| Limitations | 8 | 8 | 0 |
| **Total** | **53** | **53** | **0** |

### Verdict

**All 53 numbers are consistent with registry.** Safe to add DocRED FT composability data on this foundation.

### Minor Notes
- `llama_scierc_unconstrained` stores CF as raw count (6) not rate; computed rate 6/2451=0.245% rounds to paper's 0.24%. Consider storing the rate for consistency.
- Three experiment IDs referenced in task spec differ from actual registry names (see mapping table above).
