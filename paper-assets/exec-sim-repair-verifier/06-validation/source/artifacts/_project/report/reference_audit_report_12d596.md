# Reference Audit Report

**Paper**: Classification Succeeds Where Generation Stalls: Reformulating Execution Simulation for Code Repair Verification
**Date**: 2026-05-16
**Target**: EMNLP 2026 ARR (DDL 5/25)

---

## Summary

| Metric | Count |
|--------|-------|
| Total bib entries | 28 |
| Unique cited keys | 28 |
| Total \cite commands | 56 |
| Orphan bib entries | 0 |
| Missing bib entries | 0 |
| OpenAlex verified | 21 |
| OpenAlex not_found (false negatives) | 4 |
| OpenAlex mismatch (API quirks) | 3 |
| WebSearch verified (of not_found) | 4/4 |
| Hallucinated citations | **0** |

---

## Checks Passed

- **Citation existence**: All 28 `\cite{}` keys have corresponding bib entries.
- **Orphan entries**: Zero. Every bib entry is cited at least once.
- **Citation authenticity**: All 28 references verified as real, published papers via OpenAlex + WebSearch.
- **Venue format consistency**: All conference booktitles use consistent abbreviations (ICLR, NeurIPS, ICML, ACL, EMNLP, FSE).
- **Year correctness**: All year fields match actual publication/preprint years.
- **Required fields**: All entries have title, author, year, and venue (journal/booktitle/publisher).

---

## Issues Found and Fixed

### [Fixed] `liu2024codemind` -- Author list severely truncated

**Severity**: Warning
**Before**: `author={Liu, Changshu and others}` (1 named author)
**After**: `author={Liu, Changshu and Zhang, Shizhuo Dylan and Ibrahimzada, Ali Reza and Jabbarvand, Reyhaneh}` (complete 4-author list)
**Reason**: Having only 1 named author before "and others" is unusually aggressive truncation and may draw reviewer attention.

### [Fixed] `chowdhury2024swebenchverified` -- Wrong entry type, truncated authors, missing URL

**Severity**: Warning
**Changes**:
1. Type: `@techreport` -> `@misc` (matches official citation from swebench.com/citations.html)
2. Title: "SWE-bench Verified" -> "Introducing SWE-bench Verified" (matches official title)
3. Authors: Expanded from 3 to full 16-author list per official citation
4. Added `url` field pointing to the OpenAI blog post
5. Removed `institution` field (not standard for @misc)

---

## Issues Noted (Not Auto-Fixed)

### [Info] Citation key-year mismatches (cosmetic)

Three bib keys use a year that differs from the `year` field. This does not affect rendered output but is inconsistent:

| Key | Year in key | Year field | Reason |
|-----|-------------|------------|--------|
| `snell2024scaling` | 2024 | 2025 | arXiv 2024, published ICLR 2025 |
| `xia2024agentless` | 2024 | 2025 | arXiv 2024, published FSE 2025 |
| `dettmers2024qlora` | 2024 | 2023 | Published NeurIPS 2023 |

**Recommendation**: No action needed; keys are internal identifiers. Only fix if style guide requires key-year alignment.

### [Info] `liu2024codemind` -- Title updated in newer arXiv versions

The bib uses the v1-v4 title: "CodeMind: A Framework to Challenge Large Language Models for Code Reasoning". Newer versions (v5+, Apr 2026) use: "CodeMind: Evaluating Large Language Models for Code Reasoning". The current bib title is valid (matches the originally published version). No change required.

### [Info] arXiv papers not yet published at conferences

The following entries are arXiv preprints. None appear to have been accepted at conferences as of 2026-05-16:

- `maimon2026selfexecution` (arXiv:2604.03253, Apr 2026) -- very recent
- `meta2025cwm` (arXiv:2510.02387, Oct 2025)
- `liu2024codemind` (arXiv:2402.09664, Feb 2024)
- `abdollahi2025demystifying` (arXiv:2512.00215, Dec 2025)
- `lee2026solidcoder` (arXiv:2604.19825, Apr 2026) -- very recent
- `shum2025swerm` (arXiv:2512.21919, Dec 2025)
- `xu2025patchreasoner` (arXiv:2510.22775, Oct 2025)
- `yang2025aprsurvey` (arXiv:2506.23749, Jun 2025) -- survey
- `qwen2025qwen3` (arXiv:2505.09388, May 2025) -- tech report
- `chen2021humaneval` (arXiv:2107.03374, Jul 2021) -- OpenAI, never published at venue
- `austin2021mbpp` (arXiv:2108.07732, Aug 2021) -- Google, never published at venue

**Recommendation**: Check `meta2025cwm` and `xu2025patchreasoner` (Oct 2025) closer to submission -- they may have been accepted at ICLR/ICML 2026 by now. If so, update entry type and venue.

### [Info] OpenAlex mismatch details (all false positives)

These 3 mismatches are OpenAlex API quirks, not real errors:

| Key | Mismatch | Explanation |
|-----|----------|-------------|
| `abdollahi2025demystifying` | author: abdollahi vs abdollahi (dotless i) | Unicode normalization difference |
| `snell2024scaling` | author: snell vs charlie | API returned first name instead of last |
| `jimenez2024swebench` | author: jimenez vs jimenez-gomez | Hyphenated surname variant |

No action needed.

---

## Verification Details (Key References)

| # | Key | Method | Status | Notes |
|---|-----|--------|--------|-------|
| 1 | `meta2025cwm` | OpenAlex + WebSearch | Verified | Title, authors, year, arXiv ID all match |
| 2 | `maimon2026selfexecution` | OpenAlex + WebSearch | Verified | Confirmed arXiv:2604.03253, Apr 2026 |
| 3 | `qwen2025qwen3` | OpenAlex + WebSearch | Verified | arXiv:2505.09388, Qwen Team |
| 4 | `hu2022lora` | OpenAlex | Verified | ICLR 2022 |
| 5 | `schuirmann1987tost` | OpenAlex | Verified | J Pharmacokinetics 1987 |
| 6 | `jimenez2024swebench` | OpenAlex + WebSearch | Verified | ICLR 2024 |
| 7 | `chowdhury2024swebenchverified` | WebSearch | Verified | OpenAI blog, Aug 2024 |
| 8 | `lee2026solidcoder` | OpenAlex + WebSearch | Verified | arXiv:2604.19825, Apr 2026 |
| 9 | `shum2025swerm` | OpenAlex | Verified | arXiv:2512.21919 |
| 10 | `xu2025patchreasoner` | WebSearch | Verified | arXiv:2510.22775, confirmed on arXiv + OpenReview |
| 11 | `li2025sstar` | WebSearch | Verified | Findings of EMNLP 2025, ACL Anthology confirmed |
| 12 | `liu2024codemind` | WebSearch | Verified | arXiv:2402.09664, 4 authors from UIUC |

---

## Final Status

**Ready for submission.** No critical issues. Two warning-level issues have been fixed (author list expansion and entry type correction). Remaining items are informational.
