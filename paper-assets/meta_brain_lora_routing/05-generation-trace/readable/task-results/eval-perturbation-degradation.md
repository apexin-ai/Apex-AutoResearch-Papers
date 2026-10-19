# eval perturbation degradation

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_perturbation_degradation_20260516T202825_result.json`
- **Structured JSON:** [`03b7316cb908a7d9b4ac.json`](../../sessions/03/03b7316cb908a7d9b4ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All experiments complete. Here's the degradation table:

## LIBERO-Plus Perturbation Degradation Results

| Perturbation Type | Success Rate | vs Nominal (60%) | Episodes | Avg Steps |
|-------------------|-------------|------------------|----------|-----------|
| nominal (baseline) | 60% | — | 10 | ~150 |
| `_table_N` (table texture) | **50%** | -10pp | 20 | 157.8 |
| `_tb_N` (table+wall texture) | **65%** | +5pp | 20 | 145.0 |
| `_add_N` (distractor objects) | **65%** | +5pp | 20 | 140.1 |
| `_language_N` (paraphrased instr.) | **10%** | **-50pp** | 20 | 206.3 |

**Key findings:**

1. **Visual perturbations (table, tb) and spatial (add) cause minimal/no degradation** — the model is surprisingly robust to texture changes and distractor objects (50-65% vs 60% nominal).

2. **Language perturbation causes catastrophic failure** — 10% success (from 60%) when instructions are paraphrased. This is a 50pp drop, nearly complete collapse.

3. The language result is the strongest motivation for our research: the model is brittle to language variation but robust to visual/spatial changes. This suggests **language understanding is the primary vulnerability**, and LoRA routing for language adaptation is well-motivated.

Note: `_add_N` used `env.reset()` instead of nominal init_states (state dimension mismatch due to extra objects), and `_tb_N` slightly outperformed nominal — both suggest no meaningful visual degradation. The 60% nominal baseline on only 10 episodes has inherent variance, so ±5pp is within noise.

---
