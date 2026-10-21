# ops piqa snapshot correction

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_piqa_snapshot_correction_20260520T222932_result.json`
- **Structured JSON:** [`b38ff51830efc42274f1.json`](../../sessions/b3/b38ff51830efc42274f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。汇总表格如下（PIQA 已改为 acc_norm，其余指标不变）：

| Config | PIQA (acc_norm) | ARC-C (acc_norm) | HellaSwag (acc_norm) | WinoGrande (acc) | TruthfulQA (mc2) | GSM8K (em) |
|---|---|---|---|---|---|---|
| base_model | 0.7612 | 0.5486 | null | 0.6456 | 0.4659 | null |
| binary_ours_seed0 | 0.7465 | 0.5196 | null | 0.6385 | 0.4359 | 0.5861 |
| binary_ours_seed1 | 0.7497 | 0.5188 | null | 0.6425 | 0.4456 | null |
| binary_ours_seed2 | 0.7476 | 0.5128 | null | 0.6409 | 0.4378 | 0.5853 |
| graduated_seed0 | 0.7530 | 0.5128 | null | 0.6488 | 0.4225 | 0.5572 |
| graduated_seed1 | 0.7503 | 0.5230 | null | 0.6440 | 0.4234 | 0.5618 |
| graduated_seed2 | 0.7497 | 0.5213 | null | 0.6456 | 0.4275 | 0.5648 |
| no_filter_seed0 | 0.7541 | 0.5128 | null | 0.6519 | 0.4224 | 0.5610 |
| no_filter_seed1 | 0.7497 | 0.5213 | null | 0.6456 | 0.4237 | null |
| no_filter_seed2 | 0.7519 | 0.5239 | null | 0.6480 | 0.4277 | 0.5671 |

**关键变化**：PIQA 从旧 snapshot 的 `acc`（如 base_model=0.7579）修正为 `acc_norm`（base_model=0.7612），差值约 +0.003。

**缺失数据**：HellaSwag 全部为 null（该 benchmark 未包含在这批 eval 中）；base_model 和部分 seed 缺少 GSM8K。

修正后 snapshot 已保存至 `/root/autodl-tmp/gen-depth-contamination/results/data_consistency_snapshot_corrected.json`。

---
