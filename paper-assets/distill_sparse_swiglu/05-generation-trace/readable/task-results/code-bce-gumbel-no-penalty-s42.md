# code bce gumbel no penalty s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bce-gumbel-no-penalty-s42_20260519T065131_result.json`
- **Structured JSON:** [`2e84f3fb0599b0d97330.json`](../../sessions/2e/2e84f3fb0599b0d97330.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 代码修改
`train_bce_gumbel_no_penalty.py` = `train_bce_gumbel.py` 去掉以下三部分：
1. `lambda_sparse` 初始化和自适应更新（每 25 步 double/halve）
2. `constraint_loss = lambda_sparse * clamp(target - actual, min=0)` 
3. `--lambda_max` 参数

保留：BCE loss、Gumbel-sigmoid relaxation、tau annealing (1.0→0.1)、cosine LR schedule。

### 训练 Metrics
| Metric | No Penalty | With Lagrangian |
|---|---|---|
| Final BCE loss | 0.6307 | 0.6632 |
| Training sparsity | **0.383** | 0.504 |
| Training time | 977.6s | ~same |

### Benchmark PPL (TEAL 50% uniform)
| Variant | WikiText-2 PPL |
|---|---|
| BCE+Gumbel **no penalty** | **32.22** |
| BCE+Gumbel+Lagrangian | 38.02 |
| KL baseline | 11.79 |

### 分析

结果出乎意料：去掉 penalty controller 反而 PPL 从 38.02 改善到 32.22（-15.3%）。原因：
- 无 penalty 时，训练 sparsity 自然漂移到 0.383（低于目标 0.5），predictor 可以专注优化 BCE loss 而不被 constraint 梯度干扰
- 但 eval 统一在 50% sparsity 下，说明 predictor 学到了更好的 neuron 重要性排序
- Lagrangian penalty 在 BCE 训练中实际是负面的——它强迫训练 sparsity 向 0.5 收敛，但这个额外梯度信号反而劣化了 predictor 的判别能力

两个版本的 PPL 都远差于 KL（11.79），所以 **loss function 仍然是主要因素，Gumbel 和 Lagrangian 都是次要的**。

---
