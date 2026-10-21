# analysis w6 cross strategy per class recall

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w6_cross_strategy_per_class_recall_20260515T110628_result.json`
- **Structured JSON:** [`fbb81fa98f5ee83f2df1.json`](../../sessions/fb/fbb81fa98f5ee83f2df1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成，accuracy 全部匹配。结果汇总：

## Cross-Strategy LOO Per-Class Recall Table

| Rotation | Acc | d0-R | d1-R | d2-R | d3-R |
|---|---|---|---|---|---|
| **Pythia** |
| holdout_nucleus | 0.6935 | 1.000 | 0.443 | 0.543 | 0.788 |
| holdout_temp09 | 0.6281 | 1.000 | 0.324 | 0.395 | 0.794 |
| holdout_topk50 | 0.5151 | 1.000 | 0.922 | 0.076 | 0.062 |
| **GPT-2 XL** |
| holdout_nucleus | 0.5993 | 0.895 | 0.872 | 0.305 | 0.326 |
| holdout_temp09 | 0.5609 | 1.000 | 0.224 | **0.037** | 0.982 |
| holdout_topk50 | 0.5364 | 1.000 | 0.933 | 0.135 | 0.077 |
| **OLMo** |
| holdout_nucleus | 0.6538 | 0.980 | 0.777 | 0.397 | 0.461 |
| holdout_temp09 | 0.5816 | 1.000 | 0.254 | **0.089** | 0.984 |
| holdout_topk50 | 0.5488 | 1.000 | 0.976 | 0.191 | 0.028 |

## 关键发现

**temp09 holdout 的 d1 recall 确实异常低**（与 d1v2 AUC inversion 一致）：
- GPT-2 XL temp09: d1-R=0.224, d2-R=0.037 — 几乎所有 d2 被误分为 d3（confusion matrix: 4791/5000 → d3）
- OLMo temp09: d1-R=0.254, d2-R=0.089 — 同样 d2 大量误分为 d3（4524/5000 → d3）
- Pythia temp09: d1-R=0.324, d2-R=0.395 — 相对较好但仍是最低

**topk50 holdout 呈现相反模式**：d1 recall 极高（>0.92）但 d2/d3 recall 崩塌，说明 RF 将深层样本全部误分为 d1。

**nucleus holdout 最均衡**：各 depth recall 分布最平衡，说明 nucleus 是最"中性"的策略。

产出已保存至 `results/w6_cross_strategy_per_class_recall.json`（服务器）和 `artifacts/w6_cross_strategy_per_class/results.json`（本地）。

---
