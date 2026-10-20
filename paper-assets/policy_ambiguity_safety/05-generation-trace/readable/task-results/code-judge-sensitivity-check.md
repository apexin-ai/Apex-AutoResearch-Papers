# code judge sensitivity check

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_judge_sensitivity_check_20260520T194932_result.json`
- **Structured JSON:** [`8472a33fa6b9f5f36b59.json`](../../sessions/84/8472a33fa6b9f5f36b59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核心结论：

1. **judge_model 不是 confound**。在逻辑回归中加入 judge_model 后 p=1.0，condition 系数变化 0.0%。这是因为 judge_model 与 model 完全 confounded（每个 agent model 只有一个 judge），所以 judge 的方差被 model 固定效应吸收了。

2. **Raw rate 差异**：gpt-4.1 作为 judge 的违规率（26.0%）略高于 gpt-5.4（22.6%），χ² p=0.036。但控制 condition 后，unambiguous 条件下两者几乎相同（6.7% vs 7.1%），差异主要来自 ambiguous 条件（45.3% vs 38.0%）——这反映的是被评判模型的差异而非 judge 偏差。

3. **Within-judge 子集一致性**：两个 judge 子集中 ambiguity effect 方向和强度一致（gpt-4.1 judged: C1_delta=38.7pp, β=2.52; gpt-5.4 judged: C1_delta=30.9pp, β=2.13），核心结论 robust。

4. **Token delta** 是显著预测因子（p=0.007），加入后 AIC 从 2758 降至 2232。

脚本和结果已保存：
- 脚本：`full_study/analysis/compute_judge_sensitivity.py`
- 输出：`full_study/analysis/judge_sensitivity.json`

---
