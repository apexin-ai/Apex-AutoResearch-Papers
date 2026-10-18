# analyze eval openvla random k07 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_random_k07_long_seed42_v2_20260526T025335_result.json`
- **Structured JSON:** [`507b2dd6be548cbc11eb.json`](../../sessions/50/507b2dd6be548cbc11eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验结果汇总

**Overall SR: 38.8% (194/500)** | 耗时 516.7 min | 无错误

### Per-task SR

| Task | SR | Successes |
|------|----|-----------|
| alphabet soup + tomato sauce → basket | 48.0% | 24/50 |
| cream cheese + butter → basket | 46.0% | 23/50 |
| stove + moka pot | 58.0% | 29/50 |
| black bowl → drawer + close | 34.0% | 17/50 |
| white mug left + yellow mug right plate | 14.0% | 7/50 |
| book → caddy | 68.0% | 34/50 |
| white mug plate + chocolate pudding | 42.0% | 21/50 |
| alphabet soup + cream cheese → basket | 34.0% | 17/50 |
| both moka pots → stove | 24.0% | 12/50 |
| yellow mug → microwave + close | 20.0% | 10/50 |

### 与 k=0.9 对比

| 配置 | Overall SR | Δ vs baseline (52.8%) |
|------|-----------|----------------------|
| Baseline (no prune) | 52.8% | — |
| Random k=0.9 | 46.8% | -6.0pp |
| **Random k=0.7** | **38.8%** | **-14.0pp** |

k=0.9→k=0.7 下降 8.0pp，衰减速率 ~4.0pp/0.1k，明显快于 baseline→k=0.9 的 ~6.0pp/0.1（即 ~2.0pp/0.1k 线性外推）。**确认 cliff zone 存在**：random pruning 在保留比例降至 0.7 时加速退化，为 importance-based pruning 在此区间的优势提供了更强的 baseline 对照。

---
