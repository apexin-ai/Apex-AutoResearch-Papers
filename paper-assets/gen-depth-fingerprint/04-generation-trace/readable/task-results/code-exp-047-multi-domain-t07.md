# code exp 047 multi domain t07

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_047-multi-domain-t07_20260517T055212_result.json`
- **Structured JSON:** [`45a45806ba319e9b3d3b.json`](../../sessions/45/45a45806ba319e9b3d3b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Generation is underway. Pythia-1b is fastest (87 lines already = ~21 seeds done), Qwen3 and Mistral are generating too. Each domain needs 200 seeds × 4 lines (depth 0-3) = 800 lines. 

The job is running successfully with temperature=0.7, top_p=0.9 on 3 GPUs in parallel. Expected completion: ~2-4 hours for generation + ~30 min for feature extraction + evaluation.

I'll check back on progress. The job is tracked as `multi_domain_t07` in tmux on autodl-5090. You can check status anytime with:
- `tail -50 /root/gen-depth-fingerprint/experiments/multi_domain/run_t07.log`
- `wc -l /root/gen-depth-fingerprint/experiments/multi_domain/generations_t07/*.jsonl`

Target: 9 files × 800 lines each = 7200 total lines, then feature extraction + LOGO evaluation produces `multi_domain_results_t07.json`.

---
