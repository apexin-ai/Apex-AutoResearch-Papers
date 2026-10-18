# analysis qwen25 14b temp09

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen25_14b_temp09_20260520T035840_result.json`
- **Structured JSON:** [`a3f779997613b4f2dbc5.json`](../../sessions/a3/a3f779997613b4f2dbc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析结果

### 核心指标

| 指标 | 值 |
|------|-----|
| RF 4-class acc | **50.5%** [49.76%, 51.24%] |
| LR 4-class acc | 48.65% [48.01%, 49.38%] |
| RF 3-class (no d0) | 52.44% [51.61%, 53.23%] |
| Pairwise AUC mean | 78.28% |

### Pairwise AUC

| 对 | AUC |
|----|-----|
| d0v1 | 0.632 |
| d0v2 | 0.918 |
| d0v3 | **0.958** |
| d1v2 | 0.726 |
| d1v3 | 0.845 |
| d2v3 | 0.618 |

### 与参考值对比

- RF 4-class: 50.5% vs scale_002 nucleus 54.05% → **低 3.55pp**
- Pairwise AUC mean: 78.28% vs 参考 78.4% → **几乎一致**
- 远超 25% random baseline (2×)

### Hypothesis 验证: **PARTIAL SUCCESS**

- 深度信号在 τ=0.9 temperature sampling 下明确存在（2× random baseline）
- 4-class accuracy 略低于 nucleus（50.5% vs 54.05%），但 pairwise AUC 结构几乎完全一致
- 足以支持 Claim 2（Atlas 覆盖 3 种解码策略），信号存在但略有衰减
- Top features: 尾部分布统计量（p90_ppl, skew_ppl, kurt_ppl）

报告已注册: `art_20260520_312d80`

---
