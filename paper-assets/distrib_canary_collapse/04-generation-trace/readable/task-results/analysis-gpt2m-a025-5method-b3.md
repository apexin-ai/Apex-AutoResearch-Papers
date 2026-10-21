# analysis gpt2m a025 5method b3

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2m_a025_5method_b3_20260516T083010_result.json`
- **Structured JSON:** [`03c4f7f666d919dcdd4e.json`](../../sessions/03/03c4f7f666d919dcdd4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three subtasks complete. Summary:

**A. Registry updated** — gen_wiki_gpt2m_a025_s42 marked DONE with full metrics.

**B. Effective_rank investigation conclusion** — NOT a bug. GPT-2m starts with extremely low ER (2.37, nearly rank-2 representations), so collapse *destroys* structure → ER rises. Dose-response is monotonic (α=0.25: +258%, α=1.0: +1027%). Pythia starts high (46.6) so collapse mildly concentrates → ER drops. Implication: effective_rank direction is model-dependent; recommend caveat in paper or restrict canary list to token_entropy + ECE.

**C. 5-method lead-lag results:**
- 1/8 pairs Tier 3, 7/8 pairs Tier 2 (weaker than gpt2m_a100's 6/6 Tier 3)
- Permutation Granger: 0/8 sig (underpowered at T=11 + weak α=0.25 signal)
- Threshold onset clearly shows canary leading by 5-6 generations
- Perplexity improves (decreases) at α=0.25, so perplexity pairs fail threshold detection

Artifact registered: `art_20260516_48a33f`

---
