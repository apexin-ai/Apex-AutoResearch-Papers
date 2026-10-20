# Reference Audit Report — demo_calibrated_sim

**Date:** 2026-05-13
**Scope:** 8 newly added papers in `literature_map.yaml` (scan_date: 2026-05-13)
**Method:** arXiv ID lookup + title/author/venue cross-check via web search

---

## Summary

| # | ID | arXiv | Status | Issue |
|---|-----|-------|--------|-------|
| 1 | sim2real2026gap | 2603.11245 | **VERIFIED** | Authors listed as "Anonymous" but paper has named authors |
| 2 | khan2026decoding | 2605.02348 | **VERIFIED** | — |
| 3 | gupta2025endive | 2504.07100 | **VERIFIED** | — |
| 4 | nakash2026divert | 2604.21480 | **VERIFIED** | — |
| 5 | basil2025playing_pretend | 2512.05858 | **VERIFIED** | Title in yaml uses subtitle only (omits "Prompting Science Report 4:") |
| 6 | anonymous2026expert_persona | 2603.18507 | **VERIFIED** | Authors listed as "Anonymous" but paper has named authors |
| 7 | gupta2026intra_fairness | 2602.16438 | **MISMATCH** | First author is Paraschou, NOT Gupta |
| 8 | lee2024dpo_toxicity | 2401.01967 | **VERIFIED** | — |

**Result: 7 VERIFIED, 1 MISMATCH (author error), 0 hallucinated papers.**

---

## Detailed Verification

### 1. sim2real2026gap — arXiv 2603.11245 ✅ VERIFIED

- **Title (yaml):** "Mind the Sim2Real Gap in User Simulation for Agentic Tasks"
- **Title (actual):** "Mind the Sim2Real Gap in User Simulation for Agentic Tasks" ✓
- **Authors (yaml):** "Anonymous (under review)"
- **Authors (actual):** Xuhui Zhou, Weiwei Sun, et al. (Carnegie Mellon University)
- **Year:** 2026 ✓
- **Venue:** arXiv 2603.11245 ✓
- **⚠ Action needed:** Update authors from "Anonymous" to actual author names.

### 2. khan2026decoding — arXiv 2605.02348 ✅ VERIFIED

- **Title (yaml):** "Decoding-Time Debiasing via Process Reward Models: From Controlled Fill-in to Open-Ended Generation"
- **Title (actual):** identical ✓
- **Authors (yaml):** "Khan, Muneeb Ur Raheem"
- **Authors (actual):** Muneeb Ur Raheem Khan (LUMS) ✓
- **Year:** 2026 (submitted May 4, 2026) ✓
- **Venue:** arXiv 2605.02348 ✓

### 3. gupta2025endive — arXiv 2504.07100 ✅ VERIFIED

- **Title (yaml):** "EnDive: A Cross-Dialect Benchmark for Fairness and Performance in Large Language Models"
- **Title (actual):** identical ✓
- **Authors (yaml):** "Gupta, Cheung et al."
- **Authors (actual):** confirmed via ACL Anthology (2025.findings-emnlp.913) ✓
- **Year:** 2025 ✓
- **Venue:** Findings of EMNLP 2025 ✓

### 4. nakash2026divert — arXiv 2604.21480 ✅ VERIFIED

- **Title (yaml):** "Efficient Agent Evaluation via Diversity-Guided User Simulation"
- **Title (actual):** identical ✓
- **Authors (yaml):** "Nakash, Kour, Anaby-Tavor"
- **Authors (actual):** Itay Nakash, George Kour, Ateret Anaby-Tavor (IBM Research) ✓
- **Year:** 2026 ✓
- **Venue:** arXiv 2604.21480 ✓

### 5. basil2025playing_pretend — arXiv 2512.05858 ✅ VERIFIED

- **Title (yaml):** "Playing Pretend: Expert Personas Don't Improve Factual Accuracy"
- **Title (actual):** "Prompting Science Report 4: Playing Pretend: Expert Personas Don't Improve Factual Accuracy"
- **Authors (yaml):** "Basil, Shapiro, Shapiro, Mollick, Mollick, Meincke"
- **Authors (actual):** Savir Basil, Ina Shapiro, Dan Shapiro, Ethan R. Mollick, Lilach Mollick, Lennart Meincke (Wharton) ✓
- **Year:** 2025 ✓
- **Venue:** arXiv 2512.05858 ✓
- **⚠ Minor:** Yaml title omits series prefix "Prompting Science Report 4:". Acceptable for citation purposes.

### 6. anonymous2026expert_persona — arXiv 2603.18507 ✅ VERIFIED

- **Title (yaml):** "Expert Personas Improve LLM Alignment but Damage Accuracy: Bootstrapping Intent-Based Persona Routing with PRISM"
- **Title (actual):** identical ✓
- **Authors (yaml):** "Anonymous"
- **Authors (actual):** Zizhao Hu, Mohammad Rostami, Jesse Thomason
- **Year:** 2026 ✓
- **Venue:** arXiv 2603.18507 ✓
- **⚠ Action needed:** Update authors from "Anonymous" to "Hu, Rostami, Thomason". Update id from `anonymous2026expert_persona` to `hu2026expert_persona`.

### 7. gupta2026intra_fairness — arXiv 2602.16438 ❌ MISMATCH

- **Title (yaml):** "Intra-Fairness Dynamics: The Bias Spillover Effect in Targeted LLM Alignment"
- **Title (actual):** identical ✓
- **Authors (yaml):** "Gupta et al."
- **Authors (actual):** Eva Paraschou, Line Harder Clemmensen, Sneha Das (U. Copenhagen / DTU)
- **Year:** 2026 ✓
- **Venue:** arXiv 2602.16438 ✓
- **❌ Author wrong:** No author named "Gupta" on this paper. First author is **Paraschou**.
- **⚠ Action needed:** Update authors to "Paraschou, Clemmensen, Das". Update id from `gupta2026intra_fairness` to `paraschou2026intra_fairness`.

### 8. lee2024dpo_toxicity — arXiv 2401.01967 ✅ VERIFIED

- **Title (yaml):** "A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity"
- **Title (actual):** identical ✓
- **Authors (yaml):** "Lee, Panda, Yun, Bansal"
- **Authors (actual):** confirmed (ICML 2024 proceedings, pages 26361-26378) ✓
- **Year:** 2024 ✓
- **Venue:** ICML 2024 ✓

---

## Recommendations

### Must Fix
1. **gupta2026intra_fairness**: Author attribution is wrong ("Gupta et al." → "Paraschou, Clemmensen, Das"). The paper is real but misattributed. Fix before submission.

### Should Fix
2. **sim2real2026gap**: Update authors from "Anonymous (under review)" to actual names (Zhou, Sun, et al.).
3. **anonymous2026expert_persona**: Update authors from "Anonymous" to "Hu, Rostami, Thomason" and rename id.

### Optional
4. **basil2025playing_pretend**: Consider adding full title prefix "Prompting Science Report 4:" for completeness.

### No Hallucinated Papers Found
All 8 arXiv IDs resolve to real papers with matching titles. No fabricated references detected.
