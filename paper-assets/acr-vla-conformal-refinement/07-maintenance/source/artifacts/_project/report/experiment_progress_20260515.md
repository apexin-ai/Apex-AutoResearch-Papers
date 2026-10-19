# Experiment Progress Snapshot — 2026-05-15

Checked at ~UTC now. All PIDs alive unless noted. ETA = estimated remaining hours from now.

| exp_id | server | PID alive? | tasks_done/10 | interim_SR | last_log_line | ETA |
|--------|--------|-----------|---------------|-----------|--------------|-----|
| eval-mag-obsonly-norm003-b2 | bjb2-40593 | ✅ (14h) | 7/10 | 44.3% (31/70) | task8 "stove" rollout 5/10 | ~6h |
| eval-acr-object-v4-default-r2 | bjb1-18228 | ✅ (1h20m) | 0/10 | — | task1 "alphabet_soup" rollout 5/10 | ~25h |
| eval-obs-only-object-seed43 | bjb1-18228 | ✅ (7h31m) | 5/10 | 10.0% (5/50) | task6 "tomato_sauce" rollout 5/10 | ~7.5h |
| eval-argmin-object-seed43 | bjb1-18228 | ✅ (7h31m) | 5/10 | 10.0% (5/50) | task6 "tomato_sauce" rollout 5/10 | ~7.5h |
| eval-perdof-object-seed43 | bjb1-18228 | ✅ (6h11m) | 4/10 | 12.5% (5/40) | finished task4 "bbq_sauce" 30% | ~9h |
| eval-mag-obsonly-norm003-object | bjb1-32546 | ✅ (2h44m) | 2/10 | 10.0% (2/20) | task3 in progress | ~11h |
| eval-vla-mean-object-seed43 | bjb1-32546 | ✅ (3h44m) | 2/10 | 0.0% (0/20) | task3 "salad_dressing" rollout 5/10 | ~11h |
| eval-scalar-object-seed43 | bjb1-32546 | ✅ (3h28m) | 2/10 | 0.0% (0/20) | task3 "cream_cheese" done 0% | ~14h |
| eval-obs-only-object-norm02-seed43-r2 | bjb1-32546 | ✅ (33m) | 0/10 | — | env loaded, no rollouts yet | ~15h |
| eval-acr-object-obs-only-default | bjb1-32546 | ✅ (1h53m) | 1/10 | 0.0% (0/10) | task2 "alphabet_soup" done 0% | ~17h |
| eval-mag-perdof-norm02-object | bjb1-32546 | ✅ (2h24m) | 1/10 | 0.0% (0/10) | task2 "cream_cheese" rollout 5/10 | ~14h |
| eval-mag-obsonly-norm03-object | bjb2-28827 | ✅ (3h01m) | 1/10 | 0.0% (0/10) | task2 "cream_cheese" rollout 5/10 | ~17h |
| eval-mag-obsonly-norm005-object | bjb2-28827 | ✅ (3h02m) | 1/10 | 0.0% (0/10) | task2 "cream_cheese" rollout 5/10 | ~17h |
| eval-mag-obsonly-norm02-object | bjb2-28827 | ✅ (7m) | 0/10 | — | env loaded, no rollouts yet | ~25h+ |
| eval-mag-perdof-norm02-object | bjb2-28827 | ❌ DEAD | 0/10 | — | env loaded only, PID 127732 gone | needs restart |
| eval-mag-perdof-norm005-object | bjb2-28827 | ✅ (2h33m) | 1/10 | 0.0% (0/10) | task2 in progress | ~22h |
| eval-mag-perdof-norm003-object | bjb2-28827 | ✅ (2h44m) | 1/10 | 0.0% (0/10) | task2 "cream_cheese" in progress | ~24h |
| eval-mag-perdof-norm03-object-r3 | bjb2-28827 | ✅ (7m) | 0/10 | — | env loaded, no rollouts yet | ~25h+ |

## Summary

- **16/18 alive and progressing normally**, 1 dead (eval-mag-perdof-norm02-object on bjb2-28827)
- **bjb2-40593** (1 exp): Nearly done, ~6h remaining. Spatial benchmark running well with 44% interim SR.
- **bjb1-18228** (4 exps): 2 at 50% done (~7.5h left), 1 at 40% (~9h), 1 just started (~25h).
- **bjb1-32546** (6 exps): 20% average progress, 11-17h remaining per experiment.
- **bjb2-28827** (7 exps): Slowest server — 2 just started (7 min), 4 at ~1/10 tasks. 17-25h+ remaining. **eval-mag-perdof-norm02-object needs restart.**

## Action Needed

1. **Restart eval-mag-perdof-norm02-object on bjb2-28827** — PID 127732 is dead, 0 tasks completed, log shows only environment loading.
