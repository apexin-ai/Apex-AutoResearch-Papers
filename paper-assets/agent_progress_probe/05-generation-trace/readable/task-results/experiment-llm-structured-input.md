# experiment llm structured input

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_llm-structured-input_20260515T025406_result.json`
- **Structured JSON:** [`358e64ae38e9bc7745c9.json`](../../sessions/35/358e64ae38e9bc7745c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Current status: 900/1824 (49%), macro_f1=0.6965, 1 parse failure, ~$7.29 cost. Process 229876 still running.

The macro_f1 has been fluctuating in the 0.69–0.73 range since the 300-window mark, currently settling around 0.70. This is already a meaningful improvement over the text-only zero-shot baseline (0.6625) — roughly +3.4 points.

Estimated ~1–2 hours remaining depending on API throughput. I'll check back when you return, or you can ask me to check status anytime. Once the run completes, I'll:

1. Collect final metrics from `results.json`
2. Save the prompt template to `artifacts/llm-structured-input/prompt_template.txt`
3. Copy results locally
4. Update the registry via `update_registry`

---
