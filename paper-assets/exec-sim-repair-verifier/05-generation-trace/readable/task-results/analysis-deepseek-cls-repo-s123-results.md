# analysis deepseek cls repo s123 results

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-cls-repo-s123-results_20260518T223828_result.json`
- **Structured JSON:** [`28b93b1049a52bfea73f.json`](../../sessions/28/28b93b1049a52bfea73f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the complete summary:

---

## deepseek-cls-repo-s123 完整结果

### 训练

| 指标 | 值 |
|------|-----|
| 总步数 | 6633 (3 epochs) |
| 训练时间 | 21h30m |
| 平均 train_loss | 0.0393 |
| eval_loss | nan (所有 epoch, metric 计算 bug) |
| best checkpoint | epoch 3 (因 eval_loss=nan, 默认取最后) |

**Loss 轨迹:**

| Epoch | Loss |
|-------|------|
| 0.5 | 0.0195 |
| 1.0 | 0.0099 |
| 1.5 | 0.0081 |
| 2.0 | 0.0052 |
| 2.5 | 0.0031 |
| 3.0 | 0.0039 |

### 评估结果对比

| 指标 | seq8192 | seq2048 |
|------|---------|---------|
| Per-test Accuracy | **74.93%** | 82.62% |
| Majority baseline | 72.96% | 72.96% |
| Gap vs majority | +1.97pp | +9.67pp |
| F1 macro | **53.94%** | 71.35% |
| F1 fail | 22.84% | 53.37% |
| F1 pass | 85.03% | 89.32% |
| Precision fail | 68.11% | 97.30% |
| Recall fail | 13.72% | 36.77% |
| Recall pass | 97.62% | 99.62% |
| Unparseable | **0** | 2796 (28.6%) |
| **Variant accuracy (AND)** | **7/25 = 28.00%** | **9/25 = 36.00%** |

seq2048 的 "更高" 指标是假象: 2796 个 unparseable 样本默认预测为 pass, 而 73% 样本本身就是 pass, 所以 accuracy 被虚高了。seq8192 无 truncation, 是更可靠的度量。

### Variant-level 详细 (seq8192)

- **7/25 correct** (全部是纯 pass 的 variant, 无 fail test case)
- 所有含 fail test 的 variant 都未完全正确
- Fail recall 极低 (13.72%), 模型倾向于预测 pass

### Checkpoints

- `/root/autodl-tmp/checkpoints_deepseek_cls_repo_s123/best/` (65MB LoRA adapter, epoch 3)
- `/root/autodl-tmp/checkpoints_deepseek_cls_repo_s123/checkpoint-4422/` (epoch 2)
- `/root/autodl-tmp/checkpoints_deepseek_cls_repo_s123/checkpoint-6633/` (epoch 3)
- LoRA: r=16, alpha=32, dropout=0.05, target=[q,k,v,o_proj]

### 关键问题

1. **eval_loss=nan**: 所有 epoch 的 eval loss 都是 nan, `best_metric=inf`, `best_model_checkpoint=None`。Trainer 实际保存了最后一个 checkpoint 作为 best
2. **seq8192 variant accuracy 只有 28%**: 比 seq2048 的 36% 更低, 说明更长 context 反而让模型在某些 all-pass variant 上也犯错 (如 django-10880, django-14376)
3. **Fail detection 几乎失效**: seq8192 recall_fail=13.72%, 模型严重偏向预测 pass

---
