# code wikievents baseline status check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_baseline_status_check_20260517T181006_result.json`
- **Structured JSON:** [`3cf4dc1ff31e798304bc.json`](../../sessions/3c/3cf4dc1ff31e798304bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Status summary:

| Model | Server | GPU | Status | Docs Completed | Notes |
|-------|--------|-----|--------|----------------|-------|
| Qwen3-8B | westd-16980 | 1 | **Running** | 67/246 | Active, ~2.3 docs/min, ETA ~80 min |
| Llama-3.1-8B | westd-16980 | 0 | **CRASHED** | 52/246 | AttributeError at doc 52 |
| Mistral-7B | westd-21461 | 0 | **Running** | 27/246 | Active, GPU 90% util |

**Llama crash details:**

`run_constrained_extraction.py:985` — `parsed` is a `list` instead of `dict`, causing `parsed.get("entities", [])` to fail. The crash happened on sample 52 (`scenario_en_kairos_50`). The fix should be:

```python
n_ents = len(parsed.get("entities", [])) if parsed else 0
# → needs to handle case where parsed is a list, not dict
```

Options:
1. Fix the bug and restart Llama with `--skip_existing` to resume from doc 52
2. Wait for Qwen/Mistral to finish first, then fix and rerun Llama

Want me to fix and restart Llama now?

---
