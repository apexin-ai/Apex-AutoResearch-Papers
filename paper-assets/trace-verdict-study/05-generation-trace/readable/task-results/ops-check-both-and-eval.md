# ops check both and eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_both_and_eval_20260518T071932_result.json`
- **Structured JSON:** [`2f184683e390d87d891b.json`](../../sessions/2f/2f184683e390d87d891b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 epoch 的 eval 结果都拿到了。汇总如下：

## Experiment 2: `codellama13b_full_trace_tail2048_seed42_v2` (full sequence loss)

| Metric | Epoch 1 (ckpt-148) | Epoch 3 (final) | Delta |
|---|---|---|---|
| **accuracy** | 28.49% | 29.58% | +1.09 |
| pass_precision | 0.000 | 0.933 | +0.933 |
| pass_recall | 0.000 | 0.016 | +0.016 |
| fail_precision | 0.285 | 0.288 | +0.003 |
| fail_recall | 1.000 | 0.997 | -0.003 |
| majority baseline | 71.5% (pass) | 71.5% (pass) | — |

### Loss dilution 分析

**结论：不存在显著 loss dilution（epoch 3 没有比 epoch 1 更差），但两者都彻底失败。**

- 两个 epoch 的 accuracy 都远低于 majority baseline（71.5%），模型几乎把所有样本预测为 "fail"
- Epoch 3 相比 epoch 1 略有微弱改善：pass_recall 从 0 → 0.016（开始预测少量 pass），accuracy 从 28.49% → 29.58%
- 这不是 loss dilution 问题，而是模型根本没有学到有效的 pass/fail 区分能力。full sequence loss 在 tail-2048 设置下训练 3 个 epoch 也完全不够

### Experiment 1: `codellama13b_full_trace_tail1024_seed42_v3` (label-only loss)

训练中，当前 step 207/444（47%），预计还需 ~1h13m。checkpoint-148 已保存，但 final 尚未完成。需要等训练结束后再 eval。

---
