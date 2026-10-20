# paper final exp polish

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final-exp-polish_20260522T184716_result.json`
- **Structured JSON:** [`df6e9ca3bf1c798b34f5.json`](../../sessions/df/df6e9ca3bf1c798b34f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Files are identical. Here's a summary of all modifications:

---

### Edit 1: Table 1 caption (line 70)

**Changes:**
- Added **`\textbf{Columns:}`** and **`\textbf{Markers:}`** headers to organize the dense caption into two logical sections
- Added **"(upper bound on genuine reasoning)"** after N-H definition — critical for readers who jump to the table without reading §4.1's definition
- `"3-seed rows:"` → `"Multi-seed rows report"` (covers both 3- and 5-seed rows)
- `$^\dagger$Seed~42.` → `$^\dagger$Seed~42 only.` (clearer)
- `"5-seed raw ISR* in parentheses, same TS confound applies (no matched control for 5-seed)"` → `"5-seed raw ISR$^*$ in parentheses (same confound, no matched control)"` (tighter)
- `"Random TS driven by seed~43"` → `"Random TS driven entirely by seed~43"` (emphasizes it's a single-seed artifact)
- `"seeds~42 and~44: 0%"` → `"seeds~42/44: 0%"` (compact)
- `"not an independent reward condition"` → `"not an independent condition"` (trim)
- Fixed inconsistent `ISR*` → `ISR$^*$` in two places (was missing math formatting)

### Edit 2: §4.3 intro paragraph (line 44)

| Before | After |
|---|---|
| `...Table~\ref{tab:goodhart-landscape}); the apparent $214\times$ raw ISR advantage collapses to $1.06\times$ after controlling for premise count.` | `...Table~\ref{tab:goodhart-landscape}). The scalar ISR$^*$ advantage ($214\times$ raw) collapses to $1.06\times$ after controlling for premise count; the compositional mode shift provides the primary evidence.` |

**Rationale:** Explicitly previews the scalar/compositional two-level structure that becomes the argument through §4.3. The old text had "the apparent... advantage collapses" as a standalone fact; the new text frames it as one side of a two-level contrast, making the §4.3 narrative arc legible from the first paragraph.

### Edit 3: Premise-count confound paragraph split (lines 79–85)

**Before** (one dense paragraph, 6 claims):
```
...indicating that the scalar ISR advantage is not statistically significant.
The TS mode shift, however, is robust in the modal premise-count range...
...
The compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.
```

**After** (two paragraphs with transition):
```
...indicating that the scalar ISR advantage is not statistically significant.

The compositional evidence, however, survives this control.
In the modal premise-count range (4--6 premises, where most proved samples fall), TS reaches 19.7% under ISR versus 0% under random reward...
...
This complexity dependence is a mechanistic insight, not a confound: the compositional mode shift---not the scalar ISR difference---constitutes the primary evidence for the Goodhart effect.
```

**Changes:** (a) Paragraph break after the scalar confound conclusion; (b) Transition sentence "The compositional evidence, however, survives this control." starts the second paragraph; (c) Last two sentences merged with colon ("`insight, not a confound: the compositional mode shift...`") to offset the added transition without net line increase.

---

### Observations (not modified)

1. **β column in Table 1** — not defined in the caption. Self-evident from context (line 42 defines the reward formula with β), but a pedantic reviewer might note it. Optional fix: add `$\beta$ = reward weight` after the Columns header.
2. **"regressional Goodhart" (line 43)** — jargon from Manheim & Garrabrant, but immediately defined with an inline gloss. Acceptable for ACL/EMNLP audience. No change needed.
3. **Line 47 ("Multiplicative coupling" paragraph)** — also dense (two-sentence paragraph with 5 controls enumerated), but the §4.3 constraints don't allow much expansion within 8 pages. Could consider moving to appendix if page pressure arises.

---
