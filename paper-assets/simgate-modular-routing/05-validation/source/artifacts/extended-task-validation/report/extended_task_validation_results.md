# Extended Task Validation Results (Interim)

**Status**: 2/5 tasks COMPLETE, 2/5 IN PROGRESS, 1/5 FAILED  
**Server**: westb-13313  
**Start time**: 2026-05-20 04:36  
**Snapshot time**: 2026-05-20 06:00  
**Results path**: `/root/autodl-tmp/simgate-modular-routing/results/extended_task_validation/`

---

## Task Status Overview

| Task | GPU | Episodes | Status |
|------|-----|----------|--------|
| boil | 0 | 20/20 | ✅ COMPLETE |
| melt | 0 | 0/20 | ❌ FAILED (EngineDeadError) |
| find-living-thing | 0 | 4/20 | 🔄 RUNNING |
| use-thermometer | 1 | 20/20 | ✅ COMPLETE |
| power-component | 1 | 4/20 | 🔄 RUNNING |

### melt failure
VLLM EngineCore proc died unexpectedly during `run_episode_deterministic()` at step `generate_candidate_actions`. Crash in `vllm.v1.engine.core_client.ensure_alive()`. Script caught the error and proceeded to find-living-thing.

---

## Completed Task Analysis

### BOIL (n=20)

| Metric | Value |
|--------|-------|
| internal_death_rate | 55% (11/20) |
| det_death_rate | 25% (5/20) |
| **ΔDR** | **+30pp** |
| D (det-preferred) | 6 |
| I (internal-preferred) | 0 |
| N (no-preference) | 14 |
| Δ_full | 0.30 |
| Δ_nd | 1.00 (6/6) |
| DAF (death-asymmetry fraction) | 0.30 (6/20) |

Episode breakdown:
- int_died_det_alive: 6 (eps 0,3,4,5,16,17)
- both_dead: 5 (eps 7,9,12,15,18)
- tied_alive: 7 (eps 1,6,8,10,13,14,19)
- both_alive_same_score: 2 (eps 2,11 — both scored 3.0)
- det_died_int_alive: 0

### USE-THERMOMETER (n=20)

| Metric | Value |
|--------|-------|
| internal_death_rate | 50% (10/20) |
| det_death_rate | 20% (4/20) |
| **ΔDR** | **+30pp** |
| D (det-preferred) | 7 |
| I (internal-preferred) | 1 |
| N (no-preference) | 12 |
| Δ_full | 0.30 |
| Δ_nd | 0.75 (6/8) |
| DAF (death-asymmetry fraction) | 0.40 (8/20) |

Episode breakdown:
- int_died_det_alive: 7 (eps 0,4,5,7,9,12,15)
- det_died_int_alive: 1 (ep 3)
- both_dead: 3 (eps 16,17,18)
- tied_alive: 7 (eps 1,6,8,10,14,19)
- both_alive_same_score: 2 (eps 2,11 — scored 3.0; ep 13 — scored 3.0)

Note: ep 13 also tied at 3.0. Actually 3 eps tied at 3.0 (eps 2, 11, 13).

---

## In-Progress Task Snapshots

### FIND-LIVING-THING (n=4/20, partial)

| Metric | Value (partial) |
|--------|-----------------|
| internal_death_rate | 50% (2/4) |
| det_death_rate | 0% (0/4) |
| **ΔDR** | **+50pp** |
| D / I / N | 3 / 0 / 1 |

- ep 0: int=-100, det=0 (int_died_det_alive)
- ep 1: int=0, det=0 (tie)
- ep 2: int=8, det=17 (both_alive_det_wins)
- ep 3: int=-100, det=0 (int_died_det_alive)

### POWER-COMPONENT (n=4/20, partial)

| Metric | Value (partial) |
|--------|-----------------|
| internal_death_rate | 25% (1/4) |
| det_death_rate | 0% (0/4) |
| **ΔDR** | **+25pp** |
| D / I / N | 1 / 0 / 3 |

- ep 0: int=-100, det=0 (int_died_det_alive)
- ep 1: int=0, det=0 (tie)
- ep 2: int=0, det=0 (tie)
- ep 3: int=0, det=0 (tie)

---

## Prescreening Consistency Check

| Task | Prescreening ΔDR (n=5) | Full ΔDR (n=20) | Consistent? |
|------|------------------------|-----------------|-------------|
| boil | +30pp | **+30pp** | ✅ exact match |
| melt | +40pp | FAILED | ❌ no data |
| find-living-thing | ~+20pp | +50pp (n=4) | ⚠️ partial, direction consistent, magnitude higher |
| use-thermometer | ~+30pp | **+30pp** | ✅ exact match |
| power-component | ~+30pp | +25pp (n=4) | ⚠️ partial, direction consistent |

**Direction consistency**: All tasks with data show ΔDR > 0 (internal dies more than det), matching prescreening direction for all 4/4 available tasks.

---

## Key Observations

1. **Death asymmetry is robust for boil and use-thermometer**: At n=20, both confirm internal routing causes 30pp higher death rate than deterministic. Zero episodes where det died but internal survived (boil). Only 1 such episode in use-thermometer.

2. **No "internal-preferred" episodes in boil**: D=6, I=0. When routing makes a difference, it always hurts.

3. **use-thermometer shows rare det failure**: 1/20 episodes where det died and internal survived (ep 3), showing the effect is not perfectly one-directional.

4. **High "no-preference" rate**: 70% (boil) and 60% (use-thermometer) of episodes show no discriminative signal — both conditions produce identical outcomes. The 30% that do discriminate strongly favor det.

5. **melt needs restart**: VLLM EngineCore crash, need to re-run melt separately after current tasks finish.
