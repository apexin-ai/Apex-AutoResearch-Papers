# code plan 024 within family deep dive

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_024_within_family_deep_dive_20260521T074437_result.json`
- **Structured JSON:** [`dbda6238f40fc5275bc1.json`](../../sessions/db/dbda6238f40fc5275bc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

### Part 1: Llama-2 vs Llama-3
- **分布差异极大**：Cohen's d = −0.99，overlap 仅 0.18，Llama-3 均值高 12pp（0.53 vs 0.65）
- **Unmatched C% = 61.3%**（复现 plan_001 结果）
- **Ability-matched C% = 28.3 ± 1.6%**（quintile matching, N=75 per group, 5 seeds）
  - 从 61.3% 降到 28.3%，**ability confound 解释了约一半的 DIF**
  - 但 28.3% 仍远高于 baseline，说明**存在真实的 within-family DIF**，即使控制能力水平后 Llama-2 和 Llama-3 在不同 item 上仍有系统性差异
- **Per-subject**：world_religions (78%)、marketing (77.3%)、us_foreign_policy (76%) 最高

### Part 2: 其他 Family Pairs
- phi-2 vs phi-3、qwen vs qwen-1.5、gemma vs gemma-2 均 underpowered (N<50)
- mistral vs mixtral (547 vs 120)：overlap 0.56，d = −0.15，分布差异远小于 Llama 系列

### Part 3: Temporal Comparison
- 2023 vs 2024 的分布差异远小于 Llama-2 vs 3：KL 0.36 vs 7.93，overlap 0.66 vs 0.18，d = −0.17 vs −0.99
- Llama-2→3 的代际跳跃比整体时间演变剧烈得多

---
