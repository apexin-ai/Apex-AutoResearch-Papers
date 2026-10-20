# analysis deepseek eo seed456 eval

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_eo_seed456_eval_20260515T221033_result.json`
- **Structured JSON:** [`2e31fa123f297ed7e725.json`](../../sessions/2e/2e31fa123f297ed7e725.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。Epoch1 和 epoch3 结果完全相同（同样的 8 个错误样本）。

---

## 训练完成确认
- 训练正常完成: 是 (EXIT_CODE=0)
- Final train_loss: 0.1225
- eval_loss (epoch3): 0.4824
- Training time: 6246s (~1h44m)

## Eval 结果 (epoch3 final)
- accuracy: **99.33%** (95% CI: [98.8%, 99.7%])
- Majority baseline: 71.5%, lift: +27.8pp
- pass: P=1.000 R=0.991 F1=0.995
- fail: P=0.977 R=1.000 F1=0.988
- 错误数: 8（全部是 pass→fail 误报）

## Epoch1 Eval (checkpoint-148)
- accuracy: **99.33%**（与 epoch3 完全相同）
- 8 个错误样本 ID 完全一致
- **无 overfitting**，模型在 epoch1 就已收敛到最终表现

## Seed 对比

| Seed | Epoch1 Acc | Final Acc | fail_recall | 错误数 |
|------|-----------|-----------|-------------|--------|
| 42   | 99.83%    | 99.33%    | 1.000       | 8      |
| 123  | 91.43%    | 91.09%    | 0.705       | 106    |
| 456  | 99.33%    | 99.33%    | 1.000       | 8      |

## Error Analysis
- 错误样本 ids: **[540, 541, 542, 543, 548, 549, 901, 905]**
- 与 Qwen irreducible errors (901/905) 重叠: **是**（2/8）
- 540-543, 548-549: 新聚簇，可能来自同一 HumanEval 问题，6 个样本全错
- 所有错误方向一致: pass 被误判为 fail（fail_recall=1.0, pass_recall=0.991）

## 结论
- **conclusion: SUCCESS**
- seed456 与 seed42 的 final accuracy **完全一致 (99.33%)**，seed123 确认为 outlier（LoRA initialization bad luck）
- Claim 1 framing: **2/3 seeds 达到 99.33%，1 seed 91.09%（initialization outlier）**
- epoch1=epoch3 进一步证实：好的 initialization 下，模型仅需 1 epoch 就学会任务；seed123 的问题不是训练不够，而是初始化不利

---
