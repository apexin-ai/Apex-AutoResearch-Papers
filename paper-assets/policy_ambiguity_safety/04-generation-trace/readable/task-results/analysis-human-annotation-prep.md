# analysis human annotation prep

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_human_annotation_prep_20260522T221839_result.json`
- **Structured JSON:** [`3fddf70849efc88d899e.json`](../../sessions/3f/3fddf70849efc88d899e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All outputs are validated. Here's what was produced in `artifacts/human_annotation/`:

| File | Description |
|------|-------------|
| `prepare_annotation.py` | Stratified sampling script (reproducible, seed=42) |
| `annotation_sheet.csv` | 100 traces with all context + empty columns for annotation |
| `annotation_sheet.json` | Same data in JSON format |
| `sample_summary.json` | Distribution stats |
| `codebook.md` | Full annotation guide with definitions, real examples, decision tree, tie-breaking rules, and inter-annotator procedure |

**Sampling distribution**: 16-17 per ambiguity type, 18-24 per model (balanced within each type). Total violations pool = 614, sampled = 100. The script filters `condition=="ambiguous"` AND `violation_level in (moderate, critical)`.

---
