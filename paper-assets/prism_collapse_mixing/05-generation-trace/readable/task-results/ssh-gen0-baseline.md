# ssh gen0 baseline

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gen0-baseline_20260515T175938_result.json`
- **Structured JSON:** [`347c3bc3f480984ff290.json`](../../sessions/34/347c3bc3f480984ff290.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 seed 的 Gen 0 baseline 信号计算全部完成。结果完全相同（符合预期，因为同一模型 checkpoint）。

## Gen 0 Baseline 结果

### Aggregated (per-example 信号)
| 指标 | mean | std |
|------|------|-----|
| loss | 3.1565 | 0.5186 |
| entropy | 3.1564 | 0.4432 |
| spectral_rank | 163.72 | 8.65 |

### Corpus-level 辅助信号
| 指标 | 值 |
|------|------|
| sigma_spectral_rank | 4.42 |
| distinct-1 | 0.0387 |
| distinct-2 | 0.3412 |
| distinct-3 | 0.6871 |

### Spearman 相关
| 对 | ρ | p-value |
|---|---|---------|
| loss ↔ entropy | 0.9292 | 0.0 |
| loss ↔ spectral_rank | -0.2110 | 0.0 |

### 运行信息
- num_probe_samples: 5000
- seed42 运行耗时: ~18 min（per-example ~12 min + distinct-n ~6 min）
- seed137 运行耗时: ~20 min（稍慢，因与 build_train.py 共用 GPU 资源）
- 两个 seed 结果完全一致（per-example loss/entropy/spectral_rank 逐元素相同），distinct-n 也相同（Gen 0 的 seed 只影响生成采样，但因为模型相同且 seed 设在生成前，实际输出一致）
- 产出文件: `results/signals_gen0_seed42.json`, `results/signals_gen0_seed137.json`

---
