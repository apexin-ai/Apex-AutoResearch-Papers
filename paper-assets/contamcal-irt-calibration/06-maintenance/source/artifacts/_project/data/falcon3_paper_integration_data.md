# Falcon3-7B-Base: Paper Integration Data

**Date**: 2026-05-22
**Source**: Falcon3 eval results (s42, evaluate.py v3, 5-shot MMLU / 25-shot ARC)

---

## 1. Table 1 (tab:taxonomy) Update — Dose-Response Row

### MMLU 5-shot (seed=42)

| Dosage | Accuracy | Δ from d000 |
|--------|----------|-------------|
| d000 | 58.77% | — |
| d005 | 59.02% | +0.25pp |
| d025 | 61.23% | +2.46pp |
| d050 | 62.09% | +3.32pp |
| d100 | 62.96% | +4.19pp |

Shape: **Monotonic increase**, largest jump d005→d025 (+2.21pp), then decelerating.

### ARC 25-shot (seed=42)

| Dosage | Accuracy | Δ from d000 |
|--------|----------|-------------|
| d000 | 81.57% | — |
| d005 | 83.11% | +1.54pp |
| d025 | 84.81% | +3.24pp |
| d050 | 83.28% | +1.71pp |
| d100 | 85.58% | +4.01pp |

Shape: **General rise with d050 dip** (−1.53pp below d025, recovers at d100).

### Paper Table Row

| Model | Pre-train MMLU | d000 | d005 | d025 | d050 | d100 | Δ(d100−d000) | Peak | Pattern |
|-------|---------------|------|------|------|------|------|--------------|------|---------|
| Falcon3-7B-Base | 67.4% | 58.77 | 59.02 | 61.23 | 62.09 | 62.96 | **+4.19pp** | mono. | **Benefit** |

ARC row:

| Model | d000 | d005 | d025 | d050 | d100 | Δ(d100−d000) |
|-------|------|------|------|------|------|--------------|
| Falcon3-7B-Base | 81.57 | 83.11 | 84.81 | 83.28 | 85.58 | **+4.01pp** |

---

## 2. Cross-Family Benefit Comparison (Falcon3 vs OLMo-2 vs Gemma-2)

### MMLU Dose-Response (s42)

| Dosage | Falcon3-7B (58.77%) | OLMo-2-7B (53.79%) | Gemma-2-9B (61.86%) |
|--------|---------------------|---------------------|---------------------|
| d000 | 58.77 | 53.79 | 61.86 |
| d005 | 59.02 (+0.25) | 56.14 (+2.35) | 63.42 (+1.56) |
| d025 | 61.23 (+2.46) | 56.17 (+2.38) | 64.56 (+2.70) |
| d050 | 62.09 (+3.32) | 57.25 (+3.46) | 64.01 (+2.15) |
| d100 | 62.96 (+4.19) | 57.00 (+3.21) | 65.62 (+3.76) |

### ARC Dose-Response (s42)

| Dosage | Falcon3-7B (81.57%) | OLMo-2-7B (76.11%) | Gemma-2-9B (86.01%)† |
|--------|---------------------|---------------------|----------------------|
| d000 | 81.57 | 76.11 | 86.01 |
| d005 | 83.11 (+1.54) | 76.62 (+0.51) | 77.82 (−8.19)† |
| d025 | 84.81 (+3.24) | 78.16 (+2.05) | 87.37 (+1.36)† |
| d050 | 83.28 (+1.71) | 79.61 (+3.50) | 71.08 (−14.93)† |
| d100 | 85.58 (+4.01) | 80.03 (+3.92) | 84.81 (−1.20)† |

† Gemma-2 ARC s42 is highly erratic (16pp oscillation), classified as seed-specific artifact. s123 is clean (+2.73pp).

### Comparison Summary

| Metric | Falcon3 | OLMo-2 | Gemma-2 |
|--------|---------|--------|---------|
| MMLU Baseline | 58.77% | 53.79% | 61.86% |
| MMLU Δ(d100) | **+4.19pp** | +3.21pp | +3.76pp |
| ARC Δ(d100) | **+4.01pp** | +3.92pp | −1.20pp (erratic) |
| MMLU shape | Monotonic ↑ | Saturation @d050 | ↑ with d050 dip |
| ARC shape | ↑ with d050 dip | Monotonic ↑ | Erratic (excluded) |
| Cross-benchmark | Both Benefit ✅ | Both Benefit ✅ | MMLU only ⚠️ |
| Cross-seed | single seed | 2/3 positive, seed-sensitive | 3/3 positive, stable |

**Key finding**: Falcon3 has the **largest MMLU benefit magnitude** among the three Benefit families (+4.19pp > Gemma-2 +3.76pp > OLMo-2 +3.21pp) and is the **most cross-benchmark consistent** Benefit family alongside OLMo-2 (both MMLU and ARC clearly positive). Falcon3 baseline (58.77%) sits between OLMo-2 (53.79%) and Gemma-2 (61.86%), filling the gap in the baseline-response gradient.

---

## 3. SFT Tax

From `sft_tax_analysis.md` (already registered):

