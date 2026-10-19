# paper writing introduction d032

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_d032_20260517T160030_result.json`
- **Structured JSON:** [`da885324cb11fdec7c0a.json`](../../sessions/da/da885324cb11fdec7c0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction written to `docs/paper/sections/introduction.tex`. ~1000 words (LaTeX markup included), 4 narrative paragraphs + contributions list.

Structure:
1. **Self-jailbreak problem** (~210 words): CoT reasoning, CP definition, cites deepseekr1/qwq/harmthoughts/selfjailbreak
2. **Wrong threat model** (~160 words): TrajGuard/SafeSwitch vs SafeRemind/SafeThink, input attacks vs internal commitment
3. **Comparison gap** (~150 words): no controlled HS-vs-text evaluation, layer selection as unexamined variable, cites belinkov2019analysis
4. **Our discovery** (~220 words): 4-model evaluation, biased metric mechanism, 5/12 vs 12/12 Holm-Bonferroni, precision +15-24pp, references `tab:layer_selection` and `tab:hs_vs_text`
5. **Contributions** (3 items): each with section/table references (`sec:layer-results`, `sec:hs-text`, `sec:32b-analysis`, `sec:negative`, `tab:negative`, `app:control`)

Style checks pass: zero em-dashes, zero en-dashes, zero banned phrases, zero transition chains, no -ing phrase endings.

---
