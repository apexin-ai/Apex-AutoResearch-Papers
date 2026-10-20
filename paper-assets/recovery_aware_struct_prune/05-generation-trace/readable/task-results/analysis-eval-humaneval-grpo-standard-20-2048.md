# analysis eval humaneval grpo standard 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_humaneval_grpo_standard_20_2048_20260517T175504_result.json`
- **Structured JSON:** [`d227ebda5c1bbbf26c88.json`](../../sessions/d2/d227ebda5c1bbbf26c88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**GRPO Standard 20% @2048 结果：pass@1 = 10.37% (17/164)**

关键发现：
- @512 的 1.83% 确认为截断伪影，扩展到 2048 tokens 后提升至 10.37%（+8.54pp）
- 与 SFT RASP 20% @2048 完全相同（都是 10.37%, 17/164）
- 远优于 SFT Standard 20%（negative）
- 待 GRPO RASP @2048 结果完成对比，判断 RASP 在 GRPO 训练下是否有额外增益

---
