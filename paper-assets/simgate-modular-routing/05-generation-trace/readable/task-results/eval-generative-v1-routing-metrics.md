# eval generative v1 routing metrics

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_generative-v1-routing-metrics_20260514T081258_result.json`
- **Structured JSON:** [`614c6d7d98e61ea950e4.json`](../../sessions/61/614c6d7d98e61ea950e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**plan-002-generative-v1 路由评估结果 (negative)**

| 指标 | generative-v1 | ablation-b | 对比 |
|------|:---:|:---:|:---:|
| accuracy | 70.67% | 65.4% | +5.3pp (假象：多数类偏向) |
| balanced_accuracy | 46.67% | — | 低于 50% 随机基线 |
| internal_recall | **16.67%** | **51.5%** | **-34.8pp** |
| det_recall | 76.67% | — | — |

关键发现：
1. **Qwen3 thinking 模式问题**：推理时模型默认输出 `&lt;think>\n\n&lt;/think>` 再接内容，需要 `enable_thinking=False` 或 strip thinking
2. **路由信号未学到**：模型确实输出两种格式（232 det / 68 internal），但预测与真实标签不相关。Internal recall 仅 16.67%，远低于 ablation-b 的 51.5%
3. **之前的 51.85% 可能来自 logit-level eval**，不反映实际生成行为
4. 结论：generative routing 在当前配置下 **失败**，conclusion 更新为 negative

---
