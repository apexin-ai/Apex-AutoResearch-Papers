# Diagnostic: eval-supp-goal-reconvla-s45

**Date**: 2026-05-23
**Server**: bjb2-28827
**Verdict**: FALSE ALARM — experiment completed successfully

## Summary

The cron reported "Process exited without valid W&B metrics" but the evaluation actually ran to completion with no errors.

## Evidence

- **Log file**: `/tmp/eval_goal_reconvla_s45.log` (68 lines, no errors/tracebacks)
- **Output JSON**: `/root/acr-vla-conformal-refinement/logs/eval_goal_reconvla_seed45.json`
- **Overall SR**: 85.5% (171/200)
- **Registry status**: DONE, conclusion=success, SR=0.855

### Per-task results

| Task | SR |
|------|-----|
| open_the_middle_drawer_of_the_cabinet | 85.0% |
| put_the_bowl_on_the_stove | 95.0% |
| put_the_wine_bottle_on_top_of_the_cabinet | 90.0% |
| open_the_top_drawer_and_put_the_bowl_inside | 65.0% |
| put_the_bowl_on_top_of_the_cabinet | 95.0% |
| push_the_plate_to_the_front_of_the_stove | 100.0% |
| put_the_cream_cheese_in_the_bowl | 60.0% |
| turn_on_the_stove | 95.0% |
| put_the_bowl_on_the_plate | 85.0% |
| put_the_wine_bottle_on_the_rack | 85.0% |

## Root Cause

The eval script logs results to a local JSON file but does **not** log to W&B. The cron monitor checks for W&B metrics as its success signal, so it classified the run as failed despite normal completion. This is a monitoring gap, not an experiment failure.

## System Health (at diagnosis time)

- **Disk**: 14G/30G used (44%), no space issue
- **No OOM**: process completed all 200 rollouts across 10 tasks without interruption

## Action Required

- **No rerun needed** — results are valid and already in the registry
- **Consider**: updating the cron monitor to also check for local JSON output files as a success signal for eval runs that don't use W&B
