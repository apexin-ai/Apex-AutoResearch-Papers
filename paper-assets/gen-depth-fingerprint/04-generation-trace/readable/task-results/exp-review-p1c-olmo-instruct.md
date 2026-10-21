# exp review p1c olmo instruct

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-p1c-olmo-instruct_20260515T152127_result.json`
- **Structured JSON:** [`c6e80d01f2ab075df8f9.json`](../../sessions/c6/c6e80d01f2ab075df8f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Generation is running. Here's the status:

- **Model**: `allenai/OLMo-2-0425-1B-Instruct` (2.8GB, downloaded from HuggingFace)
- **GPU**: cuda:0, 3.6GB VRAM used, RTX 5090
- **Pipeline**: 3-step bash script in tmux session `p1c_olmo`
  1. Generate chains (995 seeds × 5 depths) — ~2.3 hours
  2. Extract features with Pythia-410M reference model
  3. Run 7-gen LOGO analysis (merges with 6 existing base model generators)
- **Scripts written**: `run_p1c_olmo_instruct.sh`, `analyze_7gen_logo.py`
- **ETA**: ~17:45 UTC for generation, feature extraction + analysis add ~30 min

I'll monitor every 20 minutes and report when results are ready.

---
