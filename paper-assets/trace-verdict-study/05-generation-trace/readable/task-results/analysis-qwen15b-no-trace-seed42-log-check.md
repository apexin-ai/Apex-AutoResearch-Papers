# analysis qwen15b no trace seed42 log check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen15b_no_trace_seed42_log_check_20260520T215558_result.json`
- **Structured JSON:** [`29b255a9bf70a6915adc.json`](../../sessions/29/29b255a9bf70a6915adc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇报如下：

## seed42 日志检查结果

### 异常检查
- **无 NaN**：grep "nan" 无匹配
- **无 OOM**：grep "oom" 无匹配  
- **训练正常完成**：444 steps，3 epochs，EXIT_CODE=0

### 训练 Loss 曲线（正常收敛，无异常跳变）

| Epoch | Train Loss | Token Accuracy | 
|-------|-----------|----------------|
| 0.07 | 1.9413 | 0.688 |
| 0.34 | 0.4716 | 0.877 |
| 0.68 | 0.2717 | 0.927 |
| 0.95 | 0.1679 | 0.955 |
| ~2.0 | ~0.06 | ~0.983 |
| ~3.0 | ~0.05 | ~0.986 |

Loss 持续单调下降，无异常。

### Eval Loss（关键信号）
- **Epoch 2.0**: eval_loss = **0.697**, eval_token_acc = 0.873
- **Epoch 3.0**: eval_loss = **0.794**, eval_token_acc = 0.870

**eval_loss 从 epoch 2→3 上升了 14%**，而 train_loss 继续下降（0.06→0.05）。这是**典型的过拟合信号**。

### seed42 vs seed123 对比

| 指标 | seed42 | seed123 | 差距 |
|------|--------|---------|------|
| **Accuracy** | **67.3%** | **75.9%** | -8.6pp |
| Majority baseline | 71.5% | 71.5% | — |
| Lift | **-4.2pp** | **+4.4pp** | — |
| Pass P/R/F1 | 0.82/0.70/0.75 | 0.83/0.84/0.83 | recall 差距大 |
| Fail P/R/F1 | 0.45/0.62/0.52 | 0.58/0.56/0.57 | precision 差距大 |

### 诊断结论

**seed42 有严重问题，但不是训练崩溃，而是泛化失败：**

1. **过拟合**：train loss 降到 0.05（token acc 98.6%）但 eval_loss 在 epoch 2→3 反弹，说明 3 epochs 训练过头了。
2. **Accuracy 低于 majority baseline**（67.3% < 71.5%），lift 为负，说明模型学到了有害的 pattern——它过度预测 fail（fail recall 0.62 但 precision 仅 0.45），把大量 pass 样本错判为 fail。
3. **seed123 正常**（75.9%，lift +4.4pp），说明 no_trace condition 本身不是问题，而是 seed42 的数据 split 或随机初始化导致模型 overfit 到了训练集特有的 spurious pattern。
4. **8.6pp 的 seed 间差异非常大**，远超正常随机波动（通常 1-3pp），这对 no_trace condition 的实验结论有影响——如果只看 seed42 会低估 no_trace 的能力。

**建议关注**：seed456 的结果是否存在（日志文件 `qwen15b_no_trace_seed456.log` 存在但 eval_results.json 未找到），三个 seed 的均值和标准差才能给出可靠结论。

---
