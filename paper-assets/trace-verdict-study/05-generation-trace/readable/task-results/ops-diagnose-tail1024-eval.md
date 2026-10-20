# ops diagnose tail1024 eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_tail1024_eval_20260518T061652_result.json`
- **Structured JSON:** [`9eae7aa14a5087d02b32.json`](../../sessions/9e/9eae7aa14a5087d02b32.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

交叉验证结果出来了：**tail-1024 checkpoint 跑 tail-512 数据得 90.7%**。

这确认了**checkpoint 本身有问题，不是测试数据的问题**。

## 诊断结论

### Eval 是否正确？
**Eval 脚本和测试数据本身没有 bug。** 验证通过：
- 测试数据条件正确（1190 样本，problem_id/label 与其他条件一致）
- 无 token 溢出（CodeLlama 最大 1314 token，远低于 2048）
- Chat template 对齐正确（eval prompt 是训练文本的 token 级前缀）
- 交叉验证证明问题在 checkpoint，不在数据

### 根因
**CodeLlama-13B tail-1024 checkpoint 本身表现差**。数据对比：

| 配置 | Accuracy | fail_recall |
|------|----------|-------------|
| CodeLlama tail-512 → tail-512 data | 97.5% | 93.8% |
| CodeLlama tail-1024 → tail-1024 data | 87.6% | 56.3% |
| CodeLlama tail-1024 → tail-512 data (交叉) | 90.7% | ~83% |
| Qwen-1.5B tail-1024 → tail-1024 data | 96.6% | 90.9% |
| DeepSeek-6.7B tail-1024 → tail-1024 data | 96.5% | 90.9% |

### 错误模式
- 148/148 错误全是 label=fail → pred=pass（模型倾向预测 pass）
- **全部错误发生在有 trace 的样本上**（无 trace 的 70 个 fail 样本 0 错误）
- trace 尾部无 assertion 错误关键词——模型无显式信号可用
- 127 个错误是 tail-1024 独有的（tail-512 模型能判对）

### 机制分析
训练使用 **full-sequence loss**（`dataset_text_field="text"`，`completion_only_loss=None`）。CodeLlama tokenizer 对同一文本产生更多 token（平均 1174 vs Qwen 978），导致 label token 在 loss 中占比极低（~0.085%）。模型训练 token accuracy 98.9%（主要是预测 trace token），但 label 预测能力不足。eval_loss 从 epoch 1（0.137）到 epoch 3（0.186）持续上升，表明过拟合。

### 建议修复
1. **用 `--label_only_loss` 重训练**（train_sft.py 已支持）——只在 label token 上计算 loss
2. 或用 **epoch 1 checkpoint**（checkpoint-148）eval，它 eval_loss 最低（0.137）
3. 或减少训练 epochs 到 1

要我执行哪个修复方案？

---
