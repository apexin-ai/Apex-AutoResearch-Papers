# analysis ood table1 aggregation

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ood_table1_aggregation_20260522T001622_result.json`
- **Structured JSON:** [`81ae81ddffb27660e279.json`](../../sessions/81/81ae81ddffb27660e279.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Table written and registered (`art_20260522_c7700c`).

**Summary of Table 1:**

- **14 OOD evals** aggregated across 4 categories: natural training (6 seeds), interventions (A/B/C), baselines (SFT, step-indep GRPO), and 8B scale-up.
- Core finding: **Seed 4 (collapse) = 30.60% OOD** (highest 1.5B), all interventions = 10–15% (worse than natural 23–31%).
- Two evals still running: Intervention B step 5 and C' step 5 — table has placeholders for these.
- File: `artifacts/table1_ood_summary.md`

---
