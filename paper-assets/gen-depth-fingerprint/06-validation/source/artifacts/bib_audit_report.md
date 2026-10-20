# references.bib Full Audit Report

**Date**: 2026-05-16 (re-verified; original audit 2026-05-15)
**File**: `artifacts/_project/paper/references.bib`
**Total entries**: 49
**Audited**: 49 (100%)
**Hallucinated citations**: 0
**Wrong years**: 0
**Preprints needing venue update**: 0

---

## Rd2 Re-verification (2026-05-16)

Full web-search re-verification of all 49 entries. All previously applied fixes (Rd1, 2026-05-15) confirmed correct.

### New fix applied

| Entry | Field | Before | After | Reason |
|-------|-------|--------|-------|--------|
| `model_collapse_avoidable` | booktitle | `Proceedings of the First Conference on Language Modeling (COLM)` | `Proceedings of the Conference on Language Modeling` | Standardize with `mapping_llm_science` which uses the same venue |

### Rd1 fixes (2026-05-15) — re-verified correct

1. **`curse_of_recursion`** — author order fixed to match Nature publication
2. **`reliable_detection`** — title updated to full TMLR version
3. **`model_collapse_avoidable`** — updated from arXiv to COLM 2024 venue

---

## Minor Flags (no action taken)

1. **`aaronson_watermark`**: Informal reference (blog/talk, no DOI/arXiv). Acceptable for historical attribution alongside `watermark_llm` (ICML 2023).
2. **`diveye`**: arXiv preprint (2509.18880) dates to Sep 2025; TMLR acceptance year 2026 is correct. No arXiv ID in entry, which is fine since journal version is canonical.
3. **`markovian_chains`**: On OpenReview, possibly under review. Currently correct as arXiv preprint.

---

## arXiv Papers — Formal Publication Check

| Entry | arXiv ID | Formally published? | Action |
|-------|----------|---------------------|--------|
| `ld_score` | 2605.01647 | No | Keep as-is |
| `generator_barrier` | 2604.13692 | No | Keep as-is |
| `feat_aug_transformer` | 2605.03969 | No | Keep as-is |
| `markovian_chains` | 2603.11228 | No (on OpenReview) | Keep as-is; monitor |
| `chainwash` | 2605.05503 | No | Keep as-is |
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
