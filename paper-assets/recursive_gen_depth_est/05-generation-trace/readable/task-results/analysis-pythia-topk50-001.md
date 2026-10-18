# analysis pythia topk50 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pythia_topk50_001_20260514T201559_result.json`
- **Structured JSON:** [`a4d6baeb9898e2a4e741.json`](../../sessions/a4/a4d6baeb9898e2a4e741.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## pythia_topk50_001 分析报告

### 结论: **SUCCESS** (PASS, 但信号衰减)

### 核心指标

| 指标 | topk50 | baseline (nucleus) | temp09 | Δ vs baseline |
|------|--------|-------------------|--------|--------------|
| RF 4-class acc | **69.6%** | 78.2% | 76.25% | **-8.6pp** |
| RF 3-class acc | **59.2%** | 70.8% | 69.83% | **-11.6pp** |
| RF 3-class filtered | **61.3%** | — | — | — |
| d1v2 AUC | **0.7518** | 0.8607 | 0.8327 | -0.109 |
| d2v3 AUC | **0.6918** | 0.8005 | 0.7928 | -0.109 |

### Feature importance
Top-5 与 baseline **完全一致**: var_surprisal, p90_ppl, mean_ppl, mean_surprisal, p75_ppl

### Code contamination (narrow)
d0=0.4%, d1=7.7%, d2=12.3%, d3=13.1%。Filtered 性能反而略高 (61.3% vs 59.2%)，code 非主因。

### Finetune loss
d0=2.2406, d1=1.6704, d2=1.4374（递减趋势正常）

### 判定
- PASS 条件满足: 4-class acc 69.6% > 40%, d1v2 AUC 0.7518 > 0.6
- 与 baseline 差距 8.6pp > 5pp 阈值，**跨策略泛化定性成立但定量存在衰减**
- 信号强度排序: **nucleus p=0.95 > temperature 0.9 > top-k k=50**
- 三种策略下 feature importance 排序一致，深度信号的统计特征模式相同，差异仅在强度

---
