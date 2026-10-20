# analysis w3 runtime extraction

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w3_runtime_extraction_20260515T085658_result.json`
- **Structured JSON:** [`4ca645cd32b56c80aab7.json`](../../sessions/4c/4ca645cd32b56c80aab7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `/home/ubuntu/.agent-ml-research-idea_gen_0509_6/projects/schema_semantic_constrained_ie/artifacts/rebuttal/w3_runtime_report.md`.

**Key numbers (avg inference time vs. unconstrained baseline):**

| Model | Dataset | grammar_only | full_s1 |
|-------|---------|-------------:|--------:|
| Qwen  | SciERC  | +1.4 %       | **−22.2 %** |
| Qwen  | DocRED  | +4.2 %       | +3.2 %  |
| Llama | SciERC  | —            | **+53.8 %** (+1.5 s/doc abs) |
| Llama | DocRED  | —            | +13.0 % |

- All 10 JSONLs contain `inference_time_seconds`; no re-runs needed.
- Qwen DocRED grammar_only mean is inflated by one 186 s outlier — median overhead is ~+2.6 %.
- Qwen SciERC full_s1 is *faster* than unconstrained (constraints shorten outputs).
- Post-hoc filtering reported as negligible (O(n) scan).
- Llama SciERC full_s1 has N=550 (1 doc missing vs. 551 baseline); noted in the report.
- Detailed JSON summaries saved server-side at `outputs/runtime_summary{,_detailed}.json`.

---
