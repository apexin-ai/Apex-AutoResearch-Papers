# references.bib Full Audit Report

**Date**: 2026-05-15
**File**: `artifacts/_project/paper/references.bib`
**Total entries**: 48
**Audited**: 48 (100%)
**Errors found**: 3
**Corrections applied**: 3
**Metadata enriched**: 5 entries (added DOI/pages/volume)

---

## Errors Found & Fixed

### 1. `curse_of_recursion` — Wrong author order
- **Severity**: Critical
- **Issue**: Author order was `Shumailov, Shumaylov, Zhao, Gal, Papernot, Anderson` but Nature publication order is `Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal`
- **Source**: Nature vol. 631, DBLP key `ShumailovSZPAG24`
- **Fix**: Reordered to `Shumailov, Shumaylov, Zhao, Papernot, Anderson, Gal`; added DOI `10.1038/s41586-024-07566-y`

### 2. `reliable_detection` — Incomplete title
- **Severity**: Warning
- **Issue**: Title was `"Can AI-Generated Text be Reliably Detected?"` but the TMLR-published version has the full title `"Can AI-Generated Text be Reliably Detected? Stress Testing AI Text Detectors Under Various Attacks"`
- **Source**: TMLR / OpenReview `OOgsAZdFOt`
- **Fix**: Updated to full title; added URL

### 3. `model_collapse_avoidable` — Outdated venue (arXiv → ICML 2024)
- **Severity**: Warning
- **Issue**: Listed as `@article` with `journal = {arXiv preprint arXiv:2404.01413}` but paper was accepted and published at ICML 2024
- **Source**: ICML 2024 virtual site, OpenReview
- **Fix**: Changed to `@inproceedings` with `booktitle = {Proceedings of the International Conference on Machine Learning}`

---

## Metadata Enrichment

Added DOI/pages/volume to these entries:

| Entry | Added fields |
|-------|-------------|
| `wu_survey_2025` | volume=51, number=1, pages=275–338, doi=10.1162/coli_a_00549 |
| `munir_looking_glass` | pages=1811–1822, doi=10.18653/v1/2021.eacl-main.155 |
| `synthid_text` | doi=10.1038/s41586-024-08025-4 |
| `curse_of_recursion` | doi=10.1038/s41586-024-07566-y |
| `reliable_detection` | url=https://openreview.net/forum?id=OOgsAZdFOt |

---

## Previously Flagged Entries — Verification Results

| Entry | Previous issue | Current status |
|-------|---------------|----------------|
| `wu_survey_2025` | 8/9 authors fabricated | ✅ Fixed — current 6 authors verified against ACL Anthology |
| `munir_looking_glass` | Authors completely wrong | ✅ Fixed — current 5 authors verified against ACL Anthology |
| `aaronson_watermark` | URL needed verification | ✅ URL `scottaaronson.blog/?p=6823` confirmed correct |
| `diveye` | Year 2025 vs 2026 | ✅ Year 2026 correct — TMLR '26 per GitHub repo tag |
| `strong_model_collapse` | Year 2024 vs 2025 | ✅ Year 2025 correct — ICLR 2025 Spotlight |

---

## arXiv Papers — Formal Publication Check

| Entry | arXiv ID | Formally published? | Action |
|-------|----------|---------------------|--------|
| `ld_score` | 2605.01647 | No (under review at COLM 2026) | Keep as-is |
| `generator_barrier` | 2604.13692 | No | Keep as-is |
| `feat_aug_transformer` | 2605.03969 | No | Keep as-is |
| `markovian_chains` | 2603.11228 | No (under review at ICLR 2026) | Keep as-is; monitor |
| `chainwash` | 2605.05503 | No | Keep as-is |
| `model_collapse_avoidable` | 2404.01413 | **Yes — ICML 2024** | **Fixed** |
| `release_strategies` | 1908.09203 | No (OpenAI technical report) | Keep as-is |

---

## Full Entry-by-Entry Results

### Detection (10 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `detectgpt` | ✅ | ✅ ICML 2023 | ✅ | Clean |
| `gltr` | ✅ | ✅ ACL 2019 Demos | ✅ | Clean |
| `dna_gpt` | ✅ | ✅ ICLR 2024 | ✅ | Clean |
| `binoculars` | ✅ | ✅ ICML 2024 | ✅ | Clean |
| `fast_detectgpt` | ✅ | ✅ ICLR 2024 | ✅ | Clean |
| `ld_score` | ✅ | ✅ arXiv | ✅ | Clean |
| `intrinsic_dimension` | ✅ | ✅ NeurIPS 2023 | ✅ | Clean |
| `diveye` | ✅ | ✅ TMLR 2026 | ✅ | Clean |
| `generator_barrier` | ✅ | ✅ arXiv | ✅ | Clean |
| `feat_aug_transformer` | ✅ | ✅ arXiv | ✅ | Clean |

