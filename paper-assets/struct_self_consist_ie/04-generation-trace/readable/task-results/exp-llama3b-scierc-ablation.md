# exp llama3b scierc ablation

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_llama3b_scierc_ablation_20260516T030431_result.json`
- **Structured JSON:** [`c6635a8bbadf0e211ebb.json`](../../sessions/c6/c6635a8bbadf0e211ebb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Phase 2 training is running on autodl-5090 (tmux session `llama3b_train`, cuda:3):
- **Model**: LLaMA-3.2-3B-Instruct, 48.6M trainable LoRA params (1.49%)
- **Data**: 1,861 SciERC training samples, 5 epochs
- **Steps**: 585 total, ~2s/step → ~19 min ETA
- **Registry**: exp_llama3b_scierc_ablation → RUNNING

Monitoring every 5 minutes. When training finishes I'll proceed to Phase 3 (merge adapter + run inference).

---
