# ssh collect medium uncurated metrics

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_medium_uncurated_metrics_20260513T214006_result.json`
- **Structured JSON:** [`5752ab266bdecdc94c1e.json`](../../sessions/57/5752ab266bdecdc94c1e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated, status = DONE, conclusion = success. Here's the complete report:

---

## GPT2-medium (355M) uncurated seed=42 — 完整 Metrics

| Gen | PPL | RankMe | kNN | Rare | Corr |
|-----|-------|--------|--------|--------|---------|
| 0 | 26.55 | 371.57 | 0.9880 | 0.0346 | +0.0219 |
| 1 | 35.12 | 403.80 | 0.9880 | 0.0281 | +0.0228 |
| 2 | 46.90 | 420.83 | 0.9880 | 0.0216 | +0.0181 |
| 3 | 57.40 | 425.35 | 0.9880 | 0.0185 | +0.0011 |
| 4 | 67.45 | 430.68 | 0.9880 | 0.0172 | -0.0046 |
| 5 | 78.55 | 438.62 | 0.9870 | 0.0159 | -0.0175 |
| 6 | 84.59 | 442.85 | 0.9870 | 0.0144 | -0.0462 |
| 7 | 91.66 | 443.98 | 0.9880 | 0.0139 | -0.0379 |

## 与 GPT2-small (125M) uncurated seed=42 对比

| 指标 | GPT2-small gen0→gen7 | GPT2-medium gen0→gen7 | 分析 |
|------|---------------------|----------------------|------|
| PPL | 36.01 → 50.28 (+39.6%) | 26.55 → 91.66 (+245.3%) | **Medium 崩塌远更严重**，绝对 PPL 增幅 65.11 vs small 的 14.27 |
| RankMe | 283.83 → 291.43 | 371.57 → 443.98 | Medium RankMe 更高且增长更大（+72.41 vs +7.6），表征发散更剧烈 |
| Rare | 0.027 → 0.009 (-66.7%) | 0.0346 → 0.0139 (-59.8%) | 趋势一致，medium 起点更高但衰减比例相近 |
| Corr | +0.006 → -0.088 | +0.022 → -0.038 | 都从正转负，small 终值更负 |
| kNN | 0.988 全程不变 | 0.988 几乎不变 | 两者一致，kNN 对 model collapse 不敏感 |

**核心发现**：GPT2-medium 的 PPL 恶化比 GPT2-small **显著更严重**（3.45x 增幅 vs 1.40x），表明更大模型在 uncurated self-iteration 下崩塌速度更快。这与 "larger models amplify model collapse" 的假设一致。Rare n-gram 衰减趋势相似，但 medium 的 RankMe 膨胀更大，说明表征空间在更大模型中分散得更厉害。

## 路径

- **Checkpoint**: `/root/autodl-tmp/div_cal_verify/results_medium_uncurated/uncurated/gen_7/checkpoint/`
- **Log**: `/root/autodl-tmp/div_cal_verify/medium_uncurated.log`
- **Results dir**: `/root/autodl-tmp/div_cal_verify/results_medium_uncurated/uncurated/`

---