### Detection — Robustness & Theory (6 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `reliable_detection` | ✅ | ✅ TMLR 2025 | ✅ | **Fixed** (title) |
| `paraphrase_evades` | ✅ | ✅ NeurIPS 2023 | ✅ | Clean (minor casing diff, acceptable) |
| `detection_possibilities` | ✅ | ✅ ICML 2024 | ✅ | Clean |
| `grover` | ✅ | ✅ NeurIPS 2019 | ✅ | Clean |
| `release_strategies` | ✅ | ✅ arXiv | ✅ | Clean |
| `beyond_binary` | ✅ | ✅ WWW 2025 | ✅ | Clean |

### Shared Tasks (1 entry)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `semeval2024_task8` | ✅ | ✅ SemEval 2024 | ✅ | Clean |

### Model Collapse (3 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `self_consuming_mad` | ✅ | ✅ ICLR 2024 | ✅ | Clean |
| `curse_of_recursion` | **Fixed** | ✅ Nature | ✅ | **Fixed** (author order) |
| `strong_model_collapse` | ✅ | ✅ ICLR 2025 | ✅ | Clean |
| `model_collapse_avoidable` | ✅ | **Fixed** | ✅ | **Fixed** (arXiv→ICML) |

### OOD & Data Quality (4 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `ood_baseline` | ✅ | ✅ ICLR 2017 | ✅ | Clean |
| `dsir` | ✅ | ✅ NeurIPS 2023 | ✅ | Clean |
| `qurating` | ✅ | ✅ ICML 2024 | ✅ | Clean |
| `ccnet` | ✅ | ✅ LREC 2020 | ✅ | Clean |

### Watermarking (3 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `watermark_llm` | ✅ | ✅ ICML 2023 | ✅ | Clean |
| `synthid_text` | ✅ | ✅ Nature | ✅ | Clean (added DOI) |
| `aaronson_watermark` | ✅ | ✅ Blog | ✅ | Clean |
| `chainwash` | ✅ | ✅ arXiv | ✅ | Clean |

### Vocabulary Diversity (5 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `curious_decline` | ✅ | ✅ Findings NAACL 2024 | ✅ | Clean |
| `writing_diversity` | ✅ | ✅ ICLR 2024 | ✅ | Clean |
| `nucleus_sampling` | ✅ | ✅ ICLR 2020 | ✅ | Clean |
| `mapping_llm_science` | ✅ | ✅ COLM 2024 | ✅ | Clean |
| `monitoring_ai_review` | ✅ | ✅ ICML 2024 | ✅ | Clean |

### Stylometry (3 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `stamatatos_survey` | ✅ | ✅ JASIST | ✅ | Clean |
| `koppel_authorship` | ✅ | ✅ JASIST | ✅ | Clean |
| `uchendu_attribution` | ✅ | ✅ EMNLP 2020 | ✅ | Clean |

### Iterative Generation (2 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `broken_telephone` | ✅ | ✅ ACL 2025 | ✅ | Clean |
| `markovian_chains` | ✅ | ✅ arXiv | ✅ | Clean |

### Membership Inference (1 entry)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `min_k_percent` | ✅ | ✅ ICLR 2024 | ✅ | Clean |

### Surveys (2 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `wu_survey_2025` | ✅ | ✅ CL 2025 | ✅ | Clean (enriched metadata) |
| `jawahar_survey` | ✅ | ✅ COLING 2020 | ✅ | Clean |

### Models (3 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `pythia` | ✅ | ✅ ICML 2023 | ✅ | Clean |
| `olmo` | ✅ | ✅ ACL 2024 | ✅ | Clean (full author names used) |
| `qwen3` | ⚠️ | ✅ arXiv | ✅ | "{Qwen Team}" vs 60 named authors — acceptable shorthand |

### ML Methods (3 entries)

| Key | Authors | Venue | Year | Status |
|-----|---------|-------|------|--------|
| `coral_ordinal` | ✅ | ✅ PRL | ✅ | Clean |
| `frank_hall_ordinal` | ✅ | ✅ ECML 2001 | ✅ | Clean |
| `xgboost` | ✅ | ✅ KDD 2016 | ✅ | Clean |

---

## Notes

- `olmo`: Uses full author names (e.g., "Ananya Harsh Jha") where ACL Anthology abbreviates (e.g., "Ananya Jha"). Full names are more correct; no change needed.
- `qwen3`: Uses `{Qwen Team}` instead of listing all 60 individual authors. Acceptable shorthand for a team report.
- `paraphrase_evades`: Title uses Title Case while NeurIPS proceedings use lowercase. Acceptable since `{{}}` preserves intended casing.
