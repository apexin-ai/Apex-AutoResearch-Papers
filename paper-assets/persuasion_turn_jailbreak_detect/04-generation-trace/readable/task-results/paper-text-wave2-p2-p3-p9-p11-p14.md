# paper text wave2 p2 p3 p9 p11 p14

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_text_wave2_p2_p3_p9_p11_p14_20260522T140858_result.json`
- **Structured JSON:** [`c61f19cba36dfbfeb114.json`](../../sessions/c6/c61f19cba36dfbfeb114.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are in place. Here's a summary of what was done:

**P11 (references):** Added `hsu2024improved` and `li2025m2s` to `references.bib`. Cited Hsu et al. in related work's single-turn defenses list. Cited M2S as a complementary approach in the same paragraph. TrajGuard and SAE Mitigators were already cited.

**P2 (scope limiting):**
- `abstract.tex`: Added "On synthetic multi-turn data," before the classification DAPT claim
- `introduction.tex`: Changed "Two-step adaptation protocol" → "Preliminary two-step adaptation protocol" with "On the synthetic benchmark" qualifier
- `conclusion.tex`: Added "On synthetic multi-turn data" scope; changed "yields a two-step protocol" → "suggest a preliminary two-step protocol"

**P3 (Mixed-LLM downgrade):**
- Reframed subsection as "exploratory cross-LLM condition"
- Added AA F1=0.504 falls below trivial all-benign baseline (~0.808)
- Added cross-LLM style confound sentence citing Appendix cross_llm

**P9 (length confound):**
- Added to Summary paragraph: length difference noted (12–20 vs 3–10 turns) with three controls (truncation 0% FPR, single-turn F1=0.773, padding −57.9pp on AA)

**P14 (scrambled labels):**
- Code confirms multi-permutation: each of the 10 TOST seeds generates an independent random permutation via `scramble_strategies(data, seed)`. Added clarifying parenthetical "(each using an independent random permutation)" to the TOST description.

**P15 (strategy annotation prompt):**
- Skipped. No separate prompt file exists; strategies are assigned during generation (embedded in `generate_crescendo_v2.py`). Appendix already describes the process and promises release.

**Page budget:** Conclusion ends on page 8. Limitations/Ethics/References on page 9+. Main text ≤ 8 pages confirmed.

---
