# code r22 within arch temporal

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r22_within_arch_temporal_20260523T081014_result.json`
- **Structured JSON:** [`940f7b9bd360280ebc9c.json`](../../sessions/94/940f7b9bd360280ebc9c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Summary of findings:

| Lineage | N_ref (2023) | N_foc (2024) | C% |
|---------|-------------|-------------|-----|
| **Llama** | 171 | 315 | **59.2%** |
| Qwen | 27 | 70 | 6.9% |
| Yi | 72 | 14 | 3.5% |
| Phi | 60 | 20 | 1.3% |

**Key takeaway:** 3/4 lineages show C% well above random baseline (0.18–1.3%). The Llama family — the best-powered comparison — shows C% = 59.2%, nearly double the overall 31.3%. This rules out the "architecture differences drive DIF" confound: even within the same architecture lineage, item difficulty ordering shifts substantially between 2023→2024.

Outputs saved to `artifacts/r22_within_arch_temporal/`:
- `within_arch_temporal.py` — analysis script
- `within_arch_results.csv` — per-lineage results
- `within_arch_report.md` — summary with interpretation

---
