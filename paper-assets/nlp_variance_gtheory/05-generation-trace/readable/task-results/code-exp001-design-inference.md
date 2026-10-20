# code exp001 design inference

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp001_design_inference_20260520T193652_result.json`
- **Structured JSON:** [`0756e0c525950122b9b8.json`](../../sessions/07/0756e0c525950122b9b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 files modified, all syntax-clean. Summary of changes:

| File | Change |
|------|--------|
| `vllm_runner.py` | `enforce_eager=True` + `VLLM_USE_V1=0` (V0 engine for all precisions); `generate()` accepts `logprobs` param, extracts `answer_logprob` and `top_logprobs` from first token |
| `generate_design.py` | 4 models × 3 precisions × 3 temps × 6 templates × 6 seeds × 4 orderings = **5,184 conditions** |
| `prompt_templates.py` | Templates 4–6 added (dash-list, "Option X:", lowercase compact); all use same `{subject}`, `{question}`, `{A}`–`{D}`, `{answer}` placeholders — compatible with `format_prompt()` |
| `run_experiment.py` | Calls `generate(..., logprobs=5)`; writes `answer_logprob` and `top_logprobs` into each JSONL record |

---
