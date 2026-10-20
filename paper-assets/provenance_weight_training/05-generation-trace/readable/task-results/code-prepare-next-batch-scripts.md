# code prepare next batch scripts

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare-next-batch-scripts_20260514T011050_result.json`
- **Structured JSON:** [`0ad9abd9ff2d0b8fb9a4.json`](../../sessions/0a/0ad9abd9ff2d0b8fb9a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 个脚本已创建并通过语法检查，未启动任何训练：

| 脚本 | 方法 | seed | 输出目录 |
|------|------|------|----------|
| `run_grid_b_seed123.sh` | grid (6 个 b 值串行) | 123 | `output/models/grid_b{X}_seed123` |
| `run_grid_b_seed456.sh` | grid (6 个 b 值串行) | 456 | `output/models/grid_b{X}_seed456` |
| `run_adaptive_seed42.sh` | adaptive | 42 | `output/models/adaptive_seed42` |
| `run_adaptive_seed123.sh` | adaptive | 123 | `output/models/adaptive_seed123` |
| `run_adaptive_seed456.sh` | adaptive | 456 | `output/models/adaptive_seed456` |

所有脚本参数与 seed42 grid-b 保持一致（200M tokens, batch 4, grad_accum 4, max_length 2048, lr 5e-5, contamination_ratio 0.4）。adaptive 脚本用 `--weighting_method adaptive` 替换了 grid 相关参数。

---
