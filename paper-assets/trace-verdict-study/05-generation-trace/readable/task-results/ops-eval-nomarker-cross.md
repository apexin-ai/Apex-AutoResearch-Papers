# ops eval nomarker cross

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-nomarker-cross_20260522T172609_result.json`
- **Structured JSON:** [`fa6b5949c010bdee8066.json`](../../sessions/fa/fa6b5949c010bdee8066.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。结果如下：

## nomarker_cross_he2mbpp 评估结果

| 指标 | nomarker (本次) | 有标记版本 (对比) |
|------|----------------|-----------------|
| **Accuracy** | **95.5%** (95% CI: [94.8%, 96.1%]) | 99.41% |
| Majority baseline | 69.0% (always predict 'pass') | — |
| Lift over majority | +26.4pp | — |

**Per-class metrics:**

| 类别 | Precision | Recall | F1 |
|------|-----------|--------|-----|
| pass | 0.99 | 0.94 | 0.97 |
| fail | 0.88 | 0.99 | 0.93 |

**对比：** 无标记版本 (95.5%) 比有标记版本 (99.41%) 低 **3.9pp**。主要损失在 pass 类的 recall（0.94）和 fail 类的 precision（0.88）——即模型倾向于过度预测 fail，一部分 pass 样本被误判为 fail。

结果已保存至 `/root/autodl-tmp/trace-verdict-study-checkpoints/nomarker_cross_he2mbpp/final/eval_results.json`。

---
