# Few-shot BCS Experiment Status

**Status**: COMPLETED (2026-05-17 20:10:03)
**Server**: cqa1-38874
**tmux session**: fewshot_bcs (engine shut down)

## Batches
12/12 completed: {count_8, count_16} x {low_bcs, high_bcs} x {0shot, 1shot, 5shot}

## Results (accuracy gap = low_bcs - high_bcs)

| Setting | count_8 | count_16 |
|---------|---------|----------|
| 0-shot  | gap=-0.0938 (low=0.8854, high=0.7917) | gap=0.0000 (low=0.7760, high=0.7760) |
| 1-shot  | gap=-0.2083 (low=0.9062, high=0.6979) | gap=-0.0052 (low=0.7552, high=0.7500) |
| 5-shot  | gap=-0.1250 (low=0.8958, high=0.7708) | gap=0.0000 (low=0.7969, high=0.7969) |

**Note**: Negative gap means low-BCS outperforms high-BCS.

## Output Files
- `eval_results.json` (22KB)
- `predictions.json` (1.3MB)
- `preprocess.json` (287KB)
- `run.log` (55KB)

## GPU
- 1x GPU, 89377/97887 MiB used, 16% util (post-experiment idle)
