# ops harvest tail2048 v3 and check qwen7b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest_tail2048_v3_and_check_qwen7b_20260518T114417_result.json`
- **Structured JSON:** [`9cd5fb4f0689c483cccf.json`](../../sessions/9c/9cd5fb4f0689c483cccf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 eval 完成。结果汇总：

```
[CodeLlama tail-2048 v3]
Epoch 3 accuracy: 41.8% (pass_f1=0.416, fail_f1=0.421)  ← 低于 majority baseline 71.5%
Epoch 1 accuracy:  7.1% (pass_f1=0.035, fail_f1=0.342)  ← 几乎未学习

[Qwen-7B head-2048]
状态: 训练完成 (444/444 steps)
Epoch 3 accuracy: 81.0% (pass_f1=0.866, fail_f1=0.674)  ← baseline+9.5%
Epoch 1 accuracy: 81.6% (pass_f1=0.870, fail_f1=0.686)  ← baseline+10.1%
```

关键发现：
- **CodeLlama tail-2048 v3 完全失败**：epoch 3 accuracy 低于 majority baseline 30 个百分点，模型严重偏向预测 fail。epoch 1 几乎不输出有效预测。
- **Qwen-7B head-2048 表现良好**：epoch 1 (81.6%) 甚至略优于 epoch 3 (81.0%)，说明模型在第 1 个 epoch 就已充分学习，后续 epoch 轻微过拟合。

---
