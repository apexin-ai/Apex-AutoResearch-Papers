# ops progress check all evals

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_progress-check-all-evals_20260515T051438_result.json`
- **Structured JSON:** [`73b3459068265e77b7a4.json`](../../sessions/73/73b3459068265e77b7a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report.

---

## bjb1-32546 — Object Benchmark (6 experiments)

All 6 processes alive. All have completed **1/10 tasks**, currently midway through T2.

| Experiment | GPU | PID | Uptime | Tasks | T1 (alphabet_soup) | T2 (cream_cheese) progress |
|---|---|---|---|---|---|---|
| reconvla | cuda:0 | 9659 | 2h37m | 1/10 | **0%** (0/10) | rollout 5/10, 0/5 |
| acr-perdof | cuda:1 | 11116 | 2h35m | 1/10 | **0%** (0/10) | rollout 5/10, 0/5 |
| acr-obs-only | cuda:2 | 13806 | 2h21m | 1/10 | **0%** (0/10) | rollout 5/10, **1/5** |
| acr-scalar | cuda:3 | 14003 | 2h21m | 1/10 | **0%** (0/10) | rollout 5/10, 0/5 |
| vla-only-k1 | cuda:4 | 39397 | **3m** | 0/10 | — | just started (loading) |
| vla-mean | cuda:5 | 18808 | 2h14m | 1/10 | **0%** (0/10) | rollout 5/10, 0/5 |

**Completed baseline** (eval-vla-only-object, K=10 single): **12% overall**
- Per-task: 0%, 10%, 20%, 20%, 0%, 10%, 0%, 10%, 20%, 30%

**Observations:**
- T1 (alphabet_soup) = 0% across all methods — confirmed hard/broken task
- obs_only is the only one showing early T2 success (1/5 at midpoint)
- vla-only-k1 just restarted ~3min ago (PID 39397 replaced the original)
- Rate: ~2.5h per task → **ETA ~20h remaining** for the 5 running experiments

---

## bjb2-28827 — **Spatial** Magnitude Sweep (6 experiments)

**Note: these are running `spatial` benchmark, not object.**

All 6 alive, all completed **2/10 tasks**, currently on T3.

| Experiment | GPU | PID | Uptime | Tasks | T1 (bowl_between) | T2 (bowl_next_to) | Avg |
|---|---|---|---|---|---|---|---|
| perdof norm=0.03 | cuda:0 | 13185 | 1h59m | 2/10 | 60% | 100% | 80% |
| perdof norm=0.05 | cuda:1 | 13456 | 1h59m | 2/10 | 50% | 100% | 75% |
| perdof norm=0.20 | cuda:2 | 13728 | 1h59m | 2/10 | 60% | 90% | 75% |
| perdof norm=0.30 | cuda:3 | 14260 | 1h59m | 2/10 | 70% | 50% | 60% |
| **obsonly norm=0.05** | cuda:4 | 14854 | 1h59m | 2/10 | **80%** | **90%** | **85%** |
| **obsonly norm=0.20** | cuda:5 | 15190 | 1h59m | 2/10 | **90%** | **100%** | **95%** |

Rate: ~1h per task → **ETA ~8h remaining**

---

## Key Takeaways

1. **obs_only >> perdof on spatial** — confirmed with more data. obsonly norm=0.2 averages 95% vs perdof best 80% on first 2 tasks.

2. **Norm magnitude effects (perdof)**: non-monotonic. 0.03 best (80%), 0.3 worst (60% — T2 drops to 50%). Suggests over-correction at high norms.

3. **Norm magnitude effects (obsonly)**: larger norm = better. 0.2 (95%) > 0.05 (85%).

4. **Object benchmark T1 is still 0% across all methods** including reconvla baseline. T2 (cream_cheese) is underway; obs_only is the early leader with 1/5.

5. **vla-only-k1 on bjb1 restarted** — only 3min of uptime, will be far behind the others.

---
