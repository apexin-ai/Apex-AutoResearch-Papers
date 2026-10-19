# audit table1 long provenance

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table1-long-provenance_20260525T021005_result.json`
- **Structured JSON:** [`74ee276dd13f557aeca8.json`](../../sessions/74/74ee276dd13f557aeca8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed. Here's the complete audit:

---

## Long Suite

**Seeds: 42, 43, 44** (consistent across all 3 modes)

**[Long] [VLA-only]** seeds=[42,43,44] mean=58.0±1.5% (Table 1: 58.0±1.5%) ✓
- seed 42: SR=58.0% file=eval_long_vla_only_seed42.json server=bjb1-32546 n_roll=20 ✓
- seed 43: SR=59.5% file=eval_long_vla_only_seed43.json server=cqa1-32758 n_roll=20 ✓
- seed 44: SR=56.5% file=eval_long_vla_only_seed44.json server=bjb1-32546 n_roll=20 ✓
- Recomputed: (58.0+59.5+56.5)/3=58.0%, std=1.500% → **EXACT MATCH**

**[Long] [CRM always-on]** seeds=[42,43,44] mean=55.8±1.2% (Table 1: 55.8±1.2%) ✓
- seed 42: SR=56.5% registry=eval-supp-long-crm-norm005-s42 server=bjb2-28827 n_roll=20 ✓
- seed 43: SR=54.5% file=eval_long_crm_obs_only_norm0.05_seed43.json server=bjb1-32546 n_roll=20 ✓
- seed 44: SR=56.5% file=eval_long_crm_obs_only_norm0.05_seed44.json server=cqa1-32758 n_roll=20 ✓
- Recomputed: (56.5+54.5+56.5)/3=55.83%, std=1.155% → **55.8±1.2% (rounded) ✓**

**[Long] [Adaptive/ACR-VLA]** seeds=[42,43,44] mean=57.7±1.5% (Table 1: 57.7±1.5%) ✓
- seed 42: SR=59.0% registry=eval-supp-long-adapt-tau025-s42 server=bjb2-28827 n_roll=20 trigger=3.9% ✓
- seed 43: SR=58.0% file=eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed43.json server=bjb1-32546 n_roll=20 trigger=4.5% ✓
- seed 44: SR=56.0% file=eval_long_adaptive_conformal_crm_norm0.2_tau0.25_seed44.json server=cqa1-32758 n_roll=20 trigger=4.9% ✓
- Recomputed: (59.0+58.0+56.0)/3=57.667%, std=1.528% → **57.7±1.5% (rounded) ✓**

---

## Gating

**ρ=0.9979** source: `src/calibrate_crm_signal.py` (registry: k2-l2-calibration, bjb2-28827) ✓
- Method: Spearman ρ(K=2 pairwise L2 distance, K=10 action variance)
- Data: LIBERO-Object, 10 tasks × 5 episodes, seed=42, n=14,512 timesteps
- p-value ≈ 0
- Alternative signals all failed: K1 CRM mag ρ=0.152, K2 CRM mag ρ=0.134, FMVD ρ=0.083

---

## τ-sweep

**Spatial (seed42, K=2):**
| τ | SR |
|---|---|
| 0.075 | 81.0% |
| 0.10 | 79.0% |
| 0.15 | 80.5% |
| 0.20 | 80.5% |
| **0.25** | **79.5%** |
| 0.30 | 80.5% |
| 0.35 | 80.0% |

**Goal (seed42, K=2):**
| τ | SR | trigger |
|---|---|---|
| 0.10 | 81.0% | 73.9% |
| 0.15 | 85.0% | 33.9% |
| **0.25** | **84.0%** | **8.3%** |
| 0.40 | 83.5% | 1.2% |

**τ=0.25 is NOT the single-suite optimum** (Spatial peak: 81.0% at τ=0.075; Goal peak: 85.0% at τ=0.15). It's a cross-suite compromise: low trigger rate (3-9%) prevents overcorrection while maintaining stable SR. Paper correctly frames this as "optimal region τ ∈ [0.20, 0.25]", not a single optimal point. ⚠️

---
