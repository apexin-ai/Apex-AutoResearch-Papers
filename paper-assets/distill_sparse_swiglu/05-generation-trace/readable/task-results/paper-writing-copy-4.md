# paper writing

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_20260516T125328_result.json`
- **Structured JSON:** [`28166a9c640aa21dac13.json`](../../sessions/28/28166a9c640aa21dac13.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction written to `paper/introduction.tex`. ~1050 words, 5 paragraphs following the specified story arc:

1. **Hook** — SwiGLU sparsity potential vs. training-free degradation (TEAL 23.31 PPL) and learned predictor overhead
2. **Structural mismatch** — BCE gradient is per-neuron factorized, but inference uses global top-k; formal gradient equation showing independence
3. **KL mechanism** — gradient chain rule through full Jacobian couples all neurons; Gumbel-Sigmoid relaxation; predictor architecture (2.37M/layer, 75.9M total)
4. **Results** — KL 11.79 vs TEAL 23.31 vs BCE 27.97; scaling 18%/49%/82%; Mistral +63%; SPON cos_sim 0.196, 2.4% recovery
5. **Contributions** — 3 bulleted items: KL eliminates compensation + gradient analysis, 2D taxonomy, phase transition + SPON orthogonality

All required citation keys, numbers, and the Figure 1 reference are included. No banned phrases used.

---
