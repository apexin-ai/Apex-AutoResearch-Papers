# check bjb1 spatial results d021

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1-spatial-results-d021_20260515T024536_result.json`
- **Structured JSON:** [`13b0d8f958f40f041886.json`](../../sessions/13/13b0d8f958f40f041886.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 232820 confirmed dead. All 4 eval processes alive. Here are the results:

---

## 1. eval-acr-spatial-v4-small (acr_vla, perdof, norm=0.1)
PID: 253085 | Status: **ALIVE** (6.3h elapsed) | GPU: GPU-06a5ec3b (1450 MiB)
Tasks: **5/10 completed**, running T6

| # | Task | Success Rate |
|---|------|-------------|
| T1 | between_plate_ramekin | 60% (6/10) |
| T2 | next_to_ramekin | 100% (10/10) |
| T3 | from_table_center | 10% (1/10) |
| T4 | on_cookie_box | 40% (4/10) |
| T5 | in_top_drawer | 0% (0/10) |
| T6-T10 | — | in progress |

Partial: **21/50 = 42.0%** | ETA: ~6h remaining

---

## 2. eval-acr-spatial-v4-obs-only-r2 (crm_obs_only, norm=0.1)
PID: 270097 | Status: **ALIVE** (4.4h elapsed) | GPU: GPU-79a1ce73 (4105 MiB)
Tasks: **4/10 completed**, T5 at rollout 5/10

| # | Task | Success Rate |
|---|------|-------------|
| T1 | between_plate_ramekin | 90% (9/10) |
| T2 | next_to_ramekin | 100% (10/10) |
| T3 | from_table_center | 0% (0/10) |
| T4 | on_cookie_box | 40% (4/10) |
| T5 | in_top_drawer | 0/5 so far (running) |
| T6-T10 | — | pending |

Partial: **23/40 = 57.5%** (4 tasks) | ETA: ~6h remaining

---

## 3. eval-argmin-only-spatial (reconvla, no CRM — baseline)
PID: 231426 | Status: **ALIVE** (9.0h elapsed) | GPU: GPU-bf477c88 (1414 MiB)
Tasks: **7/10 completed**, T8 at rollout 5/10

| # | Task | Success Rate |
|---|------|-------------|
| T1 | between_plate_ramekin | 60% (6/10) |
| T2 | next_to_ramekin | 100% (10/10) |
| T3 | from_table_center | 0% (0/10) |
| T4 | on_cookie_box | 30% (3/10) |
| T5 | in_top_drawer | 10% (1/10) |
| T6 | on_ramekin | 10% (1/10) |
| T7 | next_to_cookie_box | 90% (9/10) |
| T8 | on_stove | 0/5 so far (running) |
| T9-T10 | — | pending |

Partial: **30/70 = 42.9%** (7 tasks) | ETA: ~3h remaining

---

## 4. eval-acr-spatial-v4-scalar (crm_scalar, norm=0.1)
PID: 288939 | Status: **ALIVE** (1.2h elapsed) | GPU: GPU-7d267f8c (1450 MiB)
Tasks: **1/10 completed**, T2 at rollout 5/10

| # | Task | Success Rate |
|---|------|-------------|
| T1 | between_plate_ramekin | 60% (6/10) |
| T2 | next_to_ramekin | 5/5 so far (running) |
| T3-T10 | — | pending |

Partial: **6/10 = 60.0%** (1 task) | ETA: ~9h remaining

---

## Summary

| Experiment | Mode | Tasks Done | Partial SR | ETA |
|------------|------|-----------|-----------|-----|
| v4-small (perdof) | acr_vla | 5/10 | 42.0% | ~6h |
| obs-only-r2 | crm_obs_only | 4/10 | 57.5% | ~6h |
| argmin-only (baseline) | reconvla | 7/10 | 42.9% | ~3h |
| v4-scalar | crm_scalar | 1/10 | 60.0% | ~9h |

PID 232820: **CONFIRMED DEAD**

No JSON output files yet (eval_results/ contains only old logs from May 14, no new .json files).

---
