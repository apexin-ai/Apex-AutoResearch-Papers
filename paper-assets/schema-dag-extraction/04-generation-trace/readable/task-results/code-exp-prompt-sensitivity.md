# code exp prompt sensitivity

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_prompt_sensitivity_20260517T062052_result.json`
- **Structured JSON:** [`16e7dc4b8bf95e64c211.json`](../../sessions/16/16e7dc4b8bf95e64c211.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Full run initializing correctly: 56000 samples, 80 relations, 10 batches per count level (count_8 and count_32). Model is loading. The experiment is properly started.

**Summary:**

- Script: `/root/schema-dag-extraction/experiments/prompt_sensitivity/run_prompt_sensitivity.py`
- Tmux session: `prompt_sensitivity`
- Log: `~/runs/schema-dag-extraction/prompt_sensitivity.log`
- GPU: cuda:0 on cqa1-38874
- Design: 4 variants (v2, instruction_rewrite, cot, minimal) × 2 counts (8, 32) × 10 batches = 80 total batch evaluations
  - count_8: 12 samples/type × 8 types = 96 instances per batch
  - count_32: 12 samples/type × 32 types = 384 instances per batch
- Dry run verified: EXIT_CODE=0, 91.67% accuracy on 1 batch with v2 prompt
- Supports `--resume` for crash recovery
- Output: `experiments/prompt_sensitivity/results.json` with per-variant Pearson correlations (BCS vs accuracy)

Estimated runtime: ~2-4h (CoT variant will be slower due to longer outputs without constrained decoding).

---
