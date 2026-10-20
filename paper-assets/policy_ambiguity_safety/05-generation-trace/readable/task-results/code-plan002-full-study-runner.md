# code plan002 full study runner

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan002_full_study_runner_20260520T125514_result.json`
- **Structured JSON:** [`6f4a7889d7604366ffaa.json`](../../sessions/6f/6f4a7889d7604366ffaa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script is functional: loads 250 clauses across 5 types from the full template, all imports resolve, CLI works as expected. The script is a lightweight orchestration layer that reuses `harness.run_episode`, `judge.judge_episode`/`build_clause_index`/`load_episodes`, and `analyze.binarize_violations`/`cramers_v`/`per_clause_summary` directly from the existing modules.

Output structure:
- `full_study/episodes/{model_name}/episodes.jsonl`
- `full_study/judgments/{model_name}/judgments.jsonl`  
- `full_study/analysis/{full_statistics.json, per_clause_summary.csv, aggregated_rates.csv}`
- `full_study/errors.jsonl`

---
