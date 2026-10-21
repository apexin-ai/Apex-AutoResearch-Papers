# analysis gen1 subclass errors

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gen1-subclass-errors_20260517T231941_result.json`
- **Structured JSON:** [`580546eb6f62dcca79fd.json`](../../sessions/58/580546eb6f62dcca79fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Results saved to both `results/gen1_subclass_analysis.json` on server and the local artifact.

**Key finding**: Two statistically significant correlations provide mechanistic evidence for "larger models compress depth margins":

- **FPR vs size: rho=+0.84, p=0.009** — Gen-2+ from larger models looks like gen-1. Mistral-7B's gen-2+ has 60% FPR vs 18% for Pythia-1B. Additional generation passes through larger models fail to deepen the depth fingerprint.
- **FNR vs size: rho=-0.92, p=0.001** — Gen-1 from larger models is easily identified (FNR=6% for Mistral-7B vs 24% for Qwen3-0.6B). The first generation pass creates a strong signal, but further passes add negligible drift.

Interpretation: larger models apply a strong but saturating transformation — one pass creates a clear fingerprint, but subsequent passes don't compound the signal, compressing the gen-1/gen-2+ boundary.

---
