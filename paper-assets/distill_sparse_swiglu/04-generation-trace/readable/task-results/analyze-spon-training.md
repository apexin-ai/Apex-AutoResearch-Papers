# analyze spon training

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_spon_training_20260515T182312_result.json`
- **Structured JSON:** [`d198063142033fd2b3b5.json`](../../sessions/d1/d198063142033fd2b3b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 实验结果总结

**SPON 训练实验 (spon_training): Negative**

### 训练
- 1000 steps 正常完成，loss 在 0.38-0.47 波动未有效收敛
- Bias norm: 0 → 0.041，step 700 后饱和
- 仅 458K 可训练参数 (0.0057%)

### WikiText-2 评估 (seq_len=2048)

| 配置 | PPL | vs Dense |
|------|-----|----------|
| True Dense | 6.12 | — |
| Per-token sparse (no SPON) | 9.22 | +50.6% |
| Per-token sparse + SPON | 9.10 | +48.7% |
| TEAL global mask (参考) | 12.08 | +97.4% |

**SPON 仅恢复 3.8% 的 sparse-vs-dense gap（PPL 改善 0.12）。**

### 分析
1. Per-token predictor hard mask 本身已比 TEAL global mask 好很多（9.22 vs 12.08），残余误差的结构可能不适合用 static additive bias 补偿
2. Bias norm 极小且提前饱和，学习容量不足
3. 训练 seq_len=128 vs 评估 seq_len=2048 的 mismatch 可能也有影响

### Claim 2 影响
SPON + KL predictor 加性组合的收益 marginal。若要继续验证 Claim 2，需要更高表达力的补偿机制或在 TEAL global mask 场景下测试（误差更大，补偿空间更大）。

---
