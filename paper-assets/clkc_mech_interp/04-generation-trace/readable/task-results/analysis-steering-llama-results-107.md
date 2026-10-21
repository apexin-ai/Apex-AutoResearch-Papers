# analysis steering llama results 107

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_steering-llama-results-107_20260522T112421_result.json`
- **Structured JSON:** [`868d87f7f772644afb59.json`](../../sessions/86/868d87f7f772644afb59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

**Steering v3 Llama (plan_107): 完成，结论 NEGATIVE。**

- 进程 PID 468898 已结束，10 个 alpha 全部跑完，结果写入 `steering_results.json`
- **关键发现：probe weight direction 的 steering 效果与 random orthogonal direction 无统计差异。** 所有 Fisher p > 0.30，最大方向性 flip 仅 2/136（1.5%），远低于 15% 阈值
- 大 alpha (±20) 时 steering 和 random 都引起 ~15% flip，但这只是非定向的扰动破坏
- **Interpretation：** 线性 probe 能以 77.6% accuracy 分类 contextual vs parametric activations，但其 weight vector 不是模型决策的因果通道。Probe 找到的是相关信号，不是因果方向

对 claim 的影响：不能用 "probe weights as steering vectors" 来论证因果性。需要其他方法（如 DAS/distributed alignment search, activation patching, or causal mediation analysis）来寻找因果方向。

---
