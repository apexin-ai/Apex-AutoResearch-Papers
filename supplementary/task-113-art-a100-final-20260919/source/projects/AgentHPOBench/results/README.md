# Results

Raw experiment directories are excluded because they contain large checkpoints, caches, and duplicated upstream artifacts.

Aggregation scripts write derived artifacts to `results/summary/`, including:

- aggregate per-agent metrics;
- multiseed means and standard deviations;
- trajectory plotting inputs;
- ablation summaries;
- task-level provenance indexes.

These generated files are intentionally not tracked by Git. Every aggregate
should be reproducible from validated result JSON files and state the source
run tags and seeds.

Generate a matrix from a curated run manifest with:

```bash
python3 analysis/generate_leaderboard.py \
  --runs-config configs/result_runs.example.json \
  --output-dir results/summary
```
