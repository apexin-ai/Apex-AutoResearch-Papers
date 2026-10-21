# ssh collect epoch1 eval results

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_collect_epoch1_eval_results_20260515T140247_result.json`
- **Structured JSON:** [`b777a4bf7a26dff74ff2.json`](../../sessions/b7/b777a4bf7a26dff74ff2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

```
Epoch 1 (checkpoint-148) eval results:
- accuracy: 78.15%
- fail_recall: 23.30%  [CI: 19.1% – 27.8%]
- fail_precision: 100%
- fail_f1: 37.80%
- pass_recall: 100%
- pass_precision: 76.60%

vs Epoch 3 (final):
- accuracy: 84.45%  (Δ +6.30pp)
- fail_recall: 45.43%  (Δ +22.13pp)
- fail_f1: 62.47%  (Δ +24.67pp)
```

**结论：Epoch 1 远不如 Epoch 3。** 虽然 epoch 1 的 eval_loss 最低 (0.0679 vs 0.1121)，但实际分类性能大幅落后——accuracy 低 6.3pp，fail_recall 只有 23.3%（epoch 3 的一半）。模型在 epoch 1 时过度倾向预测 pass（pass_recall=100%, fail_recall=23.3%），到 epoch 3 才学会识别更多 fail 样本。

eval_loss 低但性能差，说明 epoch 1 模型在已答对的样本上 confidence 更高（loss 低），但覆盖面不够。Early stopping 按 eval_loss 在此场景下会选到差的 checkpoint。

---