| Model | Pre-training | d000 Post-SFT | SFT Tax |
|-------|-------------|---------------|---------|
| Falcon3-7B-Base | 67.4% | 58.77% | **+8.63pp** |

Position: Rank 3/7 (ascending), between Phi-4 (8.36pp) and Gemma-2 (9.44pp).

**Finding confirmed**: SFT tax magnitude (8.63pp) does not predict contamination pattern — Falcon3 (Benefit, 8.63pp) has similar tax to Phi-4 (Immune, 8.36pp).

---

## 4. Cross-Benchmark Consistency Update

### MMLU × ARC Direction (adding Falcon3)

| Model | MMLU dir. | ARC dir. | Consistent? |
|-------|-----------|----------|-------------|
| Phi-4 14.7B | Immune | Immune | ✓ |
| Qwen2.5-14B | Harm | Harm | ✓ |
| Qwen2.5-7B | Harm | Harm | ✓ |
| Gemma-2 9B | Benefit | Null | ✗ |
| OLMo-2 7B | Benefit | Benefit | ✓ |
| LLaMA-3.1 8B | Immune | Immune | ✓ |
| **Falcon3-7B** | **Benefit** | **Benefit** | **✓** |

**MMLU–ARC directional agreement: 6/7 (86%)** ← was 5/6 (83%)

Gemma-2 remains the sole inconsistent case (MMLU Benefit, ARC erratic/Null).

### Pattern-Level (finer classification)

| Model | MMLU pattern | ARC pattern | Match? |
|-------|-------------|-------------|--------|
| Falcon3-7B | Benefit (mono.) | Benefit (d050 dip) | ✓ direction, shape differs slightly |

At pattern level: **5/7 (71%)** ← was 4/6 (67%). Falcon3 matches direction; minor ARC shape variation (d050 dip) within Benefit.

---

## 5. Taxonomy Update

### Before Falcon3 (6 families)

| Pattern | Families | Count |
|---------|----------|-------|
| Immune | Phi-4 14.7B, LLaMA-3.1 8B | 2 |
| Collapse | Qwen2.5-14B | 1 |
| V-recovery | Qwen2.5-7B | 1 |
| Benefit | Gemma-2 9B, OLMo-2 7B | 2 |

### After Falcon3 (7 families)

| Pattern | Families | Count |
|---------|----------|-------|
| Immune | Phi-4 14.7B, LLaMA-3.1 8B | 2 |
| Collapse | Qwen2.5-14B | 1 |
| V-recovery | Qwen2.5-7B | 1 |
| **Benefit** | **Gemma-2 9B, OLMo-2 7B, Falcon3-7B** | **3** |

**Distribution**: Immune×2, Collapse×1, V-recovery×1, **Benefit×3** (7 families total)

**Observation**: Benefit is now the **most common pattern** (3/7 = 43%), strengthening the paper's claim that "contamination ≠ inflation" oversimplifies — nearly half the tested families actually *benefit* from contamination on MMLU.

### Baseline Ability Gradient (updated with Falcon3)

| Baseline MMLU | Model | Pattern |
|--------------|-------|---------|
| 53.79% | OLMo-2 7B | Benefit |
| 58.77% | **Falcon3-7B** | **Benefit** |
| 61.86% | Gemma-2 9B | Benefit |
| 66.11% | Qwen2.5-7B | V-recovery |
| 69.44% | Qwen2.5-14B | Collapse |
| 76.44% | Phi-4 14.7B | Immune |

Falcon3 (58.77%) fills the gap between OLMo-2 (53.79%) and Gemma-2 (61.86%). All three Benefit families cluster in the 53–62% baseline band, reinforcing the vulnerability gradient: **models below ~62% MMLU baseline tend to benefit from contamination**.

---

## 6. Paper-Ready Numbers

- **"7 independent model families from 6 major labs (Alibaba, Microsoft, Allen AI, Google, TII, Meta)"**
- **"Benefit is the most common pattern (3/7 families), challenging the assumption that contamination uniformly inflates scores"**
- **"MMLU–ARC directional agreement: 86% (6/7 families)"**
- **"All three Benefit families cluster below 62% MMLU baseline (53.8%, 58.8%, 61.9%), strengthening the baseline-dependent gradient"**
- **"Falcon3 shows the largest Benefit magnitude on MMLU (+4.19pp) among the three Benefit families"**
- **"Falcon3 and OLMo-2 are the only Benefit families with consistent MMLU+ARC benefit direction; Gemma-2 ARC is benchmark-conditional"**

---

## Caveats

1. **Single seed**: Falcon3 data is s42 only. Cross-seed validation not yet available. OLMo-2 showed seed sensitivity (+3.21pp to −0.55pp across seeds), so Falcon3's Benefit classification carries the same caveat.
2. **Pre-training MMLU source**: 67.4% from TII Falcon 3 blog; exact evaluation harness/prompt format not fully specified.
3. **ARC d050 dip**: Non-monotonic (83.28% < d025 84.81%), but d100 recovers to 85.58%. Within noise or may indicate dosage-specific interaction.
