# check all servers status d021

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_all-servers-status-d021_20260515T025555_result.json`
- **Structured JSON:** [`37e48945d96a31739b0a.json`](../../sessions/37/37e48945d96a31739b0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report:

---

# Experiment Status Report — 2026-05-15 10:56 UTC

---

## [bjb1-18228] reconvla baseline — spatial (reconvla, no CRM)
PID: 231426 | Status: **ALIVE** (9h08m) | GPU 0+1
Tasks: **8/10 complete**, running task 9

| Task | Success Rate |
|------|-------------|
| between_plate_ramekin | 60% (6/10) |
| next_to_ramekin | 100% (10/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 30% (3/10) |
| in_top_drawer | 10% (1/10) |
| on_ramekin | 10% (1/10) |
| next_to_cookie_box | 90% (9/10) |
| on_stove | 0% (0/10) |

Running tally: **30/80 = 37.5%**

---

## [bjb1-18228] acr_vla v4-small — spatial (crm_v3_norm/perdof, max_norm=0.1)
PID: 253085 | Status: **ALIVE** (6h26m) | GPU 0+3
Tasks: **5/10 complete**, running task 6

| Task | Success Rate |
|------|-------------|
| between_plate_ramekin | 60% (6/10) |
| next_to_ramekin | 100% (10/10) |
| from_table_center | 10% (1/10) |
| on_cookie_box | 40% (4/10) |
| in_top_drawer | 0% (0/10) |

Running tally: **21/50 = 42.0%**

---

## [bjb1-18228] crm_obs_only v4-r2 — spatial (crm_v3_norm/obs_only, max_norm=0.1)
PID: 270097 | Status: **ALIVE** (4h35m) | GPU 0
Tasks: **4/10 complete**, on task 5 (rollout 5/10, 0/5)

| Task | Success Rate |
|------|-------------|
| between_plate_ramekin | 90% (9/10) |
| next_to_ramekin | 100% (10/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 40% (4/10) |

Running tally: **23/40 = 57.5%**

---

## [bjb1-18228] crm_scalar v4 — spatial (crm_v3_norm/scalar_unc, max_norm=0.1)
PID: 288939 | Status: **ALIVE** (1h22m) | GPU 0+2
Tasks: **2/10 complete**, running task 3

| Task | Success Rate |
|------|-------------|
| between_plate_ramekin | 60% (6/10) |
| next_to_ramekin | 100% (10/10) |

Running tally: **16/20 = 80.0%** (too early to be meaningful)

---

## [bjb1-18228] acr_vla v3 — spatial (crm_v2/perdof, NO max_norm) — STALE
PID: tmux 197056 only | Status: **DEAD** (python process gone, no GPU memory)
Tasks: 5/10 done, crashed on task 6

| Task | Success Rate |
|------|-------------|
| between_plate_ramekin | 10% (1/10) |
| next_to_ramekin | 0% (0/10) |
| from_table_center | 0% (0/10) |
| on_cookie_box | 0% (0/10) |
| in_top_drawer | 0% (0/10) |

Partial tally: **1/50 = 2.0%** — old crm_v2 checkpoint, clearly broken. Tmux session orphaned.

---

## [bjb1-32546] reconvla baseline — object (reconvla, no CRM)
PID: 9659 | Status: **ALIVE** (19m) | GPU 0
Tasks: **0/10** — model loaded, running first task (no results yet)

---

## [bjb1-32546] crm_perdof — object (crm_v3_norm/perdof, max_norm=0.1)
PID: 11116 | Status: **ALIVE** (17m) | GPU 1
Tasks: **0/10** — model loaded, running first task (no results yet)

---

## [bjb1-32546] crm_obs_only — object (crm_v3_norm/obs_only, max_norm=0.1)
PID: 13806 | Status: **ALIVE** (3m) | GPU 2
Tasks: **0/10** — model loaded, running first task (no results yet)

---

## [bjb1-32546] crm_scalar — object (crm_v3_norm/scalar_unc, max_norm=0.1)
PID: 14012 | Status: **ALIVE** (3m) | GPU 3
Tasks: **0/10** — model loaded, running first task (no results yet)

---

## [bjb2-40593] reconvla baseline — object (reconvla, n_rollouts=20, K=10)
PID: 211962 | Status: **ALIVE** (~68m) | GPU 0 (shared)
Tasks: **0/10** — model loaded, no results yet

---

## [bjb2-40593] acr_vla v4-default-r3 — spatial (crm_v3_norm/perdof, NO max_norm cap)
PID: 212690 | Status: **ALIVE** (~67m) | GPU 0 (shared)
Tasks: **0/10** — model loaded, no results yet

---

# Summary

| Server | Experiment | Benchmark | Mode | Tasks Done | Running Tally | ETA |
|--------|-----------|-----------|------|-----------|--------------|-----|
| bjb1-18228 | reconvla baseline | spatial | reconvla | 8/10 | 37.5% | ~2h |
| bjb1-18228 | v4-small | spatial | acr_vla (perdof, norm=0.1) | 5/10 | 42.0% | ~6h |
| bjb1-18228 | v4-obs-only-r2 | spatial | crm_obs_only (norm=0.1) | 4/10 | 57.5% | ~7h |
| bjb1-18228 | v4-scalar | spatial | crm_scalar (norm=0.1) | 2/10 | 80.0%* | ~6h |
| bjb1-18228 | v3 (old) | spatial | acr_vla (crm_v2) | 5/10 | 2.0% | **DEAD** |
| bjb1-32546 | reconvla | object | reconvla | 0/10 | — | ~3h |
| bjb1-32546 | perdof | object | crm_perdof (norm=0.1) | 0/10 | — | ~3h |
| bjb1-32546 | obs_only | object | crm_obs_only (norm=0.1) | 0/10 | — | ~3h |
| bjb1-32546 | scalar | object | crm_scalar (norm=0.1) | 0/10 | — | ~3h |
| bjb2-40593 | reconvla | object | reconvla (n=20) | 0/10 | — | ~6h+ |
| bjb2-40593 | v4-default-r3 | spatial | acr_vla (perdof, no norm cap) | 0/10 | — | ~10h+ |

\* crm_scalar 80% based on only 2 tasks — will drop as harder tasks come in.

**Key observations:**
- **obs_only leads on spatial** at 57.5% (4 tasks), vs baseline 37.5% (8 tasks) and perdof 42.0% (5 tasks)
- The v3 run (crm_v2 checkpoint) is dead at 2% — confirms crm_v2 was broken, crm_v3_norm is the correct checkpoint
- bjb1-32546 all 4 object experiments just started (~20m), no task results yet
- bjb2-40593 both experiments just started (~1h), sharing 1 GPU — will be slow
- bjb1-32546 has GPUs 4+5 completely idle

---
