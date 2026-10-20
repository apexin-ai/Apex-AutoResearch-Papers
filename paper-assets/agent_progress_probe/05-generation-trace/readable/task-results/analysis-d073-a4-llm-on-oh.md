# analysis d073 a4 llm on oh

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d073-a4-llm-on-oh_20260516T025428_result.json`
- **Structured JSON:** [`8b8e2539817dbc4a6138.json`](../../sessions/8b/8b8e2539817dbc4a6138.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here are the final results:

## LLM Judge on OpenHands — Results

| Method | macro_F1 | f1_stag | f1_prog | accuracy | cost |
|--------|----------|---------|---------|----------|------|
| LLM zero-shot | 0.491 | 0.134 | 0.848 | 0.742 | ~$3 |
| LLM few-shot-CoT | 0.470 | 0.055 | 0.884 | 0.794 | ~$11 |
| **Structural GB (all)** | **0.967** | — | — | — | $0 |
| **Structural GB (c≥2)** | **0.992** | — | — | — | $0 |

**Key findings:**

1. **Structural advantage: +47.6pp** (all) / **+50.1pp** (conf≥2) — massive gap
2. LLM judge on OH is dramatically worse than on SWE (zero-shot 0.491 vs 0.663, few-shot-CoT 0.470 vs 0.799) — the LLM judge doesn't transfer across agent architectures
3. Few-shot-CoT actually performed *worse* than zero-shot on OH (0.470 vs 0.491) — the SWE few-shot examples are misleading on OH data
4. Both LLM modes are near-random for stagnation detection (f1_stag = 0.134/0.055) — the LLM overwhelmingly predicts "progress"
5. Total evaluation cost: ~$14 for 500 windows in 2 modes
6. Sample: 500 windows stratified from 43,376 OH conf≥2 (401 prog / 99 stag, matching ~20% stag rate)

This strongly supports the C1-structural claim: structural features provide robust cross-agent transfer (SWE→OH) while LLM-as-Judge collapses on out-of-distribution agent trajectories.

---
