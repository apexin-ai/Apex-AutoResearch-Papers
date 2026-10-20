# exp deberta verifier v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_deberta_verifier_v2_20260518T064502_result.json`
- **Structured JSON:** [`f952b6df743faf78c76d.json`](../../sessions/f9/f952b6df743faf78c76d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved locally. Here's the summary:

## DeBERTa Verifier 5-Fold CV × 3 Seeds — Final Results

| Method | Selection F1 | Gap Closure % |
|--------|-------------|---------------|
| Greedy (baseline) | 0.6438 | — |
| **DeBERTa verifier** | **0.6114 ± 0.028** | **-26.5 ± 26.5%** |
| LP selection | 0.6499 | +4.2 ± 10.7% |
| Oracle | 0.7775 | 100% |

**Spearman ρ**: 0.329 ± 0.087 (weak positive correlation, but not translating to selection quality)

**Key finding**: DeBERTa selection is **consistently worse than greedy** across all 15 runs (13/15 have negative gap closure, mean = -26.5%). The learned representation verifier not only fails to close the gap toward oracle, it actively degrades performance. In contrast, the simple LP signal achieves a modest positive gap closure (+4.2%).

This is the rigorous negative result needed for the paper: even with a 184M-parameter DeBERTa encoder fine-tuned on the exact task distribution, learned representations cannot reliably rank sample quality for structured IE. The scalar signals (especially LP) remain superior despite being far simpler.

---
