# eval spatial bypass baseline

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_spatial_bypass_baseline_20260517T103617_result.json`
- **Structured JSON:** [`efe66db293d467e55684.json`](../../sessions/ef/efe66db293d467e55684.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已有完整结果，无需重跑。**

`full_ft_seed0_100k_libero_spatial.json` 已包含 Full FT baseline 在 libero_spatial 上的 bypass eval 结果：

| Task | Description | SR |
|------|------------|-----|
| 0 | bowl between plate and ramekin → plate | 0.60 |
| 1 | bowl next to ramekin → plate | 0.42 |
| 2 | bowl from table center → plate | 0.22 |
| 3 | bowl on cookie box → plate | 0.80 |
| 4 | bowl in top drawer → plate | 0.34 |
| 5 | bowl on ramekin → plate | 0.44 |
| 6 | bowl next to cookie box → plate | 0.66 |
| 7 | bowl on stove → plate | 0.50 |
| 8 | bowl next to plate → plate | 0.74 |
| 9 | bowl on wooden cabinet → plate | 0.46 |

**Overall: 51.8%** (259/500, 95% Wilson CI: [47.4%, 56.2%])

- Checkpoint: `checkpoints/libero_full_ft_seed0_100k/checkpoint.pt`
- Config: `configs/libero_full_ft.yaml`
- Mode: baseline (bypass, no pruning)
- 10 tasks × 50 episodes = 500 total episodes
- Seed: 42

---
