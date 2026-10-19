# Reference Cross-Validation Report

**Date**: 2026-05-26
**Method**: 3 independent Workers each verified all 48 bib entries via WebSearch

## Results Summary

- **Total entries**: 48
- **Existence**: 48/48 real (0 fabricated)
- **Issues found**: 7 confirmed errors (all fixed)
- **VinePPO conflict**: Fix Worker incorrectly changed to ICML 2025 → reverted to NeurIPS 2024

## Fixed Issues

| # | bib key | Issue | Fix |
|---|---------|-------|-----|
| 1 | schulman2015trpo | Author order (Abbeel↔Moritz) | Corrected to Schulman, Levine, Moritz, Jordan, Abbeel |
| 2 | lightman2024lets | Author spelling (Yuri→Yura, Harrison→Harri) | Corrected |
| 3 | gradientcoupling2025 | Title v1→v4 | Updated to "Gradient Coupling: The Hidden Barrier..." |
| 4 | istar2025 | arXiv→ICLR 2026 | Changed to @inproceedings, year=2026 |
| 5 | wang2024mathshepherd | Venue name incomplete | Added "62nd Annual Meeting of" |
| 6-7 | kazemnejad2024vineppo | Fix Worker set ICML 2025 (wrong) | Reverted to NeurIPS 2024, title="Accurate Credit Assignment in RL for LLM Mathematical Reasoning" |

## VinePPO Conflict Resolution

- **3/3 Workers**: NeurIPS 2024
- **Fix Worker**: Changed to ICML 2025 (incorrect)
- **WebSearch verification**: Paper appears at both NeurIPS 2024 (neurips.cc/virtual/2024/98520) and ICML 2025 (icml.cc/virtual/2025/poster/45526)
- **Resolution**: NeurIPS 2024 is the original venue (bib key "2024"), title matches NeurIPS proceedings

## Pending (Director Decision)

1. turnppo2025: EACL 2026 Findings (3/3 agree)
2. ouyang2022instructgpt: "Jeffrey Wu"→"Jeff Wu" (2/3 agree)
3. 10+ unused bib entries: keep or remove?
