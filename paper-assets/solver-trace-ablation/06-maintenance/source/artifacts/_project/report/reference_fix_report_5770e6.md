# Reference Fix Report

Date: 2026-05-14
Target: `paper/references.bib` + `paper/discussion.tex`

## P0 Fixes (key errors)

| # | Key | Field | Before | After |
|---|-----|-------|--------|-------|
| 1 | `logic-rl` | author | `Xian and others` | `Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo` |
| 2 | `mellgren-prolog-grpo` | author | `Niklas Mellgren` | `Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke Poech` |
| 2 | `mellgren-prolog-grpo` | year | `2024` | `2025` |
| 3 | `rubric-grpo` | year | `2025` | `2026` |
| 4 | `demillo1978` | pages | `34--43` | `34--41` |

## P1 Fixes

| # | Key | Field | Before | After |
|---|-----|-------|--------|-------|
| 5 | `satlm` | author | `Xi Ye and others` | `Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett` |

## Orphan Audit

Verified all 10 keys flagged as potential orphans with `grep`:

| Key | Cited in `related_work.tex`? | Action |
|-----|------------------------------|--------|
| `kim-game-formalization` | yes (line 18) | keep |
| `pan-reward-misspecification` | yes (line 17) | keep |
| `prof-process-outcome` | yes (line 13) | keep |
| `progrs-outcome-conditioned` | yes (line 13) | keep |
| `llmorpheus` | yes (line 24) | keep |
| `thought-like-pro` | yes (line 8) | keep |
| `lorp` | yes (line 6) | keep |
| `fover-pei2025` | yes (line 6) | keep |
| `offutt-coupling` | yes (line 23) | keep |
| `just-mutants-real-faults` | yes (line 23) | keep |

No bib entries deleted, no new citations needed. Audit assumption that several were orphans was incorrect.

## File Cleanup

- Deleted `paper/discussion.tex` (not included from `main.tex`; merged content lives in `conclusion.tex`).

## Compile Verification

```
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

Results:
- Exit codes: all 0
- `pdfinfo main.pdf | grep Pages` -> **14 pages**
- `main.log` errors (`^!`): **0**
- `main.log` real warnings: **0** (the only `warning` substring hit is the package name `infwarerr`)
- `main.blg`: no `"I didn't find a database entry"` errors; 33 entries used
