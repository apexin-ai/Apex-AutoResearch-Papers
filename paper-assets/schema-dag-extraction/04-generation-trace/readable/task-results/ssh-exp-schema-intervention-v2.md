# ssh exp schema intervention v2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp_schema_intervention_v2_20260517T153900_result.json`
- **Structured JSON:** [`a7378c3f2e523eb4cb5a.json`](../../sessions/a7/a7378c3f2e523eb4cb5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Here's the summary of the **final, corrected** Schema Intervention results:

---

## Phase 3 Results (Corrected RENAME_MAP)

| Group | Control | Treatment | Δ | t | p | Cohen's d |
|-------|---------|-----------|---|---|---|-----------|
| HIGH-BCS (n=25) | 69.3% | 60.5% | **-8.83%** | -14.61 | <0.001 | -2.92 |
| LOW-BCS (n=25) | 90.1% | 87.1% | **-2.96%** | -5.44 | <0.001 | -1.09 |

**Interaction:** Δhigh - Δlow = **-5.88pp**, t=-7.23, **p<0.001** (highly significant)

**Rename count correlation:** r=-0.625, p<0.001

---

## Key Findings

1. **Renaming hurts accuracy in both groups**, but the damage is **3x larger in high-BCS batches** (-8.83%) vs low-BCS (-2.96%).

2. **Significant interaction** (p<0.001) — the first run showed no interaction (p=0.547) because the broken renamings ("civic registration land", "birthplace domain") inflated low-BCS damage equally.

3. **Dose-response relationship**: more renamed types per batch → larger accuracy drop (r=-0.625). High-BCS batches have 3-4 renamed types each vs 0-2 in low-BCS.

4. **Interpretation**: The LLM has deeply learned the original type names. Renaming disrupts recognition even when solo accuracy is preserved (11/12 passed). The compound effect of multiple renames in a batch creates additional confusion beyond individual type-level degradation.

---
