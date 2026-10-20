# code llm rephrase robustness

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llm-rephrase-robustness_20260516T221100_result.json`
- **Structured JSON:** [`9fdb57eea528049a6529.json`](../../sessions/9f/9fdb57eea528049a6529.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script is working correctly. Progress confirmed: 50/5000 texts rephrased in ~80s (1.6s/text).

**Estimated timeline:**
- Rephrasing: 5000 texts × 1.6s ≈ 133 min
- Feature extraction (Pythia-410M): ~15 min
- LOGO evaluation: ~5 min
- **Total: ~2.5 hours**

The script will:
1. Rephrase 5000 texts using Qwen3-0.6B-Base (context continuation, 1-3 sentences replaced per text)
2. Save intermediate `rephrased_texts.jsonl`
3. Extract 7 depth features with Pythia-410M
4. Run pooled LOGO XGBoost (train on original, test on rephrased)
5. Save results to `llm_rephrase_results.json`

Reference baselines from Condition A:
- Original: binary F1 = 0.6953
- 5% random replacement: binary F1 = 0.6496 (drop = -0.0457)

Process PID 351633 is running on autodl-5090. Want me to check back on progress later?

---
