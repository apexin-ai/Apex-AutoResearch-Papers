# code r15 mf3 subject level rho

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r15_mf3_subject_level_rho_20260522T124300_result.json`
- **Structured JSON:** [`585e2c7fe7b6a66cf0b4.json`](../../sessions/58/585e2c7fe7b6a66cf0b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Results are strong for the paper argument:

**Key numbers:**
- Aggregate ρ = 0.9965 → looks harmless
- Mean subject-level ρ = 0.9499 → meaningful degradation
- 55/57 subjects have ρ < 0.99; 22 subjects < 0.95; 5 subjects < 0.90
- Worst: `global_facts` at ρ = 0.774 with max rank displacement of 3,258 positions
- Mean |rank change| across subjects = 304 positions

**One note:** the C% vs ρ correlation is weaker than expected (ρ = −0.186, p = 0.17) — item count per subject and specific item difficulty distributions likely moderate the relationship, so it's not a clean linear dose-response at subject level.

All three outputs are written to `artifacts/r15_subject_level_rho/`:
- `subject_level_rho_report.md` — full report
- `subject_level_rho_results.csv` — per-subject data (57 rows)
- `subject_level_rho_analysis.py` — reproducible script

---
