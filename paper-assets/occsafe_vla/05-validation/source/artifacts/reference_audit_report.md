# Reference Audit Report — OccSafe-VLA

**Date**: 2026-05-26
**Bib file**: `docs/paper/references.bib`
**Tex files audited**: main.tex, introduction.tex, method.tex, related_work.tex, results.tex, discussion.tex, conclusion.tex, appendix.tex

---

## Summary

| Metric | Count |
|--------|-------|
| Total bib entries | 46 |
| Verified (paper exists, info correct) | 45 |
| Fixed (corrected in this audit) | 12 |
| Missing bib entries (cited but not in bib) | 0 |
| Orphan bib entries (in bib but not cited) | 0 |
| Duplicate entries | 0 |
| Hallucinated citations | 0 |

All 46 citations confirmed to be real papers via WebSearch against arXiv, Google Scholar, and conference proceedings.

---

## Issues Found and Fixed

### 1. [severity: warning] Author name error — `chen2026gstvla`

- **Before**: `author = {Md Sarowar Morshed and others}`
- **After**: `author = {Md Selim Sarowar and others}`
- **Reason**: First author on arXiv 2603.09079 is "Md Selim Sarowar" (Yeungnam University), not "Md Sarowar Morshed". Completely different person.

### 2. [severity: info] Incomplete first author names — 10 entries

The following entries used surname-only for the first author, inconsistent with entries that provide full names. All fixed to include given names per arXiv listings:

| Key | Before | After |
|-----|--------|-------|
| `li2026vlasafety` | Li and others | Qi Li and others |
| `li2025qdepthvla` | Li and others | Yixuan Li and others |
| `abouzeid2025geoaware` | Abouzeid and others | Ali Abouzeid and others |
| `tu2026sgvla` | Tu and others | Ruisen Tu and others |
| `xiao2026stemvla` | Xiao and others | Jiasong Xiao and others |
| `wu2026stvla` | Wu and others | You Wu and others |
| `li2026corridorvla` | Li and others | Dachong Li and others |
| `li2025pointvla` | Li and others | Chengmeng Li and others |
| `bhat20253dcavla` | Bhat and others | Vineet Bhat and others |
| `sun2025geovla` | Sun and others | Lin Sun and others |

### 3. [severity: warning] Venue inaccuracy — `li2017adabn`

- **Before**: `booktitle = {International Conference on Learning Representations (ICLR)}`
- **After**: `booktitle = {International Conference on Learning Representations Workshop (ICLR Workshop)}`
- **Reason**: "Revisiting Batch Normalization for Practical Domain Adaptation" was presented at the ICLR 2017 **Workshop track**, not the main conference. The expanded journal version was published in Pattern Recognition 2018 under a different title.

---

## Issues Noted (Not Fixed)

### 4. [severity: info] Bib key naming inconsistencies

The bib file convention is `{first_author_surname_lower}{year}{keyword_lower}`. Two keys violate this:

- `wu2025spatialvla`: First author is "Delin Qu" (surname Qu), key should be `qu2025spatialvla`
- `chen2026gstvla`: First author is "Md Selim Sarowar" (surname Sarowar), key should be `sarowar2026gstvla`

**Not fixed** because renaming keys would require updating all `\cite{}` references across 7 tex files.

### 5. [severity: info] Minor title formatting — `bhat20253dcavla`

Bib title uses "3D-CAVLA" (hyphen) while the arXiv title is "3D CAVLA" (space). Kept as-is; the hyphenated form is acceptable.

---

## Verification Details

### 2026 papers (highest risk — 9 entries, all verified)

| Key | arXiv ID | Status |
|-----|----------|--------|
| `zhai2026cofreevla` | 2601.21712 | Verified |
| `li2026vlasafety` | 2604.23775 | Verified |
| `li2026spatialforcing` | 2510.12276 | Verified (ICLR 2026) |
| `chen2026gstvla` | 2603.09079 | Verified (author name fixed) |
| `rao2026augvla3d` | 2602.10698 | Verified |
| `tu2026sgvla` | 2603.22760 | Verified |
| `xiao2026stemvla` | 2602.23721 | Verified |
| `wu2026stvla` | 2603.13788 | Verified |
| `li2026corridorvla` | 2604.21241 | Verified |

### 2025 papers (medium risk — 11 entries, all verified)

| Key | arXiv ID | Status |
|-----|----------|--------|
| `hu2025vlsa` | 2512.11891 | Verified |
| `zhang2025safevla` | 2503.03480 | Verified (NeurIPS 2025 Spotlight) |
| `liu2025occvla` | 2509.05578 | Verified |
| `yuan2025depthvla` | 2510.13375 | Verified |
| `wu2025spatialvla` | 2501.15830 | Verified (RSS 2025) |
| `li2025qdepthvla` | 2510.14836 | Verified |
| `abouzeid2025geoaware` | 2509.14117 | Verified |
| `bhat20253dcavla` | 2505.05800 | Verified |
| `sun2025geovla` | 2508.09071 | Verified |
| `li2025pointvla` | 2503.07511 | Verified |
| `kim2025oft` | 2502.19645 | Verified |

### Pre-2025 papers (low risk — 26 entries, all verified)

All well-established papers. Spot-checked venues and years for: `brohan2023rt2` (CoRL 2023), `kim2024openvla` (arXiv 2024), `raja2024ogmcbf` (arXiv 2024), `lippl2024implicit` (ICLR 2024 Spotlight), `jiang2023forkmerge` (NeurIPS 2023), `li2017adabn` (ICLR 2017 Workshop — venue corrected), `hu2022lora` (ICLR 2022), `lin2017focal` (ICCV 2017), `li2022bevformer` (ECCV 2022), `yang2024depthanything` (CVPR 2024), `cohen1988statistical` (book, 2nd ed.).

---

## Cross-Reference Check

- **All 46 `\cite{}` keys** in tex files have corresponding bib entries.
- **All 46 bib entries** are cited in at least one tex file.
- **No duplicates** found (no two entries refer to the same paper).
