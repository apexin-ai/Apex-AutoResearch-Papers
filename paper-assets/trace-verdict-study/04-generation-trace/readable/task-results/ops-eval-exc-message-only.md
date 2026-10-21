# ops eval exc message only

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_eval-exc-message-only_20260522T131430_result.json`
- **Structured JSON:** [`e8313de303a0e544b5d1.json`](../../sessions/e8/e8313de303a0e544b5d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exc_message_only_seed42 评估结果：**

| 指标 | 值 |
|---|---|
| accuracy | 0.9950 |
| pass_f1 | 0.9965 |
| fail_f1 | 0.9912 |
| pass_precision | 1.0000 |
| pass_recall | 0.9929 |
| fail_precision | 0.9826 |
| fail_recall | 1.0000 |
| n_test | 1190 |

尽管 eval_loss=0.58 远高于 exc_type_only 和 exc_stacktrace_only，准确率依然达到 99.5%，与其他 exc 子组件模型差距很小。fail_recall 满分，pass_precision 满分，分类性能非常强。

---
