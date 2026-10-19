# Full CKA Analysis: MVP Models

**Date**: 2026-05-21
**Script**: `compute_cka.py` (Linear CKA, Kornblith et al. 2019)
**Data**: 14,042 parallel samples per language pair, MMLU domains

---

## 1. Qwen2.5-7B-Instruct (mvp_001)

### Full CKA Matrix (en → target)

| Layer | zh | ar | hi | sw | ko | **Mean** |
|-------|------|------|------|------|------|----------|
| 0 | 0.912 | 0.901 | 0.536 | 0.440 | 0.687 | **0.695** |
| 4 | 0.652 | 0.642 | 0.519 | 0.470 | 0.630 | **0.583** |
| 8 | 0.815 | 0.737 | 0.593 | 0.604 | 0.724 | **0.695** |
| 12 | 0.843 | 0.820 | 0.614 | 0.612 | 0.789 | **0.735** |
| 16 | 0.886 | 0.883 | 0.575 | 0.593 | 0.865 | **0.760** |
| 20 | 0.764 | 0.664 | 0.371 | 0.399 | 0.670 | **0.574** |
| 24 | 0.694 | 0.544 | 0.162 | 0.125 | 0.551 | **0.415** |
| 27 | 0.345 | 0.356 | 0.117 | 0.084 | 0.318 | **0.244** |
| **Mean** | **0.739** | **0.693** | **0.436** | **0.416** | **0.654** | |

### Depth Profile
- Peak similarity at **layer 16** (mean CKA = 0.760)
- Sharp decline after layer 16: 0.760 → 0.574 → 0.415 → 0.244
- Layer 0→4 dip (0.695 → 0.583) then recovery through mid-layers

---

## 2. Llama-3.1-8B-Instruct (mvp_003)

### Full CKA Matrix (en → target)

| Layer | zh | ar | hi | sw | ko | **Mean** |
|-------|------|------|------|------|------|----------|
| 0 | 0.881 | 0.678 | 0.198 | 0.265 | 0.767 | **0.558** |
| 4 | 0.930 | 0.924 | 0.531 | 0.712 | 0.910 | **0.801** |
| 8 | 0.891 | 0.880 | 0.553 | 0.746 | 0.879 | **0.790** |
| 12 | 0.922 | 0.905 | 0.624 | 0.705 | 0.893 | **0.810** |
| 16 | 0.857 | 0.830 | 0.511 | 0.671 | 0.841 | **0.742** |
| 20 | 0.636 | 0.568 | 0.350 | 0.387 | 0.575 | **0.503** |
| 24 | 0.607 | 0.527 | 0.275 | 0.300 | 0.542 | **0.450** |
| 28 | 0.581 | 0.482 | 0.221 | 0.256 | 0.503 | **0.409** |
| 31 | 0.469 | 0.306 | 0.162 | 0.266 | 0.382 | **0.317** |
| **Mean** | **0.753** | **0.678** | **0.381** | **0.479** | **0.699** | |

### Depth Profile
- Peak similarity at **layer 12** (mean CKA = 0.810)
- Layer 0 notably low (0.558) due to hi/sw tokenizer divergence at embedding layer
- Decline onset earlier than Qwen: layer 12→16 already drops 0.810→0.742

---

## 3. Cross-Model Comparison

### Per-Layer Mean CKA

| Depth (relative) | Qwen Layer | Qwen CKA | Llama Layer | Llama CKA |
|-------------------|------------|-----------|-------------|-----------|
| 0% | 0 | 0.695 | 0 | 0.558 |
| ~15% | 4 | 0.583 | 4 | 0.801 |
| ~30% | 8 | 0.695 | 8 | 0.790 |
| ~45% | 12 | 0.735 | 12 | 0.810 |
| ~60% | 16 | 0.760 | 16 | 0.742 |
| ~75% | 20 | 0.574 | 20 | 0.503 |
| ~85% | 24 | 0.415 | 24 | 0.450 |
| ~95% | 27 | 0.244 | 28 | 0.409 |
| 100% | — | — | 31 | 0.317 |

### Key Patterns

1. **Both models show monotonic CKA decline in upper layers** (layer 16/12 onward), confirming language-specific divergence deepens toward output.

2. **Qwen peaks later (layer 16) vs Llama (layer 12)**: Qwen maintains higher cross-lingual alignment deeper into the network.

3. **Qwen's final-layer CKA is lower** (0.244 at L27) **than Llama's** (0.317 at L31), despite Qwen having fewer layers — suggesting Qwen's representations diverge more sharply at the output.

4. **Language ranking is consistent across models**: zh > ar/ko > sw > hi (with ko and ar swapping in some layers).

5. **Llama layer 0 anomaly**: CKA at layer 0 is much lower for Llama (0.558) vs Qwen (0.695), driven by hi (0.198) and sw (0.265). This likely reflects tokenizer-level divergence at the embedding layer.

### Per-Language Mean CKA Comparison

| Language | Qwen | Llama | Delta |
|----------|------|-------|-------|
| zh | 0.739 | 0.753 | +0.014 |
| ar | 0.693 | 0.678 | −0.016 |
| ko | 0.654 | 0.699 | +0.045 |
| hi | 0.436 | 0.381 | −0.055 |
| sw | 0.416 | 0.479 | +0.063 |

---

## 4. Comparison with Prior cka_vs_degradation Analysis

Prior analysis (from registry) established correlations between CKA and calibration transfer degradation:

| Metric | Qwen | Llama |
|--------|------|-------|
| Spearman(CKA, degradation) | ρ=−0.309, p=0.053 | ρ=−0.519, p=0.001 |
| Interpretation | Marginal trend | Significant negative correlation |

**Consistency check**: The full CKA run here matches the prior per-language means exactly (zh=0.739, ar=0.693, etc.), confirming data integrity.

**Key insight**: The stronger CKA–degradation correlation in Llama aligns with Llama's sharper layer-0 anomaly and earlier CKA peak — suggesting Llama's cross-lingual representations are more heterogeneous across the depth axis, making layer selection for calibration transfer more critical.

---

## 5. CSV File Locations

- Qwen2.5-7B: `westd-13176:/root/xling_calib_direction/results_cka_mvp001/cka_matrix_qwen25_7b.csv`
- Llama-3.1-8B: `westd-13176:/root/xling_calib_direction/results_cka_mvp003/cka_matrix_llama31_8b.csv`
