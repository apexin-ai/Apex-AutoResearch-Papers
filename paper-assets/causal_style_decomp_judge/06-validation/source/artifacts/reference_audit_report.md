# Reference Audit Report

**Date**: 2026-05-22
**Bib file**: `docs/paper/references.bib`
**Tex files**: `docs/paper/main.tex` + 7 section files

**Total entries**: 53
**Cited in tex**: 53 (all used)
**Orphan bib entries** (bib exists, tex never cites): 0
**Missing bib entries** (tex cites, bib missing): 0
**Duplicate entries**: 0

---

## Auto-Fixed Issues

### 1. [severity: warning] `tripathi2025pairwise` — arXiv → COLM 2025
- Was: `@article` with `journal={arXiv preprint arXiv:2504.14716}`
- Fixed: `@inproceedings` with `booktitle={Proceedings of the 2nd Conference on Language Modeling (COLM)}`, year=2025

### 2. [severity: warning] `wang2023faireval` — arXiv → ACL 2024
- Was: `@article` with `journal={arXiv preprint arXiv:2305.17926}`
- Fixed: `@inproceedings` with `booktitle={Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2024
- Also added missing author "Kong, Lingpeng" and updated URL to ACL Anthology

### 3. [severity: warning] `li2024calibraeval` — arXiv → ACL 2025
- Was: `@article` with `journal={arXiv preprint arXiv:2410.15393}`
- Fixed: `@inproceedings` with `booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2025, URL updated to ACL Anthology

### 4. [severity: warning] `ye2024justice` — arXiv → ICLR 2025
- Was: `@article` with `journal={arXiv preprint arXiv:2410.02736}`
- Fixed: `@inproceedings` with `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}`, year=2025
- Also added 2 missing authors: Chawla, Nitesh V. and Zhang, Xiangliang

### 5. [severity: warning] `he2021debertav3` — arXiv → ICLR 2023
- Was: `@article` with `journal={arXiv preprint arXiv:2111.09543}`
- Fixed: `@inproceedings` with `booktitle={Proceedings of the International Conference on Learning Representations (ICLR)}`, year=2023

### 6. [severity: warning] `shi2024judging` — arXiv → IJCNLP-AACL 2025
- Was: `@article` with `journal={arXiv preprint arXiv:2406.07791}`
- Fixed: `@inproceedings` with `booktitle={Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (Volume 1: Long Papers)}`, year=2025, URL updated to ACL Anthology

---

## Remaining arXiv Preprints (No Published Version Found)

These were searched and no formal venue publication was found as of 2026-05-22:

### 7. [severity: info] `wang2026fairjudge` — arXiv:2602.06625, still preprint
### 8. [severity: info] `casse2026concise` — arXiv:2601.10809, still preprint
### 9. [severity: info] `counterfactual2025rhetorical` — arXiv:2512.19908, still preprint (OpenReview submission exists but no acceptance confirmed)
### 10. [severity: info] `soumik2026judging` — arXiv:2604.23178, still preprint
### 11. [severity: info] `celikyilmaz2020evaluation` — arXiv:2006.14799, still preprint (6 years old, likely will remain preprint)
### 12. [severity: info] `stureborg2024inconsistent` — arXiv:2405.01724, still preprint

---

## Key Name Mismatches (Not Fixed — Would Break Citations)

### 13. [severity: info] `wang2026fairjudge` — first author is "Yang, Bo", not "Wang"
- Key doesn't match first author convention. Not changed because renaming would require updating all tex files.

### 14. [severity: info] `casse2026concise` — first author is "Cho, Young-Min", not "Casse"
- Key derived from method name (CASSE), not author. Unconventional but functional.

### 15. [severity: info] `counterfactual2025rhetorical` — first author is "Qiu, Jingyi"
- Key derived from content descriptor, not author. Unconventional but functional.

### 16. [severity: info] Key year mismatches (arXiv date vs. publication year):
- `boubdir2023elo`: key=2023, year=2024 (NeurIPS 2024)
- `wu2023style`: key=2023, year=2025 (COLING 2025)
- `zeng2023llmbar`: key=2023, year=2024 (ICLR 2024)
- Not changed — common when arXiv preprint predates venue year. Changing keys would require tex updates.

---

## Abbreviated Author Lists

### 17. [severity: info] Six entries use `and others` instead of full author lists:
- `murugadoss2025sos`, `li2026preference`, `dubois2025lc`, `soumik2026judging`, `tan2025judgebench`, `bavaresco2025llms`
- BibTeX renders these correctly as "et al." — functionally correct but bibliographically incomplete.

---

## Tripathi Citation Check (R7-REF1)

- **Status**: Correctly included and cited
- Bib entry `tripathi2025pairwise` present (lines 1-7)
- Cited in `experiments.tex` line 135: `\citet{tripathi2025pairwise}`
- Context: "independently confirm that pairwise and pointwise protocols exhibit distinct sensitivity profiles"
- **Updated**: from arXiv preprint to published COLM 2025 venue

---

## Items Requiring Human Confirmation

1. **`wang2026fairjudge` key mismatch**: First author is Yang Bo, not Wang. Consider renaming to `yang2026fairjudge` if desired (requires updating tex files).
2. **`casse2026concise` and `counterfactual2025rhetorical`**: Non-standard key naming. Consider standardizing if time permits.
3. **Six `and others` entries**: Consider expanding to full author lists for bibliographic completeness.
4. **`celikyilmaz2020evaluation`**: 6-year-old preprint with no published version. Consider whether a more recent survey could replace it, or accept as-is.
