# eval generative v1 metrics

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_generative-v1-metrics_20260514T081254_result.json`
- **Structured JSON:** [`87d12d4a8472ea121cf1.json`](../../sessions/87/87d12d4a8472ea121cf1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，conclusion=success。

## 总结

**plan-002-generative-v1 评估结果（306 val samples）：**

| 指标 | generative-v1 | ablation-b (baseline) |
|---|---|---|
| eval_accuracy | **75.5%** | 65.4% |
| internal_recall | **51.9%** | 51.5% |
| f1_macro | **56.2%** | 50.9% |
| balanced_accuracy | **64.8%** | — |
| is_degenerate | false | false |

**Confusion Matrix:**
```
               det_pred   int_pred
 deterministic      217         62
      internal       13         14
```

**关键发现：**
- 模型非退化，internal_recall 达标（51.9% ≈ ablation-b）
- Overall accuracy 和 f1 均显著优于 ablation-b
- 主要弱点：internal_precision 仅 18.4%，过度预测 internal（pred 76 vs GT 27），62 个 deterministic 样本被误判
- Qwen3 thinking mode 被 SFT 有效抑制（`&lt;think>\n\n&lt;/think>`），不影响路由

---
