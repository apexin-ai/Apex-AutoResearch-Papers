# paper writing experiments rewrite

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_experiments_rewrite_20260519T131430_result.json`
- **Structured JSON:** [`1a076b5e757fdcd40b4f.json`](../../sessions/1a/1a076b5e757fdcd40b4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Rewrite complete. Key changes:

**Insight-led openers** (all 6 subsections):
- Cross-Attack: "Vanilla encoders collapse under cross-attack transfer; DAPT recovers near-perfect detection"
- Decomposing: "Domain exposure is the primary detection mechanism: it accounts for the largest OOD gain, while label quality and granularity are non-factors"
- Cross-Encoder: "A hierarchy established on a single encoder could reflect architecture-specific artifacts" (explicit motivation)
- Human Data: "The evidence hierarchy is not a Qwen3-8B generation artifact"
- Perturbation: "DAPT's detection advantage persists under adversarial paraphrasing, though absolute robustness is attack-family-dependent"
- Strategy: "Beyond detection accuracy, the 9-class persuasion taxonomy provides interpretable characterization"

**Redundancy reduction**: removed "The core result appears in Table X" opener; merged prefix-length analysis with vanilla collapse paragraph; condensed figure description to one sentence; compressed Summary from ~63 to ~45 words (3 sentences).

**Sentence splitting**: Models paragraph LLM sentence (1 -> 3), Metrics std sentence (split at semicolon), Cross-Attack MLM interpretation (split at "Longer conversations..."), Decomposing McNemar sentence (split at period), Cross-Encoder RoBERTa-large opener (colon -> period).

**De-AI fixes**: eliminated -ing participial endings ("worsening with more turns" -> "degrades monotonically from"; "confirming that..." -> "show that..."); no em-dashes/en-dashes outside number ranges.

**Strategy expanded**: from 5 lines to 7, added explicit dissociation ("yet detection F1 remains near-perfect") and closing interpretive sentence about taxonomy's role.

**Perturbation tightened**: from 4 sentences to 3, insight-first opener combines conclusion + appendix ref.

All numbers, table/figure blocks, \label/\ref, and \cite preserved exactly.

---
