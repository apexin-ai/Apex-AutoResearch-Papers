# ssh submit freeform fewnerd cuda0

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_freeform_fewnerd_cuda0_20260522T124203_result.json`
- **Structured JSON:** [`b68937cacb3837e2b940.json`](../../sessions/b6/b68937cacb3837e2b940.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments submitted and registered.

**Summary:**

| Experiment | GPU | Model | Dataset | tmux session |
|---|---|---|---|---|
| `exp_fewnerd_freeform_n8_s42` | cuda:0 | qwen3-8b-fewnerd-exp021-merged | FewNERD (37,648) | `exp_fewnerd_freeform` |
| `exp_conll_freeform_n8_s42` | cuda:1 | qwen3-8b-conll2003-merged | CoNLL-2003 (3,453) | `exp_conll_freeform` |

**Changes made:**
- Patched `run_mvp_pilot.py` to expose `--use_grammar` CLI flag (lines 70-71), wired to `run_sampling_pipeline()` call (line 203)
- Both running with `--use_grammar false`, N=8, T=1.0, seed=42, `--collect_logprobs`
- Output dirs: `output/fewnerd_freeform_n8_seed42/`, `output/conll_freeform_n8_seed42/`
- Registry updated to RUNNING for both

---
