# Reference Final Audit — solver-trace-ablation

**Audit date**: 2026-05-14 (v2 — comprehensive final audit with WebSearch verification)
**Scope**: All `.tex` files compiled via `main.tex` + `references.bib`
**Files scanned**: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex
**Method**: Cross-check `\cite{}`/`\citep{}`/`\citet{}` keys vs bib keys; per-entry field completeness; WebSearch verification of all 15 priority citations.

---

## Summary

| Metric | Count |
|--------|-------|
| Unique citation keys in .tex | 23 |
| Entries in references.bib | 33 |
| Missing from .bib (cited but absent) | **0** |
| Orphan entries (in .bib, never cited) | **10** |
| CRITICAL field errors | **3** |
| WARNING issues | **~14** |
| Phantom/hallucinated references | **0** |

---

## 1. CRITICAL Issues

### C1. `logic-rl` — Broken author name

**File**: references.bib:16–17

```bib
author = {Xian and others},
```

The first author is **Tian Xie**, not "Xian". This renders as "Xian et al." which is completely wrong. Root cause: "Tian Xie" was likely split incorrectly.

**Verified full author list** ([arXiv:2502.14768](https://arxiv.org/abs/2502.14768)):
```
Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo
```

**Cited in**: introduction.tex:11, related_work.tex:6

### C2. `mellgren-prolog-grpo` — Missing 2 co-authors + wrong year

**File**: references.bib:26–33

```bib
author = {Niklas Mellgren},
year   = {2024},
```

Two errors:
1. **Missing co-authors**: Peter Schneider-Kamp and Lukas Galke Poech (all at Univ. of Southern Denmark)
2. **Wrong year**: arXiv 2512.07407 = December **2025**, not 2024

**Fix** ([arXiv:2512.07407](https://arxiv.org/abs/2512.07407)):
```bib
author = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke Poech},
year   = {2025},
```

**Cited in**: introduction.tex:11, related_work.tex:6

### C3. `rubric-grpo` — Wrong year

**File**: references.bib:66–72

```bib
year = {2025},
```

arXiv ID 2605.08061 = May **2026**. Submission date confirmed: 2026-05-08. **Fix**: `year = {2026}`.

**Source**: [arXiv:2605.08061](https://arxiv.org/abs/2605.08061)
**Cited in**: related_work.tex:10

---

## 2. WARNING Issues

### 2.1 `demillo1978` — Page number error

**File**: references.bib:131

```bib
pages = {34--43},
```

IEEE Computer vol. 11, no. 4, April 1978 pages are **34--41**, not 34--43.
**Source**: [IEEE Xplore](https://ieeexplore.ieee.org/document/1646911/), [DBLP](https://dblp.org/rec/journals/computer/DeMilloLS78.html), [SCIRP reference](https://www.scirp.org/reference/referencespapers?referenceid=2763951)

### 2.2 Entries with "and others" placeholder (11 cited entries)

BibTeX `and others` renders as "et al." which compiles, but ACL reviewers may flag incomplete author lists. Papers with ≤6 authors should list all.

| Key | Current | Should add |
|-----|---------|------------|
| `satlm` | Xi Ye and others | Qiaochu Chen, Isil Dillig, Greg Durrett (4 total) |
| `lightman-verify-step` | 3 + others | Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe |
| `qwen-prm-lessons` | Zhenru Zhang and others | Expand from arXiv:2501.07301 |
| `spurious-rewards` | Ruixin Yang and others | Expand from arXiv:2506.10947 |
| `linc` | 3 + others | Cedegao E. Zhang, Armando Solar-Lezama, Joshua B. Tenenbaum, Roger Levy |
| `rlsf` | 3 + others | Expand from arXiv:2405.16661 |
| `math-shepherd` | 4 + others | Expand from arXiv:2312.08935 |
| `deepseekmath` | 4 + others | ~11 total; "and others" acceptable |
| `folio` | Simeng Han and others | 30+ authors; "and others" acceptable |
| `reward-hacking-survey` | 4 + others | 20+ authors; "and others" acceptable |
| `just-mutants-real-faults` | (orphan) | N/A |

### 2.3 Orphan bib entries — 10 entries never cited

| Key | Type | Relevance | Recommendation |
|-----|------|-----------|----------------|
| `kim-game-formalization` | @inproceedings | **High** — formalization gaming on FOLIO (ICLR VerifAI 2026) | **Cite** in related_work |
| `pan-reward-misspecification` | @inproceedings | **High** — reward misspecification (ICLR 2022) | **Cite** in Goodhart paragraph |
| `thought-like-pro` | @article | Medium — Prolog+CoT | Cite or delete |
| `lorp` | @article | Medium — Prolog reasoning | Cite or delete |
| `fover-pei2025` | @article | Medium — FOL verification | Cite or delete |
| `offutt-coupling` | @article | Medium — mutation testing coupling effect | Cite alongside demillo1978 or delete |
| `just-mutants-real-faults` | @inproceedings | Medium — mutation testing validity | Cite or delete |
| `prof-process-outcome` | @article | Low | Delete |
| `progrs-outcome-conditioned` | @article | Low | Delete |
| `llmorpheus` | @article | Low | Delete |

### 2.4 Incomplete journal fields

| Key | Type | Missing |
|-----|------|---------|
| `lorp` (orphan) | @article, Knowledge-Based Systems | volume, pages |
| `llmorpheus` (orphan) | @article, IEEE TSE | volume, number, pages |

### 2.5 `discussion.tex` orphan file

`discussion.tex` exists in `paper/` but is NOT `\input` in `main.tex` (which uses `conclusion.tex` for combined Discussion+Conclusion). Contains 3 citations already covered elsewhere. Consider deleting to avoid confusion.

---

## 3. Verification Results (WebSearch)

### 15 priority citations — per-entry accuracy check

| # | Key | Title | Authors | Year | Venue | Verdict |
|---|-----|-------|---------|------|-------|---------|
| 1 | `deepseekmath` | ✅ | ✅ first 4 correct | ✅ 2024 | arXiv preprint | **PASS** |
| 2 | `folio` | ✅ | ✅ (30+ authors) | ✅ 2024 | ✅ EMNLP 2024 | **PASS** |
| 3 | `manheim-goodhart-taxonomy` | ✅ | ✅ Manheim, Garrabrant | ⚠️ bib=2019, v1=2018, v3=2019 | arXiv preprint | **PASS** (year defensible) |
| 4 | `gao-reward-overoptimization` | ✅ | ✅ Gao, Schulman, Hilton | ✅ 2023 | ✅ ICML 2023 | **PASS** |
| 5 | `karwowski-goodhart-rl` | ✅ | ✅ all 6 authors | ✅ 2024 | ✅ ICLR 2024 | **PASS** |
| 6 | `demillo1978` | ✅ | ✅ DeMillo, Lipton, Sayward | ✅ 1978 | ✅ Computer | **FAIL** (pages 34-43→34-41) |
| 7 | `skalse-reward-hacking` | ✅ | ✅ all 4 authors | ✅ 2022 | ✅ NeurIPS 2022 | **PASS** |
| 8 | `lightman-verify-step` | ✅ | ✅ first 3 | ✅ 2024 | ✅ ICLR 2024 | **PASS** |
| 9 | `mellgren-prolog-grpo` | ✅ | **FAIL** (1 of 3 authors) | **FAIL** (2024→2025) | arXiv | **FAIL** |
| 10 | `logic-lm` | ✅ | ✅ Pan, Albalak, Wang, Wang | ✅ 2023 | ✅ Findings EMNLP 2023 | **PASS** |
| 11 | `linc` | ✅ | ✅ first 3 | ✅ 2023 | ✅ EMNLP 2023 | **PASS** |
| 12 | `satlm` | ✅ | ⚠️ "and others" (4 total) | ✅ 2023 | ✅ NeurIPS 2023 | **PASS** |
| 13 | `rubric-grpo` | ✅ | ✅ all 5 correct | **FAIL** (2025→2026) | arXiv | **FAIL** |
| 14 | `reward-hacking-survey` | ✅ | ✅ first 4 correct | ✅ 2026 | arXiv | **PASS** |
| 15 | `lorp` | ✅ | ⚠️ 4/5 confirmed, Lizhen Cui unverified | ✅ 2025 | ✅ KBS 2025 | **PASS** (pending Cui) |

### Previously-placeholder entries status

- **rubric-grpo**: Authors now correct. **Year still wrong** (2025→2026).
- **reward-hacking-survey**: Authors correct. Year correct (2026). Minor: `archiveprefix` casing.
- **lorp**: Authors likely correct (4/5 confirmed). Journal/year correct. Missing volume/pages.

---

## 4. Format Consistency

### 4.1 arXiv field encoding — two patterns used

**Pattern A** (`eprint` + `archivePrefix`) — 8 entries:
deepseekmath, logic-rl, mellgren-prolog-grpo, rubric-grpo, gao-effective-rl-reward, spurious-rewards, bondarenko-spec-gaming, manheim-goodhart-taxonomy, rlsf, reward-hacking-survey, + orphans

**Pattern B** (`note = {arXiv:NNNN.NNNNN}`) — 7 entries:
lightman-verify-step, skalse-reward-hacking, gao-reward-overoptimization, folio, qwen-prm-lessons, math-shepherd, kim-game-formalization (orphan), karwowski-goodhart-rl

**Recommendation**: Pick Pattern A and migrate all entries for consistency.

### 4.2 `archiveprefix` casing

`reward-hacking-survey` uses `archiveprefix` (lowercase) vs `archivePrefix` (camelCase) elsewhere. BibTeX is case-insensitive on field names, so harmless but visually inconsistent.

### 4.3 Venue names — CONSISTENT ✅

No inconsistencies found:
- NeurIPS: "Advances in Neural Information Processing Systems (NeurIPS)" throughout
- EMNLP: "Proceedings/Findings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)" throughout
- ICLR: "Proceedings of the International Conference on Learning Representations (ICLR)" throughout
- No NIPS/NeurIPS or EMNLP abbreviation conflicts

---

## 5. Action Items (Prioritized)

### P0 — Must fix before submission

| # | Item | Entry | Line |
|---|------|-------|------|
| 1 | Fix author: "Xian and others" → full list (first author: Tian Xie) | `logic-rl` | bib:16 |
| 2 | Add 2 missing co-authors + fix year 2024→2025 | `mellgren-prolog-grpo` | bib:26-30 |
| 3 | Fix year 2025→2026 | `rubric-grpo` | bib:68 |
| 4 | Fix pages 34--43 → 34--41 | `demillo1978` | bib:131 |

### P1 — Should fix for reviewer-readiness

| # | Item |
|---|------|
| 5 | List all 4 authors for `satlm` (Xi Ye, Qiaochu Chen, Isil Dillig, Greg Durrett) |
| 6 | Standardize arXiv fields: migrate `note` → `eprint`+`archivePrefix` for 7 entries |
| 7 | Fix `archiveprefix` → `archivePrefix` casing in `reward-hacking-survey` |
| 8 | Remove 10 orphan entries or cite them (priority: `kim-game-formalization`, `pan-reward-misspecification`) |
| 9 | Verify Lizhen Cui as co-author of `lorp` from ScienceDirect |

### P2 — Polish for camera-ready

| # | Item |
|---|------|
| 10 | Expand "and others" to full author list for ≤6-author papers (lightman-verify-step, linc, rlsf, qwen-prm-lessons, spurious-rewards) |
| 11 | Fill volume/pages for `lorp` (Knowledge-Based Systems) |
| 12 | Delete orphan `discussion.tex` from paper directory |
