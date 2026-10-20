# Extended Task Validation — Final Status Report

**Date**: 2026-05-19  
**Server**: westb-13313  
**Model**: Qwen2.5-7B-Instruct  
**Config**: 20 episodes/task, seed=42, max_steps=30

## Task Completion Status

| Task | Episodes | Status |
|------|----------|--------|
| boil | 20/20 | Complete |
| use-thermometer | 20/20 | Complete |
| find-living-thing | 20/20 | Complete |
| power-component | 20/20 | Complete |
| melt | 0/20 | Rerun started (2026-05-20 07:18 UTC) |

## Death Rate Analysis (4 Completed Tasks)

### Summary Table

| Task | Int DR | Det DR | ΔDR (Int−Det) | D (det-pref) | I (int-pref) | N (no-pref) |
|------|--------|--------|---------------|--------------|--------------|-------------|
| boil | 55% (11/20) | 25% (5/20) | +30% | 6 | 0 | 14 |
| use-thermometer | 50% (10/20) | 20% (4/20) | +30% | 7 | 1 | 12 |
| find-living-thing | 55% (11/20) | 15% (3/20) | +40% | 10 | 0 | 10 |
| power-component | 50% (10/20) | 15% (3/20) | +35% | 7 | 0 | 13 |
| **Average** | **52.5%** | **18.75%** | **+33.75%** | **7.5** | **0.25** | **12.25** |

### Key Observations

1. **Consistent internal > deterministic death asymmetry**: All 4 tasks show ΔDR ≥ 30%, confirming the pattern seen in training tasks. Internal routing leads to substantially more deaths.
2. **Deterministic almost never loses**: Only 1 episode across all 80 (use-thermometer ep3) was internal-preferred via death asymmetry (det died, int survived). The overwhelming direction is int_died_det_alive.
3. **High no-preference rate**: Most episodes (61.25%) show no preference, driven by tied_alive or both_dead outcomes. The signal comes from the ~30-50% of episodes where death asymmetry occurs.
4. **find-living-thing is worst**: Highest ΔDR (40%) and most det-preferred labels (10/20 = 50%), suggesting this task type is especially punishing for internal routing.

### Per-Task Detailed Breakdown

#### boil (20 episodes)
- Deaths: 11 internal, 5 deterministic (5 both_dead, 6 int-only)
- Outcomes: 6 det-preferred (all death_asymmetry), 0 int-preferred, 14 no-preference
- No-preference split: 7 tied_alive, 5 both_dead, 2 tied_alive (with score>0)

#### use-thermometer (20 episodes)
- Deaths: 10 internal, 4 deterministic (3 both_dead, 7 int-only, 1 det-only)
- Outcomes: 7 det-preferred (all death_asymmetry), 1 int-preferred (ep3: det died, int alive), 12 no-preference
- Notable: Only task with an internal-preferred episode

#### find-living-thing (20 episodes)
- Deaths: 11 internal, 3 deterministic (3 both_dead, 8 int-only)
- Outcomes: 8 det-preferred (death_asymmetry) + 2 det-preferred (score_comparison), 0 int-preferred, 10 no-preference
- Notable: 2 episodes where both survived but det scored higher (eps 2, 13)

#### power-component (20 episodes)
- Deaths: 10 internal, 3 deterministic (3 both_dead, 7 int-only)
- Outcomes: 7 det-preferred (6 death_asymmetry + 1 death_asymmetry with high score gap), 0 int-preferred, 13 no-preference
- Notable: ep15 had det_final=57, ep5 had det_final=13 — deterministic sometimes achieves meaningful scores

## Melt Rerun

- **Status**: Launched in tmux session `ext-val-melt` at 2026-05-20 07:18 UTC
- **GPU**: cuda:0 (CUDA_VISIBLE_DEVICES=0)
- **Script**: `scripts/run_extended_validation_melt.sh`
- **Command**: `python src/episode_level_collection.py --task_types melt --episodes 20 --gpu_id 0 --model_path /root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct --output_dir results/extended_task_validation --start_episode 0 --seed 42 --max_steps 30`
- **Estimated time**: ~60-90 min (based on other single-task runs)
- **Monitor**: `tmux attach -t ext-val-melt` or check `results/extended_task_validation/melt/episode_summary.jsonl`
