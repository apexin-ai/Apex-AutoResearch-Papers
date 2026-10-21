# Citation Fix Report (Reviewer Issues)

## Critical 1: laban2025lost
- **Reviewer claim**: arXiv 2025 preprint should be ICLR 2026 (Oral)
- **WebSearch result**: Confirmed. ICLR 2026 Oral, also won ICLR 2026 Best Paper Award. OpenReview: https://openreview.net/forum?id=VKGTGGcwl6
- **Verdict**: Confirmed
- **Action taken**: `@article` → `@inproceedings`, removed `journal`, added `booktitle = {International Conference on Learning Representations}`, year 2025 → 2026

## Critical 2: raposo2024mixture
- **Reviewer claim**: Should be ICLR 2025, not ICML 2024
- **WebSearch result**: Confirmed. Published as conference paper at ICLR 2025. PDF header on OpenReview and proceedings.iclr.cc both state "Published as a conference paper at ICLR 2025".
- **Verdict**: Confirmed
- **Action taken**: `booktitle` changed from `International Conference on Machine Learning` to `International Conference on Learning Representations`, year 2024 → 2025

## Critical 3: he2019exposure
- **Reviewer claim**: arXiv 2019 preprint is the same paper as EMNLP 2021 "Exposure Bias versus Self-Recovery"
- **WebSearch result**: Confirmed. Same arXiv ID (1905.10617), same authors (He, Zhang, Zhou, Glass). The paper was revised and published at EMNLP 2021 with updated title. ACL Anthology: https://aclanthology.org/2021.emnlp-main.415/
- **Verdict**: Confirmed (same paper, title changed between preprint and publication)
- **Action taken**: `@article` → `@inproceedings`, title updated to "Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?", removed `journal`, added `booktitle = {Conference on Empirical Methods in Natural Language Processing}`, year 2019 → 2021. Cite key `he2019exposure` kept unchanged to avoid breaking \cite references in 8 tex files.

## Minor 1: bachlechner2021rezero
- **Reviewer claim**: "Henry Mao" should be "Huanru Henry Mao"; "Gary Cottrell" should be "Garrison W. Cottrell"
- **WebSearch result**: Confirmed. arXiv page and UAI proceedings (proceedings.mlr.press/v161/bachlechner21a.html) both list "Huanru Henry Mao" and "Garrison W. Cottrell".
- **Verdict**: Confirmed
- **Action taken**: `Mao, Henry` → `Mao, Huanru Henry`; `Cottrell, Gary` → `Cottrell, Garrison W.`

## Minor 2: brunner2020identifiability
- **Reviewer claim**: Last author should be "Roger Wattenhofer", not "Andreas Krause"
- **WebSearch result**: Confirmed. arXiv, Semantic Scholar, Google Research, and OpenReview all list authors as: Gino Brunner, Yang Liu, Damian Pascual, Oliver Richter, Massimiliano Ciaramita, Roger Wattenhofer.
- **Verdict**: Confirmed
- **Action taken**: `Krause, Andreas` → `Wattenhofer, Roger`

## Compile result: PASS
- pdflatex + bibtex + pdflatex x2: all successful (34 pages, no errors)

## bibtex warnings: None
- `warning$ -- 0` in main.blg

## Files modified
- `paper/references.bib`
- `docs/paper/references.bib`
- Both files verified identical after changes.
