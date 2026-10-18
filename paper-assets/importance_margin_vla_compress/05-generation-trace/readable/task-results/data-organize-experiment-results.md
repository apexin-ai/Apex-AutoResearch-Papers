# data organize experiment results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_organize_experiment_results_20260517T100452_result.json`
- **Structured JSON:** [`671685ea17dca7648b82.json`](../../sessions/67/671685ea17dca7648b82.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已生成完毕。汇总如下：

**输出文件** (本地 `artifacts/` + westd-27271 `artifacts/`):
- `experiment_summary.csv` - 17 行实验数据 + header
- `experiment_summary.json` - 含 3 个模块：sim_rollout_results, acis_margin_quality, pruning_sweep

**收录的实验 (17 条 sim rollout)**:

| 类别 | 数量 | 关键结果 |
|------|------|---------|
| Baseline (full FT) | 7 | seed0: object 51%, spatial 51.8%, goal 51.6%; seed42: object 44.8%, spatial 0% |
| Stage1-only pruning | 4 | 全部 0% (ACIS/random, k=0.5/0.9, zero_mask/true_removal) |
| IMM two-stage pruning | 5 | k=0.5 ACIS: 10.4%/15.4%; k=0.7 ACIS: 4.8%; bypass: 0% |
| Merge pruning | 1 | 0% (仅 20 episodes 初步测试) |

**ACIS margin quality metrics (5 个训练版本)**:
- baseline(无 IMM): margin_mean=0.015, preservation@eps0.01=33.5%
- v8c_annealing(最优): margin_mean=1.688, preservation@eps0.01=97.5%

**Pruning sweep** (v8b, 7 个 k_ratio): sweet spot at k=0.6

---
