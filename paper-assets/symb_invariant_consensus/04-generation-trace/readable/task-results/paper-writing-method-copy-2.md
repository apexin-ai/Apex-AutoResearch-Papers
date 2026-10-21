# paper writing method

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260517T164108_result.json`
- **Structured JSON:** [`16492fc6ca987f774317.json`](../../sessions/16/16492fc6ca987f774317.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

File written to `docs/paper/method.tex`. Summary:

- **~1013 words** + 4 equations across 5 subsections (~2.5 columns as targeted)
- **§3.1 Overview**: 4-stage pipeline description with SC comparison
- **§3.2 Constraint Extraction**: extraction prompt, extraction rate metric, deduplication with frequency weighting
- **§3.3 Weighted Partial MAX-SAT**: full formal notation (Eq.1 MAX-SAT objective, Eq.2 scoring function), cross-answer evaluation paragraph explaining source-answer coupling and degeneration to weighted voting (Eq.3), forward-referencing ablation results in §Experiments
- **§3.4 C0 Diagnostic**: formal definition (Eq.4), necessary-but-insufficient interpretation, zero-cost early stopping framing
- **§3.5 Scope and Limitations**: same-model self-extraction scope, explicit acknowledgment of DyLoS/Aristotle/FoVer/LogicAgent

Style checks pass: zero em-dashes, zero en-dashes, zero blacklisted words, zero "We propose" instances, no -ing phrase endings. 3 citations used (SC baseline, Z3, and 4 related methods in scope section); remaining `\cite{key}` placeholders use the specified key format.

---
