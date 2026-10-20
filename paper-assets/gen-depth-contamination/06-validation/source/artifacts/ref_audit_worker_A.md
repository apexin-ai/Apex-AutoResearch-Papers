# Reference Audit Report — Worker A

Audited: 2026-05-26
File: `docs/paper/references.bib` (37 entries)

---

## Per-Entry Verification

```
[kirchenbauer2023watermark] ✓
[drayson2025]               ✓
[schaeffer2025position]     ✓ (arXiv preprint; under review at NeurIPS 2025 per OpenReview, not yet accepted — listing as arXiv is currently correct)
[kazdan2025collapse]        ✓ (ICML 2025 poster confirmed)
[mitchell2023detectgpt]     ✓
[basani2026diveye]          ✓ (TMLR 2026 confirmed)
[zawalski2026codec]         ✓ (ICLR 2026 confirmed)
[zhang2024minkpp]           ✓ (ICLR 2025 Spotlight; year=2025 in bib is correct)
[shumailov2024collapse]     ✓ (Nature 631, pp. 755–759, 2024)
[alemohammad2024selfconsuming] ✓ (ICLR 2024)
[dohmatob2024model]         ✓ (ICML 2024)
[xie2023dsir]               ✓ (NeurIPS 2023)
[tirumala2023d4]            ✓ (NeurIPS 2023)
[xie2023doremi]             ✓ (NeurIPS 2023)
[hans2024binoculars]        ✗ | Title truncated: missing subtitle
[alain2017understanding]    ✓ (ICLR 2017 Workshop)
[belinkov2022probing]       ✓ (Computational Linguistics 48(1), 207–219, 2022)
[bao2024fast]               ✓ (ICLR 2024)
[frank2001ordinal]          ✓ (ECML 2001, pp. 145–156)
[cheng2025beyond]           ✓ (WWW 2025)
[mehta2025beyond]           ✓ (arXiv 2511.17602)
[sun2025aigt]               ✓ (ACL 2025)
[spennemann2025quantifying] ✓ (arXiv 2504.08755)
[dohmatob2025strong]        ✓ (ICLR 2025)
[wang2024semeval]           ✓ (SemEval 2024)
[gerstgrasser2024model]     ✓ (COLM 2024)
[guo2024curious]            ✓ (Findings of NAACL 2024)
[briesch2023selfconsuming]  ✓ (arXiv preprint)
[padmakumar2024writing]     ✓ (ICLR 2024)
[krishna2023paraphrasing]   ✓ (NeurIPS 2023)
[sadasivan2023detect]       ✗ | Venue outdated: published in TMLR (March 2025), bib still lists as arXiv preprint 2023
[hao2025rewrite]            ✓ (ACL 2025)
[wang2025unveiling]         ✓ (ACL 2025, pp. 12740–12755)
[fu2025theoretical]         ✓ (ICLR 2025)
[verma2024ghostbuster]      ✓ (NAACL 2024, pp. 1702–1717)
[dugan2024raid]             ✓ (ACL 2024, pp. 12463–12492)
[liang2023gpt]              ✗ | Citation context error (see below)
```

---

## Error Details

### 1. [hans2024binoculars] ✗ — Title truncated

**What's wrong:** Bib title is `Spotting {LLMs} With Binoculars`. The official PMLR proceedings title is **"Spotting LLMs With Binoculars: Zero-Shot Detection of Machine-Generated Text"**.

**Fix:**
```bibtex
title={Spotting {LLMs} With Binoculars: Zero-Shot Detection of Machine-Generated Text},
```

### 2. [sadasivan2023detect] ✗ — Venue outdated

**What's wrong:** Bib lists as `@article` / `journal={arXiv preprint arXiv:2303.11156}` / `year={2023}`. The paper was accepted at **TMLR** (Transactions on Machine Learning Research) in **March 2025** (confirmed via @TmlrPub announcement, OpenReview forum id OOgsAZdFOt). The published version has a slightly extended title.

**Fix:**
```bibtex
@article{sadasivan2023detect,
  title={Can {AI}-Generated Text be Reliably Detected?},
  author={Sadasivan, Vinu Sankar and Kumar, Aounon and Balasubramanian, Sriram and Wang, Wenxiao and Feizi, Soheil},
  journal={Transactions on Machine Learning Research},
  year={2025},
  url={https://openreview.net/forum?id=OOgsAZdFOt}
}
```

### 3. [liang2023gpt] ✗ — Citation context error (wrong cite)

**What's wrong:** In `related_work.tex:11`:
```latex
benchmarks such as RAID~\cite{dugan2024raid} and GPTZero~\cite{liang2023gpt} evaluate robustness at scale.
```
`liang2023gpt` is **"GPT detectors are biased against non-native English writers"** (Liang et al., Patterns 2023) — a study about bias in GPT detectors. It is **not** the GPTZero tool/benchmark. GPTZero is a commercial product by Edward Tian. The sentence implies `liang2023gpt` IS the GPTZero reference, which is a misattribution.

**Fix options:**
- (a) Remove the GPTZero mention or cite it properly (GPTZero has no peer-reviewed reference paper).
- (b) Rephrase to correctly use liang2023gpt: e.g., "...and bias analyses~\cite{liang2023gpt} probe detector fairness."

---

## Minor Issues (not counted as errors)

- **[guo2024curious]** Author `Chloe` missing accent → should be `Chlo{\'e}` (Chloé Clavel)
- **[dohmatob2024model]** Author `Francois` missing cedilla → should be `Fran\c{c}ois` (François Charton)

---

## Summary

| Metric | Count |
|--------|-------|
| Total entries | 37 |
| ✓ Correct | 34 |
| ✗ Errors | 3 |

**Errors:** `hans2024binoculars` (truncated title), `sadasivan2023detect` (venue outdated: arXiv → TMLR 2025), `liang2023gpt` (citation context: misattributed as GPTZero)
