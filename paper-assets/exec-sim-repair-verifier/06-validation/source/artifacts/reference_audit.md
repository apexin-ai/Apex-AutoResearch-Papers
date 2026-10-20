# Reference Audit Report

**Date**: 2026-05-15
**Paper**: exec-sim-repair-verifier (EMNLP 2026 ARR May submission)
**Total bib entries**: 26
**Total unique citation keys in .tex**: 26

---

## 1. \cite{} Completeness

All 26 citation keys found in .tex files have corresponding entries in `references.bib`.

| Citation Key | Files Used | In Bib |
|---|---|---|
| snell2024scaling | introduction, related_work | ✓ |
| meta2025cwm | introduction, method, related_work, experiments | ✓ |
| maimon2026selfexecution | introduction, related_work | ✓ |
| shum2025swerm | introduction, related_work | ✓ |
| yang2024sweagent | introduction, related_work | ✓ |
| xia2024agentless | introduction, related_work | ✓ |
| jimenez2024swebench | introduction, related_work, experiments | ✓ |
| chowdhury2024swebenchverified | introduction, related_work, experiments | ✓ |
| liu2024codemind | related_work | ✓ |
| lee2026solidcoder | related_work | ✓ |
| abdollahi2025demystifying | related_work | ✓ |
| xu2025patchreasoner | related_work | ✓ |
| li2025sstar | related_work | ✓ |
| chen2025vgsearch | related_work | ✓ |
| yang2025aprsurvey | related_work | ✓ |
| raffel2020t5 | related_work | ✓ |
| lewis2020bart | related_work | ✓ |
| rajpurkar2016squad | related_work | ✓ |
| chen2021humaneval | experiments | ✓ |
| austin2021mbpp | experiments | ✓ |
| qwen2025qwen3 | experiments | ✓ |
| hu2022lora | experiments | ✓ |
| dettmers2024qlora | experiments | ✓ |
| davison1997bootstrap | experiments | ✓ |
| schuirmann1987tost | experiments | ✓ |
| shrout1979icc | experiments | ✓ |

**Result**: ✓ No missing bib entries. No compilation errors expected.

---

## 2. Bib Entry Completeness

All 26 entries checked for required fields (title, author, year, venue).

| Key | title | author | year | venue | Placeholders |
|---|---|---|---|---|---|
| maimon2026selfexecution | ✓ | ✓ | ✓ | journal (arXiv) | None |
| meta2025cwm | ✓ | ✓ | ✓ | journal (arXiv) | None |
| liu2024codemind | ✓ | ✓ (et al.) | ✓ | journal (arXiv) | None |
| abdollahi2025demystifying | ✓ | ✓ | ✓ | journal (arXiv) | None |
| lee2026solidcoder | ✓ | ✓ | ✓ | journal (arXiv) | None |
| shum2025swerm | ✓ | ✓ | ✓ | journal (arXiv) | None |
| xu2025patchreasoner | ✓ | ✓ | ✓ | journal (arXiv) | None |
| chen2025vgsearch | ✓ | ✓ | ✓ | journal (arXiv) | None |
| snell2024scaling | ✓ | ✓ | ✓ | journal (arXiv) | None |
| li2025sstar | ✓ | ✓ | ✓ | booktitle (Findings of EMNLP) | None |
| jimenez2024swebench | ✓ | ✓ | ✓ | booktitle (ICLR) | None |
| chowdhury2024swebenchverified | ✓ | ✓ (et al.) | ✓ | institution (OpenAI) | None |
| yang2024sweagent | ✓ | ✓ | ✓ | booktitle (NeurIPS) | None |
| xia2024agentless | ✓ | ✓ | ✓ | journal (arXiv) | None |
| yang2025aprsurvey | ✓ | ✓ | ✓ | journal (arXiv) | None |
| qwen2025qwen3 | ✓ | ✓ (et al.) | ✓ | journal (arXiv) | None |
| chen2021humaneval | ✓ | ✓ (et al.) | ✓ | journal (arXiv) | None |
| austin2021mbpp | ✓ | ✓ (et al.) | ✓ | journal (arXiv) | None |
| hu2022lora | ✓ | ✓ | ✓ | booktitle (ICLR) | None |
| dettmers2024qlora | ✓ | ✓ | ✓ | booktitle (NeurIPS) | None |
| rajpurkar2016squad | ✓ | ✓ | ✓ | booktitle (EMNLP) | None |
| lewis2020bart | ✓ | ✓ | ✓ | booktitle (ACL) | None |
| raffel2020t5 | ✓ | ✓ | ✓ | journal (JMLR) | None |
| schuirmann1987tost | ✓ | ✓ | ✓ | journal | None |
| davison1997bootstrap | ✓ | ✓ | ✓ | publisher (CUP) | None |
| shrout1979icc | ✓ | ✓ | ✓ | journal + doi | None |

