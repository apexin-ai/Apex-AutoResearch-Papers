## ARR Compliance Report

**Overall**: PASS

**Date**: 2026-05-15
**Paper**: Solver Trace Ablation Reveals Reward Hacking and Meta-Level Goodhart's Law in a GRPO-Trained Neurosymbolic Formalizer
**Total pages**: 19 (8 main body + 2 references + 1 limitations + 8 appendix)

### Checklist

- [x] **Anonymization — author field**: `\author{Anonymous ACL submission}` (main.tex:23)
- [x] **Anonymization — code/data URL**: Properly anonymized as `\url{[anonymized]}` (abstract.tex:9)
- [x] **Anonymization — no identity leaks in .tex**: No author names, institutional affiliations, GitHub URLs, or email addresses found in any .tex file
- [x] **Anonymization — no identity leaks in .bib**: references.bib contains only third-party citations; no self-citations that could reveal authorship
- [x] **Anonymization — no acknowledgments**: No acknowledgments section present
- [x] **Format — acl.sty with [review]**: `\usepackage[review]{acl}` (main.tex:2) — line numbers enabled
- [x] **Format — 11pt**: `\documentclass[11pt]{article}` (main.tex:1)
- [x] **Format — page limit**: Main body (Sections 1–5) fits within 8 pages (ends on page 8)
- [x] **Limitations section**: Present as Section 6 (limitations.tex), covers model scope, ISR semantics, seed count, solver dependency, data scale
- [x] **Citation completeness**: Zero undefined citation warnings in main.log
- [x] **Label completeness**: Zero undefined label/reference warnings in main.log
- [x] **Appendix placement**: Appendix follows references and limitations (main.tex:39–40), correct order
- [x] **Appendix cross-references**: All `\ref{}` in appendix.tex point to valid labels in main body and appendix
- [x] **Bibliography compiled**: main.bbl present, no BibTeX errors

### Notes

- **Ethics statement**: Not included in-paper. Not required by ARR (optional), but the **Responsible NLP Research checklist** must be filled on the OpenReview submission form. This paper uses only publicly available data (FOLIO) and involves no human subjects — no ethical red flags.
- **Overfull/underfull boxes**: 110 warnings in main.log. Cosmetic only; not a submission blocker, but worth reviewing for camera-ready.
- **Submission form reminders**: ARR requires (1) Responsible NLP Research checklist, (2) optional reproducibility info, (3) optional supplementary materials upload — all handled on OpenReview, not in the PDF.
