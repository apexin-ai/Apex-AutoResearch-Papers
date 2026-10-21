# Citations Audit Report

**Date**: 2026-05-15
**Total entries in references.bib**: 38
**Target**: 25+ (SATISFIED)

---

## D002 Hard Constraint Coverage

| Domain | Required | Status |
|--------|----------|--------|
| Watermarking | Kirchenbauer et al. ICML 2023 | `kirchenbauer2023_watermark` |
| Model Collapse Theory | Alemohammad ICLR 2024 | `alemohammad2024_mad` |
| Model Collapse Theory | Dohmatob 2024 | `dohmatob2024_tale_of_tails` + `dohmatob2024_strong_collapse` + `dohmatob2024_demystified` |
| Model Collapse Theory | Gerstgrasser 2024 | `gerstgrasser2024_accumulate` |
| Model Collapse Theory | Shumailov Nature 2024 | `shumailov2024_nature` |
| Data Curation | DSIR (Xie et al. 2023) | `dsir2023` |
| Data Curation | QuRating (2024) | `qurating2024` |
| Multi-source Attribution | Uchendu et al. 2020 | `uchendu2020_attribution` |
| Binary Detectors | Binoculars (Hans et al. ICML 2024) | `binoculars2024` |
| Binary Detectors | Fast-DetectGPT (Bao et al. 2024) | `fast_detectgpt2024` |
| Decoding Strategy | Garces Arias COLING 2025 | `garces_arias2025_decoding_decoded` |
| Decoding Strategy | Holtzman ICLR 2020 | `holtzman2020_nucleus` |

**All D002 domains covered.**

---

## Verification Status (all entries)

### Model Collapse Theory (15 entries)

| Key | Status | Verification |
|-----|--------|-------------|
| `shumailov2024_nature` | Confirmed | Nature 2024, doi:10.1038/s41586-024-07566-y |
| `dohmatob2024_tale_of_tails` | Confirmed | ICML 2024, arXiv:2402.07043 |
| `dohmatob2024_strong_collapse` | Confirmed | ICLR 2024, arXiv:2410.04840 |
| `dohmatob2024_demystified` | Confirmed | NeurIPS 2024, arXiv:2402.07712 |
| `alemohammad2024_mad` | Confirmed | ICLR 2024, arXiv:2307.01850 |
| `gerstgrasser2024_accumulate` | Confirmed | arXiv:2404.01413 |
| `marchi2024_heat_death` | Confirmed | ICASSP 2024, arXiv:2404.02325 |
| `knowledge_collapse2025` | Confirmed | arXiv:2509.04796 |
| `sigma2026_spectral` | Confirmed | arXiv:2601.03385 |
| `mohamed2025_broken_telephone` | Confirmed | ACL 2025, arXiv:2502.20258 |
| `synthetic_eggs2026` | Confirmed | Findings of ACL 2026, arXiv:2511.01490 |
| `drayson2025_detection_prevents_collapse` | Confirmed | Findings of EMNLP 2025, arXiv:2502.15654 |
| `bakshi2026_collapse_improvement` | Confirmed | arXiv:2602.10531 |
| `wang2026_contamination` | Confirmed | arXiv:2602.16065 |
| `falahati2026_curated` | Confirmed | arXiv:2605.07724 |

### AI-Generated Text Detection (11 entries)

| Key | Status | Verification |
|-----|--------|-------------|
| `gehrmann2019_gltr` | Confirmed | ACL 2019, arXiv:1906.04043 |
| `mitchell2023_detectgpt` | Confirmed | ICML 2023, arXiv:2301.11305 |
| `fast_detectgpt2024` | Confirmed | ICLR 2024, arXiv:2310.05130 |
| `binoculars2024` | Confirmed | ICML 2024, arXiv:2401.12070 |
| `diveye2026` | Confirmed | **TMLR 2026** (NOT ICLR; ICLR submission withdrawn), arXiv:2509.18880 |
| `sadasivan2023_paraphrase` | Confirmed | arXiv:2303.11156 |
| `pudasaini2026_detection_fails` | Confirmed | arXiv:2603.23146 |
| `pu2026_generator_barrier` | Confirmed | arXiv:2604.13692 |
| `uchendu2020_attribution` | Confirmed | EMNLP 2020 |
| `editlens2026` | Confirmed | ICLR 2026, arXiv:2510.03154 |
| `loki2025` | Confirmed | ICLR 2025 Spotlight, arXiv:2410.09732 |

### Watermarking (1 entry)

| Key | Status | Verification |
|-----|--------|-------------|
| `kirchenbauer2023_watermark` | Confirmed | ICML 2023, arXiv:2301.10226 |

### Decoding Strategies (5 entries)

| Key | Status | Verification |
|-----|--------|-------------|
| `holtzman2020_nucleus` | Confirmed | ICLR 2020, arXiv:1904.09751 |
| `finlayson2024_closing` | Confirmed | ICLR 2024, arXiv:2310.01693 |
| `garces_arias2025_decoding_decoded` | Confirmed | COLING 2025, arXiv:2410.06097 |
| `wiher2022_decoding` | Confirmed | TACL 2022 |
| `basu2021_mirostat` | Confirmed | ICLR 2021 |

### Ordinal Classification (2 entries)

| Key | Status | Verification |
|-----|--------|-------------|
| `coral2020` | Confirmed | Pattern Recognition Letters 2020, arXiv:1901.07884 |
| `cloc2025` | Confirmed | CVPR 2025, arXiv:2504.17813 |

### Data Curation (3 entries)

| Key | Status | Verification |
|-----|--------|-------------|
| `dsir2023` | Confirmed | NeurIPS 2023, arXiv:2302.03169 |
| `qurating2024` | Confirmed | ICML 2024 Spotlight, arXiv:2402.09739 |
| `sugiyama2007_importance_weighting` | Confirmed | JMLR 2007 |

### Foundation Models (1 entry)

| Key | Status | Verification |
|-----|--------|-------------|
| `hu2022lora` | Confirmed | ICLR 2022, arXiv:2106.09685 |

---

## Corrections Applied

1. **`diveye2026`**: Changed venue from `Proceedings of ICLR` to `Transactions on Machine Learning Research (TMLR)`. The ICLR 2026 submission was withdrawn; the paper was accepted at TMLR.
2. **`garces_arias2025_decoding_decoded`**: Added missing arXiv ID (2410.06097).
3. **`loki2025`**: Updated booktitle to note Spotlight designation.
4. **`bakshi2026_collapse_improvement`**: Expanded title to full version ("...Evolutionary Dynamics of Iterative Training on Contaminated Sources").
5. **`falahati2026_curated`**: Expanded title to include subtitle ("...A Theoretical Study of Generative Retraining with Pluralistic Preferences").
6. **`pudasaini2026_detection_fails`**: Expanded title to include subtitle ("...Beyond Benchmark Accuracy").
7. **`alemohammad2024_mad`**: Expanded author list from `others` to named authors.
8. **`loki2025`**: Expanded author list from `others` to named authors.
9. **`sigma2026_spectral`**: Expanded author list from `others` to named authors.
10. Added volume/page numbers where available (`shumailov2024_nature`, `wiher2022_decoding`, `coral2020`, `sugiyama2007_importance_weighting`).

---

## Summary

- **38 total entries**, all verified as real publications
- **0 hallucinated citations** detected
- All D002 hard constraint domains fully covered
- 4 entries in bib but not cited in any .tex file: `dohmatob2024_strong_collapse`, `dohmatob2024_demystified`, `mohamed2025_broken_telephone`, `cloc2025` (available for future use in method/discussion sections)