**Result**: ✓ All entries structurally complete. No placeholders (TODO/TBD).

---

## 3. Citation Authenticity Verification (WebSearch)

All core citations verified against arXiv, conference proceedings, and publisher websites.

| Key | Claimed | Verified | Status |
|---|---|---|---|
| meta2025cwm | arXiv 2510.02387, Meta AI | ✓ Confirmed on arXiv and ai.meta.com | ✓ |
| shum2025swerm | arXiv 2512.21919 | ✓ Confirmed on arXiv, OpenReview | ✓ |
| jimenez2024swebench | ICLR 2024 | ✓ Confirmed: ICLR 2024 Oral | ✓ |
| chowdhury2024swebenchverified | OpenAI techreport 2024 | ✓ Confirmed on openai.com | ✓ |
| qwen2025qwen3 | arXiv 2505.09388 | ✓ Confirmed on arXiv | ✓ |
| hu2022lora | ICLR 2022 | ✓ Confirmed: ICLR 2022 Poster | ✓ |
| maimon2026selfexecution | arXiv 2604.03253 | ✓ Confirmed on arXiv (Apr 2026) | ✓ |
| yang2024sweagent | NeurIPS 2024 | ✓ Confirmed: NeurIPS 2024 Poster | ✓ |
| xia2024agentless | arXiv 2407.01489 | ✓ Confirmed; also published at FSE 2025 | ⚠ See Issue #3 |
| dettmers2024qlora | NeurIPS 2023 | ✓ Confirmed: NeurIPS 2023 Poster | ⚠ See Issue #1 |
| lee2026solidcoder | arXiv 2604.19825 | ✓ Confirmed on arXiv (Apr 2026) | ✓ |
| snell2024scaling | arXiv 2408.03314 | ✓ Confirmed; also published at ICLR 2025 Oral | ⚠ See Issue #2 |
| li2025sstar | Findings of EMNLP 2025 | ✓ Confirmed in ACL Anthology | ✓ |
| chen2025vgsearch | arXiv 2505.11730 | ✓ Confirmed; also accepted at NeurIPS 2025 | ⚠ See Issue #4 |
| xu2025patchreasoner | arXiv 2510.22775 | ✓ Confirmed on arXiv, OpenReview | ✓ |
| abdollahi2025demystifying | arXiv 2512.00215 | ✓ Confirmed on arXiv (Nov 2025) | ✓ |
| liu2024codemind | arXiv 2402.09664 | ✓ Confirmed on arXiv | ✓ |
| yang2025aprsurvey | arXiv 2506.23749 | ✓ Confirmed on arXiv | ✓ |
| rajpurkar2016squad | EMNLP 2016 | ✓ Classic, well-known | ✓ |
| lewis2020bart | ACL 2020 | ✓ Classic, well-known | ✓ |
| raffel2020t5 | JMLR 2020 | ✓ Classic, well-known | ✓ |
| chen2021humaneval | arXiv 2107.03374 | ✓ Classic, well-known | ✓ |
| austin2021mbpp | arXiv 2108.07732 | ✓ Classic, well-known | ✓ |
| davison1997bootstrap | CUP 1997 | ✓ Classic textbook | ✓ |
| schuirmann1987tost | J Pharmacokin 1987 | ✓ Classic paper | ✓ |
| shrout1979icc | Psychol Bull 1979 | ✓ Classic paper | ✓ |

**Result**: ✓ All 26 citations are real. Zero hallucinated references.

---

## 4. Orphan Entries

No bib entries are orphaned — all 26 entries are cited in at least one .tex file.

**Result**: ✓ Clean.

---

## 5. Format Consistency

### Author name format
✓ All entries use "Last, First" format consistently (e.g., `Maimon, Gallil and Yoran, Ori`).

### Year format
✓ All years are 4-digit integers, correctly formatted.

### Venue naming
✓ Conference proceedings use consistent abbreviations: ICLR, NeurIPS, EMNLP, ACL, JMLR.
✓ arXiv preprints use consistent format: `arXiv preprint arXiv:XXXX.XXXXX`.
✓ Full journal names used for non-CS venues (Journal of Pharmacokinetics, Psychological Bulletin).

