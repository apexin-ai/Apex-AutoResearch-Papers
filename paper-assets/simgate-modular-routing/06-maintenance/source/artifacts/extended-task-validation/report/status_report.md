# Extended Task Validation — Status Report

**Date**: 2026-05-20 (server time ~06:10 CST)
**Server**: westb-13313
**Purpose**: Collect counterfactual episodes on 5 excluded ScienceWorld task types to verify exclusion is not cherry-picking.

## Overall Progress

| Task | Progress | Status |
|------|----------|--------|
| boil | 20/20 | ✅ Complete |
| use-thermometer | 20/20 | ✅ Complete |
| find-living-thing | 6/20 | 🔄 Running (GPU 0, tmux: ext-val-gpu0) |
| power-component | 6/20 | 🔄 Running (GPU 1, tmux: ext-val-gpu1) |
| melt | 0/20 | ❌ Crashed (vLLM EngineDeadError) |

## Completed Task Metrics

### boil (20/20)

| Metric | Value |
|--------|-------|
| Internal death rate | 55% (11/20) |
| Deterministic death rate | 25% (5/20) |
| det-preferred | 6 (30%) |
| internal-preferred | 0 (0%) |
| no-preference | 14 (70%) |
| Det win rate (when preference exists) | 100% (6/6) |

Breakdown of no-preference: 9 tied_alive, 5 both_dead.

### use-thermometer (20/20)

| Metric | Value |
|--------|-------|
| Internal death rate | 50% (10/20) |
| Deterministic death rate | 20% (4/20) |
| det-preferred | 7 (35%) |
| internal-preferred | 1 (5%) |
| no-preference | 12 (60%) |
| Det win rate (when preference exists) | 87.5% (7/8) |

Breakdown of no-preference: 9 tied_alive, 3 both_dead.

## In-Progress Task Metrics (Partial — 6/20)

### find-living-thing (6/20, running)

| Metric | Value |
|--------|-------|
| Internal death rate | 66.7% (4/6) |
| Deterministic death rate | 33.3% (2/6) |
| det-preferred | 3 (50%) |
| internal-preferred | 0 (0%) |
| no-preference | 3 (50%) |

Rate: ~3.1 min/episode. ETA for 20/20: ~45 min from now.

### power-component (6/20, running)

| Metric | Value |
|--------|-------|
| Internal death rate | 50% (3/6) |
| Deterministic death rate | 16.7% (1/6) |
| det-preferred | 2 (33.3%) |
| internal-preferred | 0 (0%) |
| no-preference | 4 (66.7%) |

Rate: ~3.3 min/episode. ETA for 20/20: ~48 min from now.

## Crashed Task

### melt (0/20)

Crashed with `vllm.v1.engine.exceptions.EngineDeadError` during the first episode. The vLLM engine on GPU 0 died mid-run. The script continued to find-living-thing (which loaded a fresh vLLM instance).

**Restart plan**: After find-living-thing completes (~45 min), GPU 0 will be free. Run melt as a standalone task:
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/autodl-tmp/simgate-modular-routing
export SLIM_EPISODES=1
export CUDA_VISIBLE_DEVICES=0
python src/episode_level_collection.py \
    --task_types "melt" \
    --episodes 20 \
    --gpu_id 0 \
    --model_path "/root/autodl-tmp/models/Qwen/Qwen2.5-7B-Instruct" \
    --output_dir "results/extended_task_validation" \
    --start_episode 0 \
    --seed 42 \
    --max_steps 30 \
    2>&1 | tee results/extended_task_validation/logs/melt_gpu0_retry.log
```

## Summary Observations (Completed Tasks)

Across boil and use-thermometer (40 total episodes):
- **Internal routing dies more often**: avg 52.5% death rate vs. 22.5% for deterministic
- **Deterministic is preferred or equal**: det-preferred 13/40, int-preferred 1/40, no-pref 26/40
- **When there is a preference, det wins 93% of the time** (13/14)
- Pattern is consistent with the originally included tasks — these excluded tasks show the same internal-routing disadvantage, supporting the claim that exclusion was not cherry-picking

Partial results from find-living-thing and power-component (12 episodes so far) show the same trend: det-preferred in 5/12, int-preferred in 0/12.

## Next Steps

1. Wait for find-living-thing and power-component to finish (~45-50 min)
2. Restart melt on freed GPU 0
3. After all 5 tasks reach 20/20, compute final aggregated metrics and update this report
