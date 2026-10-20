# exp llama fewnerd train infer

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama_fewnerd_train_infer_20260518T082852_result.json`
- **Structured JSON:** [`61499c4baf7de5e98227.json`](../../sessions/61/61499c4baf7de5e98227.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Status summary:**

- **Training**: LLaMA-3.1-8B-Instruct LoRA on Few-NERD INTRA coarse, 4×RTX 5090, ~2.1 it/s, 24,708 steps, ETA ~3.3h
  - Config: rank=32, alpha=64, lr=2e-4, bf16, 3 epochs, effective batch=16
  - Matches Qwen Few-NERD training hyperparams
- **Prepared**: Export config (`export_config_llama_fewnerd.yaml`), analysis script (`code/analyze_llama_fewnerd.py`)
- **Next steps after training**: export LoRA → merge → vLLM inference (N=8, T=1.0, 37,648 test instances) → full analysis pipeline

The training will take ~3 hours. I'll check progress periodically and proceed with export/inference/analysis once complete.

Want me to set up a monitoring loop, or should I check back manually?

---
