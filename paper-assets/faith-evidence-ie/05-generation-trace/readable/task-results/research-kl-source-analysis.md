# research kl source analysis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_kl-source-analysis_20260514T112537_result.json`
- **Structured JSON:** [`7b1ef73ab2c0f1644300.json`](../../sessions/7b/7b1ef73ab2c0f1644300.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `artifacts/kl_analysis_report.md`。核心结论：

**KL 是 loss component，不是 metric-only。** Line 2653: `per_token_loss += beta * per_token_kl`，梯度直接流向模型参数。

**per_token_kl 没有任何 clamp 保护。** 使用 Schulman estimator `exp(r) - r - 1`，当模型偏离 reference 时 `exp()` 无上界。Policy loss 有 PPO clipping，KL 项没有——这是 TRL 的设计缺陷。

**num_iterations=2 加剧问题。** ref_logps 在 generation 时计算一次不刷新，第二轮迭代中模型已更新但 reference 不变，KL 在第二轮被放大。

**当前影响**：KL 项（~5×10⁷）已主导 loss（policy loss ~O(1)），在过度拉回模型向 reference 靠拢，拖慢学习。grad_norm 稳定是因为梯度经 softmax Jacobian 和多层传播后被衰减，不代表 KL 无害。

**崩溃风险**：以当前恶化速度，约 50-100 步后 `exp(r)` 可能溢出 bfloat16 → NaN。

**最推荐的修复**：在 TRL 源码 `per_token_kl` 计算后加 `.clamp(max=100.0)`，或直接降 `kl_coef` 到 0。

---
