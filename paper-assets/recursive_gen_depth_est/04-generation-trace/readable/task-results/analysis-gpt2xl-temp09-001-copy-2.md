# analysis gpt2xl temp09 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt2xl_temp09_001_20260514T224201_result.json`
- **Structured JSON:** [`61d355cb04c7e565268d.json`](../../sessions/61/61d355cb04c7e565268d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（已有 metrics/conclusion/notes，状态更新为 DONE）。

## gpt2xl_temp09_001 分析结果

### 核心指标

| Metric | Temp τ=0.9 | Nucleus p=0.95 (baseline) | Δ |
|--------|-----------|--------------------------|---|
| 4-class RF acc | **85.4%** [84.3, 86.5] | 83.3% [82.3, 84.5] | **+2.1pp** |
| 4-class LR acc | 81.6% [80.3, 82.7] | — | — |
| 3-class RF acc | **82.0%** [80.6, 83.4] | 79.3% [77.8, 80.6] | **+2.7pp** |
| 3-class filtered RF | 81.5% [80.0, 83.0] | — | — |
| AUC d1v2 (RF) | **0.937** | 0.913 | +0.024 |
| AUC d2v3 (RF) | 0.882 | 0.883 | -0.001 |

### Finetune Loss
- depth-1: 2.5498, depth-2: 1.6972, depth-3: 1.2922（逐层递减，符合预期）

### Feature Importance 对比

| Rank | Temp τ=0.9 | Nucleus p=0.95 |
|------|-----------|---------------|
| 1 | p90_ppl (0.263) | p90_ppl |
| 2 | mean_surprisal (0.148) | var_surprisal |
| 3 | p75_ppl (0.146) | p75_ppl |
| 4 | var_surprisal (0.121) | mean_surprisal |
| 5 | p50_ppl (0.057) | mean_ppl |

Top-4 特征完全一致（顺序微调），PPL 分位数和 surprisal 统计量主导分类。

### Code Contamination
- Filtered vs unfiltered 差距极小（82.0% → 81.5%），contamination 影响可忽略。

### 结论：**SUCCESS**

Temperature-only τ=0.9 不仅与 nucleus p=0.95 一致，还略优（+2.1pp）。深度信号对解码策略鲁棒。注意这与 Pythia 结果方向相反（Pythia temp09 降 1.9pp），说明解码策略影响是模型依赖的。

---
