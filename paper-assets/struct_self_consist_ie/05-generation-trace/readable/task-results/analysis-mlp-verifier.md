# analysis mlp verifier

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mlp_verifier_20260518T011632_result.json`
- **Structured JSON:** [`2fdec0ba2940324508d0.json`](../../sessions/2f/2fdec0ba2940324508d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。实验 exp_027 已有完整结果，无需重跑。

**核心结论：Feature Bottleneck Confirmed**

| Model | AUROC | Selection F1 | vs Greedy |
|-------|-------|-------------|-----------|
| LR (5 signals) | 0.6522 | 0.6407 | -0.34pp |
| MLP (64,32, 5 signals) | 0.6393 | 0.6386 | -0.55pp |
| RF (100 trees, 5 signals) | 0.5868 | 0.6154 | -2.87pp |
| MLP (64,32, 15 feat) | 0.6322 | 0.6339 | -1.02pp |

- MLP < LR (Δ = -0.013 AUROC): 非线性模型无法从 5 个 signals 中提取更多信息
- 加 10 个 pairwise interactions 反而更差
- 所有 supervised models 无法超越 greedy（0.6441）
- Verdict: 瓶颈在信号质量（feature bottleneck），不在 aggregation 方式。支持论文 "structural signals 是 lightweight diagnostics，不是 strong selectors" 的结论。

---
