# ops reference audit

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_reference-audit_20260523T030754_result.json`
- **Structured JSON:** [`1f382321869882b153ae.json`](../../sessions/1f/1f382321869882b153ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Reference Audit:
- Total bib entries: 47 (header comment says 33, stale)

- Missing fields:
  - sinharay2017: missing volume, number, pages (journal article, has doi only)
  - martinezplumed2019: missing volume, pages (journal article, has doi only)
  - chang2024survey: missing volume, pages (journal article, has doi only)
  - golchin2024quiz: missing volume, number, pages, doi (TACL article)
  - rafailov2023: missing pages (NeurIPS inproceedings)

- Undefined citations (cited in .tex but NOT in bib):
  - lord1980        (background.tex:5)
  - birnbaum1968    (background.tex:6)
  - barton1981      (background.tex:6)
  - zellers2019hellaswag  (sec_setup.tex:4)
  - cobbe2021gsm8k        (sec_setup.tex:4)
  - chen2021humaneval     (sec_setup.tex:4)

- Unused bib entries (in bib but NOT cited):
  - hedges1981
  - ouyang2022
  - rafailov2023

- Survey 2502.14425: NOT IN bib, NOT CITED
- Survey 2502.17521: NOT IN bib, NOT CITED

- Duplicates: None (sinharay2017 and sinharay2017personfit are different papers)

- Format issues:
  - Stale header comment ("33 entries" vs actual 47)
  - 5 journal articles missing volume/pages (listed above)
  - Conference name style generally consistent (full name + abbreviation)
```

**Critical**: 6 undefined citation keys will produce `?` in compiled PDF — `lord1980`, `birnbaum1968`, `barton1981`, `zellers2019hellaswag`, `cobbe2021gsm8k`, `chen2021humaneval` all need bib entries added.

---
