# Reference Audit Report

**Date**: 2026-05-16
**Paper**: Exception Events Are All You Need: Cross-Model Fault Detection for Verdict Prediction
**Bib file**: `docs/paper/references.bib`

## Summary

| Metric | Count |
|--------|-------|
| Total bib entries | 28 |
| Total \cite{} keys in tex | 28 |
| Missing (cited but not in bib) | 0 |
| Orphan (in bib but not cited) | 0 |
| **PASS** (verified correct) | 18 |
| **WARNING** (minor issues, fixed) | 8 |
| **FAIL** (critical errors, fixed) | 2 |

## Critical Errors (FAIL) — Fixed

### 1. `ferrando2025execute` — Fabricated authors

- **Title**: Correct — "What I Cannot Execute, I Do Not Understand: Training and Evaluating LLMs on Program Execution Traces"
- **arXiv**: 2503.05703 — correct
- **Problem**: Authors listed as "Lorenzo Ferrando, Nicola Ferraro, and others" — **completely fabricated**. No such authors exist on this paper.
- **Actual authors**: Jordi Armengol-Estape, Quentin Carbonneaux, Tianjun Zhang, Aram H. Markosyan, Volker Seeker, Chris Cummins, Melanie Kambadur, Michael F.P. O'Boyle, Sida Wang, Gabriel Synnaeve, Hugh Leather
- **Fix applied**: Replaced entire author list.
- **Citation context check**: Related work describes this paper as comparing "regular, compact, and dynamic scratchpad strategies" — consistent with actual paper content. No 张冠李戴.

### 2. `appt2024` — Fabricated authors + wrong issue number

- **Title**: Correct — "APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models"
- **Problem**: Authors listed as "Yuze He, Yun Lin, Xiang Gao, Chengyun Zuo, Shuqing Li, Xinyu Wang, Jin Song Dong" — **completely wrong**. Also `number={5}` should be `number={3}`.
- **Actual authors**: Quanjun Zhang, Chunrong Fang, Weisong Sun, Yan Liu, Tieke He, Xiaodong Hao, Zhenyu Chen
- **Fix applied**: Replaced author list; changed number from 5 to 3.
- **Citation context check**: Related work describes "fine-tuned pre-trained models with BERT+LSTM achieving 79.7% accuracy on Defects4J patches" — consistent with actual paper content.

## Warnings — Fixed

### 3. `eguchi2025etcot` — Wrong workshop name

- **Problem**: Venue listed as "ICML 2025 Workshop on Principles of Reasoning and Learning (PRAL)" — the expanded name is wrong.
- **Actual**: "ICML 2025 Workshop on Programmatic Representations for Agent Learning (PRAL)"
- **Fix applied**: Corrected workshop name.

### 4. `qwen2025coder` — Wrong year

- **Problem**: Year listed as 2025, but arXiv submission was September 2024 (ID: 2409.12186).
- **Fix applied**: Changed year to 2024. Bib key kept as `qwen2025coder` to avoid breaking tex references.

### 5. `gu2024cruxeval` — Author name discrepancies

- **Problem**: "Hugh James Leather" should be "Hugh Leather" (no middle name in proceedings); "Sida Wang" should be "Sida I. Wang" (middle initial).
- **Fix applied**: Corrected both names.

### 6. `zhou2024llm4patch` — Fabricated title prefix + incomplete authors

- **Problem**: Title had "LLM4PatchCorrect:" prefix — not part of the actual paper title. Authors listed as "Xin Zhou and others" (incomplete).
- **Actual title**: "Leveraging Large Language Model for Automatic Patch Correctness Assessment"
- **Fix applied**: Removed prefix; expanded full 9-author list; added volume/number.

### 7. `widyasari2024fusefl` — Wrong title + incomplete authors

- **Problem**: Title listed as "FuseFL: Demystifying Faulty Code with LLM via Step-by-Step Reasoning" — actual published title differs.
- **Actual title**: "Demystifying Faulty Code: Step-by-Step Reasoning for Explainable Fault Localization"
- **Fix applied**: Corrected title; expanded full 5-author list.

### 8. `tian2024debugbench` — Missing authors

- **Problem**: Missing 2 of 11 authors (Haotian Hui, Weichuan Liu).
- **Fix applied**: Added missing authors.

### 9. `haque2025traces` — Incomplete author list

- **Problem**: "Mirazul Haque, Petr Babkin, and others" — only 4 authors total, should list all.
- **Fix applied**: Expanded to full list (Haque, Babkin, Farmahinifarahani, Veloso).

### 10. `dong2024composition` — Incomplete author list

- **Problem**: "Guanting Dong, Hongyi Yuan, Keming Lu, and others" — obscures 7 co-authors.
- **Fix applied**: Expanded to full 10-author list.

## Verified Entries (PASS)

All details confirmed correct via WebSearch:

1. `chen2025tracepile` — NeurIPS 2025, arXiv 2510.23629
2. `ding2024traced` — ICSE 2024, DOI 10.1145/3597503.3608140
3. `chen2021evaluating` — arXiv 2107.03374 (Codex/HumanEval)
4. `austin2021program` — arXiv 2108.07732 (MBPP)
5. `hu2022lora` — ICLR 2022, arXiv 2106.09685
6. `deepseek2024coder` — arXiv 2401.14196
7. `wang2025dcsh` — EMNLP 2025 Findings, arXiv 2509.11686
8. `ni2024next` — ICML 2024, arXiv 2404.14662
9. `jung2025execution` — EMNLP 2025, arXiv 2506.10343
10. `xu2025cruxevalx` — ACL 2025, arXiv 2408.13001
11. `yang2025apsg` — arXiv 2505.02629
12. `spiess2025calibration` — ICSE 2025, arXiv 2402.02047
13. `foster2025mutation` — FSE 2025 Industry Track, arXiv 2501.12862
14. `huang2026tracecoder` — ICSE 2026, arXiv 2602.06875
15. `wang2025inspectcoder` — arXiv 2510.18327
16. `yadavally2024ndslicer` — FSE 2024
17. `yang2024generalization` — NAACL 2024, arXiv 2403.09162
18. `wu2026runtime` — arXiv 2604.02647

## Citation Context Check

Spot-checked all citations in Introduction and Related Work for content accuracy:
- No 张冠李戴 (misattribution) detected
- All paper descriptions match actual paper content
- The two FAIL entries had fabricated author metadata but correct title/content descriptions
