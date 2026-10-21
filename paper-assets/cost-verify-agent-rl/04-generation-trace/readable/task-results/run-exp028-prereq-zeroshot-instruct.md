# run exp028 prereq zeroshot instruct

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_exp028_prereq_zeroshot_instruct_20260515T210027_result.json`
- **Structured JSON:** [`22375bdc9256e163ffc4.json`](../../sessions/22/22375bdc9256e163ffc4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

README 确认：**Qwen3-1.7B 就是 instruct 模型**。关键摘要：

> "Qwen3 delivers groundbreaking advancements in reasoning, **instruction-following, agent capabilities**... surpassing previous QwQ (in thinking mode) and **Qwen2.5 instruct models** (in non-thinking mode)"
> 
> "**Expertise in agent capabilities**, enabling precise integration with external tools in both thinking and unthinking modes"

## 结论

**上次 exp028_prereq 已经用的是 Qwen3-1.7B（instruct）模型。** 不存在单独的 `Qwen3-1.7B-Instruct`——Qwen3 命名规范中，不带 `-Base` 后缀的就是 instruct 版本。

重新运行相同配置 = 相同结果（0% success）。这不是模型选错的问题。

## 对 D044 假设的影响

上次 0% success 的基线已经是 instruct 模型：
- **Qwen3-1.7B（instruct）零样本 = 0% success**
- **SFT checkpoint = 6.25% success**

这意味着 **SFT 并非毒药**——它实际上把 success 从 0% 提升到了 6.25%。D044 假设（"SFT 是毒药"）**不成立**。

## 可选的下一步

1. **跳过重跑**，直接用已有基线数据推进 exp028a
2. 如果想排除代码 bug，可以用 **non-thinking mode**（`enable_thinking=False`）重跑一次——但这只会改变生成风格，不太可能大幅提升 success
3. 用更大的模型（如 Qwen3-8B）做零样本基线，重新评估策略

需要你做决定——是否仍要重跑，还是基于这个发现调整方案？

---
