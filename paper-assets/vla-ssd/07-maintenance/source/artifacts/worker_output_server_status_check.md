# Server Status Check — westd-19183
**Time:** 2026-05-21 ~07:24 UTC (server time)

## Process Status

| PID | Job Name | Status | Elapsed | GPU |
|-----|----------|--------|---------|-----|
| 584349 | cf_batch_missing_v1 | **ALIVE** | 39:55 | 0 |
| 585447 | cf_batch_part2_v1 | **ALIVE** | 21:11 | 1 |
| 541379 | object_pipeline_ridge v2 | **ENDED** | — | — |

### cf_batch_missing_v1 (PID 584349)
- **Queue:** openvla/object/untrained → tracvla/spatial/untrained → tracvla/object/untrained → tracvla/goal/untrained → tracvla/long/untrained (5 tasks)
- **Task 1 (openvla/object/untrained):** DONE (27.6 min)
  - wrong=0.2308, empty=0.5688, shuffled=0.2981, paraphrased=0.0845
  - Saved → `results/libero_object_untrained/counterfactual_combined.json`
- **Task 2 (tracvla/spatial/untrained):** IN PROGRESS — condition "empty" at 3200/5000 (condition 2/4)
- **Remaining:** ~3.5 tasks → estimated ~100 min

### cf_batch_part2_v1 (PID 585447)
- **Queue:** tracvla/goal/untrained → tracvla/long/untrained (2 tasks)
- **Task 1 (tracvla/goal/untrained):** IN PROGRESS — condition "shuffled" at 3400/5000 (condition 3/4)
- **Remaining:** ~1.3 tasks → estimated ~37 min

### object_pipeline_ridge v2 (PID 541379)
- Completed in 96.3 min
- Log: `/root/runs/vla-ssd/object_pipeline_ridge_v2.log`

## GPU Utilization

| GPU | Util | VRAM Used | VRAM Total |
|-----|------|-----------|------------|
| 0 | 47% | 9,421 MiB | 97,887 MiB |
| 1 | 46% | 9,473 MiB | 97,887 MiB |

Both GPUs active, ~9.6% VRAM usage each (~H100 or A100-80GB×2).

## tmux Sessions
Could not check (tmux not in ssh_read_only whitelist).

## object_pipeline_ridge v2 Results
`/root/autodl-tmp/vla-ssd/results/libero_object/` — 6 files:

| File | Size | Modified |
|------|------|----------|
| action_r2_probing.json | 6.4K | May 21 15:23 |
| counterfactual_combined.json | 29K | May 21 16:50 |
| cross_instruction_classification.json | 1.7K | May 21 15:26 |
| l1_attention_profile.json | 4.9K | May 21 15:23 |
| pipeline.log | 4.4K | May 21 12:27 |
| rsa_analysis.json | 7.4K | May 21 15:26 |

All 6 pipeline phases completed successfully.

## Disk Usage
| Mount | Used | Available | Total | Use% |
|-------|------|-----------|-------|------|
| /root/autodl-tmp | 169G | 82G | 250G | 68% |
