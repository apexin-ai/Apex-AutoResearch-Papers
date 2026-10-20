# exp review p1c qwen06b instruct

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-p1c-qwen06b-instruct_20260515T152144_result.json`
- **Structured JSON:** [`c1f94c86ade4ab9561b3.json`](../../sessions/c1/c1f94c86ade4ab9561b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment `review-p1c-qwen06b-instruct` complete. Key findings:

**Verdict: NEGATIVE** — instruct mode significantly attenuates the depth fingerprint.

| Metric | Instruct | Base | Delta |
|--------|----------|------|-------|
| LOGO 3-class F1 | 0.667 | 0.816 | **-14.8pp** |
| Binary F1 | 0.988 | 0.988 | ~0 |
| 7-gen avg F1 | 0.767 | — | — |

**Spearman correlations are fully reversed** — instruct shows *positive* ρ where base shows *negative*:

| Feature | Instruct ρ | Base ρ |
|---------|-----------|--------|
| entropy_mean | +0.518 | -0.566 |
| ttr | +0.529 | -0.611 |
| hapax_ratio | +0.509 | -0.627 |

The instruct model's gen-1 F1 collapses to 0.284 (vs base 0.659), meaning the classifier can barely distinguish gen-1 from gen-2+ when trained on other generators. This is consistent with the Qwen3-1.7B-Instruct result — instruct tuning fundamentally changes how depth features evolve, inverting the diversity/entropy decay pattern seen in base models. Binary human-vs-machine detection remains robust (0.988) since the gen-0 vs gen-1+ boundary is unaffected.

---