---

## 6. Issues Found

### Issue #1 — `dettmers2024qlora`: Key/year mismatch [severity: info]

- **Key**: `dettmers2024qlora` (suggests year 2024)
- **Year field**: `year={2023}` (correct — NeurIPS 2023)
- **Impact**: Rendered output is correct (shows 2023). Only the internal key naming is inconsistent with the convention used by other entries where key year matches the year field.
- **Recommendation**: Rename key to `dettmers2023qlora` for consistency, or leave as-is (cosmetic only).

### Issue #2 — `snell2024scaling`: Venue outdated [severity: warning]

- **Current**: `@article`, `journal={arXiv preprint arXiv:2408.03314}`, `year={2024}`
- **Actual**: Published at **ICLR 2025** (Oral presentation). Confirmed via iclr.cc proceedings.
- **Recommendation**: Update to:
  ```bibtex
  @inproceedings{snell2025scaling,
    title={Scaling {LLM} Test-Time Compute Optimally can be More Effective than Scaling Parameters},
    author={Snell, Charlie and Lee, Jaehoon and Xu, Kelvin and Kumar, Aviral},
    booktitle={ICLR},
    year={2025}
  }
  ```
  Then update all `\cite{snell2024scaling}` → `\cite{snell2025scaling}` in .tex files.

### Issue #3 — `xia2024agentless`: Venue outdated [severity: warning]

- **Current**: `@article`, `journal={arXiv preprint arXiv:2407.01489}`, `year={2024}`
- **Actual**: Published at **FSE 2025** (ACM SIGSOFT Distinguished Paper). Confirmed via ACM DL (doi:10.1145/3715754).
- **Recommendation**: Update to:
  ```bibtex
  @inproceedings{xia2025agentless,
    title={Agentless: Demystifying {LLM}-based Software Engineering Agents},
    author={Xia, Chunqiu Steven and Deng, Yinlin and Dunn, Soren and Zhang, Lingming},
    booktitle={FSE},
    year={2025}
  }
  ```
  Then update all `\cite{xia2024agentless}` → `\cite{xia2025agentless}` in .tex files.

### Issue #4 — `chen2025vgsearch`: Venue outdated [severity: warning]

- **Current**: `@article`, `journal={arXiv preprint arXiv:2505.11730}`, `year={2025}`
- **Actual**: Accepted at **NeurIPS 2025**. Confirmed via neurips.cc virtual poster page.
- **Recommendation**: Update to:
  ```bibtex
  @inproceedings{chen2025vgsearch,
    title={Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling},
    author={Chen, Hao Mark and Lu, Guanxi and Okoshi, Yasuyuki and Mo, Zhiwen and Motomura, Masato and Fan, Hongxiang},
    booktitle={NeurIPS},
    year={2025}
  }
  ```

### Issue #5 — `meta2025cwm`: Author field is team name [severity: info]

- **Current**: `author={{Meta AI}}`
- **Actual**: The paper has 50+ individual authors from Meta FAIR (Copet, Carbonneaux, Cohen, Gehring, Kahn, Kossen, Kreuk, ..., Synnaeve).
- **Impact**: Renders as "Meta AI (2025)" which is acceptable but less standard than listing first few authors.
- **Recommendation**: Consider `author={Copet, Jade and Carbonneaux, Quentin and Cohen, Gal and others}` for more standard attribution. Alternatively, keep `{Meta AI}` if the team prefers corporate authorship (check official citation).

---

## 7. Summary

| Check | Result |
|---|---|
| All \cite keys have bib entries | ✓ 26/26 |
| All bib entries have required fields | ✓ 26/26 |
| No placeholder content | ✓ |
| No hallucinated citations | ✓ 0/26 |
| No orphan bib entries | ✓ 0 orphans |
| Author name format consistent | ✓ "Last, First" throughout |
| Year format correct | ✓ |
| Venue naming consistent | ✓ |
| **Venue updates needed** | **⚠ 3 entries** (snell, xia, chen) |
| **Key naming inconsistency** | **ℹ 1 entry** (dettmers) |
| **Author field simplification** | **ℹ 1 entry** (meta) |

**Overall**: The bibliography is clean with no critical issues. Three entries should be updated from arXiv preprint to their published conference venues before submission (Issues #2-#4). One key naming inconsistency is cosmetic only (Issue #1).
