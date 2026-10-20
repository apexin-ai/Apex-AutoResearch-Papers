# ops cleanup and extract

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup-and-extract_20260514T035244_result.json`
- **Structured JSON:** [`9d812aa193a552685348.json`](../../sessions/9d/9d812aa193a552685348.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part 1: GPU 清理 ✓

| GPU | 清理前 | 清理后 |
|-----|--------|--------|
| cuda:0 | 57390 MiB (89%) | **0 MiB (0%)** |
| cuda:1 | 57390 MiB (94%) | **0 MiB (0%)** |
| cuda:2 | 27719 MiB (78%) | 27719 MiB (不动) |
| cuda:3 | 27719 MiB (96%) | 27719 MiB (不动) |

已 kill 的进程: 59328, 60514, 59616, 60915
已 kill 的 tmux sessions: `mvp_v5_random_s020`, `mvp_v5_random_s030`
保留: `v6_importance_s025`, `v6_importance_s030` (cuda:2/3)

### Part 2: Random Metrics

#### random_s020 (sparsity=0.2, 50 problems)

| Phase | II mean | II median | CI low | CI high | outliers |
|-------|---------|-----------|--------|---------|----------|
| high_sparsity | 0.8556 | 0.3213 | -0.1241 | 1.6169 | 3 |
| mid_sparsity | 1.2581 | 0.4557 | 0.6749 | 2.0756 | 1 |
| low_sparsity | 0.9569 | 0.5919 | 0.5839 | 1.4134 | 1 |

Perplexity (high/mid/low phase):
- dense: 1.146 / 1.123 / 1.111
- attn: 5.082 / 1.628 / 17.097
- kv: 4.254 / 4.306 / 5.405
- both: 7.975 / 6.855 / 22.587

Pass/fail: **FAIL** (ci_overlap + sign_reversal both fail)

#### random_s030 (sparsity=0.3, 50 problems)

| Phase | II mean | II median | CI low | CI high | outliers |
|-------|---------|-----------|--------|---------|----------|
| high_sparsity | 22.7345 | 5.3775 | 10.3521 | 42.5520 | 1 |
| mid_sparsity | 10.9433 | 5.8865 | 7.3986 | 14.7653 | 2 |
| low_sparsity | 11.8404 | 3.7768 | 4.0973 | 23.5453 | 1 |

Perplexity (high/mid/low phase):
- dense: 1.146 / 1.123 / 1.111
- attn: 11.494 / 4.092 / 19.251
- kv: 8.103 / 8.570 / 13.492
- both: 41.345 / 24.199 / 68.530

Pass/fail: **FAIL** (ci_overlap + sign_reversal both fail)

---
