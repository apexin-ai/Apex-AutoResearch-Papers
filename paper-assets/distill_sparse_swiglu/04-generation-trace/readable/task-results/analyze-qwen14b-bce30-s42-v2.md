# analyze qwen14b bce30 s42 v2

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_qwen14b_bce30_s42_v2_20260517T163722_result.json`
- **Structured JSON:** [`b96e7d0f5571d593fe5a.json`](../../sessions/b9/b96e7d0f5571d593fe5a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The full log is only 110 lines. I already have all the data. Here's the analysis:

## 结果摘要
- **最终 PPL**: 未记录（日志中无 eval/perplexity 阶段）
- **最终 sparsity**: **6.4%**（目标 30%，严重不达标）
- **训练步数完成**: 1000/1000（正常完成，EXIT_CODE=0）
- **conclusion: negative**
- **关键发现**: 即使 lambda_max 提升 10x 至 50000，BCE 在 Qwen-14B 上最终 sparsity 仅 ~6%，从 step 50 起 sparsity 就从初始 49% 暴跌到 4.5% 并在此后整个训练过程中几乎未恢复，确认 BCE 梯度信号在 14B scale 根本无法驱动稀疏化。

## 详细数据

**Sparsity 时序轨迹**:
| Step | Sparsity | BCE Loss |
|------|----------|----------|
| 10   | 49.4%    | 0.6941   |
| 20   | 46.1%    | 0.6913   |
| 30   | 35.3%    | 0.6753   |
| 40   | 17.8%    | 0.6261   |
| 50   | 6.9%     | 0.5802   |
| 100  | 4.5%     | 0.5503   |
| 200  | 5.3%     | 0.5424   |
| 500  | 6.3%     | 0.5350   |
| 800  | 6.3%     | 0.5326   |
| 1000 | 6.4%     | 0.5324   |

**关键观察**:
1. Sparsity 在 warmup 阶段（step 10-50）从 ~50% 急剧崩塌到 ~5%，之后 950 步内仅缓慢爬升到 6.4%
2. BCE loss 从 0.69 下降到 0.53 并收敛，说明 predictor 在学习，但学到的是"几乎不 mask"
3. Regularization term (reg) 稳定在 ~0.024，说明 Lagrangian 约束虽然存在但未能推动 sparsity 上升
4. 与 v1（lambda_max=5000）对比：10x 的约束强度对最终 sparsity 几乎无改善，问题不在 lambda 大小而在 BCE 梯度本身

**结论**: Hypothesis confirmed。BCE loss 在 14B scale 的梯度信号不足以对抗 predictor 的"全保留"倾向。即使极强的 Lagrangian 约束也无法改变这一根本问题。KL divergence 作为 training signal 的必要性得到验证。

---
