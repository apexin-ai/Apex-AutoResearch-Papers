# paper r11 d054 phase1 3

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r11-d054-phase1-3_20260517T100308_result.json`
- **Structured JSON:** [`9cefa0b1756a351eb046.json`](../../sessions/9c/9cefa0b1756a351eb046.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All modifications verified. Summary of changes:

**Phase 1:**
- **Title** (main.tex): "Shape" → "Predict"
- **Abstract** (abstract.tex): Condensed to 4 sentences, kept 3 core numbers (-49pp, 2.2pp, 22-53%), expanded BCS definition, added NER/RE distinction
- **Findings** (introduction.tex): Split monolithic paragraph into 5 numbered sentences
- **Contributions** (introduction.tex): Rewritten as 4 methodological claims without specific numbers, with section references

**Phase 2 (NER/RE boundary):**
- **Abstract**: "BCS explains 22--53% ... in RE but not in NER, where the signal is absent despite significant pairwise effects"
- **Finding (2)**: "BCS predicts accuracy in RE ($R^2 = 0.22$--$0.53$) but not in NER (batch-level $r \approx 0$, n.s.)"
- **Discussion**: New "Task-dependent batch-level effects" paragraph explaining RE-specific BCS signal vs. NER null result

**Phase 3 (Practical significance):**
- **Discussion**: R² framing added (pair-level weak → batch-level sufficient for screening)
- **Discussion**: New "Practical implications" paragraph (bounded interaction, BCS threshold for RE, count-first for NER, zero-shot caveat)

Compilation: 0 errors, 21 pages total. No em-dash, no -ing phrase endings, no forbidden causal words in modified text.

---
