# analysis binary reward final

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_binary_reward_final_20260523T170603_result.json`
- **Structured JSON:** [`2e2b8df13439cb730b4c.json`](../../sessions/2e/2e2b8df13439cb730b4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已写入 `artifacts/binary_reward_final_analysis.md`。

核心数据：
- **Sign-episode correlation: 99.6%** (270/271) — 优势符号几乎完美追踪 episode 成败
- **Credit agreement: 28.0%** (76/271) — 优势符号与 action validity 严重不匹配，85.8% 被惩罚的 window 实际包含有效 action
- **Zero-advantage: 54.8%** (329/600) — 超过一半的 window 梯度为零，Iteration 2 全部为 all-fail group（100% 零梯度）
- 唯一的 sign-episode 不匹配来自 GRPO 组内归一化：ep 19 的低 return (1.29) 在高 return 组（6.98–8.15）中被分配了负 advantage

---
