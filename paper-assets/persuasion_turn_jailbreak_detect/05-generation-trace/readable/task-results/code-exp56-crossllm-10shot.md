# code exp56 crossllm 10shot

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp56_crossllm_10shot_20260522T115411_result.json`
- **Structured JSON:** [`975c7d5e34dd4fd71154.json`](../../sessions/97/975c7d5e34dd4fd71154.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp56 complete. Results:

**Adaptation Curve (Llama-benign FPR / Qwen-OOD / Llama-OOD):**

| N | Llama FPR | DD F1 | AA F1 | FITD F1 | DD_llama | AA_llama | FITD_llama |
|---|-----------|-------|-------|---------|----------|----------|------------|
| 0 | **94.5%** | 1.00 | 0.99 | 1.00 | 1.00 | 0.74 | 1.00 |
| 5 | **5.5%** | 0.69 | 0.84 | 0.99 | 0.64 | 0.04 | 0.76 |
| 10 | **3.0%** | 0.82 | 0.60 | 1.00 | 0.60 | 0.00 | 0.80 |
| 25 | **0.5%** | 0.56 | 0.27 | 0.99 | 0.08 | 0.00 | 0.52 |

**Conclusion: negative.** Benign adaptation fixes cross-LLM FPR (94.5% → 3%) but **severely degrades jailbreak detection recall**, especially for same-LLM jailbreaks (AA_llama: 0.74 → 0%). This is fundamentally different from the WildChat/OASST2 adaptation (exp45/exp51) where OOD F1 stayed near 1.0.

The root cause: unlike human-population shift (WildChat vs OASST2), cross-LLM shift creates a **confound** — benign and jailbreak conversations from Llama share stylistic features. Adding Llama-benign teaches the model "Llama style = benign", which suppresses detection of Llama-origin jailbreaks. The two-axis framework's benign-only adaptation mechanism does not extend cleanly to cross-LLM distributional shift.

---
