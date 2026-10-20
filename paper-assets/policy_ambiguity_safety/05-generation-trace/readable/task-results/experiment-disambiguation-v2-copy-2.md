# experiment disambiguation v2

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_disambiguation_v2_20260522T232321_result.json`
- **Structured JSON:** [`2415406e5edfa6c77fdb.json`](../../sessions/24/2415406e5edfa6c77fdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整，分析已完成。总结：

**数据状态**：900 episodes + 900 judgments 已全部成功完成（非失败数据），无需重跑。

**分析结果**：
- **GPT-4.1**: 违规率从 40.7% → 35.0%（-5.7pp, p=0.057，边际显著），clarification rate 最高 45.3%。authorization_scope 类型效果最强（-28pp, p=0.001）
- **DeepSeek-v3**: 49.7% → 47.3%（-2.3pp, p=0.477，不显著），clarification rate 16.7%。coreferential 类型显著下降（-16pp, p=0.02）
- **Claude Sonnet**: 30.3% → 29.3%（-1.0pp, p=0.755，不显著），clarification rate 27.7%

**关键发现**：disambiguation prompting 整体效果有限，仅 GPT-4.1 接近显著。scopal 类型在所有模型上反而增加违规（+6pp 平均），可能因消歧指令导致过度解释。结果已写入 `disambiguation_intervention/results.json`。

---
