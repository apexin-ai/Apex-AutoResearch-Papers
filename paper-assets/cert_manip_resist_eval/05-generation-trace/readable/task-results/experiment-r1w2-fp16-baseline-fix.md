# experiment r1w2 fp16 baseline fix

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_r1w2-fp16-baseline-fix_20260524T171913_result.json`
- **Structured JSON:** [`04cb259b82b45fbf4545.json`](../../sessions/04/04cb259b82b45fbf4545.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

V2 script is running. It's downloading Qwen2.5-14B-Instruct-AWQ via ModelScope now. The pipeline:

1. Download AWQ 14B via ModelScope → load → eval 200 samples
2. Download FP16 14B → load → eval 200 samples  
3. Same for 32B (AWQ + FP16)
4. 72B AWQ only (FP16 skipped - too large)

Estimated total runtime: 3-5 hours depending on download speeds and JIT compilation time. PID 18494 (Monte Carlo job) is undisturbed on the same GPU but only uses CPU.

---
