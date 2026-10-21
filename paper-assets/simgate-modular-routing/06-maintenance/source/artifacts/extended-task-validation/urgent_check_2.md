# Extended Task Validation — Urgent Check #2

**Time:** 2026-05-19  
**Server:** westb-13313

---

## 1. Overall Progress

| Task | Episodes | Target | Status |
|------|----------|--------|--------|
| boil | 20/20 | 20 | COMPLETE |
| use-thermometer | 20/20 | 20 | COMPLETE |
| find-living-thing | 15/20 | 20 | RUNNING (gpu0) |
| power-component | 16/20 | 20 | RUNNING (gpu1) |
| melt | 0/20 | 20 | CRASHED |

**Overall: 71/100 episodes done (71%)**

---

## 2. Infrastructure Status

### TMUX Sessions
- `ext-val-gpu0` — alive, running find-living-thing (created May 20 04:36)
- `ext-val-gpu1` — alive, running power-component (created May 20 04:36)
- `backbone_eval` — alive (separate experiment)
- `cap_1_7b` — alive (separate experiment)

### GPU Utilization
- GPU 0: 0% util, 28013 MiB used (VLLM::EngineCore active)
- GPU 1: 0% util, 28013 MiB used (VLLM::EngineCore active)

Note: GPU util reports 0% at query instant but inference is actively running (vLLM burst pattern). Both VLLM engines confirmed alive via `nvidia-smi`.

---

## 3. Death Rate Analysis

### boil (20 episodes)
- **Internal death rate: 55%** (11/20)
- **Deterministic death rate: 25%** (5/20)
- Labels: det-preferred=6, no-preference=14
- Signal: death_asymmetry=6, tied_alive=9, both_dead=5
- Avg score gap: 33.5

### use-thermometer (20 episodes)
- **Internal death rate: 50%** (10/20)
- **Deterministic death rate: 20%** (4/20)
- Labels: det-preferred=7, no-preference=12, internal-preferred=1
- Signal: death_asymmetry=8, tied_alive=9, both_dead=3
- Avg score gap: 30.6

### find-living-thing (15 episodes, still running)
- **Internal death rate: 47%** (7/15)
- **Deterministic death rate: 13%** (2/15)
- Labels: det-preferred=7, no-preference=8
- Signal: death_asymmetry=5, tied_alive=6, score_comparison=2, both_dead=2
- Avg score gap: 35.0

### power-component (16 episodes, still running)
- **Internal death rate: 44%** (7/16)
- **Deterministic death rate: 19%** (3/16)
- Labels: det-preferred=4, no-preference=12
- Signal: death_asymmetry=4, tied_alive=9, both_dead=3
- Avg score gap: 29.4

### Cross-Task Summary

| Task | Int Death% | Det Death% | Det-Preferred% | No-Pref% |
|------|-----------|-----------|----------------|----------|
| boil | 55% | 25% | 30% | 70% |
| use-thermometer | 50% | 20% | 35% | 60% |
| find-living-thing | 47% | 13% | 47% | 53% |
| power-component | 44% | 19% | 25% | 75% |

**Key finding:** Internal model consistently dies 2-3x more than deterministic baseline across all tasks. Death asymmetry is the dominant signal source (not score comparison).

---

## 4. Melt Status

**CRASHED** at 05:44:19 on May 20.

- Error: `vllm.v1.engine.exceptions.EngineDeadError: EngineCore encountered an issue`
- Root cause: `EngineCore proc died unexpectedly` (OOM or GPU fault)
- Crash point: `episode_level_collection.py:303` during `generate_candidate_actions`
- Result: melt directory exists but is empty (0 episodes collected)
- **No recovery attempted — melt needs manual restart**

---

## 5. ETA Estimate

- find-living-thing: 5 remaining episodes on gpu0. At ~2-3 min/episode = ~10-15 min.
- power-component: 4 remaining episodes on gpu1. At ~2-3 min/episode = ~8-12 min.
- melt: 20 episodes needed, requires manual restart on a free GPU after current tasks finish.

**Projected completion (excl. melt):** ~15-20 minutes from now for find-living-thing + power-component.  
**Melt recovery:** Must be restarted manually. Can reuse gpu0 after find-living-thing finishes.
