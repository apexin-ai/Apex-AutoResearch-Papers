# paper writing sec limitations

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_sec_limitations_20260520T235421_result.json`
- **Structured JSON:** [`612db3a70759dd7a8a4e.json`](../../sessions/61/612db3a70759dd7a8a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Limitations section written (~240 words). Covers all 6 outlined elements:

1. **Single model family** (Qwen2.5-7B) + QLoRA conservative framing (UC-3: rank-16 limits memorization → 38% is lower bound → full FT would be stronger)
2. **PSN-IRT dependency** + MML-EM refit failure ($r_a = 0.127$) → neural IRT needed for self-calibration
3. **SFT-only** contamination; post-RL deferred
4. **Power vs. benchmark size** (ARC-C $d = 0.45$, need ≥7,958 items for 80% power)
5. **Universal misfit** → absolute $\ell_z^*$ thresholds inapplicable → $\Delta\ell_z^*$ design required
6. **MML-EM discrimination recovery failure** → external parameter bank dependency

---
