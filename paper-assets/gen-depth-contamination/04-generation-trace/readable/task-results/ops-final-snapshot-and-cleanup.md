# ops final snapshot and cleanup

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_final_snapshot_and_cleanup_20260521T000452_result.json`
- **Structured JSON:** [`ac372ba164fe988d42b7.json`](../../sessions/ac/ac372ba164fe988d42b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`data_consistency_snapshot_final.json` 已保存，10 个 config 全部 5 benchmarks 无 null。

完整结果：

| Config | PIQA | ARC-C | WinoG | TQA | GSM8K |
|---|---|---|---|---|---|
| base_model | 0.7612 | 0.5486 | 0.6456 | 0.4659 | 0.6224 |
| binary_ours_seed0 | 0.7465 | 0.5196 | 0.6385 | 0.4359 | 0.5861 |
| binary_ours_seed1 | 0.7497 | 0.5188 | 0.6425 | 0.4456 | 0.5853 |
| binary_ours_seed2 | 0.7476 | 0.5128 | 0.6409 | 0.4378 | 0.5853 |
| graduated_seed0 | 0.7530 | 0.5128 | 0.6488 | 0.4225 | 0.5572 |
| graduated_seed1 | 0.7503 | 0.5230 | 0.6440 | 0.4234 | 0.5618 |
| graduated_seed2 | 0.7497 | 0.5213 | 0.6456 | 0.4275 | 0.5648 |
| no_filter_seed0 | 0.7541 | 0.5128 | 0.6519 | 0.4224 | 0.5610 |
| no_filter_seed1 | 0.7497 | 0.5213 | 0.6456 | 0.4237 | 0.5716 |
| no_filter_seed2 | 0.7519 | 0.5239 | 0.6480 | 0.4277 | 0.5671 |

备注：base_model 的 GSM8K 值来自 `scores` 字段（`full` 中缺失该 benchmark 条目），其余 49 个值均从 `full` 中按指定指标提取。全部 50 个值无 null。

---
