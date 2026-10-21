# analysis gradient evolution 018v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient-evolution-018v2_20260516T184634_result.json`
- **Structured JSON:** [`5037fe6fcd6f9f219ef7.json`](../../sessions/50/5037fe6fcd6f9f219ef7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**018v2 梯度演化 (counterfactual, without SGS):**

| Step | obs% | reward% | KL% | cont% |
|------|------|---------|-----|-------|
| 25K  | 11.6 | 28.0 | 60.3 | 0.0 |
| 75K  | 20.8 | 22.1 | 57.1 | 0.0 |
| 112K | 24.2 | 22.8 | 53.0 | 0.0 |

**With SGS (实际训练):** 全程 KL=100%，其余被阻断。

**关键对比 008d:** 008d 在无 SGS 保护下，obs 梯度从 55K 的 25.8% 暴涨到 105K 的 93%（CIVO 发作）。018v2 的 counterfactual obs 仅从 11.6% 温和增长到 24.2%——表明 SGS 成功阻止了正反馈环路的形成，obs gradient 不再指数膨胀。KL 绝对值也在稳步下降（1.08→0.59），说明模型收敛正常。

---
