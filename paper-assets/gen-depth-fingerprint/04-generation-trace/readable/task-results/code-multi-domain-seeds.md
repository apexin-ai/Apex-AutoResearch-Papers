# code multi domain seeds

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_multi-domain-seeds_20260517T033944_result.json`
- **Structured JSON:** [`d246a08423e451feaccc.json`](../../sessions/d2/d246a08423e451feaccc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment fully complete. Here's the summary:

**Multi-Domain Seeds Experiment Results**

| Domain | Binary F1 | 3-class F1 | 95% CI (binary) |
|--------|-----------|------------|-----------------|
| News | 0.7459 | 0.6516 | [0.726, 0.764] |
| Academic | 0.7386 | 0.6223 | [0.720, 0.757] |
| Code | 0.7535 | 0.6344 | [0.737, 0.770] |
| Wikipedia (baseline) | 0.8148 | 0.8632 | — |

**Conclusion: `domain_independent`**
- All 3 non-Wikipedia domains achieve binary F1 > 0.73 under LOGO-CV
- Max gap vs Wikipedia baseline: 0.076 (within the 0.15 threshold)
- Worst domain: academic (F1=0.739), Best domain: code (F1=0.754)
- The depth signal generalizes across domains — not a Wikipedia artifact

**Per-generator breakdown**: Mistral-7B is slightly harder to generalize to (held-out F1 lower), while Pythia-1B and Qwen3-1.7B show more consistent cross-generator transfer.

**Note**: The Wikipedia baseline is higher (0.81 binary) because it uses 5-fold CV rather than LOGO (trained/tested on same generators), and has more training data from the main experiment pipeline. The LOGO evaluation is a stricter test (generalize across unseen generators).

Results saved to `/root/gen-depth-fingerprint/experiments/multi_domain/multi_domain_results.json`.

---
